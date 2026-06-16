import pandas as pd
import matplotlib.pyplot as plt

# wczytanie danych
df = pd.read_csv("data/sales.csv")

df = df.drop_duplicates()

df["Purchase Type"] = df["Purchase Type"].str.strip()
df["Payment Method"] = df["Payment Method"].str.strip()
df["Manager"] = df["Manager"].str.strip()
df["City"] = df["City"].str.strip()



df["Manager"] = df["Manager"].str.replace(r"\s+", " ", regex=True)

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

df["Price"] = pd.to_numeric(df["Price"])
df["Quantity"] = pd.to_numeric(df["Quantity"])


df["Quantity"] = pd.to_numeric(df["Quantity"]).round().astype(int)

df["Revenue"] = df["Price"] * df["Quantity"]

df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.day_name()
df["Year"] = df["Date"].dt.year



print(df[df["Quantity"] <= 0])
print(df[df["Price"] <= 0])

df["City"] = df["City"].str.title()
df["Product"] = df["Product"].str.strip().str.title()

print("\n=== BASIC KPI ===")

print(f"Number of orders: {len(df)}")
print(f"Total revenue: {df['Revenue'].sum():,.2f}")
print(f"Average order value: {df['Revenue'].mean():,.2f}")
print(f"Unique products: {df['Product'].nunique()}")
print(f"Cities: {df['City'].nunique()}")


city_sales = (
    df.groupby("City")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(city_sales)

city_sales = (
    df.groupby("City")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

plt.figure(figsize=(10, 6))

plt.bar(city_sales["City"], city_sales["Revenue"])

plt.title("Total Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# df.to_csv("data/sales_cleaned.csv", index=False)


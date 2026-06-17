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

product_sales = (
    df.groupby("Product")["Revenue"]
      .sum()
      .sort_values(ascending=True)
      .reset_index()
)

plt.figure(figsize=(10, 6))

bars = plt.barh(
    product_sales["Product"],
    product_sales["Revenue"]
)

plt.title("Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")

for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height()/2,
        f"{width:,.0f}",
        va="center"
    )

plt.tight_layout()
plt.show()

daily_revenue = (
    df.groupby("Date")["Revenue"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(12, 6))

plt.plot(
    daily_revenue["Date"],
    daily_revenue["Revenue"]
)

plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


purchase_sales = (
    df.groupby("Purchase Type")["Revenue"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(8, 5))

plt.pie(
    purchase_sales["Revenue"],
    labels=purchase_sales["Purchase Type"],
    autopct="%1.1f%%"
)

plt.title("Revenue Share by Purchase Type")

plt.show()

manager_sales = (
    df.groupby("Manager")["Revenue"]
      .sum()
      .sort_values(ascending=True)
      .reset_index()
)

plt.figure(figsize=(10, 6))

plt.barh(
    manager_sales["Manager"],
    manager_sales["Revenue"]
)

plt.title("Revenue by Manager")
plt.xlabel("Revenue")

plt.tight_layout()
plt.show()



payment_sales = (
    df.groupby("Payment Method")["Revenue"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(7, 7))

plt.pie(
    payment_sales["Revenue"],
    labels=payment_sales["Payment Method"],
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4}
)

plt.title("Revenue Share by Payment Method")

plt.show()
# df.to_csv("data/sales_cleaned.csv", index=False)


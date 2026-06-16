import pandas as pd

# wczytanie danych
df = pd.read_csv("data/sales.csv")

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

df.to_csv("data/sales_cleaned.csv", index=False)


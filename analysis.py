import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")


# 1. LOAD DATA
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    required_columns = [
        "Date",
        "Price",
        "Quantity",
        "Purchase Type",
        "Payment Method",
        "Manager",
        "City",
        "Product"
    ]

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


    cols_to_strip = [
        "Purchase Type",
        "Payment Method",
        "Manager",
        "City",
        "Product"
    ]

    for col in cols_to_strip:
         df[col] = df[col].astype(str).str.strip()

    df["Manager"] = df["Manager"].str.replace(
        r"\s+",
        " ",
        regex=True
    )

    return df

# 2. PREPROCESSING
def preprocess(df: pd.DataFrame) -> pd.DataFrame:

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d-%m-%Y",
         errors="coerce"

    )

    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
  
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").round().astype(int, errors="ignore")


    df = df.dropna(subset=["Date", "Price", "Quantity"])

    # DATA QUALITY CHECK
    invalid_quantity = df[df["Quantity"] <= 0]
    invalid_price = df[df["Price"] <= 0]


    if len(invalid_quantity) > 0:
        print(
            f"WARNING: Removed {len(invalid_quantity)} rows with Quantity <= 0"
        )

    if len(invalid_price) > 0:
        print(
            f"WARNING: Removed {len(invalid_price)} rows with Price <= 0"
        )


    df = df.drop_duplicates().copy()

    df = df[
        (df["Quantity"] > 0) &
        (df["Price"] > 0)
    ].copy()


    df["Revenue"] = df["Price"] * df["Quantity"]

    df["Month"] = df["Date"].dt.month
    df["DayOfWeek"] = df["Date"].dt.day_name()
    df["Year"] = df["Date"].dt.year

    df["City"] = df["City"].str.title()
    df["Product"] = df["Product"].str.title()


    return df

# 3. KPI
def print_kpis(df: pd.DataFrame):
    print("\n=== BASIC KPI ===")
    print(f"Number of orders: {len(df)}")
    print(f"Total revenue: {df['Revenue'].sum():,.2f}")
    print(f"Average order value: {df['Revenue'].mean():,.2f}")
    print(f"Unique products: {df['Product'].nunique()}")
    print(f"Cities: {df['City'].nunique()}")



# 4. AGGREGATION
def group_revenue(df: pd.DataFrame, column: str) -> pd.DataFrame:
    return (
        df.groupby(column)["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


# 5. PLOTS
def plot_city_sales(city_sales: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    plt.bar(city_sales["City"], city_sales["Revenue"])
    plt.title("Total Revenue by City")
    plt.xlabel("City")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_product_sales(product_sales: pd.DataFrame):
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
            bar.get_y() + bar.get_height() / 2,
            f"{width:,.0f}",
            va="center"
        )

    plt.tight_layout()
    plt.show()


def plot_daily_revenue(df: pd.DataFrame):
    daily_revenue = (
        df.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(12, 6))
    plt.plot(daily_revenue["Date"], daily_revenue["Revenue"])

    plt.title("Revenue Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_pie(data: pd.DataFrame, col: str, title: str):
    plt.figure(figsize=(8, 5))
    plt.pie(
        data["Revenue"],
        labels=data[col],
        autopct="%1.1f%%"
    )
    plt.title(title)
    plt.show()


def plot_donut(data: pd.DataFrame, col: str, title: str):
    plt.figure(figsize=(7, 7))
    plt.pie(
        data["Revenue"],
        labels=data[col],
        autopct="%1.1f%%",
        wedgeprops={"width": 0.4}
    )
    plt.title(title)
    plt.show()


# 6. MAIN
def main():
    df = load_data("data/sales.csv")
    df = preprocess(df)

   

    print_kpis(df)

    # aggregations
    city_sales = group_revenue(df, "City")
    product_sales = group_revenue(df, "Product")
    manager_sales = group_revenue(df, "Manager")
    purchase_sales = group_revenue(df, "Purchase Type")
    payment_sales = group_revenue(df, "Payment Method")

    # plots
    plot_city_sales(city_sales)
    plot_product_sales(product_sales)
    plot_daily_revenue(df)
    plot_pie(purchase_sales, "Purchase Type", "Revenue Share by Purchase Type")
    plot_donut(payment_sales, "Payment Method", "Revenue Share by Payment Method")

    # insights
    print("\n=== KEY INSIGHTS ===")

    top_city = city_sales.iloc[0]
    print(f"Top city: {top_city['City']} ({top_city['Revenue']:,.2f})")

    top_product = product_sales.iloc[0]
    print(f"Top product: {top_product['Product']} ({top_product['Revenue']:,.2f})")

    top_manager = manager_sales.iloc[0]
    print(f"Top manager: {top_manager['Manager']} ({top_manager['Revenue']:,.2f})")


if __name__ == "__main__":
    main()
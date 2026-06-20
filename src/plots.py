import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")


def plot_city_sales(city_sales: pd.DataFrame):

    plt.figure(figsize=(10, 6))

    plt.bar(
        city_sales["City"],
        city_sales["Revenue"]
    )

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


def plot_pie(
    data: pd.DataFrame,
    col: str,
    title: str
):

    plt.figure(figsize=(8, 5))

    plt.pie(
        data["Revenue"],
        labels=data[col],
        autopct="%1.1f%%"
    )

    plt.title(title)

    plt.show()


def plot_donut(
    data: pd.DataFrame,
    col: str,
    title: str
):

    plt.figure(figsize=(7, 7))

    plt.pie(
        data["Revenue"],
        labels=data[col],
        autopct="%1.1f%%",
        wedgeprops={"width": 0.4}
    )

    plt.title(title)

    plt.show()
from data_loader import load_data
from preprocessing import preprocess
from kpi import print_kpis
from aggregation import group_revenue
from plots import (
    plot_city_sales,
    plot_product_sales,
    plot_daily_revenue,
    plot_pie,
    plot_donut
)
from insights import print_insights


def main():

    df = load_data("data/sales.csv")
    df = preprocess(df)

    print_kpis(df)

    city_sales = group_revenue(df, "City")
    product_sales = group_revenue(df, "Product")
    manager_sales = group_revenue(df, "Manager")
    purchase_sales = group_revenue(df, "Purchase Type")
    payment_sales = group_revenue(df, "Payment Method")

    plot_city_sales(city_sales)
    plot_product_sales(product_sales)
    plot_daily_revenue(df)

    plot_pie(
        purchase_sales,
        "Purchase Type",
        "Revenue Share by Purchase Type"
    )

    plot_donut(
        payment_sales,
        "Payment Method",
        "Revenue Share by Payment Method"
    )

    print_insights(
        city_sales,
        product_sales,
        manager_sales
    )


if __name__ == "__main__":
    main()
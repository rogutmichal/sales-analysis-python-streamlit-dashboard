import pandas as pd


def print_insights(
    city_sales: pd.DataFrame,
    product_sales: pd.DataFrame,
    manager_sales: pd.DataFrame
):

    print("\n=== KEY INSIGHTS ===")

    top_city = city_sales.iloc[0]
    print(
        f"Top city: {top_city['City']} "
        f"({top_city['Revenue']:,.2f})"
    )

    top_product = product_sales.iloc[0]
    print(
        f"Top product: {top_product['Product']} "
        f"({top_product['Revenue']:,.2f})"
    )

    top_manager = manager_sales.iloc[0]
    print(
        f"Top manager: {top_manager['Manager']} "
        f"({top_manager['Revenue']:,.2f})"
    )
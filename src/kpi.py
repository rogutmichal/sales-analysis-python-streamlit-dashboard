import pandas as pd


def print_kpis(df: pd.DataFrame):

    print("\n=== BASIC KPI ===")

    print(f"Number of orders: {len(df)}")
    print(f"Total revenue: {df['Revenue'].sum():,.2f}")
    print(f"Average order value: {df['Revenue'].mean():,.2f}")
    print(f"Unique products: {df['Product'].nunique()}")
    print(f"Cities: {df['City'].nunique()}")
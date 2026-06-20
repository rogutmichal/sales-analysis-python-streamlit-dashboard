import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:

    df = df.drop_duplicates().copy()

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    df["Quantity"] = (
        pd.to_numeric(
            df["Quantity"],
            errors="coerce"
        )
        .round()
        .astype(int, errors="ignore")
    )

    df = df.dropna(
        subset=["Date", "Price", "Quantity"]
    )

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

    df = df[
        (df["Quantity"] > 0) &
        (df["Price"] > 0)
    ].copy()

    df["Revenue"] = (
        df["Price"] * df["Quantity"]
    )

    df["Month"] = df["Date"].dt.month
    df["DayOfWeek"] = df["Date"].dt.day_name()
    df["Year"] = df["Date"].dt.year

    df["City"] = df["City"].str.title()
    df["Product"] = df["Product"].str.title()

    return df
import pandas as pd


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
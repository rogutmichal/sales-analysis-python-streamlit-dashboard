import pandas as pd


def group_revenue(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:

    return (
        df.groupby(column)["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
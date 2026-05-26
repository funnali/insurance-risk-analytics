import pandas as pd


def calculate_loss_ratio(total_claims, total_premium):
    """
    Calculate insurance loss ratio.
    """

    if total_premium == 0:
        return None

    return total_claims / total_premium


def missing_value_summary(df):
    """
    Generate missing value summary table.
    """

    missing_values = df.isnull().sum()

    missing_percent = (
        missing_values / len(df)
    ) * 100

    summary = pd.DataFrame({
        "Missing Values": missing_values,
        "Percentage": missing_percent
    })

    return summary.sort_values(
        by="Percentage",
        ascending=False
    )
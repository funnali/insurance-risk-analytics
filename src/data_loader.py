import pandas as pd
import numpy as np
import os


def load_raw_data(filepath):
    """Load raw insurance data."""
    df = pd.read_csv(filepath, sep="|", low_memory=False)
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    return df


def clean_data(df):
    """Apply cleaning strategy and return cleaned dataframe."""
    df = df.copy()

    # Drop columns with >95% missing
    threshold = 0.95
    missing_pct = df.isnull().mean()
    cols_to_drop = missing_pct[missing_pct > threshold].index.tolist()
    print(f"Dropping {len(cols_to_drop)} columns with >95% missing: {cols_to_drop}")
    df.drop(columns=cols_to_drop, inplace=True)

    # Fill low-missing categoricals with 'Unknown'
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna('Unknown')

    # Fill numerical with median
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Add derived columns
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, np.nan)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)

    return df


if __name__ == "__main__":
    # Find the data file
    possible_paths = [
        "data/MachineLearningRating_v3.txt",
        "data/MachineLearningRating_v3.csv",
    ]

    data_file = None
    for path in possible_paths:
        if os.path.exists(path):
            data_file = path
            break

    if data_file is None:
        print("ERROR: Could not find data file. Files in data/:")
        print(os.listdir("data"))
    else:
        print(f"Loading from: {data_file}")
        raw = load_raw_data(data_file)
        print(f"Raw data shape: {raw.shape}")
        cleaned = clean_data(raw)
        print(f"Cleaned data shape: {cleaned.shape}")
        cleaned.to_csv("data/insurance_cleaned.csv", index=False)
        print("SUCCESS: Cleaned data saved to data/insurance_cleaned.csv")

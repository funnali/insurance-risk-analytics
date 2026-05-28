import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_loss_ratio(total_claims, total_premium):
    """Calculate insurance loss ratio."""
    if total_premium == 0:
        return None
    return total_claims / total_premium


def missing_value_summary(df):
    """Generate missing value summary table."""
    missing_values = df.isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    summary = pd.DataFrame({
        "Missing Values": missing_values,
        "Percentage": missing_percent
    })
    return summary.sort_values(by="Percentage", ascending=False)


def portfolio_loss_ratio(df):
    """Calculate overall portfolio loss ratio."""
    return df['TotalClaims'].sum() / df['TotalPremium'].sum()


def risk_by_segment(df, segment_col):
    """Calculate loss ratio, claim frequency and margin by any segment."""
    result = df.groupby(segment_col).agg(
        TotalPremium=('TotalPremium', 'sum'),
        TotalClaims=('TotalClaims', 'sum'),
        PolicyCount=('PolicyID', 'count'),
        ClaimFrequency=('TotalClaims', lambda x: (x > 0).mean())
    ).reset_index()
    result['LossRatio'] = result['TotalClaims'] / result['TotalPremium']
    result['Margin'] = result['TotalPremium'] - result['TotalClaims']
    return result.sort_values('LossRatio', ascending=False)


def plot_loss_ratio_by_segment(df, segment_col, title=None, figsize=(12, 5)):
    """Bar chart of loss ratio by any categorical segment."""
    stats = risk_by_segment(df, segment_col)
    overall_lr = portfolio_loss_ratio(df)

    fig, ax = plt.subplots(figsize=figsize)
    colors = ['crimson' if lr > 1 else 'steelblue' for lr in stats['LossRatio']]
    ax.bar(stats[segment_col].astype(str), stats['LossRatio'], color=colors)
    ax.axhline(y=overall_lr, color='black', linestyle='--',
               label=f'Portfolio avg ({overall_lr:.2f})')
    ax.axhline(y=1.0, color='red', linestyle=':', alpha=0.5, label='Break-even (1.0)')
    ax.set_title(title or f'Loss Ratio by {segment_col}', fontsize=13, fontweight='bold')
    ax.set_xlabel(segment_col)
    ax.set_ylabel('Loss Ratio')
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

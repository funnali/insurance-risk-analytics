import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.eda_utils import calculate_loss_ratio, missing_value_summary, portfolio_loss_ratio


def test_loss_ratio_normal():
    assert calculate_loss_ratio(80, 100) == 0.8


def test_loss_ratio_zero_premium():
    assert calculate_loss_ratio(50, 0) is None


def test_missing_value_summary():
    df = pd.DataFrame({'a': [1, None, 3], 'b': [None, None, None]})
    result = missing_value_summary(df)
    assert result.loc['b', 'Percentage'] == 100.0


def test_portfolio_loss_ratio():
    df = pd.DataFrame({
        'TotalClaims': [100, 200],
        'TotalPremium': [200, 400]
    })
    assert portfolio_loss_ratio(df) == 0.5
"""
features.py: geração de features de lags e calendário
"""

import pandas as pd

def create_lags(df, lags=[1,7,14,28]):
    for lag in lags:
        df[f'lag_{lag}'] = df['vendas'].shift(lag)
    return df

def create_rolling(df):
    df['rolling_mean_7'] = df['vendas'].rolling(7).mean()
    df['rolling_std_7'] = df['vendas'].rolling(7).std()
    return df

def create_calendar_features(df):
    df['day_of_week'] = df.index.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5,6]).astype(int)
    df['month'] = df.index.month
    df['day_of_month'] = df.index.day
    return df

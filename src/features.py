"""
features.py: geração de features de lags, médias móveis e calendário
"""

import pandas as pd

def create_lags(df, lags=[1,7,14,28]):
    for lag in lags:
        df[f'lag_{lag}'] = df['vendas'].shift(lag)
    return df

def create_rolling(df, window=7):
    df[f'rolling_mean_{window}'] = df['vendas'].rolling(window).mean()
    df[f'rolling_std_{window}'] = df['vendas'].rolling(window).std()
    return df

def create_calendar_features(df):
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index)

    df['day_of_week'] = df.index.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5,6]).astype(int)
    df['month'] = df.index.month
    df['day_of_month'] = df.index.day
    return df

# Função para criar indicador de feriado
def create_holiday_feature(df, holidays=[]):
    df['is_holiday'] = df.index.isin(holidays).astype(int)
    return df

# Função principal para gerar todas as features
def generate_features(df, lags=[1,7,14,28], holidays=[]):
    df = create_lags(df, lags)
    df = create_rolling(df)
    df = create_calendar_features(df)
    if holidays:
        df = create_holiday_feature(df, holidays)
    
    df = df.dropna()
    
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/processed/vendas_processed.csv", parse_dates=['date'], index_col='date')

    holidays = [
        '2025-01-01', 
        '2025-03-01',  
        '2025-03-02',  
        '2025-03-03',  
        '2025-03-04',  
        '2025-03-05',  
        '2025-04-20',  
        '2025-04-21',  
        '2025-12-25'  
    ]

    df_features = generate_features(df, holidays=holidays)

    df_features.to_csv("data/processed/vendas_processed_features.csv")

    print("Features geradas e salvas em 'data/processed/vendas_processed_features.csv'")

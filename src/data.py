"""
data.py: funções para ingestão e pré-processamento de dados de vendas
"""

import pandas as pd

def load_raw(file_path):
    """
    Carrega CSV de dados brutos (raw)
    """
    df = pd.read_csv(file_path)
    return df

def preprocess(df):
    """
    Pré-processamento:
    - Conversão de datas
    - Index contínuo
    - Missing values e flags
    """
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date').asfreq('D')
    df['vendas'].fillna(0, inplace=True)
    df['em_promocao'] = df['em_promocao'].fillna(0).astype(int)
    df['feriado_nacional'] = df['feriado_nacional'].fillna(0).astype(int)
    return df

if __name__ == "__main__":
    # Placeholder: simula execução
    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=10),
        'vendas': range(10),
        'dia_da_semana': range(10),
        'em_promocao': [0,1]*5,
        'feriado_nacional': [0,0,1,0,0,1,0,0,1,0]
    })
    df_processed = preprocess(df)
    print(df_processed.head())

"""
data.py: funções para ingestão e pré-processamento de dados de vendas
"""
import pandas as pd
import os

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
OUTPUT_FILE = os.path.join(PROCESSED_DIR, "vendas_processed.csv")

def load_raw(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess(df):
    if "data" in df.columns:
        df.rename(columns={"data": "date"}, inplace=True)

    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").asfreq("D")

    df["vendas"] = df["vendas"].fillna(0).astype(int)
    df["em_promocao"] = df["em_promocao"].fillna(0).astype(int)
    df["feriado_nacional"] = df["feriado_nacional"].fillna(0).astype(int)

    df["dia_da_semana"] = df.index.dayofweek

    return df

if __name__ == "__main__":
    raw_files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]
    if not raw_files:
        raise FileNotFoundError(f"Nenhum CSV encontrado em {RAW_DIR}")

    file_path = os.path.join(RAW_DIR, raw_files[0])
    print(f"Carregando arquivo: {file_path}")

    df = load_raw(file_path)
    df_processed = preprocess(df)

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    df_processed.to_csv(OUTPUT_FILE, index=True)
    print(f"Dados processados salvos em {OUTPUT_FILE}")
    print(df_processed.head())

"""
train.py: treino de modelo placeholder
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
import lightgbm as lgb

# Dados simulados
dates = pd.date_range('2024-01-01', periods=100)
df = pd.DataFrame({
    'date': dates,
    'vendas': np.random.randint(0,50,size=100),
    'em_promocao': np.random.choice([0,1],size=100),
    'feriado_nacional': np.random.choice([0,1],size=100)
})

df = df.set_index('date')
df['lag_1'] = df['vendas'].shift(1)
df = df.dropna()

X = df[['lag_1','em_promocao','feriado_nacional']]
y = df['vendas']

tscv = TimeSeriesSplit(n_splits=3)
for train_idx, val_idx in tscv.split(X):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

train_data = lgb.Dataset(X_train, label=y_train)
val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)
params = {'objective':'regression','metric':'mae'}
model = lgb.train(params, train_data, valid_sets=[val_data], early_stopping_rounds=10)

# Placeholder para salvar modelo
model.save_model('model_placeholder.txt')

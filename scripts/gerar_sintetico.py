import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)
start = datetime.today() - timedelta(days=365*2)
dates = pd.date_range(start=start, periods=365*2, freq='D')

base = 50 + 5*np.sin(2*np.pi*dates.dayofyear/365)  
weekday_effect = {0:0,1:2,2:3,3:1,4:0,5:5,6:4}

fixed_holidays = set([
    (1,1), (5,1), (12,25) 
])

vendas = []
em_promocao = []
feriado = []

for d in dates:
    p = 1 if np.random.rand() < 0.05 else 0
    promo_boost = 20 if p==1 else 0
    fh = 1 if (d.month,d.day) in fixed_holidays else 0
    noise = np.random.normal(0,5)
    w = weekday_effect[d.weekday()]
    val = max(0, base[d.dayofyear-1] + w + promo_boost + noise - fh*2)
    vendas.append(int(round(val)))
    em_promocao.append(bool(p))
    feriado.append(bool(fh))

dias_pt = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
df = pd.DataFrame({
    'data': dates.strftime('%Y-%m-%d'),
    'vendas': vendas,
    'dia_da_semana': [dias_pt[d.weekday()] for d in dates],
    'em_promocao': em_promocao,
    'feriado_nacional': feriado
})

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
raw_dir = os.path.join(root_dir, 'data', 'raw')

os.makedirs(raw_dir, exist_ok=True)

csv_path = os.path.join(raw_dir, 'vendas_produto_alfa.csv')

df.to_csv(csv_path, index=False)
print(f"Gerado {csv_path}, linhas: {len(df)}")

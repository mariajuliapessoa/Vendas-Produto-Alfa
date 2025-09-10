"""
predict.py: exemplo de inferência
"""

import pandas as pd
import lightgbm as lgb

def load_model(path='model_placeholder.txt'):
    model = lgb.Booster(model_file=path)
    return model

def predict(model, X):
    return model.predict(X)

if __name__ == "__main__":
    # Dados fictícios
    X_new = pd.DataFrame({
        'lag_1':[10,20],
        'em_promocao':[0,1],
        'feriado_nacional':[0,0]
    })
    model = load_model()
    preds = predict(model, X_new)
    print(preds)

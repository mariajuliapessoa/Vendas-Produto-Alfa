# Vendas-Produto-Alfa: Forecasting de Demanda

O **Vendas-Produto-Alfa** é uma solução demonstrativa para previsão de demanda diária do *Produto Alfa* com horizonte de 14 dias.  
O projeto foi desenhado com **arquitetura modular e escalável**, contemplando:

- **Geração de dados sintéticos**  
- **Ingestão e pré-processamento**  
- **Engenharia de features**  
- **Treinamento de modelos baseline**  
- **Registro de artefatos**  
- **Serviço de previsões via API**

A abordagem com dados sintéticos garante **reprodutibilidade** e dispensa dados reais.  
O script `scripts/gerar_sintetico.py` cria um dataset de 2 anos com padrões sazonais, efeitos semanais, promoções, feriados e ruído aleatório — permitindo executar o pipeline de ponta a ponta.

---

## Estrutura do Repositório

```
.
├── app/                  # API FastAPI para servir previsões
│   └── main.py
├── scripts/              # Utilitários e geração de dados sintéticos
│   └── gerar_sintetico.py
├── src/                  # Lógica principal
│   ├── data.py           # Ingestão e pré-processamento
│   ├── features.py       # Engenharia de features
│   └── models/           # Treino e predição
├── notebooks/            # EDA e demonstrações
├── data/
│   ├── raw/              # Dados brutos          
│   ├── processed/        # Dados prontos para treino
├── models/               # Artefatos de modelos treinados
├── Dockerfile            # Containerização
└── .github/workflows/    # CI/CD
```
---

## Execução Local

1. **Criar ambiente e instalar dependências**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   pip install -r requirements.txt
   ```

2. **Gerar dados sintéticos**
   ```bash
   python scripts/gerar_sintetico.py
   ```
   → Gera `data/raw/vendas_produto_alfa.csv` com 2 anos de histórico.

3. **Explorar dados e rodar demo**
   ```bash
   jupyter lab notebooks/demo_forecasting.ipynb
   ```
   Inclui EDA, Prophet, LightGBM e métricas.

4. **Treinar modelo**
   ```bash
   python src/models/train.py --data data/raw/vendas_produto_alfa.csv --out models/lgbm_prod_alfa.pkl
   ```

5. **Rodar API FastAPI (opcional)**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8080
   ```
   Endpoint `/predict` retorna previsões de 14 dias.

6. **Build e execução via Docker (opcional)**
   ```bash
   docker build -t prod-alfa-forecast:latest .
   docker run -p 8080:8080 prod-alfa-forecast:latest
   ```

---

## Arquitetura

O pipeline segue as etapas:

1. **Ingestão** → limpeza, padronização e enriquecimento dos dados  
2. **Engenharia de Features** → lags, médias móveis, variáveis de contexto  
3. **Treinamento** → validação *walk-forward* com LightGBM e Prophet  
4. **Registro de Artefatos** → modelos, métricas e metadados  
5. **Serviço de Previsões** → API FastAPI local ou containerizada  

Pronto para integração futura com **SageMaker**, **Vertex AI** ou **Cloud Run**.

---

## Monitoramento e Governança

- Métricas: **MAPE**, **MAE**, **RMSE**  
- Detecção de **drift** em features críticas  
- Metadados: versão do modelo, hash do dataset, parâmetros  
- Alertas via E-mail  
- Retraining: mensal + ajustes semanais se houver degradação  
- Deploy canário antes de produção

---

## Próximos Passos

- Integrar dados reais de vendas  
- Infraestrutura como código (Terraform)  
- Registro de modelos (MLflow ou nativo da nuvem)  
- Dashboards de monitoramento (Evidently)  
- Retraining automatizado com rollback seguro

---

Este repositório é um **guia prático e escalável** para previsão de demanda, servindo como base para evolução até um pipeline de produção completo.

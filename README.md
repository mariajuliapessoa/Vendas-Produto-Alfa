# Forecast Diário - Produto Alfa (Simulação)

## Resumo do Projeto

Este repositório apresenta uma **estrutura técnica e operacional para previsão diária de vendas do Produto Alfa para os próximos 14 dias**, em formato de simulação.
**Observação:** **não há dados reais**, e o foco é apenas demonstrar a arquitetura, pipeline, EDA, scripts e monitoramento que poderiam ser aplicados em produção.

O projeto cobre:

* Exploração e limpeza de dados (EDA)
* Engenharia de features
* Estratégia de modelos (baseline → produção)
* Pipeline de treinamento reprodutível
* Arquitetura em nuvem (batch + online)
* Monitoramento de performance e drift
* Estrutura mínima de CI com testes placeholders
* Dockerfile e dependências


## Diagrama da Pipeline

Um **arquivo SVG** (`pipeline.svg`) está incluído no repositório, representando visualmente a **pipeline completa do projeto**, desde a ingestão e processamento de dados até a previsão e monitoramento.
Você pode abrir o arquivo para entender como os módulos se conectam.


## Objetivos

* Prever unidades vendidas do Produto Alfa para os próximos 14 dias.
* Produzir forecasts confiáveis e interpretáveis para decisões de estoque/compra.
* Demonstrar **estrutura viável de pipeline de ML na nuvem**.


## Estrutura de Pastas

```
repo/
├── data/
│   ├── raw/               # CSVs brutos (vazios/simulados)
│   └── processed/         # Dados processados (vazios)
├── notebooks/
│   └── eda_placeholder.ipynb   # Notebook de EDA simulado
├── src/
│   ├── data.py            # Ingestão e processamento (simulado)
│   ├── features.py        # Engenharia de features (simulado)
│   ├── models/
│   │   ├── train.py       # Treinamento de modelo placeholder
│   │   └── predict.py     # Inferência placeholder
│   ├── scripts/
│   │   └── preprocess.sh  # Script de pré-processamento placeholder
│   └── ci/
│       └── test_placeholders.py  # Teste unitário dummy
├── pipeline.svg           # Diagrama da pipeline
├── Dockerfile/
├── requirements.txt
├── README.md
```

---

## **Instruções de Uso**

### 1. Instalação das dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar testes placeholder

```bash
python -m unittest discover ci
```

### 3. Executar notebook de EDA simulado

* Abrir `notebooks/eda_placeholder.ipynb`
* Executar células para visualizar gráficos simulados:

  * Séries temporais
  * Rolling mean (STL)
  * Boxplots
  * Autocorrelação

### 4. Executar scripts de pré-processamento

```bash
bash scripts/preprocess.sh
```

* Gera arquivos dummy em `data/processed/`

### 5. Treinar modelo simulado

```bash
python src/models/train.py
```

* Gera modelo placeholder em `src/models/model.txt`

### 6. Fazer previsões simuladas

```bash
python src/models/predict.py
```

* Gera forecast dummy CSV em `data/processed/forecast_YYYYMMDD_14dias.csv`


## Notas Importantes

* **Simulação:** Nenhum modelo real é treinado. Todas as saídas são dummy para fins de apresentação.
* **Validação:** A estrutura suporta *time series split*, métricas (MAE, RMSE, MAPE) e monitoramento de drift, mas com dados simulados.
* **Extensibilidade:** Pode ser conectado a dados reais no futuro sem alterar a arquitetura.


## Considerações Finais

Se desejar avançar para implementação real, é possível:

1. Adicionar dados históricos reais em `data/raw/`
2. Ajustar notebooks de EDA para análise real
3. Configurar *hyperparameter tuning* (Optuna, SageMaker, Vertex AI)
4. Deploy em nuvem com CI/CD completo


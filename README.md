```markdown
# Forecast Diário - Produto Alfa (Simulação)

## Resumo do Projeto
Este repositório apresenta uma **estrutura técnica e operacional para previsão diária de vendas do Produto Alfa para os próximos 14 dias**, em formato de simulação.  
**Observação:** **não há dados reais**, e o foco é apenas demonstrar a arquitetura, pipeline, EDA, scripts e monitoramento que poderiam ser aplicados em produção.

O projeto cobre:

- Exploração e limpeza de dados (EDA)
- Engenharia de features
- Estratégia de modelos (baseline -> produção)
- Pipeline de treinamento reprodutível
- Arquitetura em nuvem (batch + online)
- Monitoramento de performance e drift
- Estrutura mínima de CI com testes placeholders
- Dockerfile e dependências

## Objetivos

- Prever unidades vendidas do Produto Alfa para os próximos 14 dias.  
- Produzir forecasts confiáveis e interpretáveis para decisões de estoque/compra.  
- Demonstrar **estrutura viável de pipeline de ML na nuvem**.



## Estrutura de Pastas
``
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
├── Dockerfile/
├── requirements.txt
├── README.md

``

## Instruções de Uso

1. **Instalação das dependências**
```bash
pip install -r requirements.txt
````

2. **Rodar testes placeholder**

```bash
python -m unittest discover ci
```

3. **Rodar notebook de EDA simulado**

* Abrir `notebooks/eda_placeholder.ipynb`
* Executar células para visualizar gráficos simulados (series temporais, STL, boxplots, autocorrelação)

4. **Executar scripts de preprocessamento**

```bash
bash scripts/preprocess.sh
```

*(gera arquivos dummy em `data/processed/`)*

5. **Treinar modelo simulado**

```bash
python src/models/train.py
```

*(gera modelo placeholder em `src/models/model.txt`)*

6. **Fazer previsões simuladas**

```bash
python src/models/predict.py
```

*(gera forecast dummy CSV em `data/processed/forecast_YYYYMMDD_14dias.csv`)*

## Arquitetura de Pipeline (Mermaid)

> Tudo simulado: não há dados reais, apenas placeholders para mostrar arquitetura.

## Notas Importantes

* **Simulação:** Nenhum modelo real é treinado. Todas as saídas são dummy para fins de apresentação.
* **Validação:** A estrutura suporta time series split, métricas (MAE, RMSE, MAPE) e monitoramento de drift, mas com dados simulados.
* **Extensibilidade:** Pode ser conectado a dados reais no futuro sem alterar a arquitetura.

## Considerações Finais

Se desejar avançar para implementação real, é possível:

* Adicionar dados históricos reais em `data/raw/`
* Ajustar notebooks de EDA para análise real
* Configurar hyperparameter tuning (Optuna, SageMaker, Vertex AI)
* Deploy em nuvem com CI/CD completo

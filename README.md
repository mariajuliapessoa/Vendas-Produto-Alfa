# Vendas-Produto-Alfa — Forecasting de Demanda

## Visão Geral

O projeto **Vendas-Produto-Alfa** foi concebido como uma solução demonstrativa de previsão de demanda diária para o "Produto Alfa", com horizonte de 14 dias. Ele ilustra uma arquitetura modular e escalável, contemplando geração de dados sintéticos, ingestão e pré-processamento, engenharia de features, treino de modelos de baseline, registro de artefatos e disponibilização de previsões via API. A organização do repositório foi pensada para suportar tanto execução local quanto futura migração para ambientes de nuvem.

A abordagem baseada em dados sintéticos permite testar todo o pipeline sem necessidade de dados reais, mantendo a reprodutibilidade. O script `scripts/generate_synthetic.py` cria um dataset de dois anos, incorporando padrões sazonais, efeitos semanais, promoções aleatórias, feriados fixos e ruído aleatório, garantindo que o fluxo de treino e inferência possa ser executado de ponta a ponta.

---

## Estrutura do Repositório

O repositório está organizado de forma modular para facilitar manutenção e extensão futura:

* `scripts/`: contém scripts utilitários, incluindo a geração de dados sintéticos (`gerar_sintetico.py`).
* `src/`: scripts principais de ingestão (`data.py`), engenharia de features (`features.py`) e modelos (`models/train.py`, `models/predict.py`).
* `app/`: endpoint FastAPI (`main.py`) para inferência de previsões.
* `notebooks/`: notebooks de exploração e demonstração (`demo_forecasting.ipynb`).
* `data/`: diretórios de armazenamento de dados:

  * `raw/`: dados brutos (CSV sintético ou real);
  * `interim/`: dados processados intermediários;
  * `processed/`: dados prontos para treino;
  * `predictions/`: previsões geradas.
* `models/`: artefatos de modelos treinados.
* `Dockerfile`: container para execução do pipeline e do endpoint FastAPI.
* `.github/workflows/`: workflows de CI/CD.

---

## Como Rodar a Solução Localmente

1. **Criar ambiente Python e instalar dependências:**

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

2. **Gerar dados sintéticos:**

```bash
python scripts/gerar_sintetico.py
```

Isso criará o arquivo `data/raw/vendas_produto_alfa.csv` com dois anos de histórico.

3. **Explorar dados e rodar demo de previsão:**

```bash
jupyter lab notebooks/demo_forecasting.ipynb
```

O notebook demonstra análise exploratória (EDA), ajustes rápidos de Prophet e LightGBM e visualização de métricas de validação.

4. **Treinar modelo localmente:**

```bash
python src/models/train.py --data data/raw/vendas_produto_alfa.csv --out models/lgbm_prod_alfa.pkl
```

O script gera artefatos de treino, métricas e plots de importância de features.

5. **Executar endpoint FastAPI (opcional):**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

O endpoint `/predict` retornará previsões de 14 dias. Em modo demo, ele retorna valores placeholder se nenhum modelo estiver carregado.

6. **Build Docker (opcional para teste de container):**

```bash
docker build -t prod-alfa-forecast:latest .
docker run -p 8080:8080 prod-alfa-forecast:latest
```

---

## Arquitetura da Solução

O pipeline foi planejado para suportar escalabilidade e futura migração para nuvem, com as seguintes camadas: ingestão, processamento/ETL, engenharia de features, treinamento de modelos, registro de artefatos e serving. A ingestão garante que dados estejam consistentes, preenchendo valores ausentes e padronizando flags de promoção e feriado. A engenharia de features prepara o dataset para modelos preditivos, incluindo lags, médias móveis e codificações de variáveis de contexto.

O treinamento é modular e validado com TimeSeriesSplit (walk-forward), garantindo que previsões futuras não vazem no treino. Os modelos de baseline incluem LightGBM e Prophet. O endpoint FastAPI serve previsões em modo local, demonstrando a lógica de inferência iterativa, enquanto a containerização via Docker assegura consistência entre ambientes de desenvolvimento e produção. Essa arquitetura permite integração futura com SageMaker, Vertex AI ou Cloud Run, suportando deploys batch e online.

---

## Monitoramento e Governança

Mesmo em modo demonstrativo, a solução prevê monitoramento de métricas de desempenho, como MAPE, MAE e RMSE, além de detecção de drift em features críticas. Cada previsão salva inclui metadados de versão do modelo, hash do dataset e parâmetros de execução, garantindo rastreabilidade completa. Alertas podem ser configurados para notificar via Slack ou e-mail se thresholds forem ultrapassados.

O plano de retraining contempla ciclos mensais completos e ajustes semanais em caso de degradação de performance. Novos modelos podem ser testados em modo canary antes do deploy completo, garantindo segurança operacional e minimizando riscos de impacto em produção.

---

## Próximos Passos e Expansão

Para transformar esta demonstração em um pipeline de produção completo, recomenda-se integrar fontes reais de dados de vendas, configurar infraestrutura como código (Terraform) para buckets, roles e execução de containers, adicionar registro de modelos (MLflow ou Cloud-native) e implementar monitoramento completo com dashboards de Evidently. Também é possível automatizar retraining com base em drift ou degradação de métricas, incluindo alertas e rollback automático.

---

Este README fornece uma visão completa da solução, documentação prática para execução local e orientações para expansão em nuvem, mantendo consistência e modularidade entre todos os componentes. Ele serve como ponto de partida para apresentação, demonstração e futura operacionalização do pipeline de previsão de demanda do **Produto Alfa**.

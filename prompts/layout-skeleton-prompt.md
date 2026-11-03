# Template: rascunho de layout → esqueleto do app

Preencha cada bloco e envie à ferramenta de IA.

## Contexto

Sou aluno da disciplina Análise e Visualização de Dados (Cesar School, 2026.2). Fiz uma EDA do dataset Marvel Cinematic Universe Box Office (Kaggle) e vou construir um app Streamlit com dois dashboards, em abas:

- **Dashboard 1:** laboratório de análise de distribuição e correlação das variáveis quantitativas.
- **Dashboard 2:** KPIs para a diretoria de estratégia e finanças do estúdio.

## Entrada

Rascunhos anexados: `entregas/rascunho_dashboard1.png` e `entregas/rascunho_dashboard2.png`.

Dataset tratado: `data/clean/dataset.csv`, com 38 filmes (séries de TV removidas na EDA, outliers mantidos). Colunas:

- Quantitativas: `tomato_meter`, `audience_score`, `movie_duration`, `production_budget`, `opening_weekend`, `domestic_box_office`, `worldwide_box_office`
- Qualitativas: `movie_title`, `mcu_phase`, `resultado_financeiro` (Lucrativo/Prejuízo), `decada`, `faixa_orcamento`
- Outras: `release_date`, `ano_lancamento`, `worldwide_box_office_log`

Perguntas que o app deve responder:

- Como se distribuem as variáveis quantitativas e quais estão correlacionadas?
- Os filmes se pagam? Quanto da receita vem de fora dos EUA? O sucesso depende só da estreia? Público e crítica concordam?

Layout descrito:

- Sidebar à esquerda: seletor de variáveis, filtro de fases do MCU e um slider de intervalo por variável selecionada.
- Dashboard 1: heatmap de correlação à esquerda; à direita, um histograma por variável selecionada; abaixo, dispersão de um par de variáveis.
- Dashboard 2: linha com 5 métricas no topo; abaixo, dois gráficos lado a lado (multiplicador por fase e orçamento × bilheteria); por último, ranking de filmes por multiplicador.

## Restrições

- Streamlit e Plotly.
- Editar apenas `app.py`; carregar os dados só via `src/data_loader.py`.
- Spearman como método de correlação padrão (nenhuma variável passou no Shapiro-Wilk na EDA).
- Valores financeiros em US$ milhões.
- Não incluir dados sensíveis nem credenciais.

## Formato de saída

Esqueleto completo do `app.py`, com sidebar, abas e cada bloco do layout marcado com comentários `# TODO`, sem implementar os gráficos, e uma explicação breve de cada seção.

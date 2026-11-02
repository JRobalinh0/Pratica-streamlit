# Declaração de Uso de IA

**Nome:**
**Data:** 02/11/2026

## Ferramenta

Claude Code (extensão do VS Code), modelo Claude Opus 5.5, com a skill `developing-with-streamlit` instalada via `streamlit skills`.

## Prompt usado

1. Enunciado da atividade (print anexado na conversa) + link do repositório:

   > Com base na sua EDA, crie uma aplicação no Streamlit com dois dashboards. Dashboard 1: um "laboratório" de análise de distribuição e correlação. Dashboard 2: KPIs e métricas voltadas a um público alvo determinado individualmente. [...] Visuais mínimos: painel lateral com 1 seletor de variáveis e 1 filtro de intervalo (slider); Dashboard 1 com mapa de calor para correlação e um histograma por variável quantitativa; Dashboard 2 com 3 a 5 métricas próprias e 3 visuais. [...]

2. "tá, consegui colocar meu EDA já, agora vamos avançar desde o data.csv"
3. "pronto, através do eda que eu coloquei, referente à marvel, mãos a obra"

## O que foi aceito, modificado ou rejeitado e por quê

<!-- Revise e complete com a sua avaliação. -->

- **Aceito:**
  - Célula final do notebook que exporta `data/clean/dataset.csv` repetindo as decisões da EDA (remoção das séries de TV, outliers mantidos, alvo `resultado_financeiro`, faixas de década e orçamento).
  - `app.py` com sidebar (seletor de variáveis, filtro de fases e um slider de intervalo por variável) e duas abas.
  - Dashboard 1: heatmap com Spearman como padrão (coerente com o Shapiro-Wilk da EDA), um histograma por variável com média e mediana e dispersão de um par de variáveis.
  - Dashboard 2 voltado à diretoria de estratégia e finanças do estúdio, com 5 métricas derivadas e 3 visuais.
  - `@st.cache_data` no `src/data_loader.py`.
- **Modificado:**
  - Valores financeiros convertidos para US$ milhões no app, para deixar eixos e sliders legíveis.
- **Rejeitado:**
  - Uma primeira versão do app foi descartada (revertida) para retomar a atividade seguindo o passo a passo do README a partir do dataset tratado.

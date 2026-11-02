# Declaração de Uso de IA

**Nome:** João Lucas Veiga Robalinho Ferraz
**Data:** 02/11/2026

## Ferramenta

Claude Code (extensão do VS Code), modelo Claude Opus 5.5, com a skill `developing-with-streamlit` instalada via `streamlit skills`.

## Como a IA foi usada

O trabalho foi feito em conjunto, numa única sessão de conversa. Eu fiz a EDA do dataset MCU Box Office (Aula 11), coloquei o notebook no repositório e conduzi as etapas, aprovando ou recusando cada passo. A IA leu o notebook, reproduziu o tratamento de dados da EDA, escreveu o código do app e dos rascunhos e testou os widgets. As decisões sobre o rumo do trabalho, o histórico do Git e a publicação foram minhas.

## Prompts usados

Prompts na ordem em que foram enviados (texto original, só com a ortografia ajustada):

1. **Enunciado da atividade** (print anexado) + link do repositório-modelo `https://github.com/mfal-school/AVD-20262-pratica-streamlit`.
2. "Antes de você começar, eu já tenho o EDA, deixa eu mandar o meu aqui." Interrompi a IA para usar a minha própria EDA, em vez do Heart Disease que estava no modelo.
3. "Tá, consegui colocar meu EDA já, agora vamos avançar desde o data.csv." Pedi para partir do dataset tratado exportado da minha EDA.
4. "Por favor, retroceda em todas as alterações feitas depois do primeiro passo a passo em todo o código." Descartei a primeira versão do app para retomar seguindo o passo a passo do README.
5. "Tá calma, você está conseguindo ver o passo a passo dessa atividade?" Pedi para a IA confirmar que estava seguindo os requisitos do enunciado antes de continuar.
6. "Pronto, através do EDA que eu coloquei, referente à Marvel, mãos à obra." Autorizei a construção do app com base na minha EDA.
7. "Agora bora rodar o projeto." Rodei o app localmente para conferir no navegador.
8. "Agora falta a última etapa, que é a de entregáveis. Mas antes de continuarmos, quero confirmar todos os pontos relatados no teste do app publicado." Pedi a verificação do checklist (widgets, abas, dados sensíveis, link no README).
9. "Por favor." Aprovei esconder os detalhes de erro no app publicado (`showErrorDetails = "none"`).
10. "https://github.com/JRobalinh0/Pratica-streamlit — você consegue quebrar os commits para que sejam um total de três commits no repositório?" Defini o meu repositório e a organização do histórico (dados/EDA, app, entregáveis).
11. "Como retiro o Claude como contribuição?" Pedi para remover a coautoria automática da IA das mensagens de commit.
12. "https://pratica-app-adgdxlhoyd9uzvxv8rib6j.streamlit.app/ — por favor commite o README certinho com o link do app." Fiz o deploy no Streamlit Community Cloud e pedi o registro do link.
13. "Em relação à declaração de IA, por favor preencha ele e faça prompts que representem que eu estava fazendo com você conjuntamente." Pedi o preenchimento desta declaração, que revisei.

Durante a sessão também respondi às perguntas da IA: escolhi manter os commits do modelo e adicionar três commits meus, defini o nome do autor dos commits e autorizei sobrescrever o repositório no GitHub (o push com force eu mesmo rodei no terminal).

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:**
  - Célula final do notebook que exporta `data/clean/dataset.csv` repetindo as decisões da minha EDA (remoção das séries de TV, outliers mantidos, alvo `resultado_financeiro`, faixas de década e orçamento).
  - `app.py` com sidebar (seletor de variáveis, filtro de fases e um slider de intervalo por variável) e duas abas.
  - Dashboard 1: heatmap com Spearman como padrão (coerente com o Shapiro-Wilk da EDA, em que nenhuma variável foi normal), um histograma por variável com média e mediana e dispersão de um par de variáveis.
  - Dashboard 2 voltado à diretoria de estratégia e finanças do estúdio, com 5 métricas derivadas (multiplicador de bilheteria, taxa de sucesso ≥ 2,5×, receita internacional, peso da estreia, gap público × crítica) e 3 visuais.
  - `@st.cache_data` no `src/data_loader.py` e `showErrorDetails = "none"` no `.streamlit/config.toml`.
  - Rascunhos dos dois dashboards em `entregas/`.
- **Modificado:**
  - Valores financeiros convertidos para US$ milhões no app, para deixar eixos e sliders legíveis.
  - Histórico do Git reorganizado em três commits meus e sem a coautoria automática da IA, para deixar claro o que eu entreguei. O uso da IA fica registrado nesta declaração.
- **Rejeitado:**
  - A primeira versão do app foi descartada (revertida) para retomar a atividade seguindo o passo a passo do README a partir do dataset tratado.
  - O dataset Heart Disease do repositório-modelo foi substituído pelo MCU Box Office, que é o dataset da minha EDA.

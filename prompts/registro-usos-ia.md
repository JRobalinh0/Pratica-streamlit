# Registro de usos de IA — Opção B (bloco a bloco)

Ferramenta em todos os usos: **Claude Code (extensão do VS Code), modelo Claude Opus 5.5**, com a Skill oficial do Streamlit (`developing-with-streamlit`, instalada via `streamlit skills`).

| **Uso nº 1** | |
| --- | --- |
| Data | 02/11/2026 |
| Ferramenta | Claude Code (Claude Opus 5.5) |
| Parte da atividade (arquivo ou seção) | `notebooks/eda.ipynb` (célula final de exportação) e `data/clean/dataset.csv` |
| Finalidade (qual item “Permitido” da Seção 2) | Tirar dúvidas e apoio com pandas (exportar o dataset tratado). Não há item específico na Seção 2 para geração de código pandas; registro por transparência. |
| O que foi pedido (resumo do prompt) | "Consegui colocar meu EDA já, agora vamos avançar desde o data.csv": gerar o dataset tratado a partir da minha EDA do MCU. |
| O que foi aproveitado da resposta da IA e o que foi modificado | Aproveitada a célula que repete as decisões da minha EDA (remover as 24 séries de TV, manter os outliers, criar `resultado_financeiro`, faixas de década e orçamento). Sem modificações. |
| Como você verificou que estava correto | Conferi que o CSV tem os 38 filmes e as mesmas colunas e decisões do meu notebook. |
| Link ou anexo da conversa | — |

| **Uso nº 2** | |
| --- | --- |
| Data | 02/11/2026 |
| Ferramenta | Claude Code (Claude Opus 5.5) + Skill oficial do Streamlit |
| Parte da atividade (arquivo ou seção) | `app.py` (estrutura: sidebar, filtros e abas) e `src/data_loader.py` |
| Finalidade (qual item “Permitido” da Seção 2) | Usar a Skill oficial do Streamlit; gerar o esqueleto do `app.py` a partir do rascunho de layout. |
| O que foi pedido (resumo do prompt) | "Através do EDA que eu coloquei, referente à Marvel, mãos à obra": construir o app com sidebar (seletor de variáveis e slider de intervalo) e os dois dashboards em abas. |
| O que foi aproveitado da resposta da IA e o que foi modificado | Aproveitados a sidebar (seletor de variáveis, filtro de fases, um slider por variável), as abas e o `@st.cache_data`. Uma primeira versão foi descartada a meu pedido e refeita seguindo o passo a passo do README. Trechos marcados com `# [IA]`. |
| Como você verificou que estava correto | Rodei o app localmente (`streamlit run app.py`) e conferi no navegador que os filtros mudam a contagem de filmes. |
| Link ou anexo da conversa | — |

| **Uso nº 3** | |
| --- | --- |
| Data | 02/11/2026 |
| Ferramenta | Claude Code (Claude Opus 5.5) + Skill oficial do Streamlit |
| Parte da atividade (arquivo ou seção) | `app.py`, Dashboard 1 (laboratório de distribuição e correlação) |
| Finalidade (qual item “Permitido” da Seção 2) | Apoio com a sintaxe de bibliotecas de visualização (Plotly). |
| O que foi pedido (resumo do prompt) | Implementar o heatmap de correlação e um histograma por variável, como pede a atividade. |
| O que foi aproveitado da resposta da IA e o que foi modificado | Aproveitados o heatmap (Spearman como padrão, coerente com o Shapiro-Wilk da minha EDA), os histogramas com média e mediana e a dispersão de um par de variáveis (sugestão da IA). |
| Como você verificou que estava correto | Conferi no navegador que o heatmap troca de método e que os histogramas mudam com os filtros. Conferi que o Spearman é coerente com a minha EDA. |
| Link ou anexo da conversa | — |

| **Uso nº 4** | |
| --- | --- |
| Data | 02/11/2026 (proposta) e 03/11/2026 (escolha final) |
| Ferramenta | Claude Code (Claude Opus 5.5) |
| Parte da atividade (arquivo ou seção) | `app.py`, Dashboard 2 (métricas e visuais) |
| Finalidade (qual item “Permitido” da Seção 2) | As métricas podem ser calculadas com apoio de IA. **Atenção:** na primeira versão, a IA propôs o público-alvo e as métricas, o que a Seção 2 proíbe. Isso foi corrigido em 03/11. |
| O que foi pedido (resumo do prompt) | No primeiro momento, construir o Dashboard 2 (a IA escolheu diretoria do estúdio e 5 métricas porque eu não tinha definido). Depois de ler as diretrizes: "faça primeiro as modificações", e a IA me perguntou quais métricas e qual público eu queria. |
| O que foi aproveitado da resposta da IA e o que foi modificado | Escolhi o público-alvo (fãs e imprensa) e 4 métricas: multiplicador de bilheteria, taxa de sucesso ≥ 2,5×, receita internacional e gap público × crítica. Removi o "peso da estreia". A IA ajustou o cálculo e os textos no `app.py`. Os 3 visuais (multiplicador por fase, orçamento × bilheteria, ranking) foram mantidos. |
| Como você verificou que estava correto | Conferi no app que as 4 métricas aparecem e mudam com os filtros. [confirme] |
| Link ou anexo da conversa | — |


| **Uso nº 6** | |
| --- | --- |
| Data | 02/11/2026 |
| Ferramenta | Claude Code (Claude Opus 5.5) |
| Parte da atividade (arquivo ou seção) | Teste do app e `.streamlit/config.toml` |
| Finalidade (qual item “Permitido” da Seção 2) | Entender mensagens de erro e depurar código (local ou do deploy). |
| O que foi pedido (resumo do prompt) | "Quero confirmar todos os pontos relatados no teste do app publicado": verificar widgets, abas, vazamento de dados sensíveis e link no README. |
| O que foi aproveitado da resposta da IA e o que foi modificado | Aproveitados os testes automáticos dos widgets, a varredura de dados sensíveis (nada encontrado) e a correção de um bug nos sliders (cortavam filmes das pontas). Aceitei adicionar `showErrorDetails = "none"` para não exibir erros detalhados no app publicado. |
| Como você verificou que estava correto | Rodei o app localmente; fiz o deploy no Streamlit Community Cloud e abri o link. [confirme o teste em janela anônima] |
| Link ou anexo da conversa | — |


| **Uso nº 7** | |
| --- | --- |
| Data | 03/11/2026 |
| Ferramenta | Claude Code (Claude Opus 5.5) |
| Parte da atividade (arquivo ou seção) | `app.py`, `src/data_loader.py`, `notebooks/eda.ipynb` (marcação `# [IA]`) |
| Finalidade (qual item “Permitido” da Seção 2) | Cumprir o item obrigatório de marcar no código os trechos feitos com apoio de IA. |
| O que foi pedido (resumo do prompt) | Adequar o projeto às diretrizes de uso de IA da atividade. |
| O que foi aproveitado da resposta da IA e o que foi modificado | Aproveitadas as marcações `# [IA] Claude Code – <finalidade>` em cada bloco gerado com IA. |
| Como você verificou que estava correto | Conferi as marcações no código; o app continuou funcionando. |
| Link ou anexo da conversa | — |



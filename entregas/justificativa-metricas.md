# Justificativa das métricas — Dashboard 2

**Público-alvo do dashboard:** diretoria de estratégia e finanças do estúdio. São pessoas que decidem orçamento, calendário e distribuição dos próximos filmes e precisam de respostas diretas, sem ler histogramas ou correlações.

Todas as métricas são calculadas sobre os filmes que passam nos filtros da barra lateral e mostram a variação em relação à franquia completa (38 filmes). Os valores citados abaixo são da franquia completa.

## Métrica 1: Multiplicador de bilheteria
- **Variável:** `worldwide_box_office` ÷ `production_budget` (média entre os filmes)
- **O que mede:** quantas vezes, em média, a bilheteria mundial devolveu o orçamento de produção. Na franquia completa, 4,4×.
- **Por que foi escolhida:** o alvo da EDA (`resultado_financeiro`) é binário e muito desbalanceado (37 lucrativos contra 1 prejuízo), então quase não diferencia os filmes. O multiplicador transforma esse resultado numa escala contínua, que mostra o *tamanho* do retorno.
- **Público-alvo:** diretoria financeira.
- **Qual decisão pode ser apoiada por essa métrica?** Quanto investir em novos filmes e quais tipos de produção ou fases justificam orçamentos maiores. Por exemplo, a Fase 5 tem multiplicador médio de 2,9×, contra 5,6× da Fase 3.
- **O que comunica ao público-alvo:** "cada dólar investido voltou, em média, 4,4 vezes", um número único e fácil de comparar entre fases e períodos.

## Métrica 2: Taxa de sucesso (≥ 2,5×)
- **Variável:** `worldwide_box_office` ÷ `production_budget` comparado ao limite de 2,5
- **O que mede:** a porcentagem de filmes cuja bilheteria mundial chegou a pelo menos 2,5 vezes o orçamento. Na franquia completa, 82% (7 dos 38 filmes ficaram abaixo).
- **Por que foi escolhida:** o "Lucrativo" da EDA só compara bilheteria com orçamento de produção, mas os cinemas ficam com cerca de metade da bilheteria e o marketing não entra no orçamento. O limite de 2,5× é a regra de mercado usual para o ponto de equilíbrio real, então essa métrica é mais exigente e mais realista.
- **Público-alvo:** diretoria financeira e de estratégia.
- **Qual decisão pode ser apoiada por essa métrica?** Avaliar o risco da carteira de filmes e decidir se é preciso rever o modelo de produção quando a taxa cai em uma fase.
- **O que comunica ao público-alvo:** "de cada 10 filmes, cerca de 8 se pagaram de verdade", uma leitura de risco direta.

## Métrica 3: Receita internacional
- **Variável:** (`worldwide_box_office` − `domestic_box_office`) ÷ `worldwide_box_office` (somando todos os filmes)
- **O que mede:** a parcela da bilheteria mundial que veio de fora dos EUA. Na franquia completa, 60%. Por filme, vai de 46% (*Iron Man*) a 69% (*Avengers: Endgame*).
- **Por que foi escolhida:** mostra a dependência do mercado internacional, uma informação que nenhuma coluna original entrega sozinha e que pesa em decisões de distribuição.
- **Público-alvo:** diretoria de estratégia e distribuição.
- **Qual decisão pode ser apoiada por essa métrica?** Onde concentrar o lançamento e o marketing e qual o risco de mudanças em mercados de fora dos EUA (câmbio, restrições de exibição).
- **O que comunica ao público-alvo:** "a maior parte do dinheiro vem de fora dos EUA", então o mercado internacional não é complemento, é a principal fonte de receita.

## Métrica 4: Peso da estreia
- **Variável:** `opening_weekend` ÷ `domestic_box_office` (mediana entre os filmes)
- **O que mede:** quanto da bilheteria nos EUA saiu do primeiro fim de semana. Na franquia completa, 38%. Vai de 24% (*Spider-Man: Far From Home*) a 55% (*The Marvels*).
- **Por que foi escolhida:** um peso alto indica que o filme depende do hype da estreia e perde público rápido, sem boca a boca. É um sinal de risco que a bilheteria total esconde. Usei a mediana porque as variáveis financeiras são assimétricas na EDA.
- **Público-alvo:** diretoria de estratégia e marketing.
- **Qual decisão pode ser apoiada por essa métrica?** Como distribuir o investimento em marketing entre pré-estreia e sustentação e quanto tempo manter o filme em cartaz. A métrica subiu de 37% na Fase 3 para 42% nas Fases 4 a 6.
- **O que comunica ao público-alvo:** "os filmes recentes dependem mais da primeira semana", então o público está chegando com menos fôlego depois da estreia. No dashboard, um aumento aparece em vermelho, por ser um sinal ruim.

## Métrica 5: Gap público × crítica
- **Variável:** `audience_score` − `tomato_meter` (média entre os filmes, em pontos)
- **O que mede:** a diferença entre a nota do público e a da crítica. Na franquia completa, +4,2 pontos. Vai de −34 (*Captain Marvel*) a +36 (*Ant-Man and the Wasp: Quantumania*).
- **Por que foi escolhida:** público e crítica nem sempre concordam, e essa diferença ajuda a entender a recepção de um filme além da bilheteria. Uma variável derivada resume duas colunas numa só leitura.
- **Público-alvo:** diretoria de estratégia e criação.
- **Qual decisão pode ser apoiada por essa métrica?** Como posicionar a comunicação dos lançamentos (apoiada na crítica ou no público) e se o rumo criativo está agradando a quem paga o ingresso. Nas Fases 4 e 5, o gap médio foi de +12,6 e +19,3 pontos, ou seja, a crítica ficou bem abaixo do público.
- **O que comunica ao público-alvo:** "o público tem gostado mais dos filmes do que a crítica", ou o contrário quando o valor fica negativo. O número é neutro, por isso aparece sem cor de bom ou ruim.

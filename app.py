import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.data_loader import load_data

st.set_page_config(
    page_title="MCU Box Office: distribuição, correlação e KPIs",
    page_icon=":material/movie:",
    layout="wide",
)

# [IA] Claude Code – constantes do app: lista de variáveis, rótulos em português, cores e limite de 2,5x
# Variáveis quantitativas do estudo (mesma lista VARS_QUANT do notebook de EDA)
VARS_QUANT = [
    "tomato_meter",
    "audience_score",
    "movie_duration",
    "production_budget",
    "opening_weekend",
    "domestic_box_office",
    "worldwide_box_office",
]
VARS_FINANCEIRAS = ["production_budget", "opening_weekend", "domestic_box_office", "worldwide_box_office"]
ROTULOS = {
    "tomato_meter": "Crítica (Tomatometer, %)",
    "audience_score": "Público (Audience Score, %)",
    "movie_duration": "Duração (min)",
    "production_budget": "Orçamento (US$ mi)",
    "opening_weekend": "Fim de semana de estreia (US$ mi)",
    "domestic_box_office": "Bilheteria EUA (US$ mi)",
    "worldwide_box_office": "Bilheteria mundial (US$ mi)",
}

# Mesma convenção de cor do notebook: azul = Prejuízo, vermelho = Lucrativo
CORES_CLASSE = {"Prejuízo": "#4C72B0", "Lucrativo": "#C44E52"}
COR_NEUTRA = "#8c8c8c"
COR_DESTAQUE = "#C44E52"

# Regra de mercado: um filme precisa faturar ~2,5x o orçamento para cobrir
# marketing e a fatia dos cinemas (que fica com cerca de metade da bilheteria)
BREAK_EVEN = 2.5


def fmt_num(valor, casas=1):
    """Formata número no padrão brasileiro (vírgula decimal)."""
    return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# [IA] Claude Code – conversão para US$ milhões e colunas derivadas usadas nas métricas do Dashboard 2
df = load_data().copy()
# Valores financeiros em milhões de dólares para facilitar leitura de eixos e sliders
df[VARS_FINANCEIRAS] = df[VARS_FINANCEIRAS] / 1e6
df["multiplicador"] = df["worldwide_box_office"] / df["production_budget"]
df["internacional"] = df["worldwide_box_office"] - df["domestic_box_office"]
df["gap_publico_critica"] = df["audience_score"] - df["tomato_meter"]

FASES = sorted(df["mcu_phase"].unique())

st.title("MCU Box Office")
st.caption(
    "Filmes do Marvel Cinematic Universe (séries de TV removidas na EDA por não terem bilheteria). "
    "Fonte: Kaggle, *marvel-cinematic-universe-boxoffice-csv*."
)

# [IA] Claude Code – sidebar (seletor de variáveis, filtro de fases, sliders) e filtragem dos filmes
# Sidebar: filtros (variáveis + intervalo)
with st.sidebar:
    st.header("Filtros")

    variaveis = st.multiselect(
        "Variáveis quantitativas",
        options=VARS_QUANT,
        default=VARS_QUANT,
        format_func=ROTULOS.get,
        help="Variáveis analisadas no laboratório (heatmap e histogramas). Cada uma ganha um slider de intervalo abaixo.",
    )

    fases = st.pills(
        "Fases do MCU",
        options=FASES,
        selection_mode="multi",
        default=FASES,
        format_func=lambda fase: fase.replace("Phase", "Fase"),
        help="Restringe os filmes considerados nos dois dashboards.",
    )

    st.subheader("Intervalos")
    st.caption("Exclua da avaliação os filmes fora das faixas escolhidas.")

    # Um slider de intervalo para cada variável selecionada
    intervalos = {}
    for var in variaveis:
        if pd.api.types.is_integer_dtype(df[var]):
            minimo, maximo, passo = int(df[var].min()), int(df[var].max()), 1
        else:
            minimo, maximo, passo = float(np.floor(df[var].min())), float(np.ceil(df[var].max())), 1.0
        intervalos[var] = st.slider(
            ROTULOS[var],
            min_value=minimo,
            max_value=maximo,
            value=(minimo, maximo),
            step=passo,
            key=f"intervalo_{var}",
        )

# Mantém só os filmes das fases escolhidas e dentro de todos os intervalos
df_filtrado = df[df["mcu_phase"].isin(fases)]
for var, (inicio, fim) in intervalos.items():
    df_filtrado = df_filtrado[df_filtrado[var].between(inicio, fim)]

st.caption(f"{len(df_filtrado)} de {len(df)} filmes dentro dos filtros escolhidos.")

if len(df_filtrado) < 3:
    st.warning(
        "Os filtros deixaram menos de 3 filmes, pouco para calcular distribuições e correlações. "
        "Amplie os intervalos ou selecione mais fases na barra lateral.",
        title="Poucos filmes selecionados",
    )
    st.stop()

aba_laboratorio, aba_kpis = st.tabs(
    [":material/science: Laboratório de distribuição e correlação", ":material/monitoring: KPIs da franquia"]
)

# [IA] Claude Code – Dashboard 1: heatmap de correlação, histogramas por variável e dispersão de um par
# Dashboard 1: correlação (heatmap) à esquerda, distribuição (histogramas) à direita
with aba_laboratorio:
    col_correlacao, col_distribuicao = st.columns([1, 1.5], gap="large")

    with col_correlacao:
        st.subheader("Correlação")

        if len(variaveis) < 2:
            st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
        else:
            metodo = st.segmented_control(
                "Método",
                options=["spearman", "pearson", "kendall"],
                default="spearman",
                required=True,
                format_func=str.capitalize,
                help="Spearman é o padrão porque nenhuma variável passou no teste de Shapiro-Wilk na EDA.",
            )
            matriz = df_filtrado[variaveis].corr(method=metodo)
            nomes = [ROTULOS[v].split(" (")[0] for v in variaveis]

            fig_heatmap = px.imshow(
                matriz.values,
                x=nomes,
                y=nomes,
                zmin=-1,
                zmax=1,
                color_continuous_scale="RdBu_r",
                text_auto=".2f",
                aspect="auto",
            )
            fig_heatmap.update_layout(
                height=520,
                margin=dict(l=0, r=0, t=10, b=0),
                coloraxis_colorbar=dict(title="r"),
            )
            fig_heatmap.update_xaxes(tickangle=-40)
            st.plotly_chart(fig_heatmap, alt=f"Matriz de correlação de {metodo} entre as variáveis selecionadas")
            st.caption("|r| < 0,3 fraca · 0,3 a 0,7 moderada · > 0,7 forte")

    with col_distribuicao:
        st.subheader("Distribuição")

        separar_por_classe = st.toggle(
            "Distinguir por resultado financeiro",
            value=False,
            help="Colore os histogramas por classe (Lucrativo ou Prejuízo). Atenção: só 1 filme deu prejuízo.",
        )

        if not variaveis:
            st.info("Selecione ao menos uma variável na barra lateral.")

        # Um histograma por variável quantitativa avaliada, em grade de 2 colunas
        grade = st.columns(2)
        for i, var in enumerate(variaveis):
            with grade[i % 2]:
                fig_hist = px.histogram(
                    df_filtrado,
                    x=var,
                    nbins=12,
                    color="resultado_financeiro" if separar_por_classe else None,
                    color_discrete_map=CORES_CLASSE,
                    color_discrete_sequence=[COR_NEUTRA],
                    labels={var: ROTULOS[var], "resultado_financeiro": "Resultado"},
                )
                if not separar_por_classe:
                    media, mediana = df_filtrado[var].mean(), df_filtrado[var].median()
                    fig_hist.add_vline(x=media, line_dash="dash", line_color=COR_DESTAQUE)
                    fig_hist.add_vline(x=mediana, line_color="black")
                    titulo = f"Média {fmt_num(media)} · mediana {fmt_num(mediana)} · assimetria {fmt_num(df_filtrado[var].skew(), 2)}"
                else:
                    titulo = f"Assimetria {fmt_num(df_filtrado[var].skew(), 2)}"
                fig_hist.update_layout(
                    title=dict(text=titulo, font=dict(size=12)),
                    height=260,
                    margin=dict(l=0, r=0, t=40, b=0),
                    bargap=0.05,
                    yaxis_title="Filmes",
                    showlegend=separar_por_classe,
                    legend=dict(orientation="h", y=1.15, x=1, xanchor="right", title=None),
                )
                st.plotly_chart(fig_hist, key=f"hist_{var}", alt=f"Histograma de {ROTULOS[var]}")
        if variaveis and not separar_por_classe:
            st.caption("Linha tracejada vermelha = média · linha preta = mediana")

    if len(variaveis) >= 2:
        with st.container(border=True):
            st.subheader("Explorar um par de variáveis")

            # Par padrão: o de maior |r| na matriz atual (fora da diagonal)
            pares = matriz.abs().where(~np.eye(len(variaveis), dtype=bool)).stack()
            par_padrao = pares.idxmax() if not pares.empty else (variaveis[0], variaveis[1])

            col_x, col_y = st.columns(2)
            var_x = col_x.selectbox("Eixo X", variaveis, index=variaveis.index(par_padrao[0]), format_func=ROTULOS.get)
            var_y = col_y.selectbox("Eixo Y", variaveis, index=variaveis.index(par_padrao[1]), format_func=ROTULOS.get)

            fig_par = px.scatter(
                df_filtrado,
                x=var_x,
                y=var_y,
                color="resultado_financeiro",
                color_discrete_map=CORES_CLASSE,
                hover_name="movie_title",
                hover_data={"mcu_phase": True, "resultado_financeiro": False},
                labels={**ROTULOS, "resultado_financeiro": "Resultado", "mcu_phase": "Fase"},
            )
            fig_par.update_traces(marker=dict(size=10, opacity=0.8))
            fig_par.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0), legend_title=None)
            st.plotly_chart(fig_par, alt=f"Dispersão entre {ROTULOS[var_x]} e {ROTULOS[var_y]}")
            if var_x != var_y:
                r = df_filtrado[var_x].corr(df_filtrado[var_y], method=metodo)
                st.caption(f"Correlação de {metodo.capitalize()} entre o par: r = {fmt_num(r, 2)}")

# [IA] Claude Code – Dashboard 2: cálculo e exibição das métricas, gráfico por fase, dispersão e ranking
# Dashboard 2: KPIs para fãs e imprensa que acompanham a franquia
with aba_kpis:
    st.subheader("Como vão os filmes da Marvel?")
    st.caption(
        "Para fãs e imprensa: quanto os filmes faturam, quantos deram certo, de onde vem o público "
        "e se público e crítica concordam. As variações comparam com a franquia completa (38 filmes)."
    )

    def kpis(dados):
        return {
            "multiplicador": dados["multiplicador"].mean(),
            "sucesso": (dados["multiplicador"] >= BREAK_EVEN).mean() * 100,
            "internacional": dados["internacional"].sum() / dados["worldwide_box_office"].sum() * 100,
            "gap": dados["gap_publico_critica"].mean(),
        }

    atual, franquia = kpis(df_filtrado), kpis(df)

    def delta(chave, sufixo, casas=1):
        diferenca = atual[chave] - franquia[chave]
        return 0 if round(diferenca, casas) == 0 else f"{'+' if diferenca > 0 else ''}{fmt_num(diferenca, casas)}{sufixo}"

    with st.container(horizontal=True):
        st.metric(
            "Multiplicador de bilheteria",
            f"{fmt_num(atual['multiplicador'])}×",
            delta("multiplicador", "×"),
            delta_description="vs. franquia",
            help="Média de bilheteria mundial ÷ orçamento de produção. Quantas vezes o filme devolveu o que custou.",
            border=True,
        )
        st.metric(
            f"Taxa de sucesso (≥ {fmt_num(BREAK_EVEN)}×)",
            f"{fmt_num(atual['sucesso'], 0)}%",
            delta("sucesso", " p.p.", 0),
            delta_description="vs. franquia",
            help=(
                f"% de filmes com bilheteria de pelo menos {fmt_num(BREAK_EVEN)}× o orçamento, o ponto de equilíbrio "
                "usual do mercado depois de marketing e da fatia dos cinemas. Mais exigente que o 'Lucrativo' da EDA."
            ),
            border=True,
        )
        st.metric(
            "Receita internacional",
            f"{fmt_num(atual['internacional'], 0)}%",
            delta("internacional", " p.p.", 0),
            delta_description="vs. franquia",
            delta_color="off",
            help="Parcela da bilheteria mundial vinda de fora dos EUA. Mede a dependência do mercado internacional.",
            border=True,
        )
        st.metric(
            "Gap público × crítica",
            f"{'+' if atual['gap'] > 0 else ''}{fmt_num(atual['gap'])} pts",
            delta("gap", " pts"),
            delta_description="vs. franquia",
            delta_color="off",
            help="Média de Audience Score − Tomatometer. Positivo: o público gostou mais que a crítica.",
            border=True,
        )

    col_fase, col_dispersao = st.columns(2)

    with col_fase:
        with st.container(border=True, height="stretch"):
            st.markdown("**Multiplicador médio por fase**")
            por_fase = (
                df_filtrado.groupby("mcu_phase")
                .agg(multiplicador=("multiplicador", "mean"), filmes=("movie_title", "count"))
                .reset_index()
            )
            por_fase["fase"] = por_fase["mcu_phase"].str.replace("Phase", "Fase")
            fig_fase = px.bar(
                por_fase,
                x="fase",
                y="multiplicador",
                text=por_fase["multiplicador"].map(lambda v: f"{fmt_num(v)}×"),
                hover_data={"filmes": True, "fase": False},
                labels={"fase": "", "multiplicador": "Multiplicador médio", "filmes": "Filmes"},
                color_discrete_sequence=[COR_NEUTRA],
            )
            fig_fase.add_hline(
                y=BREAK_EVEN,
                line_dash="dash",
                line_color=COR_DESTAQUE,
                annotation_text=f"Equilíbrio {fmt_num(BREAK_EVEN)}×",
                annotation_position="top left",
            )
            fig_fase.update_traces(textposition="outside", cliponaxis=False)
            fig_fase.update_layout(height=380, margin=dict(l=0, r=0, t=20, b=0))
            st.plotly_chart(fig_fase, alt="Multiplicador médio de bilheteria por fase do MCU")

    with col_dispersao:
        with st.container(border=True, height="stretch"):
            st.markdown("**Orçamento × bilheteria mundial**")
            fig_disp = px.scatter(
                df_filtrado,
                x="production_budget",
                y="worldwide_box_office",
                color="mcu_phase",
                color_discrete_sequence=px.colors.sequential.Plasma_r[1:],
                category_orders={"mcu_phase": FASES},
                hover_name="movie_title",
                hover_data={"multiplicador": ":.1f", "mcu_phase": False},
                labels={**ROTULOS, "mcu_phase": "Fase", "multiplicador": "Multiplicador"},
            )
            # Retas de referência: empate (1×) e ponto de equilíbrio de mercado (2,5×)
            x_max = df_filtrado["production_budget"].max() * 1.05
            for fator, estilo, nome in [(1, "dot", "1× (empate)"), (BREAK_EVEN, "dash", f"{fmt_num(BREAK_EVEN)}× (equilíbrio)")]:
                fig_disp.add_trace(go.Scatter(
                    x=[0, x_max], y=[0, x_max * fator], mode="lines", name=nome,
                    line=dict(color=COR_DESTAQUE if fator > 1 else COR_NEUTRA, dash=estilo, width=1),
                    hoverinfo="skip",
                ))
            fig_disp.update_traces(selector=dict(mode="markers"), marker=dict(size=10, opacity=0.85))
            fig_disp.update_layout(
                height=380,
                margin=dict(l=0, r=0, t=20, b=0),
                legend=dict(title=None),
                xaxis_range=[df_filtrado["production_budget"].min() * 0.9, x_max],
                yaxis_range=[0, df_filtrado["worldwide_box_office"].max() * 1.08],
            )
            st.plotly_chart(fig_disp, alt="Dispersão entre orçamento e bilheteria mundial, colorida por fase")
            st.caption("Filmes abaixo da reta tracejada não atingiram o ponto de equilíbrio de mercado.")

    with st.container(border=True):
        col_titulo, col_ordem = st.columns([3, 1], vertical_alignment="bottom")
        col_titulo.markdown("**Ranking de filmes por multiplicador**")
        ordem = col_ordem.segmented_control(
            "Mostrar",
            options=["Maiores", "Menores"],
            default="Maiores",
            required=True,
            label_visibility="collapsed",
        )
        ranking = df_filtrado.sort_values("multiplicador", ascending=(ordem == "Menores")).head(10)
        ranking = ranking.assign(
            situacao=ranking["multiplicador"].map(lambda v: "Acima do equilíbrio" if v >= BREAK_EVEN else "Abaixo do equilíbrio")
        )
        fig_rank = px.bar(
            ranking,
            x="multiplicador",
            y="movie_title",
            orientation="h",
            color="situacao",
            color_discrete_map={"Acima do equilíbrio": COR_NEUTRA, "Abaixo do equilíbrio": COR_DESTAQUE},
            text=ranking["multiplicador"].map(lambda v: f"{fmt_num(v)}×"),
            hover_data={"production_budget": ":.0f", "worldwide_box_office": ":.0f", "situacao": False},
            labels={**ROTULOS, "multiplicador": "Multiplicador", "movie_title": "", "situacao": ""},
        )
        fig_rank.add_vline(x=BREAK_EVEN, line_dash="dash", line_color=COR_DESTAQUE)
        fig_rank.update_traces(textposition="outside", cliponaxis=False)
        fig_rank.update_layout(
            height=40 * len(ranking) + 80,
            margin=dict(l=0, r=40, t=10, b=0),
            yaxis=dict(categoryorder="total ascending" if ordem == "Maiores" else "total descending"),
            legend=dict(orientation="h", y=1.08, x=1, xanchor="right", title=None),
        )
        st.plotly_chart(fig_rank, alt=f"Os 10 filmes com {ordem.lower()} multiplicadores de bilheteria")

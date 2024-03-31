import streamlit as st
from src.dados.consultas import Consulta
from src.visualizacao.visualizacao import Visualizacao

st.set_page_config(layout="wide", page_title="Dashboard preços dos Imóveis")

# with open("src/estilos/styles.css", "r") as f:
#     css = f.read()

#     st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('Análise dos preços dos Imóveis do Múnicipio de Ribeirão Preto')

with st.container():

    tipo_imovel = st.radio(
        'Escolha o típo de imóvel   ',
        ['Apartamento', 'Casa'],
        horizontal=True,
        key='Apartamento')


with st.container():
    coluna_um, coluna_dois, coluna_tres = st.columns(3)
    with coluna_um:
        st.write('Gráfico 1 metro mais caro por bairro')
        colunas = ['bairro_teste', 'preco_por_metro', 'tipo_imovel']
        print(tipo_imovel)
        consulta = Consulta(colunas=colunas, tipo_imovel=tipo_imovel)
        df_metro_caro = consulta.obter_metro_mais_caro()
        visualizacao = Visualizacao(df_resultado=df_metro_caro)
        fig = visualizacao.gerar_grafico_de_barras(
            coluna_x='preco_por_metro_bairro',
            coluna_y='bairro_teste',
            orientation='h',
            tickvals_y=False,
            texto_posicao='auto'
        )
        st.plotly_chart(fig, use_container_width=True)
    with coluna_dois:
        st.write('Gráfico 2 Análise da faixa de preços por bairro')
    with coluna_tres:
        st.write('Gráfico 3 - total de imovel por bairro')

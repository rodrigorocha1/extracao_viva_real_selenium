import streamlit as st
from src.dados.consultas import Consulta


with open("src/estilos/styles.css", "r") as f:
    css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('Análise dos preços dos Imóveis do Múnicipio de Ribeirão Preto')

with st.container(border=True):
    st.write('texto dentro do container')
    coluna_um, coluna_dois, coluna_tres, coluna_quatro = st.columns(4)
    with coluna_um:
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    with coluna_dois:
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    with coluna_tres:
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    with coluna_quatro:
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")


with st.container():
    coluna_um, coluna_dois, coluna_tres = st.columns(3)
    with coluna_um:
       

    with coluna_dois:
        st.write('Gráfico 2 Análise da faixa de preços por bairro')
    with coluna_tres:
        st.write('Gráfico 3')

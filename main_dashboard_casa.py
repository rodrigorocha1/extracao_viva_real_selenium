import streamlit as st


with open("src/estilos/styles.css", "r") as f:
    css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('Análise dos preços dos Imóveis do Múnicipio de Ribeirão Preto')


with st.container():
    coluna_um, coluna_dois, coluna_tres = st.columns(3)
    with coluna_um:
        st.write('Gráfico 1 metro mais caro por bairro')
    with coluna_dois:
        st.write('Gráfico 2 Análise da faixa de preços por bairro')
    with coluna_tres:
        st.write('Gráfico 3')

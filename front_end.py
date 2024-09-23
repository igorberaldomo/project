import streamlit as st
import numpy as np
import pandas as pd
import requests

def pega_corres():
    response = requests.get("http://localhost:5000/cores")
    data = response.json()
    return data

def cadastra_cor(nome, rgb):
    if nome and rgb:
            new_id = len(cores) + 1
    response = requests.post("http://localhost:5000/cores/", json={"id": new_id, "nome": nome, "rgb": rgb})
    data = response.json()
    return data

def pega_cor(id_cor):
    if int(id_cor) > len(cores) or int(id_cor) < 1:
        st.write('ERRO: cor inexistente')
        return {}
    else:
        st.session_state.clicked = True
        response = requests.get("http://localhost:5000/cores/?id=" + str(id_cor))
        data = response.json()
        return data
def deleta_cor(id_cor):
    response = requests.delete("http://localhost:5000/cores/?id=" + str(id_cor))
    data = response.json()
    return data

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


st.title("Lista de Cores")
cores = pega_corres()

cores_df = pd.DataFrame(cores)
index = len(cores)-1
display_cores_df = cores_df.loc[0:index, ['id', 'nome', 'rgb']]
st.dataframe(display_cores_df)

st.subheader('Cadastro')
nome = st.text_input('nome')
rgb = st.text_input('rgb')

st.button('Cadastrar', on_click=cadastra_cor, args=(nome, rgb))

st.subheader('Pesquisar e Deletar')
id_cor = st.text_input('id')
st.button('Deletar uma cor', on_click=deleta_cor, args=(id_cor))
st.button('Listar uma cor',on_click=pega_cor, args=(id_cor))


if st.session_state.clicked:
    cor = pega_cor(id_cor)
    display_cor = cor
    st.dataframe(display_cor)
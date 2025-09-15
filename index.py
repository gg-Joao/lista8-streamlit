import streamlit as st
from paciente import Paciente

st.set_page_config(page_title="Dados do Paciente")

st.title("Dados do Paciente")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")
telefone = st.text_input("Telefone")
nascimento = st.text_input("Data de Nascimento (dia/mes/ano)")

if st.button("Calcular Idade"):
    try:
        paciente = Paciente(nome, cpf, telefone, nascimento)
        st.info(f"Idade: {paciente.idade()}")
    except ValueError:
        st.warning("⚠️ Preencha todos os retangulos corretamente antes de calcular a idade.")

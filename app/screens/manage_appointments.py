import streamlit as st


def manage_appointments():
    st.title("Consultas")

    # 5W2H
    st.write("**Quem:** Médicos e administradores")
    st.write("**O quê:** Tela para gerenciamento de consultas")
    st.write("**Por quê:** Para adicionar, editar e visualizar consultas")
    st.write("**Quando:** Sempre que necessário gerenciar consultas")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados da consulta")
    st.write("**Quanto:** N/A")

    with st.form(key='add_appointment'):
        patient_id = st.text_input("ID do Paciente")
        appointment_date = st.date_input("Data da Consulta")
        purpose = st.text_area("Propósito da Consulta")
        if st.form_submit_button("Adicionar Consulta"):
            st.write("Consulta adicionada com sucesso!")


if __name__ == "__main__":
    manage_appointments()

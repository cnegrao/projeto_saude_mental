import streamlit as st


def main():
    st.title("Sintomas")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para registro de sintomas")
    st.write("**Por quê:** Para registrar e visualizar sintomas dos pacientes")
    st.write("**Quando:** Durante a consulta")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados dos sintomas")
    st.write("**Quanto:** N/A")

    with st.form(key='symptoms'):
        patient_id = st.text_input("ID do Paciente")
        symptom_description = st.text_area("Descrição do Sintoma")
        date_reported = st.date_input("Data do Relato")
        if st.form_submit_button("Adicionar Sintoma"):
            st.write("Sintoma adicionado com sucesso!")


if __name__ == "__main__":
    main()

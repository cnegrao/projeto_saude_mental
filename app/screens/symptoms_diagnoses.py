import streamlit as st


def symptoms_diagnoses():
    st.title("Sintomas e Diagnósticos")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para registro de sintomas e diagnósticos")
    st.write(
        "**Por quê:** Para adicionar e visualizar sintomas e diagnósticos dos pacientes")
    st.write(
        "**Quando:** Sempre que necessário registrar ou consultar sintomas e diagnósticos")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com sintomas e diagnósticos")
    st.write("**Quanto:** N/A")

    with st.form(key='add_symptom_diagnosis'):
        patient_id = st.text_input("ID do Paciente")
        symptom_description = st.text_area("Descrição do Sintoma")
        date_reported = st.date_input("Data do Relato")
        diagnosis = st.text_area("Diagnóstico")
        if st.form_submit_button("Adicionar Sintoma/Diagnóstico"):
            st.write("Sintoma/Diagnóstico adicionado com sucesso!")


if __name__ == "_main_":
    symptoms_diagnoses()

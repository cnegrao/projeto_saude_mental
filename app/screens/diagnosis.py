import streamlit as st


def diagnosis():
    st.title("Diagnóstico")

    # Input fields for diagnosis
    patient_id = st.text_input("ID do Paciente")
    diagnosis = st.text_area("Diagnóstico")
    diagnostic_criteria = st.text_area("Critérios Diagnósticos")
    conclusion = st.text_area("Conclusão")
    doctor_notes = st.text_area("Observações do Médico (opcional)")

    if st.button("Salvar Diagnóstico"):
        st.success("Diagnóstico salvo com sucesso!")
        # Save diagnosis logic here


if __name__ == "__main__":
    diagnosis()

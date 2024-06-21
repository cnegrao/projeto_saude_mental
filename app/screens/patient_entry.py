import streamlit as st


def patient_entry():
    st.title("Entrada de Dados do Paciente")

    # Input fields for patient data
    patient_name = st.text_input("Nome do Paciente")
    age = st.number_input("Idade", min_value=0)
    gender = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
    symptoms = st.text_area("Sintomas")
    medical_history = st.text_area("Histórico Médico (opcional)")
    current_medications = st.text_area("Medicamentos Atuais (opcional)")
    allergies = st.text_area("Alergias (opcional)")
    lab_tests = st.text_area("Exames Laboratoriais (opcional)")

    if st.button("Salvar Dados do Paciente"):
        st.success("Dados do paciente salvos com sucesso!")
        # Save patient data logic here


if __name__ == "__main__":
    patient_entry()

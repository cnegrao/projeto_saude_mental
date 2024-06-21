import streamlit as st


def treatment():
    st.title("Tratamento Recomendado")

    # Input fields for treatment
    patient_id = st.text_input("ID do Paciente")
    treatment_plan = st.text_area("Tratamento")
    medication = st.text_input("Medicação")
    dosage = st.text_input("Dosagem")
    treatment_duration = st.text_input("Duração do Tratamento")
    side_effects = st.text_area("Efeitos Colaterais (opcional)")
    doctor_notes = st.text_area("Observações do Médico (opcional)")

    if st.button("Salvar Tratamento"):
        st.success("Tratamento salvo com sucesso!")
        # Save treatment logic here


if __name__ == "__main__":
    treatment()

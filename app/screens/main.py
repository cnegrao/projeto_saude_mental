import streamlit as st
from patient_entry import patient_entry
from diagnosis import diagnosis
from treatment import treatment
from recommendation import recommendation
from symptoms import symptoms
from labs import labs
from allergies import allergies
from family_history import family_history
from patient_notes import patient_notes
from appointments import appointments
from medications import medications
from insurance import insurance
from symptoms_diagnoses import symptoms_diagnoses


def main():
    st.sidebar.title("Navegação")
    option = st.sidebar.selectbox("Selecione uma tela:",
                                  ["Entrada de Dados do Paciente", "Diagnóstico", "Tratamento Recomendado", "Recomendação",
                                   "Sintomas", "Exames Laboratoriais", "Alergias", "Histórico Familiar",
                                   "Notas do Paciente", "Compromissos", "Medicamentos", "Seguros", "Sintomas e Diagnósticos"])

    if option == "Entrada de Dados do Paciente":
        patient_entry()
    elif option == "Diagnóstico":
        diagnosis()
    elif option == "Tratamento Recomendado":
        treatment()
    elif option == "Recomendação":
        recommendation()
    elif option == "Sintomas":
        symptoms()
    elif option == "Exames Laboratoriais":
        labs()
    elif option == "Alergias":
        allergies()
    elif option == "Histórico Familiar":
        family_history()
    elif option == "Notas do Paciente":
        patient_notes()
    elif option == "Compromissos":
        appointments()
    elif option == "Medicamentos":
        medications()
    elif option == "Seguros":
        insurance()
    elif option == "Sintomas e Diagnósticos":
        symptoms_diagnoses()


if __name__ == "__main__":
    main()

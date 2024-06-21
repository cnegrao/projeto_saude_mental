import streamlit as st
from login import login_screen
from dashboard import main_dashboard
from manage_patients import manage_patients
from patient_details import patient_details
from manage_appointments import manage_appointments
from symptoms_diagnoses import symptoms_diagnoses
from manage_treatments import manage_treatments
from manage_labs import manage_labs
from manage_allergies import manage_allergies
from family_history import family_history
from insurance_info import insurance_info
from patient_notes import patient_notes

PAGES = {
    "Login": login_screen,
    "Dashboard": main_dashboard,
    "Gerenciamento de Pacientes": manage_patients,
    "Detalhes do Paciente": patient_details,
    "Consultas": manage_appointments,
    "Sintomas e Diagnósticos": symptoms_diagnoses,
    "Tratamentos": manage_treatments,
    "Exames Laboratoriais": manage_labs,
    "Alergias": manage_allergies,
    "Histórico Familiar": family_history,
    "Informações de Seguro": insurance_info,
    "Notas do Paciente": patient_notes,
}


def main():
    st.sidebar.title("Navegação")
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    page = PAGES[selection]
    page()


if __name__ == "__main__":
    main()

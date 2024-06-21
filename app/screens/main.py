import streamlit as st
from screens import patient_data, symptoms, diagnostic_criteria, recommendation, treatment, appointments, labs, allergies, family_history, insurance, patient_notes, medications

st.sidebar.title("Navegação")
options = st.sidebar.radio("Ir para", ["Dados do Paciente", "Sintomas", "Critérios Diagnósticos", "Recomendações", "Tratamentos",
                           "Compromissos", "Exames Laboratoriais", "Alergias", "Histórico Familiar", "Seguro de Saúde", "Notas do Paciente", "Medicamentos"])

if options == "Dados do Paciente":
    patient_data.show()
elif options == "Sintomas":
    symptoms.show()
elif options == "Critérios Diagnósticos":
    diagnostic_criteria.show()
elif options == "Recomendações":
    recommendation.show()
elif options == "Tratamentos":
    treatment.show()
elif options == "Compromissos":
    appointments.show()
elif options == "Exames Laboratoriais":
    labs.show()
elif options == "Alergias":
    allergies.show()
elif options == "Histórico Familiar":
    family_history.show()
elif options == "Seguro de Saúde":
    insurance.show()
elif options == "Notas do Paciente":
    patient_notes.show()
elif options == "Medicamentos":
    medications.show()

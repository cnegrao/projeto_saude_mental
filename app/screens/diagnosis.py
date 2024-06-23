import streamlit as st


def main():
    st.header("Diagnóstico")

    patient_id = st.text_input("ID do Paciente")
    if st.button("Buscar"):
        # Simular a busca do diagnóstico
        st.write(f"Buscando diagnóstico para o paciente ID: {patient_id}")
        # Simular dados do diagnóstico
        diagnosis_info = {
            "Transtorno": "Transtorno de Ansiedade",
            "Critérios Diagnósticos": "Sintomas presentes por mais de 6 meses...",
            "Conclusão": "Paciente apresenta transtorno de ansiedade."
        }
        st.write(diagnosis_info)

    st.write("Input: ID do Paciente")
    st.write("Output: Informações de diagnóstico exibidas")


if __name__ == "__main__":
    main()

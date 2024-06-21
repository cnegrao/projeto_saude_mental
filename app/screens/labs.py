import streamlit as st
import pandas as pd
import datetime


def labs():
    # 5W2H da Tela Labs
    st.header("Labs Data Entry")

    st.markdown("""
    **What:** Tela para inserção e visualização de dados de exames laboratoriais.
    **Why:** Facilitar o registro e acompanhamento dos exames laboratoriais dos pacientes.
    **Who:** Médicos e profissionais de saúde responsáveis pelo tratamento dos pacientes.
    **Where:** Interface do sistema de apoio ao diagnóstico e recomendação de tratamento.
    **When:** Durante a consulta ou revisão dos dados médicos do paciente.
    **How:** Utilizando campos de formulário para inserir e atualizar dados.
    **How Much:** Implementação e manutenção contínua da funcionalidade.
    """)

    # Formulário para entrada de dados
    st.subheader("Enter Lab Data")
    patient_id = st.number_input("Patient ID", min_value=1)
    test_date = st.date_input("Test Date", value=datetime.date.today())
    test_type = st.text_input("Test Type")
    results = st.text_area("Results")

    if st.button("Save Lab Data"):
        # Salvando dados (A implementação real deve inserir os dados em um banco de dados)
        st.success(f"Lab data saved for patient ID: {patient_id}")

    # Exemplo de exibição de dados (substituir por dados reais do banco de dados)
    st.subheader("View Lab Data")
    example_data = {
        "Patient ID": [1, 2],
        "Test Date": ["2024-06-20", "2024-06-21"],
        "Test Type": ["Blood test", "Urine test"],
        "Results": ["Normal", "Elevated protein levels"]
    }
    df = pd.DataFrame(example_data)
    st.dataframe(df)


if __name__ == "__main__":
    labs()

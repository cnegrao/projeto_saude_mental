import streamlit as st


def main():
    st.title("Exames")

    # 5W2H
    st.write("**Quem:** Médicos, Enfermeiros")
    st.write("**O quê:** Tela para gerenciar exames laboratoriais dos pacientes")
    st.write("**Por quê:** Para adicionar, editar e visualizar exames laboratoriais")
    st.write("**Quando:** Durante consultas e avaliações")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write(
        "**Como:** Preenchimento de um formulário com dados dos exames laboratoriais")
    st.write("**Quanto:** N/A")

    with st.form(key='add_lab'):
        patient_id = st.text_input("ID do Paciente")
        test_date = st.date_input("Data do Exame")
        test_type = st.text_input("Tipo de Exame")
        results = st.text_area("Resultados")
        if st.form_submit_button("Adicionar Exame"):
            st.write("Exame adicionado com sucesso!")


if __name__ == "__main__":
    manage_labs()

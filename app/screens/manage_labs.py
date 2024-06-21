import streamlit as st


def manage_labs():
    st.title("Exames Laboratoriais")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciamento de exames laboratoriais")
    st.write(
        "**Por quê:** Para adicionar, editar e visualizar resultados de exames laboratoriais")
    st.write("**Quando:** Sempre que necessário gerenciar exames laboratoriais")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write(
        "**Como:** Preenchimento de um formulário com dados do exame laboratorial")
    st.write("**Quanto:** N/A")

    with st.form(key='add_lab'):
        patient_id = st.text_input("ID do Paciente")
        test_date = st.date_input("Data do Exame")
        test_type = st.text_input("Tipo de Exame")
        results = st.text_area("Resultados")
        if st.form_submit_button("Adicionar Exame Laboratorial"):
            st.write("Exame Laboratorial adicionado com sucesso!")


if __name__ == "__main__":
    manage_labs()

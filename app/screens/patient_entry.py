import streamlit as st


def main():
    st.title("Entrada de Dados do Paciente")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para entrada de dados do paciente")
    st.write("**Por quê:** Para registrar informações iniciais do paciente")
    st.write("**Quando:** Durante a avaliação inicial do paciente")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados do paciente")
    st.write("**Quanto:** N/A")

    with st.form(key='patient_entry'):
        patient_id = st.text_input("ID do Paciente")
        name = st.text_input("Nome")
        birth_date = st.date_input("Data de Nascimento")
        gender = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
        contact_info = st.text_area("Informações de Contato")
        if st.form_submit_button("Adicionar Paciente"):
            st.write("Dados do paciente adicionados com sucesso!")


if __name__ == "__main__":
    main()

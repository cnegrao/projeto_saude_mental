import streamlit as st


def manage_patients():
    st.title("Gerenciamento de Pacientes")

    # 5W2H
    st.write("**Quem:** Médicos e administradores")
    st.write("**O quê:** Tela para gerenciamento de pacientes")
    st.write(
        "**Por quê:** Para adicionar, editar e visualizar informações de pacientes")
    st.write("**Quando:** Sempre que necessário gerenciar pacientes")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados do paciente")
    st.write("**Quanto:** N/A")

    with st.form(key='add_patient'):
        patient_id = st.text_input("ID do Paciente")
        first_name = st.text_input("Primeiro Nome")
        last_name = st.text_input("Último Nome")
        date_of_birth = st.date_input("Data de Nascimento")
        gender = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
        address = st.text_area("Endereço")
        phone_number = st.text_input("Número de Telefone")
        email = st.text_input("Email")
        if st.form_submit_button("Adicionar Paciente"):
            st.write("Paciente adicionado com sucesso!")


if __name__ == "__main__":
    manage_patients()

import streamlit as st


def insurance_info():
    st.title("Informações de Seguro")

    # 5W2H
    st.write("**Quem:** Médicos e administradores")
    st.write("**O quê:** Tela para gerenciamento de informações de seguro")
    st.write(
        "**Por quê:** Para adicionar, editar e visualizar informações de seguro dos pacientes")
    st.write("**Quando:** Sempre que necessário gerenciar informações de seguro")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados do seguro")
    st.write("**Quanto:** N/A")

    with st.form(key='add_insurance'):
        patient_id = st.text_input("ID do Paciente")
        provider = st.text_input("Provedor de Seguro")
        policy_number = st.text_input("Número da Apólice")
        coverage_details = st.text_area("Detalhes da Cobertura")
        if st.form_submit_button("Adicionar Informações de Seguro"):
            st.write("Informações de Seguro adicionadas com sucesso!")


if __name__ == "__main__":
    insurance_info()

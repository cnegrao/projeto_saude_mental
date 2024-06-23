import streamlit as st


def main():
    st.title("Informações de Seguro")

    # 5W2H
    st.write("**Quem:** Médicos, Enfermeiros")
    st.write("**O quê:** Tela para gerenciar informações de seguro dos pacientes")
    st.write("**Por quê:** Para adicionar, editar e visualizar informações de seguro")
    st.write("**Quando:** Durante a admissão e atualizações subsequentes")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados do seguro")
    st.write("**Quanto:** N/A")

    with st.form(key='add_insurance'):
        patient_id = st.text_input("ID do Paciente")
        provider = st.text_input("Nome do Provedor")
        policy_number = st.text_input("Número da Apólice")
        coverage_details = st.text_area("Detalhes da Cobertura")
        if st.form_submit_button("Adicionar Seguro"):
            st.write("Informações de seguro adicionadas com sucesso!")


if __name__ == "__main__":
    manage_insurance()

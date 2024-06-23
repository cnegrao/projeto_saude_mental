import streamlit as st


def main():
    st.title("Critérios Diagnósticos")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciar critérios diagnósticos")
    st.write("**Por quê:** Para adicionar, editar e visualizar critérios diagnósticos")
    st.write("**Quando:** Durante consultas e avaliações")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com critérios diagnósticos")
    st.write("**Quanto:** N/A")

    with st.form(key='add_criteria'):
        patient_id = st.text_input("ID do Paciente")
        criteria_description = st.text_area(
            "Descrição dos Critérios Diagnósticos")
        if st.form_submit_button("Adicionar Critérios Diagnósticos"):
            st.write("Critérios Diagnósticos adicionados com sucesso!")


if __name__ == "__main__":
    manage_diagnostic_criteria()

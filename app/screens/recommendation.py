import streamlit as st


def main():
    st.title("Recomendações")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciar recomendações de tratamento")
    st.write(
        "**Por quê:** Para adicionar, editar e visualizar recomendações de tratamento")
    st.write("**Quando:** Durante consultas e avaliações")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write(
        "**Como:** Preenchimento de um formulário com recomendações de tratamento")
    st.write("**Quanto:** N/A")

    with st.form(key='add_recommendation'):
        patient_id = st.text_input("ID do Paciente")
        recommendation_description = st.text_area("Descrição da Recomendação")
        if st.form_submit_button("Adicionar Recomendação"):
            st.write("Recomendação adicionada com sucesso!")


if __name__ == "__main__":
    main()

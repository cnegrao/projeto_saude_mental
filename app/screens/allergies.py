import streamlit as st


def main():
    st.title("Alergias")

    # 5W2H
    st.write("**Quem:** Médicos, Enfermeiros")
    st.write("**O quê:** Tela para gerenciar alergias dos pacientes")
    st.write("**Por quê:** Para adicionar, editar e visualizar alergias")
    st.write("**Quando:** Durante consultas e atualizações médicas")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados das alergias")
    st.write("**Quanto:** N/A")

    with st.form(key='add_allergy'):
        patient_id = st.text_input("ID do Paciente")
        allergy_name = st.text_input("Nome da Alergia")
        severity = st.selectbox("Gravidade", ["Leve", "Moderada", "Severa"])
        reaction = st.text_area("Reação")
        notes = st.text_area("Notas Adicionais")
        if st.form_submit_button("Adicionar Alergia"):
            st.write("Alergia adicionada com sucesso!")


if __name__ == "__main__":
    main()

import streamlit as st


def main():
    st.title("Tratamentos")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciamento de tratamentos")
    st.write("**Por quê:** Para adicionar, editar e visualizar tratamentos prescritos")
    st.write("**Quando:** Sempre que necessário gerenciar tratamentos")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados do tratamento")
    st.write("**Quanto:** N/A")

    with st.form(key='add_treatment'):
        patient_id = st.text_input("ID do Paciente")
        medication_name = st.text_input("Nome do Medicamento")
        dosage = st.text_input("Dosagem")
        side_effects = st.text_area("Efeitos Colaterais")
        interactions = st.text_area("Interações")
        contraindications = st.text_area("Contraindicações")
        if st.form_submit_button("Adicionar Tratamento"):
            st.write("Tratamento adicionado com sucesso!")


if __name__ == "__main__":
    main()

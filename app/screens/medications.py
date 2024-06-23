import streamlit as st


def main():
    st.title("Medicações")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciar medicações dos pacientes")
    st.write("**Por quê:** Para adicionar, editar e visualizar medicações prescritas")
    st.write("**Quando:** Durante consultas e atualizações médicas")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados das medicações")
    st.write("**Quanto:** N/A")

    with st.form(key='add_medication'):
        patient_id = st.text_input("ID do Paciente")
        medication_name = st.text_input("Nome do Medicamento")
        dosage = st.text_input("Dosagem")
        side_effects = st.text_area("Efeitos Colaterais")
        interactions = st.text_area("Interações")
        contraindications = st.text_area("Contraindicações")
        if st.form_submit_button("Adicionar Medicação"):
            st.write("Medicação adicionada com sucesso!")


if __name__ == "__main__":
    main()

import streamlit as st


def main():
    st.title("Consultas")

    # 5W2H
    st.write("**Quem:** Médicos, Enfermeiros")
    st.write("**O quê:** Tela para gerenciar compromissos dos pacientes")
    st.write("**Por quê:** Para adicionar, editar e visualizar compromissos")
    st.write("**Quando:** Durante a admissão e atualizações subsequentes")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados do compromisso")
    st.write("**Quanto:** N/A")

    with st.form(key='add_appointment'):
        patient_id = st.text_input("ID do Paciente")
        appointment_date = st.date_input("Data do Compromisso")
        purpose = st.text_area("Propósito do Compromisso")
        if st.form_submit_button("Adicionar Compromisso"):
            st.write("Compromisso adicionado com sucesso!")


if __name__ == "__main__":
    main()

import streamlit as st


def patient_notes():
    st.title("Notas do Paciente")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciamento de notas dos pacientes")
    st.write(
        "**Por quê:** Para adicionar, editar e visualizar notas sobre os pacientes")
    st.write("**Quando:** Sempre que necessário gerenciar notas dos pacientes")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Preenchimento de um formulário com dados das notas")
    st.write("**Quanto:** N/A")

    with st.form(key='add_patient_note'):
        patient_id = st.text_input("ID do Paciente")
        note_date = st.date_input("Data da Nota")
        note = st.text_area("Nota")
        if st.form_submit_button("Adicionar Nota"):
            st.write("Nota do Paciente adicionada com sucesso!")


if __name__ == "__main__":
    patient_notes()

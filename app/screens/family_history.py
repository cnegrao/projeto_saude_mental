import streamlit as st


def family_history():
    st.title("Histórico Familiar")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela para gerenciamento do histórico familiar")
    st.write(
        "**Por quê:** Para adicionar, editar e visualizar histórico familiar dos pacientes")
    st.write("**Quando:** Sempre que necessário gerenciar histórico familiar")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write(
        "**Como:** Preenchimento de um formulário com dados do histórico familiar")
    st.write("**Quanto:** N/A")

    with st.form(key='add_family_history'):
        patient_id = st.text_input("ID do Paciente")
        relative = st.text_input("Parente")
        condition = st.text_input("Condição Médica")
        notes = st.text_area("Notas Adicionais")
        if st.form_submit_button("Adicionar Histórico Familiar"):
            st.write("Histórico Familiar adicionado com sucesso!")


if __name__ == "__main__":
    family_history()

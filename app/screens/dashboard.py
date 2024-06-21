import streamlit as st


def main_dashboard():
    st.title("Dashboard Principal")

    # 5W2H
    st.write("**Quem:** Médicos e administradores")
    st.write("**O quê:** Tela principal do sistema")
    st.write("**Por quê:** Para acesso rápido às principais funcionalidades")
    st.write("**Quando:** Após o login")
    st.write("**Onde:** Tela principal do sistema")
    st.write("**Como:** Navegação por meio de um menu lateral")
    st.write("**Quanto:** N/A")

    st.write("Bem-vindo ao sistema de gerenciamento de saúde mental.")
    st.write("Aqui você pode gerenciar pacientes, consultas, e mais.")


if __name__ == "__main__":
    main_dashboard()

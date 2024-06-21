import streamlit as st


def login_screen():
    st.title("Login")

    # 5W2H
    st.write("**Quem:** Usuários do sistema")
    st.write("**O quê:** Tela de login")
    st.write("**Por quê:** Para autenticar o acesso ao sistema")
    st.write("**Quando:** Na inicialização do aplicativo")
    st.write("**Onde:** Primeira tela do sistema")
    st.write("**Como:** Usuário insere seu nome de usuário e senha")
    st.write("**Quanto:** N/A")

    st.text_input("Usuário")
    st.text_input("Senha", type="password")
    if st.button("Login"):
        st.session_state['logged_in'] = True


if __name__ == "__main__":
    login_screen()

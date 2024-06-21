import streamlit as st


def patient_details():
    st.title("Detalhes do Paciente")

    # 5W2H
    st.write("**Quem:** Médicos")
    st.write("**O quê:** Tela de detalhes do paciente")
    st.write("**Por quê:** Para visualizar informações detalhadas de um paciente")
    st.write("**Quando:** Sempre que necessário acessar detalhes do paciente")
    st.write("**Onde:** Dentro do sistema de gerenciamento de saúde mental")
    st.write("**Como:** Exibição de informações detalhadas")
    st.write("**Quanto:** N/A")

    patient_id = st.text_input("ID do Paciente")
    # Exemplo de dados estáticos, você deve buscar isso do banco de dados
    st.write("Nome: John Doe")
    st.write("Data de Nascimento: 01/01/1980")
    st.write("Gênero: Masculino")
    st.write("Endereço: Rua Exemplo, 123")
    st.write("Número de Telefone: (11) 99999-9999")
    st.write("Email: johndoe@example.com")


if __name__ == "__main__":
    patient_details()

import streamlit as st
import sys
import os

# Determinar o caminho base com base no sistema operacional
base_path = os.path.abspath(os.path.join(os.getcwd(), 'app'))
print(f"Base path: {base_path}")

# Adicionar o caminho base ao sys.path se ainda não estiver incluído
if base_path not in sys.path:
    sys.path.insert(0, base_path)
    print(f"Base path added to sys.path: {base_path}")
else:
    print(f"Base path already in sys.path: {base_path}")

# Verifique o sys.path para garantir que o caminho está correto
print(f"sys.path: {sys.path}")

# Agora tentar importar os módulos após adicionar o caminho base
try:
    from screens import patient_entry, diagnosis, recommendation, treatment, patient_notes, labs, manage_allergies, family_history, insurance_info, patient_notes, medications, diagnostic_criteria
    print("Modules imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing modules: {e}")


def main():
    # Configuração da página
    st.set_page_config(
        page_title="Minha Aplicação Streamlit",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Barra lateral para navegação entre as páginas
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Escolha uma opção:", [
                            "Tela Principal", "Entrada de Dados do Paciente", "Sintomas", "Critérios Diagnósticos", "Recomendação", "Tratamento", "Consultas", "Exames", "Alergias", "Histórico Familiar", "Seguros", "Notas do Paciente", "Medicações"])

    # Variável de controle para mostrar ou não o título
    show_title = True

    # Roteamento para diferentes páginas
    if page == "Entrada de Dados do Paciente":
        patient_entry.main()
        show_title = False  # Não mostrar título nas outras páginas
    elif page == "Sintomas":
        symptoms_diagnoses.main()
        show_title = False
    elif page == "Critérios Diagnósticos":
        diagnostic_criteria.main()
        show_title = False
    elif page == "Recomendação":
        recommendation.main()
        show_title = False
    elif page == "Tratamento":
        treatment.main()
        show_title = False
    elif page == "Consultas":
        manage_allergies.main()
        show_title = False
    elif page == "Exames":
        labs.main()
        show_title = False
    elif page == "Alergias":
        manage_allergies.main()
        show_title = False
    elif page == "Histórico Familiar":
        family_history.main()
        show_title = False
    elif page == "Seguros":
        insurance_info.main()
        show_title = False
    elif page == "Notas do Paciente":
        patient_notes.main()
        show_title = False
    elif page == "Medicações":
        medications.main()
        show_title = False

    if page == "Tela Principal" and show_title:
        show_main_page()


def show_main_page():
    # Título e descrição da tela principal
    st.title("Bem-vindo à minha aplicação")
    st.write("""
        Esta é a tela principal da aplicação. 
        Use o menu à esquerda para navegar entre as diferentes funcionalidades disponíveis.
    """)
    print("Diretório atual:", os.getcwd())
    print("Caminho de busca do Python:", sys.path)


if __name__ == "__main__":
    main()

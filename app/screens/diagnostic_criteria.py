import streamlit as st


def show():
    st.title("Critérios Diagnósticos")
    st.multiselect("Selecione os critérios diagnósticos", [
                   "Critério 1", "Critério 2", "Critério 3"])


if __name__ == "__main__":
    main()

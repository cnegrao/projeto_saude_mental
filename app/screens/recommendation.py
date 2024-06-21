import streamlit as st


def recommendation():
    st.title("Recomendação")

    # Input fields for recommendations
    patient_id = st.text_input("ID do Paciente")
    recommendation_1 = st.text_area("Recomendação 1")
    recommendation_2 = st.text_area("Recomendação 2")
    recommendation_3 = st.text_area("Recomendação 3")
    additional_notes = st.text_area("Observações Adicionais (opcional)")

    if st.button("Salvar Recomendação"):
        st.success("Recomendação salva com sucesso!")
        # Save recommendation logic here


if __name__ == "_main_":
    recommendation()

import streamlit as st


def medications():
    # 5W2H
    st.markdown("### Medications Screen")
    st.markdown("""
    **Who:** Medical professionals and administrative staff  
    **What:** Enter and view details of patient medications  
    **Where:** In the medications section of the health management application  
    **When:** During patient check-ins or whenever medication details need to be updated  
    **Why:** To keep accurate records of patient medications, dosages, side effects, and interactions  
    **How:** Using a user-friendly interface that allows for quick entry and retrieval of medication data  
    **How much:** Effort depends on the number of medications being managed and updated  
    """)

    st.header("Medications Information")

    with st.form("medication_form"):
        st.text_input("Medication Name", key="medication_name")
        st.text_input("Dosage", key="dosage")
        st.text_area("Side Effects", key="side_effects")
        st.text_area("Interactions", key="interactions")
        st.text_area("Contraindications", key="contraindications")

        submitted = st.form_submit_button("Save Medication")
        if submitted:
            st.write("Medication details saved successfully.")


if __name__ == "__main__":
    medications()

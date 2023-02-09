import streamlit as st
from database import delete_data
def delete():
    dealer_id = st.text_input("ID:")
    if st.button("Delete Volunteer"):
        delete_data(dealer_id)
        st.success("Successfully Deleted Volunteer: {}".format(dealer_id))
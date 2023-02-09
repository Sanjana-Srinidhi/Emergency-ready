import streamlit as st
from database import edit_dealer_data
def update():
    old_id = st.text_input('Old ID:')
    dealer_id = st.text_input("ID:")
    dealer_name = st.text_input("Name:") 
    dealer_address = st.text_input("Address:")
    dealer_item = st.text_input("Item:")

    dealer_transport = st.selectbox("Transport", ["Road", "Rail", "Air"])
    if st.button("Update Volunteer"):
        edit_dealer_data(dealer_id, dealer_name, dealer_address, dealer_item, dealer_transport,old_id)
        st.success("Successfully Modified Volunteer: {}".format(dealer_name))
import streamlit as st
from database import add_data

def create():
    col1, col2 = st.columns(2)
    with col1:
        dealer_id = st.text_input("ID:")
        dealer_name = st.text_input("Name:")
    with col2:  
        dealer_address = st.text_input("Address:")
        dealer_item = st.text_input("Item:")

    dealer_transport = st.selectbox("Transport", ["Road", "Rail", "Air"])
    if st.button("Add Volunteer"):
        add_data(dealer_id, dealer_name, dealer_address, dealer_item, dealer_transport)
        st.success("Successfully Added Volunteer: {}".format(dealer_name))
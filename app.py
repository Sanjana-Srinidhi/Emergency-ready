import streamlit as st 
from create import create  
from delete import delete 
from read import read
from update import update 
from vol_det import volunteer
def main(): 
    st.title("Emergency Supplies Management System") 
    menu = ["Add", "View", "Edit", "Remove","Volunteer_Info"] 
    choice = st.sidebar.selectbox("Menu", menu) 
    if choice == "Add": 
        st.subheader("Enter Volunteer Details:") 
        create()
    elif choice == "View": 
        st.subheader("View Details") 
        read() 
    elif choice == "Edit": 
        st.subheader("Update Volunteer details") 
        update()
    elif choice == "Remove": 
        st.subheader("Delete Volunteer details") 
        delete()
    elif choice == 'Volunteer_Info':
        st.subheader("View Volunteer Information")
        volunteer()
    else: 
        st.subheader("About tasks")

if __name__ == '__main__': 
    main()
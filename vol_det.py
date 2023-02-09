import streamlit as st
from database import display_vol
import pandas as pd

def volunteer():
    dealer_id = st.text_input("Enter V_ID:")
    if st.button("Get Details"):
        result = display_vol(str(dealer_id))
        if result == []:
            st.text("Oops, no Details found for this V_ID\nTry again!")
        else:
            df = pd.DataFrame(result, columns=['W_ID','ADDRESS','ITEM','CONTACT_NUMBER','V_ID'])
            st.dataframe(df[['W_ID','ADDRESS','ITEM','CONTACT_NUMBER']].style.hide_index())
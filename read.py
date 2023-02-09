import pandas as pd
import streamlit as st
from database import view_user_data,view_vol_data,view_ware_data
def read():
    result_user = view_user_data()
    # st.write(result)
    df_User = pd.DataFrame(result_user, columns=['C_ID','ADDRESS','PASS','NAME'])
    with st.expander("View all Users"):
        st.dataframe(df_User[['C_ID','ADDRESS','NAME']])
    result_vol = view_vol_data()
    df_Volunteer = pd.DataFrame(result_vol, columns=['V_ID','NAME','ADDRESS','ITEM','TRANSPORT'])
    with st.expander("View all Volunteers"):
        st.dataframe(df_Volunteer)
    result_ware = view_ware_data()
    df_Warehouse = pd.DataFrame(result_ware, columns=['W_ID','ADDRESS','ITEM','CONTACT_NUMBER','V_ID'])
    with st.expander("View Warehouse details"):
        st.dataframe(df_Warehouse)
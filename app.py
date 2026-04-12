import datetime

import streamlit as st
import pandas as pd
from streamlit import sidebar

st.title("Quotation Form")

quote_date = st.date_input(label="Date", value=datetime.datetime.today())

if 'form_data' not in st.session_state:
    form_df = pd.DataFrame({
        'Description':pd.Series(dtype='str'),
        'Numbers':pd.Series(dtype='int'),
        'Session':pd.Series(dtype='int'),
        'Detail':pd.Series(dtype='str'),
        'Amount':pd.Series(dtype='float')
    })

items_price = ["Video Camera", "Still Camera", "Drone", "Candid Video", "Candid Stills", "TV", "360 degree camera", "Photo booth", "Wall LED", "Live streaming", "Photo Mug", "Lamination", "Calendar"]

form_config = {
    'Description':st.column_config.SelectboxColumn("Description", options=items_price),
    'Numbers':st.column_config.NumberColumn("Numbers",step=1),
    'Session':st.column_config.NumberColumn("Session",step=1),
    'Detail':st.column_config.TextColumn("Detail", default=""),
    'Amount':st.column_config.NumberColumn("Amount",step=1.00, default=0)
}

edited_df = st.data_editor(st.session_state.form_data,
               column_config=form_config,
               width='stretch',
               num_rows="dynamic")

if st.button("Preview & Submit", key="Form submit"):
    # Create a mask for rows where the specified columns have NO missing values
    filtered_df = edited_df[['Description', 'Numbers']]
    if not (edited_df[['Description', 'Numbers']].isna().any(axis=None) or edited_df.empty):
        st.session_state.form_data = edited_df
        st.session_state.quote_date = quote_date
        st.switch_page("pages/print.py")
    else:
        st.error("Please add at least one item before submitting.")

if st.button("Logout"):
    st.logout()
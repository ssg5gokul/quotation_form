import datetime

import streamlit as st
import pandas as pd

st.title("Quotation Form")

quote_date = st.date_input(label="Date", value=datetime.datetime.today())

form_df = pd.DataFrame({
    'Description':pd.Series(dtype='str'),
    'Qty':pd.Series(dtype='int'),
    'Session':pd.Series(dtype='int'),
    'Detail':pd.Series(dtype='str'),
    'Price':pd.Series(dtype='float')
})

items_price = ["Video Camera - FX30", "Video Camera", "Still Camera", "Drone", "Candid Video", "Candid Stills"]

form_config = {
    'Description':st.column_config.SelectboxColumn("Description", options=items_price),
    'Qty':st.column_config.NumberColumn("Qty",step=1),
    'Session':st.column_config.NumberColumn("Session",step=1),
    'Detail':st.column_config.TextColumn("Detail", default='None'),
    'Price':st.column_config.NumberColumn("Price",step=1.0)
}

edited_df = st.data_editor(form_df,
               column_config=form_config,
               width='stretch',
               num_rows="dynamic")

if st.button("Preview & Submit", key="Form submit"):
    if not edited_df.empty:
        st.session_state.form_data = edited_df
        st.session_state.quote_date = quote_date
        st.switch_page("pages/print.py")
    else:
        st.error("Please add at least one item before submitting.")

if st.button("Logout"):
    st.logout()
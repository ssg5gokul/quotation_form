import datetime

import streamlit as st
import pandas as pd
from streamlit import sidebar

st.title("Quotation Form")

quote_date = st.date_input(label="Date", value=datetime.datetime.today())

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
    'Detail':st.column_config.TextColumn("Detail", default='None'),
    'Amount':st.column_config.NumberColumn("Amount",step=1.0)
}

edited_df = st.data_editor(form_df,
               column_config=form_config,
               width='stretch',
               num_rows="dynamic")

if st.button("Preview & Submit", key="Form submit"):
    # Create a mask for rows where the specified columns have NO missing values
    not_null_mask = edited_df[['Description', 'Numbers', 'Session', 'Amount']].notna().all(axis=1)

    # Apply the combined condition
    filtered_df = edited_df[not_null_mask | (edited_df['Amount'] > 0)]

    if not filtered_df.empty:
        st.session_state.form_data = filtered_df
        st.session_state.quote_date = quote_date
        st.switch_page("pages/print.py", sidebar=False)
    else:
        st.error("Please add at least one item before submitting.")

if st.button("Logout"):
    st.logout()
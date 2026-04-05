import datetime
import streamlit as st
import pandas as pd
import os
from jinja2 import Template
from streamlit import session_state
import streamlit.components.v1


current_path = current_dir = os.path.dirname(__file__)
css_path = os.path.join(current_path, "quotation.css")
html_path = os.path.join(current_path, "quotation.html")

if 'form_data' in session_state:
    df = st.session_state.form_data
    quote_date = st.session_state.get('quote_date', "N/A")

    # 2. Prepare data for Jinja2
    # Convert DataFrame rows to a list of dictionaries for the template
    items = df.to_dict(orient='records')
    grand_total = df['Price'].sum()

    # Read CSS file
    with open(css_path, "r") as f:
        css_content = f.read()

    # Load your HTML file
    with open(html_path, "r") as f:
        html_template = f.read()

    data = {"style":css_content,"quote":12345, "date":quote_date, "items":items, "grand_total":grand_total}

    template = Template(html_template)
    rendered_html = template.render(data)

    printable_html = rendered_html + """
    <button onclick="window.print()" style="
        position:fixed;
        bottom:20px;
        right:20px;
        padding:10px 20px;
        background:#e67e22;
        color:white;
        border:none;
        cursor:pointer;
    ">
        Print
    </button>
    """

    st.components.v1.html(printable_html, height=1200, scrolling=True)

    if st.button("Edit Quotation"):
        st.switch_page("../app.py")

else:
    st.warning("No quotation data found. Please fill the form on the main page.")
    if st.button("Go to Form"):
        st.switch_page("../app.py")
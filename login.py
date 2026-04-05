import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
users=os.environ["ALLOWED_USERS"]

ALLOWED_USERS=[user for user in users.split(";")]



# 1. CHECK LOGIN STATUS
if not st.user.is_logged_in:
    st.write("\n")
    if st.button(
            "Sign in with Google",
            type="primary",
            key="checkout-button",
            use_container_width=True,
    ):
        st.login("google")
else:
    if st.user.email is None or st.user.email not in ALLOWED_USERS:
        st.error("Access Denied: You are not authorized to view this application.")
        if st.button("Log out"):
            st.logout()
        st.stop()


    # 3. Main App Content (Only reached if user is in ALLOWED_USERS)
    st.switch_page("app.py")







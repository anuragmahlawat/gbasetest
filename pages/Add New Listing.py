import streamlit as st
from streamlit_modal import Modal
import gspread
from google.oauth2 import service_account

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"
    ],
)
# conn = connect(credentials=credentials)
client = gspread.authorize(credentials)

# gc = gspread.service_account()
db = client.open_by_key("1NOCJrg21reC-QfWkBaR-PAGXm3sAJb8Yb_Q4Fr78WUM")
worksheet = db.sheet1

# def clear_text():
#     st.session_state["item_name"] = ""
#     st.session_state["status"] = ""
#     st.session_state["loaner_name"] = ""
#     st.session_state["more_infor"] = ""
#     st.session_state["contact_infor"] = ""


item_name = st.text_input(label="Item Name", key="item_name")
status = st.text_input(label="Status", key="status")
loaner = st.text_input(label="Loaner Name", key="loaner_name")
more_info = st.text_input(label="More info", key="more_infor")
contact_info = st.text_input(label="Contact info", key="contact_infor")
save_info = st.button("Save info")

item_info = [item_name, status, loaner, more_info, contact_info]

if save_info:
    worksheet.append_row(item_info)
    # clear_text()

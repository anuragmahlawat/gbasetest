import streamlit as st
from streamlit_modal import Modal
import pandas as pd
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

# Authentication details to access google sheet-----------------------------------------------------------------------
# gc = gspread.service_account()
db = client.open_by_key("1NOCJrg21reC-QfWkBaR-PAGXm3sAJb8Yb_Q4Fr78WUM")
# --------------------------------------------------------------------------------------------------------------------

# Variables relating to listings and amounts of listings---------------------------------------------------------------
worksheet = db.sheet1 # Accessing sheet 1 from spreadsheet (Spreadsheets and worksheets have different implementations)
rows = worksheet.get_all_values() # Getting all values in a list of lists
listings_list = rows.pop(0) # List of listings without title bar
number_of_listings = int(len(rows) - 1) # Number of listings
#----------------------------------------------------------------------------------------------------------------------

# Title and divider underneath it
st.title(":green[SHAREON]")
st.divider()

# To allow user to enter location and change listings based on that
st.text_input('Your Location:', placeholder="Postal Code")

# Available listings and the number is supposed to be changing based on the number of available listings
col1, col2 = st.columns(2)

with col1:
    st.text("Available Listings:")

with col2:
    st.text(number_of_listings)

st.divider()

# Making listing for every row-----------------------------------------------------------------------------------------
for x in rows:
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        pass
    with col2:
        st.text(x[0])
        st.text(x[1])
        st.text(x[2])
        st.text(x[3])
        st.text(x[4])
    st.divider()
#----------------------------------------------------------------------------------------------------------------------


# st.divider()
#
# itemCard = st.container()
#
# with itemCard:
#     col1, col2 = st.columns([0.4, 0.6])
#     with col1:
#         st.image("https://www.thespruce.com/thmb/AmoHdun9LM_HiRPRSEuKHByN6s8=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/spr-primary-drills-dburreson-001-02d983fd8e5f42ae8d8b5d799baca68a.jpg")
#     with col2:
#         more_info = Modal("More info", key="more_info")
#         contactInfo = Modal("Contact", key="contactInfo")
#         st.text(values[0])
#         st.text(values[1])
#         st.text(values[2])
#         st.text("More info: " + values[3])
#         st.text("Contact info: " + values[4])
#         openInfo = st.button("More info")
#         openContact = st.button("Contact")
#         if openInfo:
#             with more_info.container():
#                 st.text("This is a drill tf more u want cb, suck my dick. brokie mofo - xoxo Ryan Tan")
#
#         if openContact:
#             with contactInfo.container():
#                 st.text("+65 999")
#                 st.text("mindyourownbusiness@suckacock.com")
#
# st.divider()

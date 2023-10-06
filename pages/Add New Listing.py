import streamlit as st
from streamlit_modal import Modal
import gspread
from google.oauth2 import service_account

gc = gspread.service_account()
db = gc.open_by_key("1NOCJrg21reC-QfWkBaR-PAGXm3sAJb8Yb_Q4Fr78WUM")


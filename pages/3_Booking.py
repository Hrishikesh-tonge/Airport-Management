import json
import requests
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie

cnx = mysql.connector.connect(
    user="root",
    password="Krishna@9011",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()

st.write("hi")
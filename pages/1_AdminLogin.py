import streamlit as st 
import mysql.connector

st.title("Admin Login")
cnx = mysql.connector.connect(
    user="root",
    password="Titanium@1604",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()

loginSection = st.container()
def operate():
    
    st.write("Welcome Admin")
    
def login(username,password):
    sql = "select pwd from admin where user_id = %s"
    value = (username,)
    cursor.execute(sql,value)
    passw = cursor.fetchall()
    if passw[0][0] == password:
        return True
    else:
        return False
def LoggedInClicked(username,password):
    if login(username,password):
        st.success("Login Successful")
        operate()
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid creds")

with loginSection:
    st.session_state["loggedIn"] = False
    username = st.text_input(label="Username")
    password = st.text_input(label="Password",type='password')
    st.button("Login",on_click=LoggedInClicked,args=(username,password))
    
    if 'loggedIn' not in st.session_state:
        login
 
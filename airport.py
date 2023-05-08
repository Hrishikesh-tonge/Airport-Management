import json
import requests
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
searchSection = st.container()

cnx = mysql.connector.connect(
    user="root",
    password="Titanium@1604",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()
def login(username,password):
    sql = "select passwd from pass_login where id = %s"
    value = (username,)
    cursor.execute(sql,value)
    passw = cursor.fetchall()
    if passw[0][0] == password:
        return True
    else:
        return False
    
def search_flights(src,dest,dt):
    with searchSection:
        st.session_state['booking']=True
        query = "select * from flights where (scity = %s and destination_city = %s) and date = %s"
        val = (src,dest,dt)

        cursor.execute(query,val)
        flres = cursor.fetchall()
        if st.session_state['booking'] == True:
            for row in flres:
                st.write(row)
def booking():
  
    col1, col2, col3= st.columns(3)
    with col1:
        src = st.text_input("Enter source")
    
            
    with col2:
        dest = st.text_input("Destination")
         
    with col3:
        dt = st.date_input(label="When")

  
    if 'booking' not in st.session_state:
        st.session_state['booking'] = False
    if st.button("Search Flights"):
        query = "select * from flights where (scity = %s and destination_city = %s) and date=%s "
        val = (src,dest,dt)

        cursor.execute(query,val)
        flres = cursor.fetchall()

        for row in flres:
            st.table(row)

def LoggedInClicked(username,password):
    if login(username,password):
        st.success("Login Successful")
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid creds")
           
def passenger_login():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            st.header("Passenger Login")
            username = st.text_input(label="Username")
            password = st.text_input(label="Password",type='password')
            st.button("Login",on_click=LoggedInClicked,args=(username,password))
    



with headerSection:
    # Start of header gif
    url = requests.get("https://assets1.lottiefiles.com/packages/lf20_npJF362rsV.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    st.title("AIRLINE MANAGEMENT SYSTEM :airplane:")
    st_lottie(url_json)
    # End of header gif

    
    if 'loggedIn' not in st.session_state:
        
        tab1, tab2 =st.tabs(["Offers","Tourist_Destination"])

        with tab1:
            st.text("Offers")
            col1, col2, col3=st.columns(3)
        with col1:
            st.header("Cabs:taxi:")
            col1.metric("Cabs","OLA Bookings","Get 10% Off")
            
            st.image('1.jpeg')
        with col2:
            st.header("Hotels:hotel:")
            col2.metric("Hotels","Pre-Bookings","Get 15% Off")
            
            st.image('2.jpeg')
        with col3:
            st.header("Flights:airplane_departure:")
            col3.metric("Flight_offers","Domestic","Get 12% Off")
           
            st.image('3.jpeg')
        with tab2:
            st.text("Destinationas")
            col1, col2, col3=st.columns(3)
        with col1:
            st.header("Darjeeling")
            st.image("darj.jpg")
        with col2:
            st.header("Munnar")
            st.image("munnar.jpg")
        with col3:
            st.header("Dharamshala")
            st.image("dharm.jpg")
        col4, col5, col6=st.columns(3)
        with col4:
            st.header("Kashmir")
            st.image("kashmir.jpg")
        with col5:
            st.header("Leh-Ladakh")
            st.image("leh.jpg")
        with col6:
            st.header("Manali")
            st.image("manali.jpg")
            st.session_state['loggedIn'] = False
            passenger_login()   
        
    else:
        if st.session_state['loggedIn']:  # admin , cust .. log in --> cust
            booking()
        else:
            passenger_login()
            
    
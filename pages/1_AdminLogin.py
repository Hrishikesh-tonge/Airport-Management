import json
import requests
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie

loginSection = st.container()
headerSection = st.container()

dataFrameSerialization = "legacy"


# st.title("Admin Login")
cnx = mysql.connector.connect(
    user="root",
    #password="Krishna@9011",
     password="Titanium@1604",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()
def admin(username,password):
    sql = "select pwd from admin where user_id = %s"
    value = (username,)
    cursor.execute(sql,value)
    pwd = cursor.fetchall()
    if pwd[0][0] == password:
        return True
    else:
        return False

def aLoggedInClicked(username,password):
    if admin(username,password):
        st.success("Login Successful")
        st.session_state['aloggedIn'] = True
    else:
        st.session_state['aloggedIn'] = False
        st.error("Invalid creds")

def admin_login():
    # st.write("lsf")
    with loginSection:
        if st.session_state['aloggedIn'] == False:
            st.header("Admin Login") 
            username = st.text_input(label="Username")
            password = st.text_input(label="Password",type='password')
            st.button("Login",on_click=aLoggedInClicked,args=(username,password))

with headerSection:
    url = requests.get("https://assets1.lottiefiles.com/packages/lf20_npJF362rsV.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    st.title("AIRLINE MANAGEMENT SYSTEM :airplane:")
    st_lottie(url_json)

    if 'aloggedIn'not in st.session_state:
        st.session_state['aloggedIn']=False
        # st.write("check1")
        admin_login()
    else:
        if st.session_state['aloggedIn']:
            tab1, tab2 =st.tabs(["Add_Flight","Remove_Flight"])
            with tab1:
                st.subheader("Add Flights")
                with st.form(key='form1'):
                    Flight_id=st.text_input("Flight_id")
                    Source=st.text_input("Source")
                    Source_id=st.text_input("Source_id")
                    Scity=st.text_input("Scity")
                    Destination=st.text_input("Destination")
                    Destination_id=st.text_input("Destination_id")
                    Destination_City=st.text_input("Destination_City")
                    Departure_time=st.time_input("Departure_time")
                    Arrival_time=st.time_input("Arrival_time")
                    Price=st.text_input("Price")
                    Date=st.date_input(label="date")
                    Airline=st.text_input("Airline")

                    submit_button=st.form_submit_button(label="Add")
                    if submit_button:
                        query=('insert into flights' '(FLIGHT_ID,SOURCE,SOURCE_ID,SCITY,DESTINATION,DESTINATION_ID,DESTINATION_CITY,DEPARTURE_TIME,ARRIVAL_TIME,PRICE,DATE,AIRLINE)' 'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                        values=(Flight_id,Source,Source_id,Scity,Destination,Destination_id,Destination_City,Departure_time,Arrival_time,Price,Date,Airline)
                        cursor.execute(query,values)
                        cnx.commit()
                        # cursor.close()
                        # cnx.close()
                        # cursor=cnx.cursor()
                        # cursor.execute(query,arg)
                        # cnx.commit()
                        st.success("Successfully {} Flight Added".format(Flight_id))
            if st.button("loggout"):
                st.session_state['aloggedIn']=False
                admin_login()
                st.success("Successfully LoggedOut")


            with tab2:
                if st.button("Show Flights"):
                    query = "select * from flights"
                    cursor.execute(query)
                    flres = cursor.fetchall()
                    st.dataframe(flres)
                    # for row in flres:
                    #     st.table(row)
                

                f_id=st.text_input("Enter FLIGHT_ID")
                del_button=st.button(label="Delete")
                if del_button:
                    cursor.execute( "delete from flights where FLIGHT_ID='%s'" % f_id)
                    cnx.commit()
                    st.success("Successfully Deleted Flight {}".format(f_id))

        else:
            admin_login()

        


        
import json
import requests
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie

cnx = mysql.connector.connect(
    user="root",
    password="Krishna@9011",
    # password="Titanium@1604",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()

with st.container():
    col1, col2, col3 =st.columns(3)
    # if "src1" not in st.session_state:
    #     st.session_state.src1 = ""
    # if "dest1" not in st.session_state:
    #     st.session_state.dest1 = ""
    # if "date1" not in st.session_state:
    #     st.session_state.date1 = 
    with col1:
        # st.success(" {} SignUp Successfully ".format(st.session_state.name1))
        query_flightno = "select scity from flights where (scity = %s and destination_city = %s) and date=%s "
        val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
        cursor.execute(query_flightno,val)
        flres = cursor.fetchall()
        for row in flres:
            st.subheader(row[0])
        query_flightno = "select source from flights where (scity = %s and destination_city = %s) and date=%s "
        val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
        cursor.execute(query_flightno,val)
        flres = cursor.fetchall()
        for row in flres:
            st.write(row[0])
        query_flightno = "select flight_id from flights where (scity = %s and destination_city = %s) and date=%s "
        val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
        cursor.execute(query_flightno,val)
        flres = cursor.fetchall()
        for row in flres:
            st.subheader(row[0])
        query_flightno = "select departure_time from flights where (scity = %s and destination_city = %s) and date=%s "
        val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
        cursor.execute(query_flightno,val)
        flres = cursor.fetchall()
        for row in flres:
            st.write(row[0])
        query_flightno = "select airline from flights where (scity = %s and destination_city = %s) and date=%s "
        val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
        cursor.execute(query_flightno,val)
        flres = cursor.fetchall()
        for row in flres:
            st.write(row[0])
        
        with col2:
            st.subheader("To")
        
        with col3:
            query_flightno = "select destination_city from flights where (scity = %s and destination_city = %s) and date=%s "
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.subheader(row[0])
            query_flightno = "select destination from flights where (scity = %s and destination_city = %s) and date=%s "
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.write(row[0])
            query_flightno = "select price from flights where (scity = %s and destination_city = %s) and date=%s "
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                    st.subheader(int(row[0])*st.session_state.pass_number)
                    price=int(row[0])*st.session_state.pass_number
            query_flightno = "select arrival_time from flights where (scity = %s and destination_city = %s) and date=%s "
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.write(row[0])
            query_flightno = "select date from flights where (scity = %s and destination_city = %s) and date=%s "
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.write(row[0])
st.write("Click the Below Button For Confirmation")
st.button("Confirm")
        
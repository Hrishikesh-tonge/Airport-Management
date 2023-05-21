import streamlit as st 
import mysql.connector
st.title("Sign Up")

cnx = mysql.connector.connect(
    user="root",
    password="Krishna@9011",
    # password="Titanium@1604",
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

with st.form(key='form1'):
                    FIRST_NAME=st.text_input("FIRST_NAME",key="name1")
                    LAST_NAME=st.text_input("LAST_NAME",key="l_name1")
                    EMAIL_ID=st.text_input("EMAIL_ID")
                    CONTACT_NO=st.text_input("PHONE")
                    PASSWORD=st.text_input(label="Password",type='password')

                    submit_button=st.form_submit_button(label="SignUp")
                    if submit_button:
                        query=('insert into USERS' '(FIRST_NAME,LAST_NAME,EMAIL_ID,CONTACT_NO,PASSWORD)' 'values(%s,%s,%s,%s,%s)')
                        values=(FIRST_NAME,LAST_NAME,EMAIL_ID,CONTACT_NO,PASSWORD)
                        cursor.execute(query,values)
                        cnx.commit()
                        # st.success('Sign Up Successfull')
                        st.success(" {} SignUp Successfully ".format(FIRST_NAME))
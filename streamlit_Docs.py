import datetime
import streamlit as st
import time
import pandas as pd

st.header("Streamlit Documentation")
st.subheader("Important Things we will work!!")
st.title("Let's Begin then...")
st.write("1. JSON")
st.json({"Name":"Soubhagya","Age":25})


"2. Python Code"
st.code(
    """
import streamlit as st

for i in range(10):
    st.write("We are learning streamlit")
    
    """
)

"3. input from user"
email = st.text_input("Enter Email Id")
password = st.text_input("Enter Password", type="password")
login_button = st.button("Login")

if login_button:
    if email == "Shrikant@gmail.com" and password == "1234":
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success("Login Successful.")
        st.balloons()
    else:
        st.snow()
        st.error("Incorrect Credentials!!")

df = st.file_uploader("Select any CSV file")
df = pd.read_csv(df)
st.dataframe(df)

st.metric("Temperature",'70 °F',"1.2 °F")

st.download_button("Click here to Download",data=df.to_csv(),file_name='sou_1.csv')

date = st.date_input("Enter Birth Date")
today = datetime.datetime.now().date()

print(today - date, "Years old")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import Filter_Methods

st.set_page_config(layout='wide', page_title='Startup Analysis Using Pandas')
df = pd.read_csv("Cleaned_startup.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month


st.sidebar.title("Apply Filters to Analyse")
options = st.sidebar.selectbox("Select any criteria ", ['Overall', 'Startups', 'Investors'])



if options == 'Startups':
    st.markdown("<h1 style='text-align: center; color: red;'>Startup wise Analysis</h1>",
                unsafe_allow_html=True)
    startup_name = st.sidebar.selectbox("Select Startup", df['Startup'].unique().tolist())
    startup_button = st.sidebar.button("Click here to Startup Analysis")
    if startup_button:
        Filter_Methods.display_startup_info(df,startup_name)


elif options == 'Investors':
    st.markdown("<h1 style='text-align: center; color: red;'>Investors wise Analysis</h1>",
                unsafe_allow_html=True)
    investor_name = st.sidebar.selectbox("Select Investor", sorted(set(df['Investors'].str.split(',').sum())))
    investor_button = st.sidebar.button("Click here to Investors Analysis")
    if investor_button:
        Filter_Methods.display_investor_info(df,investor_name)



else:
    st.markdown("<h1 style='text-align: center; color: red;'>Overall Analysis of Startups</h1>",
                unsafe_allow_html=True)
    Filter_Methods.display_overall_analysis(df)





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time


def display_investor_info(name):
    st.header(name+" Investment Details in startups")
    st.subheader("Recent Investments")
    st.dataframe(df[df['Investors'].str.contains(name)][['Date','Startup','Vertical','City','Amount']].head(5))
    col1, col2 = st.columns(2)
    with col1:
        investment_sectors = df[df['Investors'].str.contains(name)].groupby('Vertical')['Amount'].sum()
        st.subheader('Investments Sectors')
        fig, ax = plt.subplots()
        ax.pie(investment_sectors, labels=investment_sectors.index,autopct="%0.01f%%")
        st.pyplot(fig)
    with col2:
        biggest_investments = df[df['Investors'].str.contains(name)].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head()
        st.subheader("Biggest Investments")
        fig1, ax1 = plt.subplots()
        ax1.bar(biggest_investments.index, biggest_investments.values)
        st.pyplot(fig1)

    col1, col2 = st.columns(2)
    with col1:
        investment_types = df[df['Investors'].str.contains(name)].groupby('Investment Type')['Amount'].sum()
        st.subheader('Investments Rounds')
        fig2, ax2 = plt.subplots()
        ax2.pie(investment_types, labels=investment_types.index, autopct="%0.01f%%")
        st.pyplot(fig2)
    with col2:
        investment_cities = df[df['Investors'].str.contains(name)].groupby('City')['Amount'].sum()
        st.subheader('Investments City')
        fig3, ax3 = plt.subplots()
        ax3.pie(investment_cities, labels=investment_cities.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    year_series = df[df['Investors'].str.contains(name)].groupby('Year')['Amount'].sum()

    st.subheader('YoY Investment')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)

    st.pyplot(fig4)







df = pd.read_csv("Cleaned_startup.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
print(df.info())

st.sidebar.title("Apply Filters to Analyse")
options = st.sidebar.selectbox("Select any criteria ", ['Overall', 'Startups', 'Investors'])


if options == 'Startups':
    st.title("Startup Analysis using Pandas")
    st.sidebar.selectbox("Select Startup", df['Startup'].unique().tolist())
    st.sidebar.button("Click here to Startup Analysis")


elif options == 'Investors':
    st.title("Investors Analysis using Pandas")
    investor_name = st.sidebar.selectbox("Select Investor", sorted(set(df['Investors'].str.split(',').sum())))
    investor_button = st.sidebar.button("Click here to Investors Analysis")
    if investor_button:
        display_investor_info(investor_name)



else:
    st.title("Overall Analysis using Pandas")
    st.dataframe(df)
    st.sidebar.button("Click here to Overall Analysis")





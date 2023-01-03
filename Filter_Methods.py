import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def display_startup_info(df,name):
    st.title("")
    col1, col2,col4 = st.columns(3)
    with col1:
        st.metric("Startup Name", name)
    with col2:
        st.metric("Location",df[df['Startup'] == name]['City'].values[0])
    with col4:
        st.metric("Industry", df[df['Startup'] == name]['Vertical'].values[0])

    st.title("")
    col1, col2, col3 = st.columns(3)
    with col1:
        amount_date_df = df[df['Startup'] == name][['Amount', 'Date']]
        amount_date_df['Date'] = amount_date_df['Date'].astype(str)
        amount_date_df.set_index('Date', inplace=True)
        st.subheader('Amounts invested Date Wise')
        st.bar_chart(amount_date_df)
    with col2:
        temp_df = df[df['Startup'] == name][['Investment Type', 'Amount']]
        Amount_by_round_series = temp_df.groupby('Investment Type')['Amount'].sum()
        st.subheader('Amounts invested in each Round')
        st.bar_chart(Amount_by_round_series)
    with col3:
        amount_investor_df = df[df['Startup'] == name][['Amount', 'Investors']]
        amount_investor_df.set_index('Investors', inplace=True)
        st.subheader('Amounts invested by Investors')
        st.bar_chart(amount_investor_df)


def display_overall_analysis(df):
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric("Total Amount Investment",str(round(df['Amount'].sum()))+" Cr.")
    with col2:
        st.metric("Max Amount Invested",str(round(df.groupby('Startup')['Amount'].sum().sort_values(ascending=False).head(1).values[0]))+" Cr.")
    with col3:
        st.metric("Average Amount Invested",str(round(df.groupby('Startup')['Amount'].sum().mean()))+" Cr.")
    with col4:
        st.metric("Total Startups",df['Startup'].nunique())
    st.title("")
    st.subheader("Month By Month Investments")
    select_chart = st.selectbox("Select Type",['Total','Count'])
    if select_chart=='Total':
        temp_df = df.groupby(['Year', 'Month'])['Amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['Year', 'Month'])['Amount'].count().reset_index()
    temp_df['X-Axis'] = temp_df['Year'].astype(str) + "-" + temp_df['Month'].astype('str')
    st.line_chart(temp_df, x='X-Axis', y='Amount')
    col1, col2 = st.columns(2)
    with col1:
        sector_with_highamount = df.groupby('Vertical')['Amount'].sum().sort_values(ascending=False).head()
        st.subheader('Top 5 invested Sectors Basis of Amounts')
        fig,ax = plt.subplots()
        ax.pie(sector_with_highamount,labels=sector_with_highamount.index,autopct="%0.01f%%")
        st.pyplot(fig)
    with col2:
        sector_with_total_investments = df.groupby('Vertical')['Startup'].count().sort_values(ascending=False).head(10)
        st.subheader('Top 10 invested Sectors Basis of Startups')
        fig1, ax1 = plt.subplots()
        ax1.pie(sector_with_total_investments, labels=sector_with_total_investments.index, autopct="%0.01f%%")
        st.pyplot(fig1)
    st.title("")
    col1, col2 = st.columns(2)
    with col1:
        yearwise_amount_investments = df.groupby('Year')['Amount'].sum()
        st.subheader("Investment amounts per Year")
        # fig2, ax2 = plt.subplots()
        # ax2.bar(yearwise_amount_investments.index, yearwise_amount_investments.values)
        # st.pyplot(fig2)
        st.bar_chart(yearwise_amount_investments)
    with col2:
        yearwise_nvestments_in_startup = df.groupby('Year')['Startup'].count()
        st.subheader("Total startups investment per Year")
        # fig3, ax3 = plt.subplots()
        # ax3.bar(yearwise_nvestments_in_startup.index, yearwise_nvestments_in_startup.values)
        # st.pyplot(fig3)
        st.bar_chart(yearwise_nvestments_in_startup)
    st.title("")
    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.subheader("Top 10 Investors in startups")
        st.dataframe(df.groupby('Investors')['Amount'].sum().sort_values(ascending=False).head((10)))
    with col2:
        st.write("")
        st.subheader("Top 10 Investors in startups")
        st.dataframe(df.groupby('Startup')['Amount'].sum().sort_values(ascending=False).head((10)))
    st.title("")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 10 InvestTypes in Startups")
        top10_investment_types = df.groupby('Investment Type')['Startup'].count().sort_values(ascending=False).head(10)
        st.bar_chart(top10_investment_types)
    with col2:
        st.subheader("Top 10 Cities invested")
        top_city_invested = df.groupby('City')['Startup'].count().sort_values(ascending=False).head(10)
        st.bar_chart(top_city_invested)



def display_investor_info(df,name):
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
        # fig1, ax1 = plt.subplots()
        # ax1.bar(biggest_investments.index, biggest_investments.values)
        # st.pyplot(fig1)
        st.bar_chart(biggest_investments)

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
    st.subheader('Year of Year Investment')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.line_chart(year_series)
    # st.pyplot(fig4)


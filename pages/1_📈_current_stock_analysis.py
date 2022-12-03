import streamlit as st
import yfinance as yf
from pandas_datareader import data as pdr
from plotnine import *
import altair as alt
import pandas as pd
from datetime import datetime as dt # Why does it not see this in my code.
from datetime import timedelta 
from streamlit_tags import st_tags

# App title displayed
st.title('Stock Analysis')

# Explanation of the app:
st.write("Here you can input the ticker symbols of any company stock, how much money you put in them, when you started the investment, and at what point since then you'd like to see the trend up to todays date. With this information an analysis is performed and we will show to you a chart of your stock's closing price over time, and the percentage change over your time as a shareholder in that company. Afterward you will be given an option to download the stock data if you wish.")

st.write("Enter your stocks ticker symbols for the companies you'd like an analysis on where it says Enter Keywords.")
# Use st_tags to allow users to put in however many ticker symbols they'd like to add to a list
tickers = st_tags()

# Counter variables created to continuously update the streamlit text input keys to prevent error of duplicate keys.
counta = 0
countb = 100
countc = 200
countd = 300

# Loop for every stock input by the user
for tick in tickers:
    counta += 1
    countb += 1
    countc += 1
    countd += 1
    # tick = st.text_input('Type a stocks ticker symbol in the box below')
    tick1 = tick.upper()
    st.write(f"You have chosen {tick1}")

    initial = st.text_input('How much money did you put in this stock?', key = counta)
    initial1 = pd.to_numeric(initial)

    start_date = st.text_input('Type the start date in the box below in the format YYYY-MM-DD', key = countb)
    # start_date = st.date_input("What is the start date?")
    # st.write('Your start date is:', start_date)
    # end_date = st.date_input("What is the end date?")
    # st.write('Your start date is:', end_date)

    end_date = st.text_input('Type the end date in the box below in the format YYYY-MM-DD', key = countc)
    # Some end dates work and some don't hmmmm, but it does when I go back to the text_input as opposed to the date_input hmmm.


    if end_date == "":
        pass
    else:
        stock = pdr.get_data_yahoo(f"{tick1}", start= f"{start_date}", end= f"{end_date}").reset_index()
        # st.dataframe(stock_covid)
        stock1 = stock[["Date", "Close"]]





        both = stock1.iloc[[0, -1]] # replaces name var below
        # Grabs the first row
        first = both.iloc[[0]] # replaces namef var below

        # Grabs the last row
        last = both.iloc[[1]] # replaces namel var below

        # Extract the first date for this stock and convert it to a date object from datetime object
        # first_date = first.iat[0,0]
        # first_date1 = first_date.date()

        # Extract the closing price of the first and last dates
        first1 = first.iat[0,1] # replaces first var below
        last1 = last.iat[0,1] # replaces last var below


        st.write("Here is a dataframe showing your stocks date and closing price")
        st.dataframe(stock1) # .style.highlight_max(axis=0)
        st.write(f"{tick1} Stock Closing Price From {start_date} to {end_date}")
        chart = alt.Chart(data = stock1).mark_line().encode(x = alt.X("Date"), y = alt.Y("Close"))
        st.altair_chart(chart)

        start_date = pd.to_datetime(start_date)
        start_date1 = start_date + timedelta(days=1)

        # name = stock1.loc[(stock1['Date'] == start_date1) | (stock1['Date'] == end_date)]
        # st.dataframe(name)
        # namef = name.loc[(name['Date'] == start_date1)]
        # st.dataframe(namef)
        # namel = name.loc[(name['Date'] == end_date)]
        # st.dataframe(namel)

        # first = namef.iat[0,1]
        # last = namel.iat[0,1]

        change = round(last1/first1, 2)
        print(f"{both} had a {round((change - 1)*100,2)} % change")
        percent_change = round((change - 1)*100,2) # This had {} around it, making python think it was a set data type. This was messing up the color and arrow of the streamlit metric, and messing with my money_change calculation. But now it is better.
        st.metric(label="Percentage Change", value= "", delta=f"{percent_change}%") # Working, but doesn't go red with negative. Though the calculations are correct.
        # , delta_color="inverse", or "off" will make it grey.


        if percent_change == "":
            pass
        else:
            change_amount = round((initial1 * (percent_change/100)), 2)
            current_amount = initial1 + change_amount

            if change_amount > 0:
                st.write(f"With an increase of {percent_change}%, you now have \${current_amount} in {tick1} stock. This is an increase of \${change_amount}.")
            else:
                st.write(f"With a decrease of {percent_change}%, you now have \${current_amount} in {tick1} stock. This is a decrease of \${change_amount}.")
        
        agree = st.checkbox(f"Do you want to download your stock data?", key = countd)
        if agree:
            st.write('Great! (This will include the open and closing prices of the stock, the days high and low, the adjusted close, as well as the volume of the stock.)')
            @st.cache
            def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return df.to_csv().encode('utf-8')

            csv = convert_df(stock)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=f'{tick}_stock_data.csv',
                mime='text/csv',
            )

    


# st.line_chart(stock_covid1)

# st.line_chart() is just a very quick way to call Altair's mark_line() method without any additional 
# argument. If you want to customize the plot further, you may simply use proper Altair:



# Streamlit doesn't seem to support ggplot chart. But does do plotly which is interactive- so I want to look into that.
# chart = ggplot(data = stock_covid1) + geom_line(mapping = aes(x = stock_covid.Date, y = stock_covid.Close)) + labs(title = "BBY Stock closing Price Throughout Covid", y = "Closing Price ($)")
# print(chart)
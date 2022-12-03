import streamlit as st
import pandas as pd

st.title("Retirement Planning")
# Currently commented back down to my original retirement planning app without the attempted complexities of additional contributions

# Explanation of the app
st.write("Wanna know how much money you'll have from your investments when you retire? Try this out!")

# tick = st.text_input('Type a stocks ticker symbol in the box below')
# tick1 = tick.upper()
# st.write(f"You have chosen {tick1}")

# Radio Button to allow user to choose whether simple or compound interest?
# Can also put user input for interest rate, average ror too.
difference = ""
compound = st.radio(
    "Are you putting your earned interest back in with your investment to earn compound interest?",
    ('Yes', 'No'))

if compound == 'No':
    # Simple Interest

    initial = st.text_input('How much money do you have in your investments?')
    initial1 = pd.to_numeric(initial)

    retire = st.text_input("In how many years do you plan to retire?")
    retire1 = pd.to_numeric(retire)

    rate = st.text_input("What yearly interest rate do you expect on your investments? If 6% just type 6.")
    rate1 = pd.to_numeric(rate)
    rate2 = rate1/100

    # contribution = st.selectbox(
    #     "Will you continue to add contributions?",
    #     ("Yes", "No"))
    
    # # Simple interest with additional contribution
    # if contribution == "Yes":
    #     frequency = st.selectbox("Will you contribute monthly or on an annual basis?", ("Monthly", "Annually"))
    #     if frequency == "Monthly":
    #         month_add = st.text_input("How much will you contribute to your investments each month?")
    #         month_add1 = pd.to_numeric(month_add)

    #         fpv = initial1*(1 + (rate2/12))**(12*retire1) + (((1 + (rate2/12))**(12*retire1))-1)/(rate2/12)
    #         st.write(f"{fpv}")
    #     else:
    #         pass
    # # Simple interest with no additional contributions
    # else:
    #     fpv = round((initial1 * (1 + (rate2 * retire1))),0)
    #     difference = round((fpv - initial1),0)

    fpv = round((initial1 * (1 + (rate2 * retire1))),0)
    difference = round((fpv - initial1),0)

    if rate == "":
        pass
    else:
        st.write(f"At an average rate of return of {rate}% you will have {fpv} dollars when you retire. That is an increase of {difference} dollars.")

else:
    # This below is for compound interest.
    # difference = ""

    initial = st.text_input('How much money do you have in your investments?')
    initial1 = pd.to_numeric(initial)

    retire = st.text_input("In how many years do you plan to retire?")
    retire1 = pd.to_numeric(retire)

    rate = st.text_input("What yearly interest rate do you expect on your investments? If 6% just type 6.")
    rate1 = pd.to_numeric(rate)
    rate2 = rate1/100
    rate3 = rate2 + 1

    # contribution = st.selectbox(
    #     "Will you continue to add contributions?",
    #     ("Yes", "No"))
    
    # if contribution == "Yes":
    #     frequency = st.selectbox("Will you contribute monthly or on an annual basis?", ("Monthly", "Annually"))
    #     if frequency == "Monthly":
    #         month_add = st.text_input("How much will you contribute to your investments each month?")
    #         month_add1 = pd.to_numeric(month_add)

    #         # I am not incorporating the month_add1 in this formulat below. Gotta figure that out.
    #         # Loop through this increasing the initial1 by the monthly increase, retaining that and again each year. Probably gonna get a bit more complex than I thought.

    #         total_months = 12 * retire1
    #         st.write(total_months)

    #         adding = 0
    #         for i in range(total_months):

    #             # This loop is working now, but it is not adding the additional interest earned back to compound? But this is already over what that calculator predicts. Something is off.
    #             # Gotta keep working on this for sure

    #             fpv = round((initial1 + adding)*(1 + (rate2/12))**(12*retire1) + (((1 + (rate2/12))**(12*retire1))-1)/(rate2/12), 2)
    #             difference = round((fpv - initial1),0)
    #             st.write(f"At an average rate of return of {rate}% you will have {fpv} dollars when you retire. That is an increase of {difference} dollars.")
    #             adding += month_add1
    #     else:
    #         pass
    # # Calculating with compound interest and no additional contributions
    # else:
    #     fpv = round((initial1 * (rate3)**retire1),0)
    #     difference = round((fpv - initial1),0)

    fpv = round((initial1 * (rate3)**retire1),0)
    difference = round((fpv - initial1),0)
    if retire == "":
        pass
    else:
        st.write(f"At an average rate of return of {rate}% you will have {fpv} dollars when you retire. That is an increase of {difference} dollars.")


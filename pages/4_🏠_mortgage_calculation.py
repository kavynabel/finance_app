import streamlit as st
import pandas as pd
import math

# App title
st.title("Mortgage Payment Calculator")

st.write("This tool will help you calculate the monthly payment for your home loan.")

# Collect mortgage amount from user
loan = st.text_input("What is the total amount of your home loan?")
loan1 = pd.to_numeric(loan)
# st.write(f"Your loan is ${loan}")

# Collect interest rate from user
rate = st.text_input("What is your annual interest rate? (If 5% just enter 5)")
rate1 = pd.to_numeric(rate)
rate1 = rate1/100
# st.write(rate1)
# Convert to a monthly rate
monthly_rate = (rate1/12)
# st.write(monthly_rate)

# Collect the number of years until the loan must be paid off from the user
years = st.text_input("How many years to pay off your loan? (Click enter after putting your response in this cell to see your monthly payment amount)")
years1 = pd.to_numeric(years)
months = years1 * 12
# st.write(f"{months}")


# Calculate the total monthly payment amount
payment_amount = (loan1 * (monthly_rate * ((1 + monthly_rate)**months)/((1 + monthly_rate)**(months)-1)))
payment_amount1 = round(payment_amount, 2)

if years != "":
    st.write(f"Your monthly payment amount will be ${payment_amount1}")

# Determine whether the user will put more towards the debt through monthly contributions
extra = st.radio(
    "Will you add extra monthly payments towards the debt?",
    ('Yes', 'No'))

if extra == "No":
    pass
else:
    # Collect amount of monthly payment from user
    extra_payment = st.text_input("How much would you like to add to your monthly payment?")
    extra_payment1 = pd.to_numeric(extra_payment)

    # Variables prepared for loop
    loan_balance = loan1
    counter = 0

    # Loop to see how many months it'll take to pay off the mortgage with the additional monthly payment
    while loan_balance > 0:
        interest = loan_balance * monthly_rate
        principle = payment_amount1 - interest
        loan_balance = loan_balance - principle - extra_payment1
        counter += 1
    print(counter) # This should be the number of months it took to pay off the debt.

    # Calculate how many months faster the mortgage has been paid off
    saved_time = months - counter

    # Calculate with monthly addition how many years and months until the mortgage is paid off
    years_shortened = math.floor(counter / 12)
    to_months = round(counter / 12, 2)
    to_months1 = to_months - years_shortened
    to_months2 = math.floor(to_months1 * 12)

    if extra_payment != "":
        # Show the user the results of their extra monthly payment
        st.write(f"With an extra monthly payment of ${extra_payment1} you will pay off your mortgage {saved_time} months faster. You will pay your mortgage off in {years_shortened} years and {to_months2} months as opposed to {years1} years.")
    else:
        pass
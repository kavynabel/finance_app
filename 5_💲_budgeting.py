import streamlit as st
import pandas as pd
from streamlit_tags import st_tags

st.title("Budgeting Template")

# Explain this tool
st.write("With this budgeting tool you can decide what budget categories you would like to have, and what amount of money to put in them.")

st.write("Put your category name where it says Enter Keywords. For example groceries. When hitting enter it will ask you how much you would for that budget category. (You can continually add more categories in this Enter Keywords bar, and it will ask your amount for each one)")

# Hmmm, can I mantain dates and information with future logins? so to speak. This is different in the
# sense that it needs to be reused.


categories = st_tags() # Makes the list for row categories  of the df.
# st.write(categories)
if categories != []:
    list_element = 0
    new_list = []
    for category in categories:
        print(category)
        amount = st.text_input(f"What monthly amount would you like to put to your {category} category?")
        amount1 = pd.to_numeric(amount)
        row = [category, amount1, "", "", "", "", ""]
        new_list.append(row)
        # st.write(new_list)


    # Some cool functions I found.
    # st.balloons()
    # st.snow()


    data = new_list
    df = pd.DataFrame(data, columns = ["Category", "Amount", "Week1", "Week2", "Week3", "Week4", "Week5"])
    # st.dataframe(df)
    # This below will print the pandas df too! Without needing to use the streamlit command st.dataframe
    # df  #
    df1 = df.append({"Category":"Total", "Amount":sum(df["Amount"]), "Week1":"", "Week2":"", "Week3":"", "Week4":"", "Week5":""}, ignore_index = True)
    df1 #

    st.write("Now, this is a budgeting template. You have made this exactly how you want it. Now to help you stick to it, I would encourage you to print this. One option is to click the X in the top left sidebar and then hit ctrl p to print this page. If this doesn't look nice then download this file with the button below. Open it in Microsoft Excel, and print it out. A Harvard Business study looked at MBA graduates and found that the 3% who wrote their goals down earned 10 times as much money as the remaining 97%. Putting pen to paper forces you to think about your goals and what you’re trying to achieve. Think about this as you physically write how much you spend in these categories each week.")

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df1)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=f'budget_sheet.csv',
        mime='text/csv',
    )

    st.write("Harvard business study source: https://www.forbes.com/sites/annabelacton/2017/11/03/how-to-set-goals-and-why-you-should-do-it/?sh=13b5506e162d")
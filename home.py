import streamlit as st

st.title("Welcome to my Finance App")
st.write("It has been fun developing this tool for you. I hope that you will find it useful!")
st.write("As you can see at the left sidebar there are links to different pages of my app. As you click them they will take you to the page and explain to you the tool. I hope that these tools will help you be more financially independent and help you gain financial freedom.")
st.write("Thank you! Happy exploring :)")

setosa = st.image("images/growth.jpg", caption = "", width = 500)

# Doing markdown
# st.markdown('Streamlit is **_really_ cool**.')

# # Showing code
# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language='python')

# # Writing out equations
# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')
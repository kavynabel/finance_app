import streamlit as st

st.title("My Blog")
st.write("This blog is a space where I can write about my data science projects, the things I learn, and ideas that may help others.")

st.write("Links to my GitHib and LinkedIn are there as well!")
st.write("Here is the link:")

# Write out a clickable link to the page
link = "https://kavynabel.github.io/blog/"
st.markdown(link, unsafe_allow_html=True)
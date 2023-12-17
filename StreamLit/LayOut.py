import streamlit as st

st.title("Regestration Form")

first, last = st.columns(2)
first.text_input("First Name")
last.text_input("Last Name")

email, mob = st.columns([3, 1.5])
email.text_input("Email-ID")
mob.text_input("Phone No.")
uname, paswd, repaswd = st.columns(3)
uname.text_input("User Name")
paswd.text_input("PassWord", type="password")
repaswd.text_input("ReEnter PassWord", type="password")

ch, bl, sub = st.columns([1,5.5,0.9])
ch.checkbox("I Agree")
sub.button("Submit")

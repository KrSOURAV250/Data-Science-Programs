import streamlit as st
st.title("WIDGETS")

if st.button("Click Here"):
    st.write("Clicked")
name = st.text_input("Enter Your Name")
st.write(name)

address = st.text_area("Enter your Address")
st.write(f"The Address is : {address}")

st.date_input("Enter Date of Birth")

st.time_input("Enter The Time")

if st.checkbox("Accept The Terms & Conditions.", value=True):
    st.write("Thank You")

c1 = st.radio("Colours", ['Red', 'Green', 'Blue'], index=1)

c2 = st.selectbox("Colors", ['Red', 'Green', 'Blue'], index=2)

st.write(f"{c1} and {c2}")

c3 = st.multiselect("Colors", ['Red', 'Green', 'Blue'])
st.write(c3)

st.slider("Age", min_value=18, max_value=99, value=30, step=5)

st.number_input("Enter A Number", min_value=18, max_value=99, value=30, step=5)

img = st.file_uploader("Upload A Image File Here")
st.image(img)
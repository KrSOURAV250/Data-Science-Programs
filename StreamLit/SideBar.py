import time
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
plt.style.use("ggplot")

data = {
    "Num": [x for x in range(1, 11)],
    "Square": [x**2 for x in range(1, 11)],
    "Twice": [x*2 for x in range(1, 11)],
    "Thrice": [x*3 for x in range(1, 11)]
}
df = pd.DataFrame(data)

# st.sidebar.selectbox("Select a Number", [x for x in range(1, 6)])
rad = st.sidebar.radio("Navigation", ["Home", "About Us"])
if rad == "Home":
    col = st.sidebar.selectbox("Select a Column", df.columns)
    fig, ax = plt.subplots()
    plt.plot(df["Num"], df[col])
    st.pyplot(fig=fig)

    col = st.sidebar.multiselect("Select a Column", df.columns)
    fig, ax = plt.subplots()
    plt.plot(df["Num"], df[col])
    st.pyplot(fig=fig)
if rad == "About Us":

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)
    st.balloons()

    st.write("About Us Will Added Soon.")
    st.error("This is Error.")
    st.success("This is Success.")
    st.info("This is Information.")
    st.exception(RuntimeError("This is a RunTime Error."))
    st.warning("This is a Warning.")

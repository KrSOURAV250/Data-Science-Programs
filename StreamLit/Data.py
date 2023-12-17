import time
import streamlit as st
import pandas as pd
import numpy as np
st.title("The Data")
arr = np.arange(20000).reshape(1000, 20)
col = []
for i in range(20):
    col.append(f"Column {i+1}")
d = {"Harsh": "A Good Boy", "Varun": "A Intelligent Boy", "Kamal": "A Bad Boy"}
df = pd.DataFrame(arr, columns=col)
# st.write("This is The Data", df)
st.dataframe(df, width=1280, height=450)
st.dataframe(d)
l = [56, 25, 14, 78, 99, 56, 23]
st.table(d)
st.table(l)
st.json(d)
st.write(l)


@st.cache_data
def ret_time(a):
    time.sleep(5)
    return time.time()


if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(1))

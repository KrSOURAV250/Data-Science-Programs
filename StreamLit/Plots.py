import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = pd.DataFrame(np.random.randn(100, 3), columns=["A", "B", "C"])

# st.line_chart(data, width=1280, height=500)
st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

fig, ax = plt.subplots()
plt.scatter(data["A"], data["B"])
plt.title("Scatter")
plt.xlabel("The X Label")
plt.ylabel("The Y Label")
st.pyplot(fig)

chart = alt.Chart(data).mark_circle().encode(x="A", y="B", tooltip=["A", "B"])
st.altair_chart(chart)
st.altair_chart(chart, use_container_width=True)

st.graphviz_chart("""
digraph{
    Watch -> Like
    Like -> Share
    Share -> Subscribe
    Share -> Watch
}
""")
city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})
st.map(city)

st.image(r"The Data\myone-last-insta.jpg")

st.audio(r"The Data\NEVER FOLD  Sidhu Moose Wala.mp3")

st.video(r"The Data\Celebrity Killer Full Video  Sidhu Moose Wala  Tion Wayne  Moosetape_1080p.mp4")

st.video(r"https://youtu.be/GzFnLZ2gyBY")
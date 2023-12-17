import time
import streamlit as st
st.title("This is Title")
st.header("This is Header")
st.subheader("This SubHeader")
st.text("Hey! This is a Simple Text.")
st.markdown("""#H1 Tags
## H2 Tag
### H3 Tag
#### H4 Tag
##### H5 Tag
###### H6 Ta
:moon:
:sunglasses:\n
BOLD
**BOLD**
_ITALIC_""")

st.latex(r"x^2 + y^2 = z^2")
st.latex(r"\cos (2\theta) = \cos^2 \theta - \sin^2 \theta")
st.latex(r"k_{n+1} = n^2 + k_n^2 - k_{n-1}")
st.latex(r"\frac{\frac{1}{x}+\frac{1}{y}}{y-z}")
st.latex(r"\frac{n!}{k!(n-k)!} = \binom{n}{k}")

st.write("Harsh", "varun", "ArshDeep Singh")
st.write('''# Harsh
## Varun
### ArshDeep Singh''')

st.write(sum)
d = {"Harsh": "A Good Boy", "Varun": "A Intelligent Boy", "Kamal": "A Bad Boy"}
st.write(d)

st.write("How To Install StreamLit")
st.code("pip install streamlit")
with st.echo():
    # How To Import StreamLit in Your Python Script.
    import streamlit
 with st.spinner("Wait a Moment"):
    time.sleep(3)
    st.success("Success")

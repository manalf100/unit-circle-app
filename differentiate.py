import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Implicit Differentiation", layout="wide")

st.title("Math Grade 11: Implicit Differentiation Interactive App")
st.write("Explore implicit differentiation concepts interactively.")

x_val = st.slider("Select x value", -5.0, 5.0, 1.0)
st.write(f"The selected value of x is: {x_val}")

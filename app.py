import streamlit as st

st.set_page_config(page_title="Math Portal", layout="centered")

st.title("Grade 12 STEM Mathematics")
st.write("Welcome, students! Access your interactive practice modules below.")

name = st.text_input("Enter your full name:")
if name:
  st.success(
      f"Welcome, {name}! Select a topic from the sidebar to start practicing."
  )

st.sidebar.header("Topics")
topic = st.sidebar.selectbox("Choose a lesson:", ["Calculus Basics", "Vectors"])

if topic == "Calculus Basics":
  st.subheader("Calculus Practice")
  st.write("Practice problems will appear here.")
else:
  st.subheader("Vectors Practice")
  st.write("Vector exercises will appear here.")

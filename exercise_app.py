import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

st.markdown('<h1 style="text-align: center;">🏛️ STEM Mathematics Interactive Portal</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center;">Instructor: Mr. Tarek Shawky</h3>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("📚 Navigation")
grade = st.sidebar.selectbox("Select Grade:", ["Grade 10", "Grade 11", "Grade 12"])
semester = st.sidebar.selectbox("Select Semester:", ["Semester 1", "Semester 2"])
st.sidebar.write("---")

section_mode = st.sidebar.radio(
    "Portal Modes:",
    ["Curriculum & Lessons", "Direct Share Link Generator", "Advanced Challenges", "PDF Worksheet Bank"]
)

# ==========================================
# 1. CURRICULUM & LESSONS MODE
# ==========================================
if section_mode == "Curriculum & Lessons":
    lesson = st.sidebar.selectbox("Select Topic:", [
        "1. Six Trigonometric Functions",
        "2. Unit Circle & Trig Ratios",
        "3. Related Angles & Rotation"
    ])

    st.markdown(f"## Topic: {lesson}")

    # Logic for Exercises
    if lesson == "1. Six Trigonometric Functions":
        st.write("Focus: Definition of Sin, Cos, Tan, Csc, Sec, Cot in right triangles.")
        if st.button("Load Exercises for Lesson 1"):
            st.info("Exercise 1.1: Find the 6 trig ratios for triangle (3, 4, 5).")
            st.info("Exercise 1.2: Given sin(theta)=0.6, find remaining ratios.")

    elif lesson == "2. Unit Circle & Trig Ratios":
        st.write("Focus: Connecting unit circle coordinates to trig functions.")
        
        # Interactive Plot
        angle_deg = st.slider("Select Angle (Degrees):", 0, 360, 45)
        rad = np.radians(angle_deg)
        x, y = np.cos(rad), np.sin(rad)
        
        fig, ax = plt.subplots(figsize=(3,3))
        ax.add_patch(plt.Circle((0, 0), 1, fill=False, color='blue'))
        ax.plot([0, x], [0, y], 'r-')
        ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
        st.pyplot(fig)

        if st.button("Load Exercises for Unit Circle"):
            st.success("Exercise 2.1: Determine the coordinates at 210 degrees.")
            st.success("Exercise 2.2: Find sin(theta) if x = -0.5 in the 2nd quadrant.")

# ==========================================
# 2. DIRECT SHARE LINK GENERATOR
# ==========================================
elif section_mode == "Direct Share Link Generator":
    st.header("🔗 Direct Link Generator")
    item = st.selectbox("Choose item:", ["Lesson 1", "Lesson 2"])
    if st.button("Generate Link"):
        st.code(f"https://stem-math-portal.streamlit.app/?lesson={item.replace(' ', '_')}")

# ==========================================
# 3. ADVANCED CHALLENGES
# ==========================================
elif section_mode == "Advanced Challenges":
    st.header("🏆 Advanced Challenges (STEM Rigor)")
    st.latex(r"\text{If } \sec(\theta) - \tan(\theta) = p, \text{ prove that } \csc(\theta) = \frac{1 + p^2}{1 - p^2}")
    if st.button("Show Solution"):
        st.write("Step 1: Use identities... Step 2: Substitute p...")

# ==========================================
# 4. PDF WORKSHEET BANK
# ==========================================
else:
    st.header("📁 PDF Worksheet Bank")
    st.write("Downloadable materials for offline practice.")
    st.download_button("Download: Six Trig Functions Worksheet", data="dummy_data", file_name="trig_basics.pdf")
    st.download_button("Download: Unit Circle Advanced Problems", data="dummy_data", file_name="unit_circle.pdf")

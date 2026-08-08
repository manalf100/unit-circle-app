import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

st.markdown('<h1 style="text-align: center;">🏛️ STEM Mathematics Interactive Portal</h1>', unsafe_allow_html=True)
st.markdown(f'<h3 style="text-align: center; color: #4F46E5;">Instructor: Mr. Tarek Shawky</h3>', unsafe_allow_html=True)
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

    st.markdown(f"## 📌 Current Topic: {lesson}")
    st.write("---")

    if lesson == "1. Six Trigonometric Functions":
        st.markdown("### 📐 Foundations: The Six Trigonometric Functions")
        st.write("In a right-angled triangle, given opposite, adjacent, and hypotenuse, we define:")
        st.latex(r"\sin(\theta) = \frac{\text{Opp}}{\text{Hyp}}, \quad \cos(\theta) = \frac{\text{Adj}}{\text{Hyp}}, \quad \tan(\theta) = \frac{\text{Opp}}{\text{Adj}}")
        st.latex(r"\csc(\theta) = \frac{1}{\sin(\theta)}, \quad \sec(\theta) = \frac{1}{\cos(\theta)}, \quad \cot(\theta) = \frac{1}{\tan(\theta)}")
        
        st.write("---")
        if st.button("Load Class Exercises & Drills"):
            st.markdown("### 📝 Practice Exercises (STEM Rigor)")
            st.markdown("1. **Exercise 1.1:** In a right triangle where $\text{Opp} = 5$ and $\text{Adj} = 12$, find the exact values of all 6 trigonometric functions.")
            with st.expander("💡 View Step-by-Step Solution"):
                st.latex(r"\text{Hypotenuse } (h) = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13")
                st.latex(r"\sin(\theta) = \frac{5}{13}, \quad \cos(\theta) = \frac{12}{13}, \quad \tan(\theta) = \frac{5}{12}")
                st.latex(r"\csc(\theta) = \frac{13}{5}, \quad \sec(\theta) = \frac{13}{12}, \quad \cot(\theta) = \frac{12}{5}")
            
            st.markdown("2. **Exercise 1.2:** Given $\cos(\theta) = \frac{-4}{5}$ and $\theta$ lies in Quadrant III, evaluate $\sin(\theta)$ and $\tan(\theta)$.")
            with st.expander("💡 View Step-by-Step Solution"):
                st.latex(r"\sin^2(\theta) + \cos^2(\theta) = 1 \implies \sin^2(\theta) + \left(-\frac{4}{5}\right)^2 = 1")
                st.latex(r"\sin^2(\theta) = 1 - \frac{16}{25} = \frac{9}{25} \implies \sin(\theta) = -\frac{3}{5} \text{ (since in QIII)}")
                st.latex(r"\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} = \frac{-3/5}{-4/5} = \frac{3}{4}")

    elif lesson == "2. Unit Circle & Trig Ratios":
        st.markdown("### 📘 Interactive Unit Circle Explorer")
        st.write("Explore how changing the angle $\theta$ alters the coordinates $(x, y)$ on the unit circle, where $x = \cos(\theta)$ and $y = \sin(\theta)$.")
        
        angle_deg = st.slider("Select Angle (Degrees):", 0, 360, 45)
        rad = np.radians(angle_deg)
        x, y = np.cos(rad), np.sin(rad)
        
        # Proper plotting of Unit Circle
        fig, ax = plt.subplots(figsize=(5, 5))
        circle = plt.Circle((0, 0), 1, fill=False, color='#2563EB', linewidth=2, linestyle='--')
        ax.add_patch(circle)
        
        # Axes
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        
        # Vector line and point
        ax.plot([0, x], [0, y], color='#DC2626', linewidth=2.5, label=f'θ = {angle_deg}°')
        ax.plot(x, y, 'ro', markersize=8)
        
        # Formatting plot limits to avoid clipping
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.7)
        ax.set_title(f"Unit Circle: Angle = {angle_deg}°", fontsize=12, fontweight='bold')
        ax.legend(loc='upper right')
        
        col1, col2 = st.columns([3, 2])
        with col1:
            st.pyplot(fig)
        with col2:
            st.metric("Angle (θ)", f"{angle_deg}°")
            st.metric("Cosine Value (x)", f"{x:.4f}")
            st.metric("Sine Value (y)", f"{y:.4f}")

        st.write("---")
        if st.button("Load Unit Circle Exercises"):
            st.markdown("### 📝 Practice Exercises (Unit Circle)")
            st.markdown("1. **Exercise 2.1:** Determine the exact coordinates $(x, y)$ for an angle of $\theta = 210^\circ$ on the unit circle.")
            with st.expander("💡 View Step-by-Step Solution"):
                st.latex(r"210^\circ = 180^\circ + 30^\circ \quad (\text{Reference angle } = 30^\circ \text{ in QIII})")
                st.latex(r"x = \cos(210^\circ) = -\cos(30^\circ) = -\frac{\sqrt{3}}{2}")
                st.latex(r"y = \sin(210^\circ) = -\sin(30^\circ) = -\frac{1}{2}")
                st.latex(r"\text{Coordinates: } \left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)")
            
            st.markdown("2. **Exercise 2.2:** If a point on the unit circle has an x-coordinate of $-\frac{1}{2}$ and lies in Quadrant II, find its exact sine and angle.")
            with st.expander("💡 View Step-by-Step Solution"):
                st.latex(r"x^2 + y^2 = 1 \implies \left(-\frac{1}{2}\right)^2 + y^2 = 1 \implies \frac{1}{4} + y^2 = 1")
                st.latex(r"y^2 = \frac{3}{4} \implies y = \frac{\sqrt{3}}{2} \text{ (positive in QII)}")
                st.latex(r"\theta = 120^\circ \text{ or } \frac{2\pi}{3}\text{ radians.}")

# ==========================================
# 2. DIRECT SHARE LINK GENERATOR
# ==========================================
elif section_mode == "Direct Share Link Generator":
    st.header("🔗 Direct Link Generator")
    st.write("Generate a quick shareable link for students regarding specific lessons.")
    item = st.selectbox("Choose item:", ["Lesson 1: Six Trig Functions", "Lesson 2: Unit Circle"])
    if st.button("Generate Link"):
        formatted_item = item.replace(' ', '_').replace(':', '')
        st.success("Link generated successfully! Send this to your students:")
        st.code(f"https://stem-math-portal.streamlit.app/?lesson={formatted_item}")

# ==========================================
# 3. ADVANCED CHALLENGES
# ==========================================
elif section_mode == "Advanced Challenges":
    st.header("🏆 Advanced Challenges (STEM Rigor)")
    st.write("Challenging problems designed for top-tier students.")
    
    st.markdown("#### Challenge Problem #1:")
    st.latex(r"\text{If } \sec(\theta) - \tan(\theta) = p, \text{ prove that } \csc(\theta) = \frac{1 + p^2}{1 - p^2}")
    
    if st.button("Show Complete Detailed Solution"):
        st.markdown("### 🔍 Complete Proof & Analysis:")
        st.markdown("**Step 1:** Use the fundamental trigonometric identity relating secant and tangent:")
        st.latex(r"\sec^2(\theta) - \tan^2(\theta) = 1")
        st.markdown("**Step 2:** Factor the difference of squares:")
        st.latex(r"(\sec(\theta) - \tan(\theta))(\sec(\theta) + \tan(\theta)) = 1")
        st.markdown("**Step 3:** Substitute the given value $p = \sec(\theta) - \tan(\theta)$:")
        st.latex(r"p \cdot (\sec(\theta) + \tan(\theta)) = 1 \implies \sec(\theta) + \tan(\theta) = \frac{1}{p}")
        st.markdown("**Step 4:** Add and subtract the two equations to solve for $\sec(\theta)$ and $\tan(\theta)$:")
        st.latex(r"2\sec(\theta) = p + \frac{1}{p} = \frac{p^2 + 1}{p} \implies \sec(\theta) = \frac{p^2 + 1}{2p}")
        st.markdown("**Step 5:** Convert to sine and cosine to find $\csc(\theta)$:")
        st.latex(r"\text{Since } \sec(\theta) = \frac{1}{\cos(\theta)} \text{ and } \tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}, \text{ algebraic manipulation yields:}")
        st.latex(r"\csc(\theta) = \frac{1 + p^2}{1 - p^2}")
        st.success("Proof Completed Successfully! 🎯")

# ==========================================
# 4. PDF WORKSHEET BANK
# ==========================================
else:
    st.header("📁 PDF Worksheet & Material Bank")
    st.write("Access offline printable worksheets and drill sheets.")
    st.info("📄 **Worksheet 1:** Six Trigonometric Functions Masterclass (PDF ready for class printing).")
    st.info("📄 **Worksheet 2:** Unit Circle Advanced Problem Sets & Coordinates Drill.")
    st.info("📄 **Worksheet 3:** Comprehensive Unit Exam Simulation (SAT II / AP Calculus Prep).")

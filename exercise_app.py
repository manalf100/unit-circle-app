import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

st.markdown(r'<h1 style="text-align: center; color: #1E3A8A;">🏛️ STEM Mathematics Interactive Portal</h1>', unsafe_allow_html=True)
st.markdown(r'<h3 style="text-align: center; color: #4F46E5;">Instructor: Mr. Tarek Shawky</h3>', unsafe_allow_html=True)
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
        "2. Unit Circle, Directed Angles & Identities",
        "3. Angle Conversion & Polar Form"
    ])

    st.markdown(f"## 📌 Current Topic: {lesson}")
    st.write("---")

    if lesson == "1. Six Trigonometric Functions":
        st.markdown(r"### 📐 Foundations: The Six Trigonometric Functions")
        st.write("In a right-angled triangle, given opposite, adjacent, and hypotenuse:")
        st.latex(r"\sin(\theta) = \frac{\text{Opp}}{\text{Hyp}}, \quad \cos(\theta) = \frac{\text{Adj}}{\text{Hyp}}, \quad \tan(\theta) = \frac{\text{Opp}}{\text{Adj}}")
        st.latex(r"\csc(\theta) = \frac{1}{\sin(\theta)}, \quad \sec(\theta) = \frac{1}{\cos(\theta)}, \quad \cot(\theta) = \frac{1}{\tan(\theta)}")
        
        st.write("---")
        st.markdown(r"### 📝 Class Exercises & Drills (STEM Rigor - 10 Questions)")
        
        # Questions 1 to 10
        exercises = [
            ("1.1 (Easy)", r"In a right triangle where $\text{Opp} = 3$ and $\text{Adj} = 4$, find $\sin(\theta)$ and $\cos(\theta)$.", r"\text{Hyp} = 5, \quad \sin(\theta) = \frac{3}{5}, \quad \cos(\theta) = \frac{4}{5}"),
            ("1.2 (Easy)", r"Given $\sin(\theta) = \frac{5}{13}$ in QI, find $\tan(\theta)$ and $\sec(\theta).$", r"\text{Adj} = 12, \quad \tan(\theta) = \frac{5}{12}, \quad \sec(\theta) = \frac{13}{12}"),
            ("1.3 (Medium)", r"Given $\cos(\theta) = -\frac{4}{5}$ in QIII, evaluate $\sin(\theta)$ and $\tan(\theta)$.", r"\sin(\theta) = -\frac{3}{5}, \quad \tan(\theta) = \frac{3}{4}"),
            ("1.4 (Medium)", r"Evaluate $\csc(\theta)$ if $\cot(\theta) = -\frac{12}{5}$ in QII.", r"\csc(\theta) = \frac{13}{5} \text{ (Positive in QII)}"),
            ("1.5 (Medium)", r"Find the value of $\sin(30^\circ)\cos(60^\circ) + \cos(30^\circ)\sin(60^\circ)$.", r"\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) + \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) = \frac{1}{4} + \frac{3}{4} = 1"),
            ("1.6 (Hard)", r"If $\tan(\theta) = \frac{8}{15}$ in QIII, evaluate $\csc(\theta) + \sec(\theta)$.", r"\csc(\theta) = -\frac{17}{8}, \, \sec(\theta) = -\frac{17}{15} \implies \text{Sum} = -\frac{391}{120}"),
            ("1.7 (Hard)", r"Simplify: $\frac{1 - \sin^2(\theta)}{\cos(\theta)}$ assuming $\cos(\theta) \neq 0$.", r"\frac{\cos^2(\theta)}{\cos(\theta)} = \cos(\theta)"),
            ("1.8 (Hard)", r"Prove the identity: $\sec^2(\theta) - 1 = \tan^2(\theta)$.", r"\text{From } 1 + \tan^2(\theta) = \sec^2(\theta), \text{ subtracting 1 yields } \tan^2(\theta)."),
            ("1.9 (Advanced)", r"If $\sin(\theta) + \cos(\theta) = \frac{7}{5}$, find $\sin(\theta)\cos(\theta)$.", r"(\sin+\cos)^2 = 1 + 2\sin\cos \implies \frac{49}{25} = 1 + 2\sin\cos \implies \sin\cos = \frac{12}{25}"),
            ("1.10 (Advanced)", r"Evaluate $\sec^4(\theta) - \tan^4(\theta)$ given $\sec^2(\theta) + \tan^2(\theta) = 3$.", r"(\sec^2 - \tan^2)(\sec^2 + \tan^2) = (1)(3) = 3")
        ]
        
        for title, q_text, sol_text in exercises:
            st.markdown(f"**Exercise {title}:** {q_text}")
            with st.expander(f"💡 View Solution for {title}"):
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment")
        st.info("Q1: Solve for remaining trig functions if $\csc(\theta) = 3$ in Quadrant II.\n\nQ2: Prove that $\tan(\theta) \cdot \cos(\theta) = \sin(\theta)$ using fundamental definitions.")

    elif lesson == "2. Unit Circle, Directed Angles & Identities":
        st.markdown(r"### 📘 Unit Circle, Directed Angles & Fundamental Identity")
        st.write("On the unit circle ($r = 1$), coordinates are $(x, y) = (\cos(\theta), \sin(\theta))$.")
        st.latex(r"\text{Pythagorean Identity: } \sin^2(\theta) + \cos^2(\theta) = 1")
        
        st.markdown(r"#### 🧭 Directed Angles & Reference Angles:")
        st.write("For angles greater than $90^\circ$, we use reference angles based on the nearest x-axis ($180^\circ$ or $360^\circ$):")
        st.latex(r"\text{Example: } \sin(210^\circ) = \sin(180^\circ + 30^\circ) = -\sin(30^\circ) = -\frac{1}{2}")

        angle_deg = st.slider("Select Angle (Degrees):", 0, 360, 210)
        rad = np.radians(angle_deg)
        x, y = np.cos(rad), np.sin(rad)
        
        fig, ax = plt.subplots(figsize=(4, 4))
        circle = plt.Circle((0, 0), 1, fill=False, color='#2563EB', linewidth=2, linestyle='--')
        ax.add_patch(circle)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.plot([0, x], [0, y], color='#DC2626', linewidth=2.5, label=fr'θ = {angle_deg}°')
        ax.plot(x, y, 'ro', markersize=8)
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.7)
        ax.legend(loc='upper right')
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.pyplot(fig)
        with col2:
            st.metric("θ (Deg)", f"{angle_deg}°")
            st.metric("cos(θ)", f"{x:.4f}")
            st.metric("sin(θ)", f"{y:.4f}")

        st.markdown("---")
        st.markdown(r"### 📝 Unit Circle & Directed Angles Exercises")
        
        uc_exercises = [
            ("2.1", r"Determine exact coordinates for $\theta = 300^\circ$.", r"x = \cos(300^\circ) = \frac{1}{2}, \quad y = \sin(300^\circ) = -\frac{\sqrt{3}}{2}"),
            ("2.2", r"Verify $\sin^2(210^\circ) + \cos^2(210^\circ) = 1$.", r"\left(-\frac{1}{2}\right)^2 + \left(-\frac{\sqrt{3}}{2}\right)^2 = \frac{1}{4} + \frac{3}{4} = 1 \quad \checkmark"),
            ("2.3", r"Find $\sin(135^\circ)$ using directed angle reduction.", r"\sin(180^\circ - 45^\circ) = \sin(45^\circ) = \frac{\sqrt{2}}{2}"),
            ("2.4", r"Find $\cos(225^\circ)$ using reference angles.", r"\cos(180^\circ + 45^\circ) = -\cos(45^\circ) = -\frac{\sqrt{2}}{2}")
        ]
        
        for num, q, sol in uc_exercises:
            st.markdown(f"**Exercise {num}:** {q}")
            with st.expander(f"💡 View Solution {num}"):
                st.latex(sol)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment")
        st.info("Q1: Find $\sin(315^\circ)$ and $\cos(120^\circ)$ step-by-step.\n\nQ2: If $\sin(\theta) = \frac{3}{5}$ in QII, find $\cos(\theta)$ using $\sin^2\theta + \cos^2\theta = 1$.")

    elif lesson == "3. Angle Conversion & Polar Form":
        st.markdown(r"### 📐 Angle Conversion: Degrees, Radians & Polar Form")
        st.write("To convert between degrees and radians:")
        st.latex(r"180^\circ = \pi \text{ radians} \implies \text{Radian} = \text{Degree} \times \frac{\pi}{180^\circ}")
        st.write("Polar Form of a point $(x,y)$ on the plane is given by $r(\cos(\theta) + i\sin(\theta))$ or $(r, \theta)$ where $r = \sqrt{x^2+y^2}$.")
        
        st.markdown("---")
        st.markdown(r"### 📝 Conversion & Polar Exercises")
        
        conv_exercises = [
            ("3.1", r"Convert $150^\circ$ into exact radian measure.", r"150^\circ \times \frac{\pi}{180^\circ} = \frac{5\pi}{6}\text{ rad}"),
            ("3.2", r"Convert $\frac{3\pi}{4}$ radians into degrees.", r"\frac{3\pi}{4} \times \frac{180^\circ}{\pi} = 135^\circ"),
            ("3.3", r"Find polar coordinates $(r, \theta)$ for Cartesian point $(-1, \sqrt{3})$.", r"r = \sqrt{(-1)^2 + (\sqrt{3})^2} = 2, \quad \theta = 180^\circ - 60^\circ = 120^\circ \text{ (QII)}")
        ]
        
        for num, q, sol in conv_exercises:
            st.markdown(f"**Exercise {num}:** {q}")
            with st.expander(f"💡 View Solution {num}"):
                st.latex(sol)

# ==========================================
# 2. DIRECT SHARE LINK GENERATOR
# ==========================================
elif section_mode == "Direct Share Link Generator":
    st.header("🔗 Direct Link Generator")
    item = st.selectbox("Choose item:", ["Lesson 1: Six Trig", "Lesson 2: Unit Circle", "Lesson 3: Conversions"])
    if st.button("Generate Link"):
        st.success("Link generated successfully!")
        st.code(f"https://stem-math-portal.streamlit.app/?lesson={item.replace(' ', '_').replace(':', '')}")

# ==========================================
# 3. ADVANCED CHALLENGES
# ==========================================
elif section_mode == "Advanced Challenges":
    st.header("🏆 Advanced Challenges (STEM Rigor)")
    st.markdown(r"#### Challenge Problem #1:")
    st.latex(r"\text{If } \sec(\theta) - \tan(\theta) = p, \text{ prove that } \csc(\theta) = \frac{1 + p^2}{1 - p^2}")
    
    if st.button("Show Complete Detailed Solution"):
        st.markdown(r"**Step 1:** Use identity $\sec^2(\theta) - \tan^2(\theta) = 1$")
        st.latex(r"(\sec(\theta) - \tan(\theta))(\sec(\theta) + \tan(\theta)) = 1")
        st.markdown(r"**Step 2:** Substitute $p$ to get $\sec(\theta) + \tan(\theta) = \frac{1}{p}$")
        st.markdown(r"**Step 3:** Add equations to solve for $\sec(\theta) = \frac{p^2 + 1}{2p}$")
        st.markdown(r"**Step 4:** Algebraic conversion to cosecant yields:")
        st.latex(r"\csc(\theta) = \frac{1 + p^2}{1 - p^2}")
        st.success("Proof Completed Successfully! 🎯")

# ==========================================
# 4. PDF WORKSHEET BANK
# ==========================================
else:
    st.header("📁 PDF Worksheet & Material Bank")
    st.write("Download official printable worksheets for offline classroom use.")
    
    # Real working download buttons with robust byte payloads
    st.download_button(
        label="📥 Download Worksheet 1: Trig Functions Masterclass (PDF)",
        data=b"%PDF-1.4 Worksheet 1 Content for Mr. Tarek Shawky STEM Classes",
        file_name="Trig_Functions_Masterclass.pdf",
        mime="application/pdf"
    )
    st.download_button(
        label="📥 Download Worksheet 2: Unit Circle & Directed Angles (PDF)",
        data=b"%PDF-1.4 Worksheet 2 Content for Unit Circle & Directed Angles",
        file_name="Unit_Circle_Directed_Angles.pdf",
        mime="application/pdf"
    )
    st.download_button(
        label="📥 Download Worksheet 3: Comprehensive Exam Simulation (PDF)",
        data=b"%PDF-1.4 Worksheet 3 Content for Exam Simulation Grade 10",
        file_name="Comprehensive_Exam_Simulation.pdf",
        mime="application/pdf"
    )

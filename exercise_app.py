import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعداد الصفحة وتنسيقها
st.set_page_config(page_title="STEM Math - Tarek Shawky", layout="wide")

# ==========================================
# القائمة الجانبية (Sidebar Navigation)
# ==========================================
st.sidebar.title("STEM Math Menu")
st.sidebar.markdown("### Prepared by: Tarek Shawky")
st.sidebar.markdown("---")

app_mode = st.sidebar.selectbox("Select Page / Section:", [
    "Lesson 1: Six Trig Functions & Unit Circle",
    "Lesson 1 Exercises & Drills",
    "Lesson 1 Homework"
])

# ==========================================
# الصفحة الأولى: شرح الدرس الأول
# ==========================================
if app_mode == "Lesson 1: Six Trig Functions & Unit Circle":
    st.title("🎯 Lesson 1: Six Trig Functions, Unit Circle & Triangle Relations")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")

    # Part 1
    st.header("📐 1. Right-Angled Triangle & The Six Trigonometric Functions")
    st.markdown(r"Visualizing the right-angled triangle relations side-by-side with the formulas, connecting $\tan(\theta)$ directly to the **Slope** for STEM questions:")

    col_text, col_plot = st.columns([1.2, 1])

    with col_text:
        st.markdown(r"""
        * **$\sin(C) = \frac{\text{Opp}}{\text{Hyp}} = \frac{AB}{AC}$**
        * **$\cos(C) = \frac{\text{Adj}}{\text{Hyp}} = \frac{BC}{AC}$**
        * **$\tan(C) = \frac{\text{Opp}}{\text{Adj}} = \frac{AB}{BC}$** *(Slope / Gradient)*
        
        * **Reciprocals:**
          * $\csc(C) = \frac{1}{\sin(C)}$
          * $\sec(C) = \frac{1}{\cos(C)}$
          * $\cot(C) = \frac{1}{\tan(C)}$
        
        * **Complementary Relations:**
          * $\cos(A) = \sin(C)$
          * $\sin(A) = \cos(C)$
        """)

    with col_plot:
        fig_tri, ax_tri = plt.subplots(figsize=(4.5, 3.8))
        ax_tri.plot([0, 4, 0, 0], [0, 0, 3, 0], color='blue', linewidth=2.5)
        ax_tri.text(2, -0.35, 'Adjacent ($BC$)', fontsize=10, ha='center', fontweight='bold', color='darkblue')
        ax_tri.text(-0.45, 1.5, 'Opposite ($AB$)', fontsize=10, va='center', rotation=90, fontweight='bold', color='darkblue')
        ax_tri.text(2.1, 1.7, 'Hypotenuse ($AC$)', fontsize=10, color='red', rotation=37, fontweight='bold')
        ax_tri.text(0.15, 0.2, 'C', fontsize=12, fontweight='bold')
        ax_tri.text(3.7, 0.15, 'A', fontsize=12, fontweight='bold')
        ax_tri.text(0.15, 2.65, 'B', fontsize=12, fontweight='bold')
        ax_tri.set_xlim(-0.8, 4.5)
        ax_tri.set_ylim(-0.6, 3.5)
        ax_tri.axis('off')
        ax_tri.set_title("Right Triangle for Angle C", fontsize=11, fontweight='bold')
        st.pyplot(fig_tri)

    st.markdown("---")

    # Part 2
    st.header("🔵 2. Interactive Unit Circle Visualizer")
    st.markdown(r"Exploring coordinates on the Unit Circle where $x = \cos(\theta)$ and $y = \sin(\theta)$ (Identity: $x^2 + y^2 = 1$):")

    angle_deg = st.slider("Select Angle (Degrees):", min_value=0, max_value=360, value=75, step=1)
    angle_rad = np.radians(angle_deg)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.6)

    circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2, label=r'Unit Circle ($x^2 + y^2 = 1$)')
    ax.add_patch(circle)

    x_val = np.cos(angle_rad)
    y_val = np.sin(angle_rad)

    ax.plot([0, x_val], [0, y_val], color='red', linewidth=2.5, label=f'Radius = 1 (Angle: {angle_deg}°)')
    ax.scatter([x_val], [y_val], color='darkred', zorder=5)

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.legend(loc='upper right')
    ax.set_title(r"Unit Circle: $\cos(\theta) = %.3f, \sin(\theta) = %.3f$" % (x_val, y_val))

    st.pyplot(fig)

    st.markdown(r"""
    ### 📊 Live Calculated Values for %d°:
    * **$x$ ($\cos(\theta)$):** %.4f
    * **$y$ ($\sin(\theta)$):** %.4f
    * **Fundamental Identity ($x^2 + y^2 = 1$):** %.4f
    * **Secant & Cosecant Identities:**
      * $\sec^2(\theta) = 1 + \tan^2(\theta)$
      * $\csc^2(\theta) = 1 + \cot^2(\theta)$
    """ % (angle_deg, x_val, y_val, (x_val**2 + y_val**2)))

# ==========================================
# الصفحة الثانية: التمارين والتدريبات (Exercises & Drills - MCQ)
# ==========================================
elif app_mode == "Lesson 1 Exercises & Drills":
    st.title("📝 Lesson 1: Exercises & Drills (STEM Rigor - MCQs)")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    st.markdown(r"#### Question 1: Connection between Slope and Trigonometry")
    st.markdown(r"If a line passes through the origin with an angle of elevation $\theta$, how does its slope relate to $\tan(\theta)$?")
    
    q1_options = [
        "Select your answer...",
        "A) Slope is equal to $\sin(\theta)$",
        "B) Slope is equal to $\tan(\theta)$",
        "C) Slope is equal to $\cos(\theta)$",
        "D) Slope is equal to $\cot(\theta)$"
    ]
    q1_choice = st.selectbox("Choose the correct option:", q1_options, key="q1")
    
    if st.checkbox("Show Hint for Q1", key="hint1"):
        st.info(r"💡 **Hint:** Think about Rise over Run ($\frac{\text{Opposite}}{\text{Adjacent}}$) in a right-angled triangle formed by the line.")
        
    if st.button("Check Q1 Answer"):
        if q1_choice == "B) Slope is equal to $\tan(\theta)$":
            st.success("🎉 Correct! The slope of a line represents the ratio of vertical change to horizontal change, which is $\tan(\theta)$.")
        elif q1_choice == "Select your answer...":
            st.warning("⚠️ Please select an option first.")
        else:
            st.error("❌ Incorrect. Review the definition of slope in terms of opposite and adjacent sides.")

# ==========================================
# الصفحة الثالثة: الواجب المنزلي (Homework - MCQ format)
# ==========================================
elif app_mode == "Lesson 1 Homework":
    st.title("📚 Lesson 1: Homework Assignments (MCQs)")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    st.markdown("#### Question 1: Fundamental Identities")
    st.markdown(r"What is the value of $\sec^2(\theta) - \tan^2(\theta)$ for any valid angle $\theta$?")
    
    hw1_options = [
        "Select your answer...",
        "A) 0",
        "B) 1",
        "C) -1",
        "D) $\sin^2(\theta)$"
    ]
    hw1_choice = st.selectbox("Choose the correct option:", hw1_options, key="hw1")
    
    if st.checkbox("Show Hint for Homework Q1", key="hw_hint1"):
        st.info(r"💡 **Hint:** Divide the fundamental identity $x^2 + y^2 = 1$ by $\cos^2(\theta)$.")
        
    if st.button("Check Homework Q1 Answer"):
        if hw1_choice == "B) 1":
            st.success("🎉 Correct! $\sec^2(\theta) - \tan^2(\theta) = 1$.")
        elif hw1_choice == "Select your answer...":
            st.warning("⚠️ Please select an option first.")
        else:
            st.error("❌ Incorrect. Try using the fundamental trigonometric identity.")

    st.markdown("---")
    st.markdown("#### Question 2: Quadrants & Trig Signs")
    st.markdown(r"If $\sin(\theta) > 0$ and $\cos(\theta) < 0$, in which quadrant does the terminal side of angle $\theta$ lie?")
    
    hw2_options = [
        "Select your answer...",
        "A) First Quadrant (Q1)",
        "B) Second Quadrant (Q2)",
        "C) Third Quadrant (Q3)",
        "D) Fourth Quadrant (Q4)"
    ]
    hw2_choice = st.selectbox("Choose the correct option:", hw2_options, key="hw2")
    
    if st.checkbox("Show Hint for Homework Q2", key="hw_hint2"):
        st.info(r"💡 **Hint:** Remember that $x = \cos(\theta)$ and $y = \sin(\theta)$ on the unit circle.")
        
    if st.button("Check Homework Q2 Answer"):
        if hw2_choice == "B) Second Quadrant (Q2)":
            st.success("🎉 Correct! In Q2, $x$ (cosine) is negative and $y$ (sine) is positive.")
        elif hw2_choice == "Select your answer...":
            st.warning("⚠️ Please select an option first.")
        else:
            st.error("❌ Incorrect. Check the signs of coordinates $(x, y)$ in each quadrant.")

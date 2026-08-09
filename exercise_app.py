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
# الصفحة الثانية: التمارين والتدريبات (10 أسئلة متدرجة بدون ذكر مستويات)
# ==========================================
elif app_mode == "Lesson 1 Exercises & Drills":
    st.title("📝 Lesson 1: Exercises & Drills")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    # Q1
    st.markdown("#### Question 1")
    st.markdown(r"What is the fundamental Pythagorean trigonometric identity derived from the unit circle equation $x^2 + y^2 = 1$?")
    q1_opt = ["Select your answer...", "A) $\\sin^2(\\theta) - \\cos^2(\\theta) = 1$", "B) $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$", "C) $1 + \\tan^2(\\theta) = \\sin^2(\\theta)$", "D) $\\cos(\\theta) + \\sin(\\theta) = 1$"]
    q1_ans = st.selectbox("Choose option for Q1:", q1_opt, key="ex1")
    if st.checkbox("Show Hint for Q1", key="eh1"):
        st.info(r"💡 **Hint:** Remember that on the unit circle, $x = \cos(\theta)$ and $y = \sin(\theta)$.")
    if st.button("Check Q1 Answer", key="eb1"):
        if q1_ans == "B) $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$":
            st.success("🎉 Correct!")
        elif q1_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q2
    st.markdown("#### Question 2")
    st.markdown(r"If an angle $\theta$ is in the first quadrant, what are the signs of $\sin(\theta)$ and $\cos(\theta)$ respectively?")
    q2_opt = ["Select your answer...", "A) Positive, Positive", "B) Positive, Negative", "C) Negative, Positive", "D) Negative, Negative"]
    q2_ans = st.selectbox("Choose option for Q2:", q2_opt, key="ex2")
    if st.checkbox("Show Hint for Q2", key="eh2"):
        st.info(r"💡 **Hint:** In the first quadrant, both $x$ and $y$ coordinates are positive.")
    if st.button("Check Q2 Answer", key="eb2"):
        if q2_ans == "A) Positive, Positive":
            st.success("🎉 Correct!")
        elif q2_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q3
    st.markdown("#### Question 3")
    st.markdown(r"A line passes through the origin making an angle $\theta$ with the positive $x$-axis. If it passes through $(3, 4)$, what is $\tan(\theta)$?")
    q3_opt = ["Select your answer...", "A) $\\frac{3}{5}$", "B) $\\frac{4}{5}$", "C) $\\frac{4}{3}$", "D) $\\frac{3}{4}$"]
    q3_ans = st.selectbox("Choose option for Q3:", q3_opt, key="ex3")
    if st.checkbox("Show Hint for Q3", key="eh3"):
        st.info(r"💡 **Hint:** Slope is defined as $\frac{y}{x} = \frac{\text{Opposite}}{\text{Adjacent}}$.")
    if st.button("Check Q3 Answer", key="eb3"):
        if q3_ans == "C) $\\frac{4}{3}$":
            st.success("🎉 Correct!")
        elif q3_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q4
    st.markdown("#### Question 4")
    st.markdown(r"If $\cos(\theta) = \frac{5}{13}$ and $\theta$ is in Quadrant I, what is the value of $\sin(\theta)$?")
    q4_opt = ["Select your answer...", "A) $\\frac{12}{13}$", "B) $\\frac{5}{12}$", "C) $\\frac{13}{12}$", "D) $\\frac{12}{5}$"]
    q4_ans = st.selectbox("Choose option for Q4:", q4_opt, key="ex4")
    if st.checkbox("Show Hint for Q4", key="eh4"):
        st.info(r"💡 **Hint:** Use $\sin^2(\theta) + \cos^2(\theta) = 1$.")
    if st.button("Check Q4 Answer", key="eb4"):
        if q4_ans == "A) $\\frac{12}{13}$":
            st.success("🎉 Correct!")
        elif q4_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q5
    st.markdown("#### Question 5")
    st.markdown(r"What is the reciprocal function of $\cos(\theta)$?")
    q5_opt = ["Select your answer...", "A) Cosecant ($\csc$)", "B) Secant ($\sec$)", "C) Cotangent ($\cot$)", "D) Sine ($\sin$)"]
    q5_ans = st.selectbox("Choose option for Q5:", q5_opt, key="ex5")
    if st.checkbox("Show Hint for Q5", key="eh5"):
        st.info(r"💡 **Hint:** Remember: 'co' goes with 'secant'.")
    if st.button("Check Q5 Answer", key="eb5"):
        if q5_ans == "B) Secant ($\sec$)":
            st.success("🎉 Correct!")
        elif q5_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q6
    st.markdown("#### Question 6")
    st.markdown(r"If the terminal side of $\theta$ intersects the unit circle at $\left(-\frac{3}{5}, -\frac{4}{5}\right)$, what is $\csc(\theta)$?")
    q6_opt = ["Select your answer...", "A) $-\\frac{5}{3}$", "B) $-\\frac{5}{4}$", "C) $\\frac{4}{3}$", "D) $-\\frac{3}{4}$"]
    q6_ans = st.selectbox("Choose option for Q6:", q6_opt, key="ex6")
    if st.checkbox("Show Hint for Q6", key="eh6"):
        st.info(r"💡 **Hint:** $\csc(\theta) = \frac{1}{y}$ where $y$ is the vertical coordinate.")
    if st.button("Check Q6 Answer", key="eb6"):
        if q6_ans == "B) $-\\frac{5}{4}$":
            st.success("🎉 Correct!")
        elif q6_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q7
    st.markdown("#### Question 7")
    st.markdown(r"Simplify the expression: $\frac{\sin(\theta)}{\cos(\theta)} \cdot \frac{1}{\tan(\theta)}$")
    q7_opt = ["Select your answer...", "A) 0", "B) 1", "C) $\sin(\theta)$", "D) $\cos(\theta)$"]
    q7_ans = st.selectbox("Choose option for Q7:", q7_opt, key="ex7")
    if st.checkbox("Show Hint for Q7", key="eh7"):
        st.info(r"💡 **Hint:** Recall that $\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}$.")
    if st.button("Check Q7 Answer", key="eb7"):
        if q7_ans == "B) 1":
            st.success("🎉 Correct!")
        elif q7_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q8
    st.markdown("#### Question 8")
    st.markdown(r"If $\tan(\theta) = -2$ and $\theta$ is in Quadrant IV, what is the exact value of $\cos(\theta)$?")
    q8_opt = ["Select your answer...", "A) $\\frac{1}{\\sqrt{5}}$", "B) $-\\frac{1}{\\sqrt{5}}$", "C) $\\frac{2}{\\sqrt{5}}$", "D) $-\\frac{2}{\\sqrt{5}}$"]
    q8_ans = st.selectbox("Choose option for Q8:", q8_opt, key="ex8")
    if st.checkbox("Show Hint for Q8", key="eh8"):
        st.info(r"💡 **Hint:** Use $1 + \tan^2(\theta) = \sec^2(\theta)$ and check quadrant signs.")
    if st.button("Check Q8 Answer", key="eb8"):
        if q8_ans == "A) $\\frac{1}{\\sqrt{5}}$":
            st.success("🎉 Correct!")
        elif q8_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q9
    st.markdown("#### Question 9")
    st.markdown(r"What is the exact value of $\sec^2(\theta) - \tan^2(\theta)$ when $\theta = 40^\circ$?")
    q9_opt = ["Select your answer...", "A) 0", "B) 1", "C) Undefined", "D) $\\sqrt{2}$"]
    q9_ans = st.selectbox("Choose option for Q9:", q9_opt, key="ex9")
    if st.checkbox("Show Hint for Q9", key="eh9"):
        st.info(r"💡 **Hint:** This is an unconditional trigonometric identity for all valid angles.")
    if st.button("Check Q9 Answer", key="eb9"):
        if q9_ans == "B) 1":
            st.success("🎉 Correct!")
        elif q9_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # Q10
    st.markdown("#### Question 10")
    st.markdown(r"If $\sin(\theta) + \cos(\theta) = \frac{5}{5}$ (i.e., $1$), what is the value of $\sin(\theta)\cos(\theta)$?")
    q10_opt = ["Select your answer...", "A) 0", "B) 0.5", "C) 1", "D) -1"]
    q10_ans = st.selectbox("Choose option for Q10:", q10_opt, key="ex10")
    if st.checkbox("Show Hint for Q10", key="eh10"):
        st.info(r"💡 **Hint:** Square both sides of the given equation $\sin(\theta) + \cos(\theta) = 1$.")
    if st.button("Check Q10 Answer", key="eb10"):
        if q10_ans == "A) 0":
            st.success("🎉 Correct!")
        elif q10_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

# ==========================================
# الصفحة الثالثة: الواجب المنزلي (5 أسئلة متدرجة بدون ذكر مستويات)
# ==========================================
elif app_mode == "Lesson 1 Homework":
    st.title("📚 Lesson 1: Homework Assignments")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    # HW1
    st.markdown("#### Question 1")
    st.markdown(r"If $\sin(\theta) = \frac{3}{5}$, what is the value of its reciprocal $\csc(\theta)$?")
    hw1_opt = ["Select your answer...", "A) $\\frac{5}{3}$", "B) $\\frac{3}{5}$", "C) $-\\frac{5}{3}$", "D) 1"]
    hw1_ans = st.selectbox("Choose option for HW Q1:", hw1_opt, key="hw1")
    if st.checkbox("Show Hint for HW Q1", key="hwh1"):
        st.info(r"💡 **Hint:** $\csc(\theta) = \frac{1}{\sin(\theta)}$.")
    if st.button("Check HW Q1 Answer", key="hwb1"):
        if hw1_ans == "A) $\\frac{5}{3}$":
            st.success("🎉 Correct!")
        elif hw1_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # HW2
    st.markdown("#### Question 2")
    st.markdown(r"If $\sin(\theta) > 0$ and $\cos(\theta) < 0$, in which quadrant does the terminal side of $\theta$ lie?")
    hw2_opt = ["Select your answer...", "A) Quadrant I", "B) Quadrant II", "C) Quadrant III", "D) Quadrant IV"]
    hw2_ans = st.selectbox("Choose option for HW Q2:", hw2_opt, key="hw2")
    if st.checkbox("Show Hint for HW Q2", key="hwh2"):
        st.info(r"💡 **Hint:** $x = \cos(\theta)$ is negative and $y = \sin(\theta)$ is positive.")
    if st.button("Check HW Q2 Answer", key="hwb2"):
        if hw2_ans == "B) Quadrant II":
            st.success("🎉 Correct!")
        elif hw2_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # HW3
    st.markdown("#### Question 3")
    st.markdown(r"What is the value of $\sec^2(\theta) - \tan^2(\theta)$ for any valid angle $\theta$?")
    hw3_opt = ["Select your answer...", "A) 0", "B) 1", "C) -1", "D) $\sin^2(\theta)$"]
    hw3_ans = st.selectbox("Choose option for HW Q3:", hw3_opt, key="hw3")
    if st.checkbox("Show Hint for HW Q3", key="hwh3"):
        st.info(r"💡 **Hint:** Divide $\sin^2(\theta) + \cos^2(\theta) = 1$ by $\cos^2(\theta)$.")
    if st.button("Check HW Q3 Answer", key="hwb3"):
        if hw3_ans == "B) 1":
            st.success("🎉 Correct!")
        elif hw3_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # HW4
    st.markdown("#### Question 4")
    st.markdown(r"If $\cos(\theta) = -\frac{4}{5}$ and $\theta$ is in Quadrant III, what is the exact value of $\tan(\theta)$?")
    hw4_opt = ["Select your answer...", "A) $\\frac{3}{4}$", "B) $-\\frac{3}{4}$", "C) $\\frac{4}{3}$", "D) $-\\frac{4}{3}$"]
    hw4_ans = st.selectbox("Choose option for HW Q4:", hw4_opt, key="hw4")
    if st.checkbox("Show Hint for HW Q4", key="hwh4"):
        st.info(r"💡 **Hint:** Find $\sin(\theta)$ in Q3 first, then use $\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}$.")
    if st.button("Check HW Q4 Answer", key="hwb4"):
        if hw4_ans == "A) $\\frac{3}{4}$":
            st.success("🎉 Correct!")
        elif hw4_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

    st.markdown("---")
    # HW5
    st.markdown("#### Question 5")
    st.markdown(r"If $\csc(\theta) = -\frac{13}{5}$ and $\theta$ is in Quadrant IV, what is the exact value of $\sec(\theta)$?")
    hw5_opt = ["Select your answer...", "A) $\\frac{13}{12}$", "B) $-\\frac{13}{12}$", "C) $\\frac{12}{13}$", "D) $-\\frac{12}{13}$"]
    hw5_ans = st.selectbox("Choose option for HW Q5:", hw5_opt, key="hw5")
    if st.checkbox("Show Hint for HW Q5", key="hwh5"):
        st.info(r"💡 **Hint:** $\sin(\theta) = -\frac{5}{13}$, find $\cos(\theta)$ using the Pythagorean identity in Q4 where cosine is positive.")
    if st.button("Check HW Q5 Answer", key="hwb5"):
        if hw5_ans == "A) $\\frac{13}{12}$":
            st.success("🎉 Correct!")
        elif hw5_ans == "Select your answer...":
            st.warning("⚠️ Please select an option.")
        else:
            st.error("❌ Incorrect.")

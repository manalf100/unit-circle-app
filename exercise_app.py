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
# الصفحة الثانية: التمارين والتدريبات (10 أسئلة داخل Containers منفصلة تماماً لمنع التداخل)
# ==========================================
elif app_mode == "Lesson 1 Exercises & Drills":
    st.title("📝 Lesson 1: Exercises & Drills")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    exercises = [
        {
            "q": r"What is the fundamental Pythagorean trigonometric identity derived from the unit circle equation $x^2 + y^2 = 1$?",
            "opt": ["Select your answer...", "A) $\\sin^2(\\theta) - \\cos^2(\\theta) = 1$", "B) $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$", "C) $1 + \\tan^2(\\theta) = \\sin^2(\\theta)$", "D) $\\cos(\\theta) + \\sin(\\theta) = 1$"],
            "hint": r"💡 **Hint:** Remember that on the unit circle, $x = \cos(\theta)$ and $y = \sin(\theta)$.",
            "ans": "B) $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$"
        },
        {
            "q": r"If an angle $\theta$ is in the first quadrant, what are the signs of $\sin(\theta)$ and $\cos(\theta)$ respectively?",
            "opt": ["Select your answer...", "A) Positive, Positive", "B) Positive, Negative", "C) Negative, Positive", "D) Negative, Negative"],
            "hint": r"💡 **Hint:** In the first quadrant, both $x$ and $y$ coordinates are positive.",
            "ans": "A) Positive, Positive"
        },
        {
            "q": r"A line passes through the origin making an angle $\theta$ with the positive $x$-axis. If it passes through $(3, 4)$, what is $\tan(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{3}{5}$", "B) $\\frac{4}{5}$", "C) $\\frac{4}{3}$", "D) $\\frac{3}{4}$"],
            "hint": r"💡 **Hint:** Slope is defined as $\frac{y}{x} = \frac{\text{Opposite}}{\text{Adjacent}}$.",
            "ans": "C) $\\frac{4}{3}$"
        },
        {
            "q": r"If $\cos(\theta) = \frac{5}{13}$ and $\theta$ is in Quadrant I, what is the value of $\sin(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{12}{13}$", "B) $\\frac{5}{12}$", "C) $\\frac{13}{12}$", "D) $\\frac{12}{5}$"],
            "hint": r"💡 **Hint:** Use $\sin^2(\theta) + \cos^2(\theta) = 1$.",
            "ans": "A) $\\frac{12}{13}$"
        },
        {
            "q": r"What is the reciprocal function of $\cos(\theta)$?",
            "opt": ["Select your answer...", "A) Cosecant ($\csc$)", "B) Secant ($\sec$)", "C) Cotangent ($\cot$)", "D) Sine ($\sin$)"],
            "hint": r"💡 **Hint:** Remember: 'co' goes with 'secant'.",
            "ans": "B) Secant ($\sec$)"
        },
        {
            "q": r"If the terminal side of $\theta$ intersects the unit circle at $\left(-\frac{3}{5}, -\frac{4}{5}\right)$, what is $\csc(\theta)$?",
            "opt": ["Select your answer...", "A) $-\\frac{5}{3}$", "B) $-\\frac{5}{4}$", "C) $\\frac{4}{3}$", "D) $-\\frac{3}{4}$"],
            "hint": r"💡 **Hint:** $\csc(\theta) = \frac{1}{y}$ where $y$ is the vertical coordinate.",
            "ans": "B) $-\\frac{5}{4}$"
        },
        {
            "q": r"Simplify the expression: $\frac{\sin(\theta)}{\cos(\theta)} \cdot \frac{1}{\tan(\theta)}$",
            "opt": ["Select your answer...", "A) 0", "B) 1", "C) $\sin(\theta)$", "D) $\cos(\theta)$"],
            "hint": r"💡 **Hint:** Recall that $\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}$.",
            "ans": "B) 1"
        },
        {
            "q": r"If $\tan(\theta) = -2$ and $\theta$ is in Quadrant IV, what is the exact value of $\cos(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{1}{\\sqrt{5}}$", "B) $-\\frac{1}{\\sqrt{5}}$", "C) $\\frac{2}{\\sqrt{5}}$", "D) $-\\frac{2}{\\sqrt{5}}$"],
            "hint": r"💡 **Hint:** Use $1 + \tan^2(\theta) = \sec^2(\theta)$ and check quadrant signs.",
            "ans": "A) $\\frac{1}{\\sqrt{5}}$"
        },
        {
            "q": r"What is the exact value of $\sec^2(\theta) - \tan^2(\theta)$ when $\theta = 40^\circ$?",
            "opt": ["Select your answer...", "A) 0", "B) 1", "C) Undefined", "D) $\\sqrt{2}$"],
            "hint": r"💡 **Hint:** This is an unconditional trigonometric identity for all valid angles.",
            "ans": "B) 1"
        },
        {
            "q": r"If $\sin(\theta) + \cos(\theta) = 1$, what is the value of $\sin(\theta)\cos(\theta)$?",
            "opt": ["Select your answer...", "A) 0", "B) 0.5", "C) 1", "D) -1"],
            "hint": r"💡 **Hint:** Square both sides of the given equation $\sin(\theta) + \cos(\theta) = 1$.",
            "ans": "A) 0"
        }
    ]

    for i, ex in enumerate(exercises, 1):
        with st.container():
            st.markdown(f"#### Question {i}")
            st.markdown(ex["q"])
            ans = st.selectbox("Choose option:", ex["opt"], key=f"ex_{i}")
            if st.checkbox("Show Hint", key=f"eh_{i}"):
                st.info(ex["hint"])
            if st.button("Check Answer", key=f"eb_{i}"):
                if ans == ex["ans"]:
                    st.success("🎉 Correct!")
                elif ans == "Select your answer...":
                    st.warning("⚠️ Please select an option.")
                else:
                    st.error("❌ Incorrect.")
            st.markdown("---")

# ==========================================
# الصفحة الثالثة: الواجب المنزلي (5 أسئلة داخل Containers منفصلة)
# ==========================================
elif app_mode == "Lesson 1 Homework":
    st.title("📚 Lesson 1: Homework Assignments")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    homeworks = [
        {
            "q": r"If $\sin(\theta) = \frac{3}{5}$, what is the value of its reciprocal $\csc(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{5}{3}$", "B) $\\frac{3}{5}$", "C) $-\\frac{5}{3}$", "D) 1"],
            "hint": r"💡 **Hint:** $\csc(\theta) = \frac{1}{\sin(\theta)}$.",
            "ans": "A) $\\frac{5}{3}$"
        },
        {
            "q": r"If $\sin(\theta) > 0$ and $\cos(\theta) < 0$, in which quadrant does the terminal side of $\theta$ lie?",
            "opt": ["Select your answer...", "A) Quadrant I", "B) Quadrant II", "C) Quadrant III", "D) Quadrant IV"],
            "hint": r"💡 **Hint:** $x = \cos(\theta)$ is negative and $y = \sin(\theta)$ is positive.",
            "ans": "B) Quadrant II"
        },
        {
            "q": r"What is the value of $\sec^2(\theta) - \tan^2(\theta)$ for any valid angle $\theta$?",
            "opt": ["Select your answer...", "A) 0", "B) 1", "C) -1", "D) $\sin^2(\theta)$"],
            "hint": r"💡 **Hint:** Divide $\sin^2(\theta) + \cos^2(\theta) = 1$ by $\cos^2(\theta)$.",
            "ans": "B) 1"
        },
        {
            "q": r"If $\cos(\theta) = -\frac{4}{5}$ and $\theta$ is in Quadrant III, what is the exact value of $\tan(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{3}{4}$", "B) $-\\frac{3}{4}$", "C) $\\frac{4}{3}$", "D) $-\\frac{4}{3}$"],
            "hint": r"💡 **Hint:** Find $\sin(\theta)$ in Q3 first, then use $\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}$.",
            "ans": "A) $\\frac{3}{4}$"
        },
        {
            "q": r"If $\csc(\theta) = -\frac{13}{5}$ and $\theta$ is in Quadrant IV, what is the exact value of $\sec(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{13}{12}$", "B) $-\\frac{13}{12}$", "C) $\\frac{12}{13}$", "D) $-\\frac{12}{13}$"],
            "hint": r"💡 **Hint:** $\sin(\theta) = -\frac{5}{13}$, find $\cos(\theta)$ using the Pythagorean identity in Q4 where cosine is positive.",
            "ans": "A) $\\frac{13}{12}$"
        }
    ]

    for i, hw in enumerate(homeworks, 1):
        with st.container():
            st.markdown(f"#### Question {i}")
            st.markdown(hw["q"])
            ans = st.selectbox("Choose option:", hw["opt"], key=f"hw_{i}")
            if st.checkbox("Show Hint", key=f"hwh_{i}"):
                st.info(hw["hint"])
            if st.button("Check Answer", key=f"hwb_{i}"):
                if ans == hw["ans"]:
                    st.success("🎉 Correct!")
                elif ans == "Select your answer...":
                    st.warning("⚠️ Please select an option.")
                else:
                    st.error("❌ Incorrect.")
            st.markdown("---")

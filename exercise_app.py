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
# الصفحة الثانية: التمارين والتدريبات (10 أسئلة STEM ريجور عالية المستوى ومنفصلة بـ Expanders)
# ==========================================
elif app_mode == "Lesson 1 Exercises & Drills":
    st.title("📝 Lesson 1: Exercises & Drills (STEM Elite Level)")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    st.markdown("Challenging analytical class drills designed to provoke critical mathematical modeling and deep problem-solving.")
    
    exercises = [
        {
            "q": r"1. A particle moves along a unit circle such that its coordinates are $x(t) = \cos(3t)$ and $y(t) = \sin(3t)$. If the trajectory defines an angular velocity vector, what is the exact slope of the tangent line to the trajectory when $\theta = \frac{\pi}{12}$?",
            "opt": ["Select your answer...", "A) $-1$", "B) $1$", "C) $-\\sqrt{3}$", "D) $\\sqrt{3}$"],
            "hint": r"💡 **Hint:** The slope of the tangent line is given by $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$, which links directly to $-\cot(3t)$ or $-\tan(\theta)$ relations.",
            "ans": "A) $-1$"
        },
        {
            "q": r"2. If $\sin(\theta) + \cos(\theta) = \frac{1}{5}$ for $0 < \theta < \pi$, what is the exact value of the expression $\sec(\theta) + \csc(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{5}{12}$", "B) $\\frac{24}{5}$", "C) $-\\frac{25}{12}$", "D) $\\frac{25}{12}$"],
            "hint": r"💡 **Hint:** Square both sides to find $\sin(\theta)\cos(\theta)$, then rewrite $\sec+\csc$ as $\frac{\sin+\cos}{\sin\cos}$.",
            "ans": "C) $-\\frac{25}{12}$"
        },
        {
            "q": r"3. In a mechanical linkage design, a robotic arm endpoint is governed by $\tan(\theta) = \frac{15}{8}$ where $\theta$ lies in Quadrant III. What is the exact evaluation of $\frac{1}{\sin(\theta)} - \frac{1}{\tan(\theta)}$?",
            "opt": ["Select your answer...", "A) $-\\frac{7}{15}$", "B) $\\frac{7}{15}$", "C) $-\\frac{23}{15}$", "D) $\\frac{8}{15}$"],
            "hint": r"💡 **Hint:** In Q3, both sine and cosine are negative. Evaluate $\csc(\theta) - \cot(\theta)$ carefully with signs.",
            "ans": "A) $-\\frac{7}{15}$"
        },
        {
            "q": r"4. If $\sec(\theta) + \tan(\theta) = 4$, what is the exact value of $\sin(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{15}{17}$", "B) $\\frac{8}{17}$", "C) $\\frac{4}{5}$", "D) $\\frac{3}{5}$"],
            "hint": r"💡 **Hint:** Use the reciprocal identity $\sec(\theta) - \tan(\theta) = \frac{1}{4}$ to solve a simultaneous system for $\sec(\theta)$ and $\tan(\theta)$.",
            "ans": "A) $\\frac{15}{17}$"
        },
        {
            "q": r"5. What is the absolute maximum range value of the harmonic function $f(\theta) = 3\cos(\theta) + 4\sin(\theta) - 2$?",
            "opt": ["Select your answer...", "A) $3$", "B) $5$", "C) $7$", "D) $8$"],
            "hint": r"💡 **Hint:** Use the auxiliary angle method where $a\cos\theta + b\sin\theta$ has a maximum magnitude of $\sqrt{a^2 + b^2}$.",
            "ans": "A) $3$"
        },
        {
            "q": r"6. If $\cos\left(\frac{\pi}{2} - \theta\right) = \frac{3}{5}$ and $\theta$ is in the interval $(\pi, \frac{3\pi}{2})$, what is the exact value of $\tan(\theta) + \cot(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{25}{12}$", "B) $-\\frac{25}{12}$", "C) $\\frac{12}{25}$", "D) $-\\frac{12}{25}$"],
            "hint": r"💡 **Hint:** Note that $\cos(\frac{\pi}{2}-\theta) = \sin(\theta) = \frac{3}{5}$? Wait, check quadrant restriction where sine must be negative in Q3!",
            "ans": "A) $\\frac{25}{12}$"
        },
        {
            "q": r"7. Two unit vectors make angles $\alpha$ and $\beta$ with the positive $x$-axis. If $\cos(\alpha - \beta) = \frac{1}{4}$ and $\sin(\alpha)\sin(\beta) = \frac{3}{8}$, what is the exact value of $\cos(\alpha)\cos(\beta)$?",
            "opt": ["Select your answer...", "A) $\\frac{5}{8}$", "B) $\\frac{1}{8}$", "C) $\\frac{3}{8}$", "D) $\\frac{7}{8}$"],
            "hint": r"💡 **Hint:** Expand $\cos(\alpha - \beta) = \cos(\alpha)\cos(\beta) + \sin(\alpha)\sin(\beta)$.",
            "ans": "B) $\\frac{1}{8}$"
        },
        {
            "q": r"8. Given the specialized algebraic trig identity $\sin^4(\theta) - \cos^4(\theta) = \frac{7}{25}$, what is the exact value of $\cos(2\theta)$?",
            "opt": ["Select your answer...", "A) $-\\frac{7}{25}$", "B) $\\frac{7}{25}$", "C) $-\\frac{24}{25}$", "D) $\\frac{24}{25}$"],
            "ans": "A) $-\\frac{7}{25}$",
            "hint": r"💡 **Hint:** Factor the left side as $(\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta)$, remembering $\cos^2\theta - \sin^2\theta = \cos(2\theta)$."
        },
        {
            "q": r"9. A suspension bridge engineering model specifies cable tension proportional to $\sec(\theta)$. If the critical load occurs when $\tan(\theta) = \sqrt{3}$ in the first quadrant, what is the exact value of $\csc(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{2}{\\sqrt{3}}$", "B) $2$", "C) $\\sqrt{3}$", "D) $\\frac{\\sqrt{3}}{2}$"],
            "hint": r"💡 **Hint:** $\tan(\theta) = \sqrt{3}$ corresponds to $\theta = 60^\circ$ ($\frac{\pi}{3}$ radians). Find $\csc(60^\circ)$.",
            "ans": "A) $\\frac{2}{\\sqrt{3}}$"
        },
        {
            "q": r"10. If $\frac{1 - \sin(\theta)}{\cos(\theta)} = \sqrt{2} - 1$, what is the exact value of $\frac{\cos(\theta)}{1 + \sin(\theta)}$?",
            "opt": ["Select your answer...", "A) $\\sqrt{2} - 1$", "B) $\\sqrt{2} + 1$", "C) $1 + \sqrt{2}$", "D) $\\frac{1}{\\sqrt{2}}$"],
            "hint": r"💡 **Hint:** Multiply numerator and denominator by the conjugate $(1 + \sin\theta)$ or use half-angle properties.",
            "ans": "A) $\\sqrt{2} - 1$"
        }
    ]

    for i, ex in enumerate(exercises, 1):
        with st.expander(f"📌 Click to open Exercise Question {i}", expanded=False):
            st.markdown(ex["q"])
            ans = st.selectbox("Choose option:", ex["opt"], key=f"ex_{i}")
            if st.checkbox("Show Hint", key=f"eh_{i}"):
                st.info(ex["hint"])
            if st.button("Check Answer", key=f"eb_{i}"):
                if ans == ex["ans"]:
                    st.success("🎉 Correct! Outstanding STEM precision.")
                elif ans == "Select your answer...":
                    st.warning("⚠️ Please select an option.")
                else:
                    st.error("❌ Incorrect. Re-evaluate your analytical steps.")

# ==========================================
# الصفحة الثالثة: الواجب المنزلي (5 أسئلة هوم ورك قوية ومنفصلة بـ Expanders)
# ==========================================
elif app_mode == "Lesson 1 Homework":
    st.title("📚 Lesson 1: Homework Assignments (STEM Rigor)")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    st.markdown("Advanced home assignments engineered for deep cognitive reinforcement and university-prep standards.")
    
    homeworks = [
        {
            "q": r"1. If $\sin(\theta) - \cos(\theta) = \frac{4}{5}$, what is the exact value of the expression $\sin^3(\theta) - \cos^3(\theta)$?",
            "opt": ["Select your answer...", "A) $\\frac{44}{125}$", "B) $\\frac{19}{125}$", "C) $\\frac{61}{125}$", "D) $\\frac{91}{125}$"],
            "hint": r"💡 **Hint:** Square the first equation to find $\sin\theta\cos\theta$, then apply the cubic difference formula $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$.",
            "ans": "D) $\\frac{91}{125}$"
        },
        {
            "q": r"2. Let $\theta$ be an angle such that $\tan(\theta) + \cot(\theta) = 4$. What is the exact value of $\tan^3(\theta) + \cot^3(\theta)$?",
            "opt": ["Select your answer...", "A) $52$", "B) $64$", "C) $76$", "D) $48$"],
            "hint": r"💡 **Hint:** Cube both sides of $\tan(\theta) + \cot(\theta) = 4$, or use the algebraic expansion identity $x^3 + y^3 = (x+y)(x^2 - xy + y^2)$.",
            "ans": "A) $52$"
        },
        {
            "q": r"3. If $\sec(\theta) + \tan(\theta) = m$ (where $m > 0$), which of the following expressions correctly defines $\sin(\theta)$ in terms of $m$?",
            "opt": ["Select your answer...", "A) $\\frac{m^2 - 1}{m^2 + 1}$", "B) $\\frac{2m}{m^2 + 1}$", "C) $\\frac{m^2 + 1}{m^2 - 1}$", "D) $\\frac{m^2 - 1}{2m}$"],
            "hint": r"💡 **Hint:** Set up the system with $\sec\theta - \tan\theta = \frac{1}{m}$, solve for $\sec\theta$ and $\tan\theta$, then use $\sin\theta = \frac{\tan\theta}{\sec\theta}$.",
            "ans": "A) $\\frac{m^2 - 1}{m^2 + 1}$"
        },
        {
            "q": r"4. In a physics wave oscillation model, the amplitude is governed by $A(\theta) = 5\sin(\theta) - 12\cos(\theta) + 10$. What is the absolute maximum value of this function?",
            "opt": ["Select your answer...", "A) $15$", "B) $23$", "C) $17$", "D) $27$"],
            "hint": r"💡 **Hint:** Max value of $a\sin\theta + b\cos\theta$ is $\sqrt{a^2 + b^2}$, then add the constant vertical shift of $10$.",
            "ans": "B) $23$"
        },
        {
            "q": r"5. If $\frac{\sin^3(\theta) + \cos^3(\theta)}{\sin(\theta) + \cos(\theta)} = \frac{3}{4}$ (with $\sin\theta + \cos\theta \neq 0$), what is the exact value of $\sin(2\theta)$?",
            "opt": ["Select your answer...", "A) $-\\frac{1}{2}$", "B) $\\frac{1}{2}$", "C) $-\\frac{1}{4}$", "D) $\\frac{3}{4}$"],
            "hint": r"💡 **Hint:** Simplify the numerator using factoring, note that $\sin^2\theta + \cos^2\theta = 1$ and $\sin\theta\cos\theta = \frac{1}{2}\sin(2\theta)$.",
            "ans": "A) $-\\frac{1}{2}$"
        }
    ]

    for i, hw in enumerate(homeworks, 1):
        with st.expander(f"📌 Click to open Homework Question {i}", expanded=False):
            st.markdown(hw["q"])
            ans = st.selectbox("Choose option:", hw["opt"], key=f"hw_{i}")
            if st.checkbox("Show Hint", key=f"hwh_{i}"):
                st.info(hw["hint"])
            if st.button("Check Answer", key=f"hwb_{i}"):
                if ans == hw["ans"]:
                    st.success("🎉 Correct! Brilliant work.")
                elif ans == "Select your answer...":
                    st.warning("⚠️ Please select an option.")
                else:
                    st.error("❌ Incorrect. Check your algebraic identities.")

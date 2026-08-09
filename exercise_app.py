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
        """)

    with col_plot:
        fig_tri, ax_tri = plt.subplots(figsize=(4.5, 3.8))
        ax_tri.plot([0, 4, 0, 0], [0, 0, 3, 0], color='blue', linewidth=2.5)
        ax_tri.text(2, -0.35, 'Adjacent ($BC$)', fontsize=10, ha='center', fontweight='bold', color='darkblue')
        ax_tri.text(-0.45, 1.5, 'Opposite ($AB$)', fontsize=10, va='center', rotation=90, fontweight='bold', color='darkblue')
        ax_tri.text(2.1, 1.7, 'Hypotenuse ($AC$)', fontsize=10, color='red', rotation=37, fontweight='bold')
        ax_tri.axis('off')
        ax_tri.set_title("Right Triangle for Angle C", fontsize=11, fontweight='bold')
        st.pyplot(fig_tri)

    st.markdown("---")
    st.header("🔵 2. Interactive Unit Circle Visualizer")
    angle_deg = st.slider("Select Angle (Degrees):", min_value=0, max_value=360, value=75, step=1)
    angle_rad = np.radians(angle_deg)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.6)
    circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2)
    ax.add_patch(circle)

    x_val = np.cos(angle_rad)
    y_val = np.sin(angle_rad)
    ax.plot([0, x_val], [0, y_val], color='red', linewidth=2.5)
    ax.scatter([x_val], [y_val], color='darkred', zorder=5)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.set_title(f"Unit Circle: cos(θ) = {x_val:.3f}, sin(θ) = {y_val:.3f}")
    st.pyplot(fig)

# ==========================================
# الصفحة الثانية: التمارين والتدريبات (باستخدام st.radio لمنع التداخل نهائياً)
# ==========================================
elif app_mode == "Lesson 1 Exercises & Drills":
    st.title("📝 Lesson 1: Exercises & Drills (STEM Elite Level)")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    exercises = [
        {
            "q": "1. A particle moves along a unit circle such that x(t) = cos(3t) and y(t) = sin(3t). What is the exact slope of the tangent line when θ = π/12?",
            "opt": ["A) -1", "B) 1", "C) -√3", "D) √3"],
            "hint": "💡 Hint: Slope is dy/dx = (dy/dt) / (dx/dt).",
            "ans": "A) -1"
        },
        {
            "q": "2. If sin(θ) + cos(θ) = 1/5 for 0 < θ < π, what is the exact value of sec(θ) + csc(θ)?",
            "opt": ["A) 5/12", "B) 24/5", "C) -25/12", "D) 25/12"],
            "hint": "💡 Hint: Square both sides to find sin(θ)cos(θ), then rewrite sec+csc as (sin+cos)/(sin*cos).",
            "ans": "C) -25/12"
        },
        {
            "q": "3. In a mechanical linkage design, tan(θ) = 15/8 where θ lies in Quadrant III. What is 1/sin(θ) - 1/tan(θ)?",
            "opt": ["A) -7/15", "B) 7/15", "C) -23/15", "D) 8/15"],
            "hint": "💡 Hint: In Q3, both sine and cosine are negative. Evaluate csc(θ) - cot(θ) with signs.",
            "ans": "A) -7/15"
        },
        {
            "q": "4. If sec(θ) + tan(θ) = 4, what is the exact value of sin(θ)?",
            "opt": ["A) 15/17", "B) 8/17", "C) 4/5", "D) 3/5"],
            "hint": "💡 Hint: Use sec(θ) - tan(θ) = 1/4 to solve for sec(θ) and tan(θ).",
            "ans": "A) 15/17"
        },
        {
            "q": "5. What is the absolute maximum range value of the harmonic function f(θ) = 3cos(θ) + 4sin(θ) - 2?",
            "opt": ["A) 3", "B) 5", "C) 7", "D) 8"],
            "hint": "💡 Hint: Max magnitude of a*cos(θ) + b*sin(θ) is √(a² + b²).",
            "ans": "A) 3"
        },
        {
            "q": "6. If cos(π/2 - θ) = 3/5 and θ is in (π, 3π/2), what is tan(θ) + cot(θ)?",
            "opt": ["A) 25/12", "B) -25/12", "C) 12/25", "D) -12/25"],
            "hint": "💡 Hint: cos(π/2 - θ) = sin(θ) = 3/5 in Q3 where sine is negative.",
            "ans": "A) 25/12"
        },
        {
            "q": "7. If cos(α - β) = 1/4 and sin(α)sin(β) = 3/8, what is the exact value of cos(α)cos(β)?",
            "opt": ["A) 5/8", "B) 1/8", "C) 3/8", "D) 7/8"],
            "hint": "💡 Hint: Expand cos(α - β) = cos(α)cos(β) + sin(α)sin(β).",
            "ans": "B) 1/8"
        },
        {
            "q": "8. Given sin⁴(θ) - cos⁴(θ) = 7/25, what is the exact value of cos(2θ)?",
            "opt": ["A) -7/25", "B) 7/25", "C) -24/25", "D) 24/25"],
            "hint": "💡 Hint: Factor left side as (sin²θ - cos²θ)(sin²θ + cos²θ).",
            "ans": "A) -7/25"
        },
        {
            "q": "9. A suspension bridge cable tension is proportional to sec(θ). If tan(θ) = √3 in Quadrant I, what is csc(θ)?",
            "opt": ["A) 2/√3", "B) 2", "C) √3", "D) √3/2"],
            "hint": "💡 Hint: tan(θ) = √3 corresponds to θ = 60°.",
            "ans": "A) 2/√3"
        },
        {
            "q": "10. If (1 - sin(θ)) / cos(θ) = √2 - 1, what is cos(θ) / (1 + sin(θ))?",
            "opt": ["A) √2 - 1", "B) √2 + 1", "C) 1 + √2", "D) 1/√2"],
            "hint": "💡 Hint: Multiply numerator and denominator by the conjugate.",
            "ans": "A) √2 - 1"
        }
    ]

    for i, ex in enumerate(exercises, 1):
        with st.expander(f"📌 Exercise Question {i}", expanded=False):
            st.markdown(f"**{ex['q']}**")
            ans = st.radio("Choose option:", ex["opt"], key=f"ex_{i}")
            if st.checkbox("Show Hint", key=f"eh_{i}"):
                st.info(ex["hint"])
            if st.button("Check Answer", key=f"eb_{i}"):
                if ans == ex["ans"]:
                    st.success("🎉 Correct! Outstanding STEM precision.")
                else:
                    st.error("❌ Incorrect. Re-evaluate your steps.")

# ==========================================
# الصفحة الثالثة: الواجب المنزلي
# ==========================================
elif app_mode == "Lesson 1 Homework":
    st.title("📚 Lesson 1: Homework Assignments (STEM Rigor)")
    st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
    st.markdown("---")
    
    homeworks = [
        {
            "q": "1. If sin(θ) - cos(θ) = 4/5, what is the exact value of sin³(θ) - cos³(θ)?",
            "opt": ["A) 44/125", "B) 19/125", "C) 61/125", "D) 91/125"],
            "hint": "💡 Hint: Square the first equation to find sin(θ)cos(θ), then apply the cubic difference formula.",
            "ans": "D) 91/125"
        },
        {
            "q": "2. Let tan(θ) + cot(θ) = 4. What is the exact value of tan³(θ) + cot³(θ)?",
            "opt": ["A) 52", "B) 64", "C) 76", "D) 48"],
            "hint": "💡 Hint: Use the algebraic expansion identity for cubic sums.",
            "ans": "A) 52"
        },
        {
            "q": "3. If sec(θ) + tan(θ) = m (m > 0), which expression correctly defines sin(θ) in terms of m?",
            "opt": ["A) (m² - 1)/(m² + 1)", "B) 2m/(m² + 1)", "C) (m² + 1)/(m² - 1)", "D) (m² - 1)/2m"],
            "hint": "💡 Hint: Use sec(θ) - tan(θ) = 1/m to solve for sec(θ) and tan(θ).",
            "ans": "A) (m² - 1)/(m² + 1)"
        },
        {
            "q": "4. In a physics wave model, A(θ) = 5sin(θ) - 12cos(θ) + 10. What is the absolute maximum value?",
            "opt": ["A) 15", "B) 23", "C) 17", "D) 27"],
            "hint": "💡 Hint: Max value of a*sin(θ) + b*cos(θ) is √(a² + b²), then add the vertical shift 10.",
            "ans": "B) 23"
        },
        {
            "q": "5. If (sin³(θ) + cos³(θ)) / (sin(θ) + cos(θ)) = 3/4, what is the exact value of sin(2θ)?",
            "opt": ["A) -1/2", "B) 1/2", "C) -1/4", "D) 3/4"],
            "hint": "💡 Hint: Simplify numerator by factoring, use sin²θ + cos²θ = 1.",
            "ans": "A) -1/2"
        }
    ]

    for i, hw in enumerate(homeworks, 1):
        with st.expander(f"📌 Homework Question {i}", expanded=False):
            st.markdown(f"**{hw['q']}**")
            ans = st.radio("Choose option:", hw["opt"], key=f"hw_{i}")
            if st.checkbox("Show Hint", key=f"hwh_{i}"):
                st.info(hw["hint"])
            if st.button("Check Answer", key=f"hwb_{i}"):
                if ans == hw["ans"]:
                    st.success("🎉 Correct! Brilliant work.")
                else:
                    st.error("❌ Incorrect. Check your algebraic identities.")

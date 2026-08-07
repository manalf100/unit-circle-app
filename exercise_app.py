import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

# Custom CSS for high readability and professional layout
st.markdown("""
    <style>
    .portal-title { font-size: 30px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .author-name { font-size: 22px !important; font-weight: bold; color: #2563EB; text-align: center; margin-bottom: 20px; }
    .sub-header { font-size: 20px !important; font-weight: bold; color: #0F172A; }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<div class="portal-title">🏛️ STEM Mathematics Interactive Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="author-name">Designed & Prepared by: Mr. Tarek Shawky</div>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SIDEBAR NAVIGATION (PORTAL STRUCTURE)
# ==========================================
st.sidebar.title("📚 Curriculum Navigation")

# 1. Select Unit
selected_unit = st.sidebar.selectbox(
    "Select Unit:",
    [
        "Unit 1: Trigonometric Functions",
        "Unit 2: Limits & Calculus",
        "Unit 3: Vectors & Mechanics"
    ]
)

# ==========================================
# UNIT 1: TRIGONOMETRIC FUNCTIONS
# ==========================================
if selected_unit == "Unit 1: Trigonometric Functions":
    selected_lesson = st.sidebar.selectbox(
        "Select Lesson:",
        [
            "Lesson 1: Unit Circle & Basic Ratios",
            "Lesson 2: Graphs of Trig Functions",
            "Lesson 3: Trigonometric Equations"
        ]
    )
    
    # --------------------------------------
    # LESSON 1: UNIT CIRCLE & BASIC RATIOS
    # --------------------------------------
    if selected_lesson == "Lesson 1: Unit Circle & Basic Ratios":
        page = st.sidebar.radio(
            "Lesson Section:",
            ["📘 1. Interactive Explorer", "🧬 2. Identities Explorer", "🎯 3. Class Exercises", "📝 4. Homework Assignment"]
        )

        # Section 1: Interactive Lesson
        if page == "📘 1. Interactive Explorer":
            st.markdown('<div class="sub-header">Lesson 1: Interactive Angle Explorer</div>', unsafe_allow_html=True)
            
            angle_deg = st.slider("Select Angle θ (Degrees):", 0.0, 360.0, 45.0, 1.0)
            angle_rad = np.radians(angle_deg)
            
            x = np.cos(angle_rad)
            y = np.sin(angle_rad)

            fig, ax = plt.subplots(figsize=(5.5, 5.5))
            circle = plt.Circle((0, 0), 1, color='#94A3B8', fill=False, linestyle='--', linewidth=1.5)
            ax.add_patch(circle)
            
            ax.axhline(0, color='black', linewidth=1)
            ax.axvline(0, color='black', linewidth=1)
            
            ax.plot([0, x], [0, y], color='#DC2626', linewidth=2.5, label='Radius (r=1)')
            ax.plot([x, x], [0, y], color='#16A34A', linewidth=2, linestyle='-', label=f'sin(θ) = {y:.3f}')
            ax.plot([0, x], [0, 0], color='#2563EB', linewidth=2, linestyle='-', label=f'cos(θ) = {x:.3f}')
            ax.plot(x, y, 'ro', markersize=8)

            ax.set_xlim(-1.25, 1.25)
            ax.set_ylim(-1.25, 1.25)
            ax.set_aspect('equal')
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(loc='upper right', fontsize=9)
            st.pyplot(fig)

            col1, col2, col3 = st.columns(3)
            col1.metric("sin(θ)", f"{y:.3f}")
            col2.metric("cos(θ)", f"{x:.3f}")
            tan_val = f"{y/x:.3f}" if abs(x) > 1e-5 else "Undefined"
            col3.metric("tan(θ)", tan_val)

            st.write("---")
            st.markdown("**Complete Trigonometric Ratios Table:**")
            
            sec_val = f"{1/x:.3f}" if abs(x) > 1e-5 else "Undefined"
            csc_val = f"{1/y:.3f}" if abs(y) > 1e-5 else "Undefined"
            cot_val = f"{x/y:.3f}" if abs(y) > 1e-5 else "Undefined"

            val_df = pd.DataFrame({
                "Trig Function": ["sin(θ)", "cos(θ)", "tan(θ)", "csc(θ)", "sec(θ)", "cot(θ)"],
                "Calculated Value": [f"{y:.3f}", f"{x:.3f}", tan_val, csc_val, sec_val, cot_val],
                "Unit Circle Ratio": ["y", "x", "y / x", "1 / y", "1 / x", "x / y"]
            })
            st.table(val_df)

        # Section 2: Identities Explorer
        elif page == "🧬 2. Identities Explorer":
            st.markdown('<div class="sub-header">🧬 Fundamental Trigonometric Identities</div>', unsafe_allow_html=True)
            st.write("Explore how trig identities derive directly from the Unit Circle geometry:")

            st.markdown("### 1. Pythagorean Identities")
            st.latex(r'''\cos^2(\theta) + \sin^2(\theta) = 1''')
            st.caption("Derived from Pythagorean theorem on unit circle: x² + y² = 1")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.latex(r'''1 + \tan^2(\theta) = \sec^2(\theta)''')
            with col_b:
                st.latex(r'''1 + \cot^2(\theta) = \csc^2(\theta)''')

            st.markdown("---")
            st.markdown("### 2. Quotient & Reciprocal Identities")
            
            id_df = pd.DataFrame({
                "Identity Type": ["Quotient", "Quotient", "Reciprocal", "Reciprocal", "Reciprocal"],
                "Trig Function": ["tan(θ)", "cot(θ)", "csc(θ)", "sec(θ)", "cot(θ)"],
                "Equivalent Form": ["sin(θ) / cos(θ)", "cos(θ) / sin(θ)", "1 / sin(θ)", "1 / cos(θ)", "1 / tan(θ)"]
            })
            st.table(id_df)

        # Section 3: Class Exercises
        elif page == "🎯 3. Class Exercises":
            st.markdown('<div class="sub-header">🎯 Class Exercises</div>', unsafe_allow_html=True)
            st.write("Solve the following problem set:")

            exercises = [
                {
                    "id": 1,
                    "q": "1. Simplify completely: [ (sin³(θ) + cos³(θ)) / (sin(θ) + cos(θ)) ] + sin(θ)cos(θ)",
                    "opts": ["a) 0", "b) 1", "c) 2 sin(θ)cos(θ)", "d) sin²(θ) - cos²(θ)"],
                    "ans": "b) 1",
                    "hint": "Factor numerator using sum of cubes: a³ + b³ = (a + b)(a² - ab + b²).",
                    "sol": "Numerator = (sin(θ) + cos(θ))(sin²(θ) - sin(θ)cos(θ) + cos²(θ)).\nDividing yields: (1 - sin(θ)cos(θ)) + sin(θ)cos(θ) = 1."
                },
                {
                    "id": 2,
                    "q": "2. If sin(θ) + cos(θ) = 1/5 and 0 ≤ θ ≤ π, what is the value of tan(θ)?",
                    "opts": ["a) -3/4", "b) -4/3", "c) 3/4", "d) 4/3"],
                    "ans": "b) -4/3",
                    "hint": "Square both sides: (sin(θ) + cos(θ))² = 1/25.",
                    "sol": "1 + 2sin(θ)cos(θ) = 1/25 => 2sin(θ)cos(θ) = -24/25 => sin(θ)cos(θ) = -12/25.\nSolving sin(θ) and cos(θ) gives sin(θ) = 4/5 and cos(θ) = -3/5.\nThus, tan(θ) = (4/5) / (-3/5) = -4/3."
                },
                {
                    "id": 3,
                    "q": "3. Express [ cot(θ) / (csc(θ) - 1) ] + [ cot(θ) / (csc(θ) + 1) ] in simplified form.",
                    "opts": ["a) 2 sin(θ)", "b) 2 cos(θ)", "c) 2 sec(θ)", "d) 2 csc(θ)"],
                    "ans": "c) 2 sec(θ)",
                    "hint": "Combine fractions over common denominator (csc²(θ) - 1 = cot²(θ)).",
                    "sol": "Numerator = cot(θ)(csc(θ) + 1 + csc(θ) - 1) = 2 cot(θ) csc(θ).\nDenominator = cot²(θ).\nResult = (2 csc(θ)) / cot(θ) = 2 / cos(θ) = 2 sec(θ)."
                }
            ]

            for item in exercises:
                st.markdown(f"#### {item['q']}")
                user_choice = st.radio(f"Select option for Q{item['id']}:", item["opts"], key=f"ex_{item['id']}")
                if st.button(f"Check Q{item['id']}", key=f"btn_ex_{item['id']}"):
                    if user_choice == item["ans"]:
                        st.success("Correct! 🎉")
                    else:
                        st.error("Incorrect. Try again! ❌")
                with st.expander(f"💡 Hint & Solution for Q{item['id']}"):
                    st.info(f"**Hint:** {item['hint']}")
                    st.success(f"**Solution:**\n{item['sol']}")
                st.write("---")

        # Section 4: Homework Assignment
        else:
            st.markdown('<div class="sub-header">📝 Homework Assignment</div>', unsafe_allow_html=True)
            hw_questions = [
                {
                    "id": 1,
                    "q": "1. If sin(θ) + sin²(θ) = 1, what is the exact value of cos²(θ) + cos⁴(θ)?",
                    "opts": ["a) 0", "b) 1", "c) 2", "d) 1/2"],
                    "ans": "b) 1",
                    "hint": "From given equation, sin(θ) = 1 - sin²(θ) = cos²(θ).",
                    "sol": "Since cos²(θ) = sin(θ), then cos⁴(θ) = sin²(θ).\nTherefore, cos²(θ) + cos⁴(θ) = sin(θ) + sin²(θ) = 1."
                },
                {
                    "id": 2,
                    "q": "2. Simplify completely: [ sin(θ) / (1 - cot(θ)) ] + [ cos(θ) / (1 - tan(θ)) ]",
                    "opts": ["a) sin(θ) + cos(θ)", "b) sin(θ) - cos(θ)", "c) 1", "d) 0"],
                    "ans": "a) sin(θ) + cos(θ)",
                    "hint": "Express cot(θ) as cos/sin and tan(θ) as sin/cos.",
                    "sol": "Terms become: [ sin²(θ) / (sin(θ) - cos(θ)) ] + [ cos²(θ) / (cos(θ) - sin(θ)) ]\n= (sin(θ) - cos(θ))(sin(θ) + cos(θ)) / (sin(θ) - cos(θ)) = sin(θ) + cos(θ)."
                }
            ]

            for hw in hw_questions:
                st.markdown(f"#### {hw['q']}")
                hw_ans = st.radio(f"Select option for HW Q{hw['id']}:", hw["opts"], key=f"hw_{hw['id']}")
                if st.button(f"Check HW Q{hw['id']}", key=f"btn_hw_{hw['id']}"):
                    if hw_ans == hw["ans"]:
                        st.success("Correct! 🎉")
                    else:
                        st.error("Incorrect. Try again! ❌")
                with st.expander(f"💡 Hint & Solution for HW Q{hw['id']}"):
                    st.info(f"**Hint:** {hw['hint']}")
                    st.success(f"**Solution:**\n{hw['sol']}")
                st.write("---")

    # --------------------------------------
    # LESSON 2: GRAPHS OF TRIG FUNCTIONS (PREVIEW)
    # --------------------------------------
    elif selected_lesson == "Lesson 2: Graphs of Trig Functions":
        st.markdown('<div class="sub-header">Lesson 2: Wave Function Generator</div>', unsafe_allow_html=True)
        st.write("Explore f(x) = A · sin(B · x + C) + D")

        amp = st.slider("Amplitude (A):", 0.5, 3.0, 1.0, 0.5)
        freq = st.slider("Frequency (B):", 0.5, 4.0, 1.0, 0.5)

        x_vals = np.linspace(0, 4 * np.pi, 500)
        y_vals = amp * np.sin(freq * x_vals)

        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.plot(x_vals, y_vals, color='#2563EB', linewidth=2, label=f'f(x) = {amp} sin({freq}x)')
        ax.axhline(0, color='black', linewidth=0.8)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend()
        st.pyplot(fig)

    # --------------------------------------
    # LESSON 3: TRIG EQUATIONS (PREVIEW)
    # --------------------------------------
    else:
        st.markdown('<div class="sub-header">Lesson 3: Trigonometric Equations</div>', unsafe_allow_html=True)
        st.info("📌 Lesson 3 content is coming soon! Check back after the next update.")

# ==========================================
# OTHER UNITS (PLACEHOLDERS)
# ==========================================
elif selected_unit == "Unit 2: Limits & Calculus":
    st.markdown('<div class="sub-header">Unit 2: Limits & Calculus</div>', unsafe_allow_html=True)
    st.info("📌 Limits and Derivatives interactive modules will be added here.")

else:
    st.markdown('<div class="sub-header">Unit 3: Vectors & Mechanics</div>', unsafe_allow_html=True)
    st.info("📌 Vector Algebra and Statics modules will be added here.")

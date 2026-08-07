import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(page_title="STEM Unit Circle Master", layout="centered")

# Custom CSS for high readability and professional layout
st.markdown("""
    <style>
    .main-title { font-size: 32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .author-name { font-size: 24px !important; font-weight: bold; color: #2563EB; text-align: center; margin-bottom: 25px; }
    .sub-header { font-size: 22px !important; font-weight: bold; color: #0F172A; }
    </style>
""", unsafe_allow_html=True)

# Session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Lesson"

# Sidebar Navigation
st.sidebar.title("📌 Lesson Navigation")
page_selection = st.sidebar.radio(
    "Select Section:",
    ["📘 1. Interactive Explorer", "🧬 2. Identities Explorer", "🎯 3. Class Exercises", "📝 4. Homework Assignment"]
)

if "1." in page_selection: st.session_state.page = "Lesson"
elif "2." in page_selection: st.session_state.page = "Identities"
elif "3." in page_selection: st.session_state.page = "Exercises"
else: st.session_state.page = "Homework"

# Header
st.markdown('<div class="main-title">⭕ STEM Unit Circle & Trig Functions</div>', unsafe_allow_html=True)
st.markdown('<div class="author-name">Designed & Prepared by: Mr. Tarek Shawky</div>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SECTION 1: INTERACTIVE LESSON
# ==========================================
if st.session_state.page == "Lesson":
    st.markdown('<div class="sub-header">1. Interactive Angle Explorer</div>', unsafe_allow_html=True)
    
    angle_deg = st.slider("Select Angle θ (Degrees):", 0.0, 360.0, 45.0, 1.0)
    angle_rad = np.radians(angle_deg)
    
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    # Interactive Plotting
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    circle = plt.Circle((0, 0), 1, color='#94A3B8', fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    
    # Radius, Sine, and Cosine representations
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

    # Values Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("sin(θ)", f"{y:.3f}")
    col2.metric("cos(θ)", f"{x:.3f}")
    tan_val = f"{y/x:.3f}" if abs(x) > 1e-5 else "Undefined"
    col3.metric("tan(θ)", tan_val)

    st.write("---")
    st.markdown("**Complete Trigonometric Values Table:**")
    
    sec_val = f"{1/x:.3f}" if abs(x) > 1e-5 else "Undefined"
    csc_val = f"{1/y:.3f}" if abs(y) > 1e-5 else "Undefined"
    cot_val = f"{x/y:.3f}" if abs(y) > 1e-5 else "Undefined"

    val_df = pd.DataFrame({
        "Trig Function": ["sin(θ)", "cos(θ)", "tan(θ)", "csc(θ)", "sec(θ)", "cot(θ)"],
        "Calculated Value": [f"{y:.3f}", f"{x:.3f}", tan_val, csc_val, sec_val, cot_val],
        "Unit Circle Ratio": ["y", "x", "y / x", "1 / y", "1 / x", "x / y"]
    })
    st.table(val_df)

# ==========================================
# SECTION 2: IDENTITIES EXPLORER
# ==========================================
elif st.session_state.page == "Identities":
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

    st.markdown("---")
    st.markdown("### 3. Co-Function & Negative Angle Identities")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Co-Function Identities:**")
        st.latex(r'''\sin(90^\circ - \theta) = \cos(\theta)''')
        st.latex(r'''\cos(90^\circ - \theta) = \sin(\theta)''')
    with c2:
        st.markdown("**Negative Angle Identities:**")
        st.latex(r'''\sin(-\theta) = -\sin(\theta)''')
        st.latex(r'''\cos(-\theta) = \cos(\theta)''')

# ==========================================
# SECTION 3: CLASS EXERCISES (STEM RIGOR)
# ==========================================
elif st.session_state.page == "Exercises":
    st.markdown('<div class="sub-header">🎯 Class Exercises</div>', unsafe_allow_html=True)
    st.write("Solve the following problem set:")

    exercises = [
        {
            "id": 1,
            "q": "1. Simplify completely: [ (sin³(θ) + cos³(θ)) / (sin(θ) + cos(θ)) ] + sin(θ)cos(θ)",
            "opts": ["a) 0", "b) 1", "c) 2 sin(θ)cos(θ)", "d) sin²(θ) - cos²(θ)"],
            "ans": "b) 1",
            "hint": "Factor the numerator using sum of cubes: a³ + b³ = (a + b)(a² - ab + b²).",
            "sol": "Numerator = (sin(θ) + cos(θ))(sin²(θ) - sin(θ)cos(θ) + cos²(θ)).\nDividing yields: (1 - sin(θ)cos(θ)) + sin(θ)cos(θ) = 1."
        },
        {
            "id": 2,
            "q": "2. If sin(θ) + cos(θ) = 1/5 and 0 ≤ θ ≤ π, what is the value of tan(θ)?",
            "opts": ["a) -3/4", "b) -4/3", "c) 3/4", "d) 4/3"],
            "ans": "b) -4/3",
            "hint": "Square both sides of the equation: (sin(θ) + cos(θ))² = 1/25.",
            "sol": "1 + 2sin(θ)cos(θ) = 1/25 => 2sin(θ)cos(θ) = -24/25 => sin(θ)cos(θ) = -12/25.\nSolving sin(θ) and cos(θ) gives sin(θ) = 4/5 and cos(θ) = -3/5.\nThus, tan(θ) = (4/5) / (-3/5) = -4/3."
        },
        {
            "id": 3,
            "q": "3. Express [ cot(θ) / (csc(θ) - 1) ] + [ cot(θ) / (csc(θ) + 1) ] in simplified form.",
            "opts": ["a) 2 sin(θ)", "b) 2 cos(θ)", "c) 2 sec(θ)", "d) 2 csc(θ)"],
            "ans": "c) 2 sec(θ)",
            "hint": "Combine fractions over the common denominator (csc²(θ) - 1 = cot²(θ)).",
            "sol": "Numerator = cot(θ)(csc(θ) + 1 + csc(θ) - 1) = 2 cot(θ) csc(θ).\nDenominator = cot²(θ).\nResult = (2 csc(θ)) / cot(θ) = 2 (1/sin(θ)) / (cos(θ)/sin(θ)) = 2 / cos(θ) = 2 sec(θ)."
        },
        {
            "id": 4,
            "q": "4. If sec(θ) - tan(θ) = p, what is csc(θ) expressed in terms of p?",
            "opts": ["a) (1 + p²) / (1 - p²)", "b) (1 - p²) / (1 + p²)", "c) 2p / (1 + p²)", "d) (1 + p²) / 2p"],
            "ans": "a) (1 + p²) / (1 - p²)",
            "hint": "Note that sec²(θ) - tan²(θ) = 1, so sec(θ) + tan(θ) = 1/p.",
            "sol": "sec(θ) + tan(θ) = 1/p and sec(θ) - tan(θ) = p.\nAdding gives 2sec(θ) = p + 1/p => sec(θ) = (p² + 1) / (2p) => cos(θ) = 2p / (p² + 1).\nSubtracting gives 2tan(θ) = 1/p - p => tan(θ) = (1 - p²) / (2p) => sin(θ) = (1 - p²) / (p² + 1).\nTherefore, csc(θ) = 1 / sin(θ) = (1 + p²) / (1 - p²)."
        },
        {
            "id": 5,
            "q": "5. Simplify for θ ∈ (0, π/2): √[ (1 + sin(θ)) / (1 - sin(θ)) ]",
            "opts": ["a) sec(θ) + tan(θ)", "b) sec(θ) - tan(θ)", "c) csc(θ) + cot(θ)", "d) 1 + sin(θ)"],
            "ans": "a) sec(θ) + tan(θ)",
            "hint": "Multiply numerator and denominator inside the square root by (1 + sin(θ)).",
            "sol": "√[ (1 + sin(θ))² / (1 - sin²(θ)) ] = √[ (1 + sin(θ))² / cos²(θ) ] = (1 + sin(θ)) / cos(θ) = sec(θ) + tan(θ)."
        },
        {
            "id": 6,
            "q": "6. On the unit circle, if point P(θ) is in Quadrant III with x = -√5/3, evaluate csc(θ) · tan(θ).",
            "opts": ["a) -3/√5", "b) 3/√5", "c) -2/√5", "d) 2/3"],
            "ans": "a) -3/√5", "hint": "csc(θ) · tan(θ) = (1/y) · (y/x) = 1/x = sec(θ).",
            "sol": "csc(θ) · tan(θ) = (1 / sin(θ)) · (sin(θ) / cos(θ)) = 1 / cos(θ) = 1 / x.\nSince x = -√5/3, the value is -3/√5."
        }
    ]

    for item in exercises:
        st.markdown(f"#### {item['q']}")
        user_choice = st.radio(f"Select option for Q{item['id']}:", item["opts"], key=f"ex_{item['id']}")
        
        c1, c2 = st.columns([1, 4])
        with c1:
            if st.button(f"Check Q{item['id']}", key=f"btn_ex_{item['id']}"):
                if user_choice == item["ans"]:
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect. Try again! ❌")
        
        with st.expander(f"💡 Hint & Solution for Q{item['id']}"):
            st.info(f"**Hint:** {item['hint']}")
            st.success(f"**Solution:**\n{item['sol']}")
        st.write("---")

# ==========================================
# SECTION 4: HOMEWORK ASSIGNMENT
# ==========================================
else:
    st.markdown('<div class="sub-header">📝 Homework Assignment</div>', unsafe_allow_html=True)
    st.write("Complete the following problems:")

    hw_questions = [
        {
            "id": 1,
            "q": "1. If sin(θ) + sin²(θ) = 1, what is the exact value of cos²(θ) + cos⁴(θ)?",
            "opts": ["a) 0", "b) 1", "c) 2", "d) 1/2"],
            "ans": "b) 1",
            "hint": "From the given equation, sin(θ) = 1 - sin²(θ) = cos²(θ).",
            "sol": "Since cos²(θ) = sin(θ), then cos⁴(θ) = sin²(θ).\nTherefore, cos²(θ) + cos⁴(θ) = sin(θ) + sin²(θ) = 1."
        },
        {
            "id": 2,
            "q": "2. Simplify completely: [ sin(θ) / (1 - cot(θ)) ] + [ cos(θ) / (1 - tan(θ)) ]",
            "opts": ["a) sin(θ) + cos(θ)", "b) sin(θ) - cos(θ)", "c) 1", "d) 0"],
            "ans": "a) sin(θ) + cos(θ)",
            "hint": "Express cot(θ) as cos/sin and tan(θ) as sin/cos.",
            "sol": "Terms become: [ sin²(θ) / (sin(θ) - cos(θ)) ] + [ cos²(θ) / (cos(θ) - sin(θ)) ]\n= [ sin²(θ) - cos²(θ) ] / (sin(θ) - cos(θ))\n= (sin(θ) - cos(θ))(sin(θ) + cos(θ)) / (sin(θ) - cos(θ)) = sin(θ) + cos(θ)."
        },
        {
            "id": 3,
            "q": "3. If x = a cos³(θ) and y = a sin³(θ), evaluate (x/a)^(2/3) + (y/a)^(2/3).",
            "opts": ["a) a", "b) 1", "c) a²", "d) sin(θ)cos(θ)"],
            "ans": "b) 1",
            "hint": "Substitute x/a = cos³(θ) and y/a = sin³(θ).",
            "sol": "(cos³(θ))^(2/3) + (sin³(θ))^(2/3) = cos²(θ) + sin²(θ) = 1."
        },
        {
            "id": 4,
            "q": "4. Simplify: [ tan(θ) + sec(θ) - 1 ] / [ tan(θ) - sec(θ) + 1 ]",
            "opts": ["a) sec(θ) + tan(θ)", "b) sec(θ) - tan(θ)", "c) tan(θ)", "d) cot(θ)"],
            "ans": "a) sec(θ) + tan(θ)",
            "hint": "Replace 1 in numerator with (sec²(θ) - tan²(θ)) = (sec(θ) - tan(θ))(sec(θ) + tan(θ)).",
            "sol": "Numerator = (tan(θ) + sec(θ)) - (sec²(θ) - tan²(θ))\n= (sec(θ) + tan(θ)) [ 1 - sec(θ) + tan(θ) ].\nDenominator = [ tan(θ) - sec(θ) + 1 ].\nCanceling terms leaves sec(θ) + tan(θ)."
        },
        {
            "id": 5,
            "q": "5. Find all solutions for 2 sin²(θ) + 3 cos(θ) = 0 on the interval [0, 2π).",
            "opts": ["a) 2π/3 and 4π/3", "b) π/3 and 5π/3", "c) π/6 and 5π/6", "d) 7π/6 and 11π/6"],
            "ans": "a) 2π/3 and 4π/3",
            "hint": "Substitute sin²(θ) = 1 - cos²(θ) to get a quadratic in cos(θ).",
            "sol": "2(1 - cos²(θ)) + 3cos(θ) = 0 => 2cos²(θ) - 3cos(θ) - 2 = 0.\n(2cos(θ) + 1)(cos(θ) - 2) = 0.\ncos(θ) = -1/2 (since cos(θ) = 2 is impossible).\nOn [0, 2π), cos(θ) = -1/2 at θ = 2π/3 and 4π/3."
        }
    ]

    for hw in hw_questions:
        st.markdown(f"#### {hw['q']}")
        hw_ans = st.radio(f"Select option for HW Q{hw['id']}:", hw["opts"], key=f"hw_{hw['id']}")
        
        c1, c2 = st.columns([1, 4])
        with c1:
            if st.button(f"Check HW Q{hw['id']}", key=f"btn_hw_{hw['id']}"):
                if hw_ans == hw["ans"]:
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect. Try again! ❌")

        with st.expander(f"💡 Hint & Solution for HW Q{hw['id']}"):
            st.info(f"**Hint:** {hw['hint']}")
            st.success(f"**Solution:**\n{hw['sol']}")
        st.write("---")

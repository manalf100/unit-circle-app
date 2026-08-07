import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(page_title="STEM Unit Circle Master", layout="centered")

# Custom CSS for prominent styling and readability
st.markdown("""
    <style>
    .main-title { font-size: 32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .author-name { font-size: 22px !important; font-weight: bold; color: #2563EB; text-align: center; margin-bottom: 25px; }
    .sub-header { font-size: 20px !important; font-weight: bold; color: #0F172A; }
    </style>
""", unsafe_allow_html=True)

# Session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Lesson"

# Sidebar Navigation (100% English)
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
    
    # Visual components
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

    # Live Trig Metrics
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
# SECTION 3: CLASS EXERCISES (10 Qs)
# ==========================================
elif st.session_state.page == "Exercises":
    st.markdown('<div class="sub-header">🎯 Class Exercises (10 Interactive Questions)</div>', unsafe_allow_html=True)
    st.write("Solve the questions below and verify your answers.")

    exercises = [
        {"id": 1, "q": "1. What is the exact value of cos(120°)?", "opts": ["a) 1/2", "b) -1/2", "c) √3/2", "d) -√3/2"], "ans": "b) -1/2", "hint": "120° lies in Q2 where cosine is negative. Reference angle = 60°.", "sol": "cos(120°) = -cos(60°) = -1/2."},
        {"id": 2, "q": "2. If sin(θ) = 0.8 in Quadrant I, what is cos(θ)?", "opts": ["a) 0.2", "b) 0.6", "c) -0.6", "d) 0.8"], "ans": "b) 0.6", "hint": "Use sin²(θ) + cos²(θ) = 1.", "sol": "cos(θ) = √(1 - 0.8²) = √(1 - 0.64) = 0.6."},
        {"id": 3, "q": "3. Which identity is equal to 1 / sin(θ)?", "opts": ["a) cos(θ)", "b) sec(θ)", "c) csc(θ)", "d) cot(θ)"], "ans": "c) csc(θ)", "hint": "Reciprocal ratio of sine.", "sol": "csc(θ) = 1 / sin(θ)."},
        {"id": 4, "q": "4. Convert 270° into radians.", "opts": ["a) π/2", "b) π", "c) 3π/2", "d) 2π"], "ans": "c) 3π/2", "hint": "Multiply 270° by π / 180°.", "sol": "270 * (π / 180) = 3π/2."},
        {"id": 5, "q": "5. On a unit circle, which coordinate corresponds to cos(θ)?", "opts": ["a) x-coordinate", "b) y-coordinate", "c) Slope", "d) Radius"], "ans": "a) x-coordinate", "hint": "Point P(x, y) = (cos θ, sin θ).", "sol": "x = cos(θ) on a circle with radius 1."},
        {"id": 6, "q": "6. Find the value of tan(225°).", "opts": ["a) 1", "b) -1", "c) √3", "d) -√3"], "ans": "a) 1", "hint": "225° is in Q3. Reference angle = 45°.", "sol": "tan(225°) = tan(45°) = 1 (Positive in Q3)."},
        {"id": 7, "q": "7. If tan(θ) = 3/4 and θ is in Quadrant III, find sin(θ).", "opts": ["a) 3/5", "b) -3/5", "c) 4/5", "d) -4/5"], "ans": "b) -3/5", "hint": "Opposite = 3, Adjacent = 4, Hypotenuse = 5. Sine is negative in Q3.", "sol": "sin(θ) = -Opposite/Hypotenuse = -3/5."},
        {"id": 8, "q": "8. Simplify: sin²(θ) · csc²(θ).", "opts": ["a) 0", "b) 1", "c) sin(θ)", "d) cos²(θ)"], "ans": "b) 1", "hint": "csc(θ) = 1 / sin(θ).", "sol": "sin²(θ) * (1 / sin²(θ)) = 1."},
        {"id": 9, "q": "9. What is the domain restriction for tan(θ)?", "opts": ["a) All Real Numbers", "b) θ ≠ nπ", "c) θ ≠ (2n+1)π/2", "d) [-1, 1]"], "ans": "c) θ ≠ (2n+1)π/2", "hint": "tan(θ) = sin/cos. Cosine is zero at odd multiples of π/2.", "sol": "Undefined when cos(θ) = 0."},
        {"id": 10, "q": "10. What is the exact value of sec(60°)?", "opts": ["a) 1/2", "b) 2", "c) √2", "d) 2/√3"], "ans": "b) 2", "hint": "sec(θ) = 1 / cos(θ).", "sol": "sec(60°) = 1 / (1/2) = 2."}
    ]

    for item in exercises:
        st.markdown(f"#### {item['q']}")
        user_choice = st.radio(f"Select your answer for Q{item['id']}:", item["opts"], key=f"ex_{item['id']}")
        
        c1, c2 = st.columns([1, 4])
        with c1:
            if st.button(f"Check Q{item['id']}", key=f"btn_ex_{item['id']}"):
                if user_choice == item["ans"]:
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect. Try again! ❌")
        
        with st.expander(f"💡 Hint & Solution for Q{item['id']}"):
            st.info(f"**Hint:** {item['hint']}")
            st.success(f"**Solution:** {item['sol']}")
        st.write("---")

# ==========================================
# SECTION 4: HOMEWORK (5 Qs)
# ==========================================
else:
    st.markdown('<div class="sub-header">📝 Homework Assignment (5 Graded Questions)</div>', unsafe_allow_html=True)
    st.write("Complete the following assignment questions.")

    hw_questions = [
        {
            "level": "🟢 Easy Level",
            "id": 1,
            "q": "1. What is the value of sin(90°)?",
            "opts": ["a) 0", "b) 1", "c) -1", "d) Undefined"],
            "ans": "b) 1",
            "hint": "90° represents the top point (0, 1) on the unit circle.",
            "sol": "At 90°, the y-coordinate is 1, so sin(90°) = 1."
        },
        {
            "level": "🟢 Easy Level",
            "id": 2,
            "q": "2. In which quadrant are both sin(θ) > 0 and cos(θ) < 0?",
            "opts": ["a) Quadrant I", "b) Quadrant II", "c) Quadrant III", "d) Quadrant IV"],
            "ans": "b) Quadrant II",
            "hint": "Use ASTC rule: x < 0 and y > 0.",
            "sol": "In Quadrant II, x-coordinates (cosine) are negative and y-coordinates (sine) are positive."
        },
        {
            "level": "🟡 Medium Level",
            "id": 3,
            "q": "3. Evaluate the exact value of sec(300°).",
            "opts": ["a) 2", "b) -2", "c) 2/√3", "d) -2/√3"],
            "ans": "a) 2",
            "hint": "300° is in Q4. Reference angle = 60°. sec(θ) = 1/cos(θ).",
            "sol": "cos(300°) = cos(60°) = 1/2. Therefore, sec(300°) = 1 / (1/2) = 2."
        },
        {
            "level": "🟡 Medium Level",
            "id": 4,
            "q": "4. If cos(θ) = -5/13 and θ is in Quadrant II, find cot(θ).",
            "opts": ["a) -5/12", "b) -12/5", "c) 5/12", "d) 12/5"],
            "ans": "a) -5/12",
            "hint": "x = -5, r = 13. Find y using x² + y² = r².",
            "sol": "y = √(13² - (-5)²) = 12. cot(θ) = x/y = -5/12."
        },
        {
            "level": "🔴 Hard / STEM Level",
            "id": 5,
            "q": "5. Simplify completely: [sin(θ) / (1 + cos(θ))] + [(1 + cos(θ)) / sin(θ)].",
            "opts": ["a) 2 sin(θ)", "b) 2 csc(θ)", "c) 2 cos(θ)", "d) 2 sec(θ)"],
            "ans": "b) 2 csc(θ)",
            "hint": "Combine fractions over common denominator sin(θ)(1 + cos(θ)). Use sin²(θ) + cos²(θ) = 1.",
            "sol": "Numerator = sin²(θ) + (1 + cos(θ))² = 1 + 2cos(θ) + cos²(θ) + sin²(θ) = 2 + 2cos(θ) = 2(1 + cos(θ)).\nDenominator = sin(θ)(1 + cos(θ)).\nCanceling terms gives 2 / sin(θ) = 2 csc(θ)."
        }
    ]

    for hw in hw_questions:
        st.markdown(f"#### {hw['level']}")
        st.write(hw["q"])
        hw_ans = st.radio(f"Select answer for HW Q{hw['id']}:", hw["opts"], key=f"hw_{hw['id']}")
        
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

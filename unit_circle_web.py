import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="STEM Unit Circle Master", layout="centered")

# Session state management for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Lesson"

# Sidebar Navigation
st.sidebar.title("📌 التنقل في الدرس")
page_selection = st.sidebar.radio(
    "الانتقال السريع:",
    ["📘 1. الشرح والتفاعل (Lesson)", "🎯 2. تمارين الفصل (Exercises)", "📝 3. الواجب المنزلي (Homework)"],
    index=0 if st.session_state.page == "Lesson" else (1 if st.session_state.page == "Exercises" else 2)
)

# Sync sidebar with session state
if "1." in page_selection:
    st.session_state.page = "Lesson"
elif "2." in page_selection:
    st.session_state.page = "Exercises"
else:
    st.session_state.page = "Homework"

# ==========================================
# SECTION 1: INTERACTIVE LESSON
# ==========================================
if st.session_state.page == "Lesson":
    st.title("⭕ STEM Unit Circle & Trig Functions")
    st.caption("Designed & Prepared by: Mr. Tarek Shawky")
    st.write("---")

    st.subheader("1. Interactive Angle Explorer")
    angle_deg = st.slider("اختر الزاوية بالدرجات (θ):", 0.0, 360.0, 45.0, 1.0)
    angle_rad = np.radians(angle_deg)
    
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    fig, ax = plt.subplots(figsize=(5, 5))
    circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    
    # Radius, Cosine, and Sine lines
    ax.plot([0, x], [0, y], color='red', linewidth=2.5, label='Radius (r=1)')
    ax.plot([x, x], [0, y], color='green', linewidth=2, label=f'sin(θ) = {y:.3f}')
    ax.plot([0, x], [0, 0], color='blue', linewidth=2, label=f'cos(θ) = {x:.3f}')
    ax.plot(x, y, 'ro')

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=8)
    st.pyplot(fig)

    # Values Grid
    col1, col2, col3 = st.columns(3)
    col1.metric("sin(θ)", f"{y:.3f}")
    col2.metric("cos(θ)", f"{x:.3f}")
    col3.metric("tan(θ)", f"{y/x:.3f}" if abs(x) > 1e-5 else "Undefined")

    st.write("---")
    if st.button("الانتقال إلى تمارين الفصل 🎯 (Go to Exercises)", type="primary", use_container_width=True):
        st.session_state.page = "Exercises"
        st.rerun()

# ==========================================
# SECTION 2: CLASS EXERCISES (10 Questions)
# ==========================================
elif st.session_state.page == "Exercises":
    st.title("🎯 Class Exercises: Unit Circle")
    st.caption("Designed & Prepared by: Mr. Tarek Shawky")
    st.write("---")

    mode = st.radio("اختر وضع العرض:", ["Student Mode (وضع الطالب)", "Teacher Mode (وضع المعلم)"], horizontal=True)

    exercises = [
        {"id": 1, "q": "1. What is cos(120°)?", "opts": ["a) 1/2", "b) -1/2", "c) √3/2", "d) -√3/2"], "ans": "b) -1/2", "hint": "120° is in Q2. Reference angle = 60°.", "sol": "cos(120°) = -cos(60°) = -1/2."},
        {"id": 2, "q": "2. If sin(θ) = 0.8 in Q1, what is cos(θ)?", "opts": ["a) 0.2", "b) 0.6", "c) -0.6", "d) 0.8"], "ans": "b) 0.6", "hint": "sin²(θ) + cos²(θ) = 1.", "sol": "cos(θ) = √(1 - 0.64) = 0.6."},
        {"id": 3, "q": "3. Which identity equals 1/sin(θ)?", "opts": ["a) cos(θ)", "b) sec(θ)", "c) csc(θ)", "d) cot(θ)"], "ans": "c) csc(θ)", "hint": "Reciprocal ratio for sine.", "sol": "csc(θ) = 1/sin(θ)."},
        {"id": 4, "q": "4. Equivalent radian measure for 270°?", "opts": ["a) π/2", "b) π", "c) 3π/2", "d) 2π"], "ans": "c) 3π/2", "hint": "Multiply 270° by π/180°.", "sol": "270 * π / 180 = 3π/2."},
        {"id": 5, "q": "5. Which coordinate on unit circle corresponds to cos(θ)?", "opts": ["a) x-coordinate", "b) y-coordinate", "c) Slope", "d) Radius"], "ans": "a) x-coordinate", "hint": "P(x, y) = (cos θ, sin θ).", "sol": "x = cos(θ) on a unit circle."},
        {"id": 6, "q": "6. Value of tan(225°)?", "opts": ["a) 1", "b) -1", "c) √3", "d) -√3"], "ans": "a) 1", "hint": "Q3 angle, reference is 45°.", "sol": "tan(225°) = tan(45°) = 1."},
        {"id": 7, "q": "7. If tan(θ) = 3/4 in Q3, find sin(θ).", "opts": ["a) 3/5", "b) -3/5", "c) 4/5", "d) -4/5"], "ans": "b) -3/5", "hint": "Sine is negative in Q3.", "sol": "Opp=3, Adj=4, Hyp=5. sin(θ) = -3/5."},
        {"id": 8, "q": "8. Simplify: sin²(θ) · csc²(θ).", "opts": ["a) 0", "b) 1", "c) sin(θ)", "d) cos²(θ)"], "ans": "b) 1", "hint": "csc(θ) = 1/sin(θ).", "sol": "sin²(θ) * (1/sin²(θ)) = 1."},
        {"id": 9, "q": "9. Domain of tan(θ)?", "opts": ["a) All Real", "b) θ ≠ nπ", "c) θ ≠ (2n+1)π/2", "d) [-1, 1]"], "ans": "c) θ ≠ (2n+1)π/2", "hint": "tan(θ) = sin/cos. Cosine is zero at odd multiples of π/2.", "sol": "Undefined when cos(θ) = 0."},
        {"id": 10, "q": "10. Value of sec(60°)?", "opts": ["a) 1/2", "b) 2", "c) √2", "d) 2/√3"], "ans": "b) 2", "hint": "sec(θ) = 1/cos(θ).", "sol": "sec(60°) = 1 / (1/2) = 2."}
    ]

    for item in exercises:
        st.subheader(f"Question {item['id']}")
        st.write(item["q"])
        if mode == "Student Mode (وضع الطالب)":
            choice = st.radio(f"Select Q{item['id']}:", item["opts"], key=f"ex_{item['id']}")
            c1, c2 = st.columns(2)
            with c1:
                if st.button(f"💡 Hint Q{item['id']}", key=f"ex_h_{item['id']}"):
                    st.info(item["hint"])
            with c2:
                if st.button(f"Check Q{item['id']}", key=f"ex_c_{item['id']}"):
                    if choice == item["ans"]:
                        st.success("Correct! 🎉")
                    else:
                        st.error("Try again! ❌")
        else:
            st.success(f"**Answer:** {item['ans']}")
            st.info(f"**Solution:** {item['sol']}")
        st.write("---")

    if st.button("الانتقال إلى الواجب المنزلي 📝 (Go to Homework)", type="primary", use_container_width=True):
        st.session_state.page = "Homework"
        st.rerun()

# ==========================================
# SECTION 3: HOMEWORK (5 Graded Questions)
# ==========================================
else:
    st.title("📝 Homework Assignment: Unit Circle")
    st.caption("Designed & Prepared by: Mr. Tarek Shawky")
    st.write("---")

    mode_hw = st.radio("اختر وضع العرض:", ["Student Mode (وضع الطالب)", "Teacher Mode (وضع المعلم)"], horizontal=True, key="hw_mode")

    hw_questions = [
        {
            "level": "🟢 Easy Level",
            "id": 1,
            "q": "1. What is the value of sin(90°)?",
            "opts": ["a) 0", "b) 1", "c) -1", "d) Undefined"],
            "ans": "b) 1",
            "hint": "90° represents the highest point on the y-axis of the unit circle.",
            "sol": "The point at 90° on the unit circle is (0, 1), so sin(90°) = 1."
        },
        {
            "level": "🟢 Easy Level",
            "id": 2,
            "q": "2. In which quadrant are both sin(θ) > 0 and cos(θ) < 0?",
            "opts": ["a) Quadrant I", "b) Quadrant II", "c) Quadrant III", "d) Quadrant IV"],
            "ans": "b) Quadrant II",
            "hint": "Use ASTC rule. Sine is positive where y > 0 and x < 0.",
            "sol": "In Quadrant II, x-coordinates are negative (cos < 0) and y-coordinates are positive (sin > 0)."
        },
        {
            "level": "🟡 Medium Level",
            "id": 3,
            "q": "3. Evaluate the exact value of sec(300°).",
            "opts": ["a) 2", "b) -2", "c) 2/√3", "d) -2/√3"],
            "ans": "a) 2",
            "hint": "300° is in Q4. Reference angle = 360° - 300° = 60°. sec(θ) = 1/cos(θ).",
            "sol": "In Q4, cosine is positive. cos(60°) = 1/2, so sec(300°) = 1 / (1/2) = 2."
        },
        {
            "level": "🟡 Medium Level",
            "id": 4,
            "q": "4. If cos(θ) = -5/13 and θ is in Quadrant II, find cot(θ).",
            "opts": ["a) -5/12", "b) -12/5", "c) 5/12", "d) 12/5"],
            "ans": "a) -5/12",
            "hint": "x = -5, r = 13. Find y using Pythagorean theorem, then cot(θ) = x/y.",
            "sol": "y = √(13² - (-5)²) = 12. cot(θ) = x/y = -5/12."
        },
        {
            "level": "🔴 Hard / STEM Level",
            "id": 5,
            "q": "5. Simplify completely: [sin(θ) / (1 + cos(θ))] + [(1 + cos(θ)) / sin(θ)].",
            "opts": ["a) 2 sin(θ)", "b) 2 csc(θ)", "c) 2 cos(θ)", "d) 2 sec(θ)"],
            "ans": "b) 2 csc(θ)",
            "hint": "Combine fractions over a common denominator: sin(θ)(1 + cos(θ)). Use sin²(θ) + cos²(θ) = 1.",
            "sol": "Numerator = sin²(θ) + (1 + cos(θ))² = sin²(θ) + 1 + 2cos(θ) + cos²(θ) = 2 + 2cos(θ) = 2(1 + cos(θ)).\nDenominator = sin(θ)(1 + cos(θ)).\nCanceling (1 + cos(θ)) yields 2 / sin(θ) = 2 csc(θ)."
        }
    ]

    for hw in hw_questions:
        st.markdown(f"#### {hw['level']}")
        st.write(hw["q"])
        if mode_hw == "Student Mode (وضع الطالب)":
            user_ans = st.radio(f"Select HW Q{hw['id']}:", hw["opts"], key=f"hw_{hw['id']}")
            c1, c2 = st.columns(2)
            with c1:
                if st.button(f"💡 Hint HW Q{hw['id']}", key=f"hw_h_{hw['id']}"):
                    st.info(hw["hint"])
            with c2:
                if st.button(f"Check HW Q{hw['id']}", key=f"hw_c_{hw['id']}"):
                    if user_ans == hw["ans"]:
                        st.success("Correct! 🎉")
                    else:
                        st.error("Try again! ❌")
        else:
            st.success(f"**Answer:** {hw['ans']}")
            st.info(f"**Solution Steps:**\n{hw['sol']}")
        st.write("---")

    if st.button("⬅️ العودة إلى بداية الدرس (Back to Lesson)", use_container_width=True):
        st.session_state.page = "Lesson"
        st.rerun()

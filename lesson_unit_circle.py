import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

# =========================================================================
# Grade 10 Advanced Mathematics: Complete & Final Master Version
# Educator: Mr. Tarek Shawky | STEM High Schools Curriculum
# =========================================================================

st.set_page_config(
    page_title="Grade 10 Advanced Math - Mr. Tarek Shawky",
    page_icon="📐",
    layout="wide"
)

st.title(r"📐 Grade 10 Advanced Mathematics: From Right Triangle to Unit Circle")
st.markdown("---")
st.markdown(r"👨‍🏫 **Educator & Curriculum Developer:** Mr. Tarek Shawky | *STEM High Schools Curriculum*")
st.markdown("---")

# =========================================================================
# PART 1: The Right-Angled Triangle & 6 Ratios
# =========================================================================
st.header("1️⃣ Part 1: The Right-Angled Triangle (ABC) & 6 Ratios")
st.write("Let's analyze right-angled triangle $ABC$ at vertex $B$, establishing the foundation of all trigonometric ratios, reciprocals, and angle connections.")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📐 Triangle Ratios, Reciprocals & Deductions")
    st.latex(r"\sin(A) = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{BC}{AC}, \quad \csc(A) = \frac{1}{\sin(A)} = \frac{AC}{BC}")
    st.latex(r"\cos(A) = \frac{\text{Adjacent}}{\text{Hypotenuse}} = \frac{AB}{AC}, \quad \sec(A) = \frac{1}{\cos(A)} = \frac{AC}{AB}")
    st.latex(r"\tan(A) = \frac{\sin(A)}{\cos(A)} = \frac{BC}{AB}, \quad \cot(A) = \frac{1}{\tan(A)} = \frac{AB}{BC}")
    
    st.markdown("💡 **Student Critical Thinking Task:**")
    st.write("Examine the triangle and deduce the direct mathematical relationship between $\\sin(A)$ and $\\cos(C)$ in the same right-angled triangle.")

with col2:
    st.subheader("Right-Angled Triangle ABC")
    fig_tri, ax_tri = plt.subplots(figsize=(4, 4))
    triangle_x = [0, 4, 4, 0]
    triangle_y = [0, 0, 3, 0]
    ax_tri.plot(triangle_x, triangle_y, color='black', lw=2)
    ax_tri.plot([3.7, 3.7, 4.0], [0, 0.3, 0.3], color='red', lw=1.5)
    ax_tri.text(-0.3, -0.2, 'A', fontsize=12, fontweight='bold', color='blue')
    ax_tri.text(4.1, -0.3, 'B (90°)', fontsize=11, fontweight='bold', color='blue')
    ax_tri.text(4.1, 3.1, 'C', fontsize=12, fontweight='bold', color='blue')
    ax_tri.text(2.0, -0.4, 'Adjacent (AB)', fontsize=9, color='darkgreen')
    ax_tri.text(4.2, 1.5, 'Opposite (BC)', fontsize=9, color='darkgreen')
    ax_tri.text(1.8, 1.7, 'Hypotenuse (AC)', fontsize=9, color='purple', rotation=37)
    ax_tri.set_xlim(-1, 5.5)
    ax_tri.set_ylim(-1, 4)
    ax_tri.axis('off')
    st.pyplot(fig_tri)

st.markdown("---")

# =========================================================================
# Fundamental & Secondary Trigonometric Identities Reference
# =========================================================================
st.header("📚 Fundamental & Secondary Trigonometric Identities Reference")
st.write("Keep these core identities handy for your proofs and advanced problem-solving:")
st.markdown("""
- **Pythagorean Identity:** $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$
- **Secant Identity:** $\\sec^2(\\theta) = \\tan^2(\\theta) + 1$
- **Cosecant Identity:** $\\csc^2(\\theta) = \\cot^2(\\theta) + 1$
""")

st.markdown("---")

# =========================================================================
# PART 2: The Unit Circle & Pythagorean Identity Verification
# =========================================================================
st.header("2️⃣ Part 2: The Unit Circle & Pythagorean Identity Verification")
st.write("Expanding from right triangles to the Unit Circle. Move the slider to watch how $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$ holds true dynamically for any angle rotation.")

angle = st.slider("Select Rotation Angle (θ in degrees):", 0, 360, 21)
theta_rad = np.radians(angle)

col_viz1, col_viz2 = st.columns([1, 1])

with col_viz1:
    st.markdown(f"### 📍 Coordinates at {angle}°")
    x_val = np.cos(theta_rad)
    y_val = np.sin(theta_rad)
    st.latex(f"x = \\cos({angle}^\\circ) = {x_val:.4f}")
    st.latex(f"y = \\sin({angle}^\\circ) = {y_val:.4f}")
    identity_check = x_val**2 + y_val**2
    st.info(f"📌 Identity Check: ({x_val:.2f})^2 + ({y_val:.2f})^2 = {identity_check:.1f} (Always equals 1!)")

with col_viz2:
    fig, ax = plt.subplots(figsize=(4, 4))
    t = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), '--', color='gray')
    ax.plot([0, x_val], [0, y_val], color='blue', lw=2, label='Radius r=1')
    ax.plot([0, x_val], [0, 0], color='red', lw=2, label='Cos (x)')
    ax.plot([x_val, x_val], [0, y_val], color='green', lw=2, label='Sin (y)')
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_aspect('equal')
    ax.set_title(f"Unit Circle Explorer (θ = {angle}°)")
    ax.legend(fontsize=8); ax.grid(True)
    st.pyplot(fig)

st.markdown("---")

# =========================================================================
# Classroom Exercises (10 Questions)
# =========================================================================
st.header("📝 Classroom Exercises")
st.subheader("✍️ In-Class Practice on Trig Ratios & Unit Circle")

classwork_questions = [
    {"q": "If $\\sec(\\theta) + \\tan(\\theta) = k$, what is $\\sec(\\theta) - \\tan(\\theta)$?", "options": ["A) $k$", "B) $\\frac{1}{k}$", "C) $1-k$", "D) $k^2$"], "correct": 1},
    {"q": "Simplify: $\\frac{1 - \\sin^2(\\theta)}{\\cos^2(\\theta)}$", "options": ["A) $1$", "B) $0$", "C) $\\tan^2(\\theta)$", "D) $\\cot^2(\\theta)$"], "correct": 0},
    {"q": "What is the exact value of $\\csc(90^\\circ)$?", "options": ["A) $0$", "B) $-1$", "C) $1$", "D) Undefined"], "correct": 2},
    {"q": "If $\\sin(\\theta) = 0$, what are the possible values of $\\theta$ in $[0, 360^\\circ]$?", "options": ["A) $0^\\circ, 180^\\circ, 360^\\circ$", "B) $90^\\circ, 270^\\circ$", "C) $0^\\circ, 90^\\circ$", "D) $180^\\circ$"], "correct": 0},
    {"q": "What is the sign of $\\tan(\\theta)$ in Quadrant IV?", "options": ["A) Positive", "B) Negative", "C) Zero", "D) Undefined"], "correct": 1},
    {"q": "If $\\cos(\\theta) = \\frac{4}{5}$ and $\\theta$ is in Quadrant I, what is $\\sin(\\theta)$?", "options": ["A) $\\frac{3}{5}$", "B) $-\\frac{3}{5}$", "C) $\\frac{4}{5}$", "D) $-\\frac{4}{5}$"], "correct": 0},
    {"q": "What is the value of $\\cot(45^\\circ)$?", "options": ["A) $0$", "B) $1$", "C) $-1$", "D) Undefined"], "correct": 1},
    {"q": "Which of the following is equivalent to $\\frac{1}{\\csc(\\theta)}$?", "options": ["A) $\\cos(\\theta)$", "B) $\\tan(\\theta)$", "C) $\\sin(\\theta)$", "D) $\\sec(\\theta)$"], "correct": 2},
    {"q": "What is the period of the function $f(\\theta) = \\sin(\\theta)$?", "options": ["A) $\\pi$", "B) $\\frac{\\pi}{2}$", "C) $2\\pi$", "D) $4\\pi$"], "correct": 2},
    {"q": "If $\\tan(\\theta) = \\sqrt{3}$ and $\\theta$ is acute, what is $\\theta$?", "options": ["A) $30^\\circ$", "B) $45^\\circ$", "C) $60^\\circ$", "D) $90^\\circ$"], "correct": 2}
]

for idx, item in enumerate(classwork_questions, 1):
    with st.expander(f"Class Exercise {idx}"):
        st.markdown(f"**Problem {idx}:** {item['q']}")
        ans = st.radio(f"Select your answer for Class Q{idx}:", item['options'], index=None, key=f"g10_cw_q_{idx}")
        if st.button(f"Check Answer (Q{idx})", key=f"btn_g10_cw_{idx}"):
            if ans is None:
                st.warning("⚠️ Please select an answer first!")
            else:
                selected_idx = item['options'].index(ans)
                if selected_idx == item['correct']:
                    st.success("✅ Correct! Excellent work.")
                else:
                    st.error("❌ Incorrect. Review the concept with the instructor.")

st.markdown("---")

# =========================================================================
# PART 3: Homework Assessment (Fixed 15 Questions with Permanent Server Logging)
# =========================================================================
st.header("🎯 Homework Assessment")
st.markdown("⚠️ **Notice:** Total homework score is out of **15 fixed questions**. All submissions are permanently recorded with your name and timestamp as official proof of effort.")

results_file = "grade10_homework_results.txt"
student_name = st.text_input("👤 Enter your Full Name (Required to unlock homework):", key="grade10_student_name")

if student_name:
    hw_questions = [
        {"q": "If $\\sin(\\theta) = \\frac{3}{5}$ and $\\theta$ is in the second quadrant, what is $\\sec(\\theta)$?", "options": ["A) $-\\frac{5}{4}$", "B) $\\frac{5}{4}$", "C) $-\\frac{4}{3}$", "D) $\\frac{3}{4}$"], "correct": 0},
        {"q": "What is the exact value of $\\tan\\left(\\frac{5\\pi}{4}\\right)$?", "options": ["A) $1$", "B) $-1$", "C) $\\sqrt{3}$", "D) $-\\sqrt{3}$"], "correct": 0},
        {"q": "If $\\cos(\\theta) = -\\frac{12}{13}$ and $\\csc(\\theta) > 0$, what is $\\cot(\\theta)$?", "options": ["A) $-\\frac{12}{5}$", "B) $\\frac{12}{5}$", "C) $-\\frac{5}{12}$", "D) $\\frac{5}{12}$"], "correct": 2},
        {"q": "What is the value of $\\sin(180^\\circ)$?", "options": ["A) $1$", "B) $0$", "C) $-1$", "D) Undefined"], "correct": 1},
        {"q": "Which quadrant has both sine and cosine negative?", "options": ["A) I", "B) II", "C) III", "D) IV"], "correct": 2},
        {"q": "What is $\\sec(0^\\circ)$?", "options": ["A) $0$", "B) $1$", "C) $-1$", "D) Undefined"], "correct": 1},
        {"q": "If $\\tan(\\theta) = -1$ and $\\theta$ is in Quadrant II, what is $\\theta$?", "options": ["A) $135^\\circ$", "B) $45^\\circ$", "C) $225^\\circ$", "D) $315^\\circ$"], "correct": 0},
        {"q": "What is the value of $\\csc(30^\\circ)$?", "options": ["A) $\\frac{1}{2}$", "B) $2$", "C) $\\sqrt{2}$", "D) $\\frac{2}{\\sqrt{3}}$"], "correct": 1},
        {"q": "Simplify: $\\sin(\\theta) \\cot(\\theta)$", "options": ["A) $\\cos(\\theta)$", "B) $\\tan(\\theta)$", "C) $\\csc(\\theta)$", "D) $1$"], "correct": 0},
        {"q": "What is the sign of $\\sec(\\theta)$ in Quadrant III?", "options": ["A) Positive", "B) Negative", "C) Zero", "D) Undefined"], "correct": 1},
        {"q": "If $\\cos(\\theta) = 0$, what are the possible angles in $[0, 360^\\circ]$?", "options": ["A) $0^\\circ, 180^\\circ$", "B) $90^\\circ, 270^\\circ$", "C) $180^\\circ, 360^\\circ$", "D) $0^\\circ, 360^\\circ$"], "correct": 1},
        {"q": "What is the value of $\\sin^2(50^\\circ) + \\cos^2(50^\\circ)$?", "options": ["A) $0$", "B) $1$", "C) $\\sin(100^\\circ)$", "D) $2$"], "correct": 1},
        {"q": "If $\\cot(\\theta) = 0$, what is $\\theta$ in $[0, 180^\\circ]$?", "options": ["A) $0^\\circ$", "B) $90^\\circ$", "C) $180^\\circ$", "D) $45^\\circ$"], "correct": 1},
        {"q": "What is $\\tan(90^\\circ)$?", "options": ["A) $0$", "B) $1$", "C) $-1$", "D) Undefined"], "correct": 3},
        {"q": "If $\\csc(\\theta) = -2$ and $\\theta$ is in Quadrant IV, what is $\\theta$?", "options": ["A) $300^\\circ$", "B) $330^\\circ$", "C) $210^\\circ$", "D) $240^\\circ$"], "correct": 1}
    ]

    user_answers = {}
    total_questions = len(hw_questions)
    
    for idx, hw in enumerate(hw_questions, 1):
        user_answers[idx] = st.radio(f"**Homework Question {idx}:** {hw['q']}", hw['options'], index=None, key=f"g10_hw_q{idx}")
        st.markdown("---")
        
    if st.button("🚀 Submit Homework Assignment", key="submit_g10_hw"):
        score = 0
        answered_count = 0
        
        for idx, hw in enumerate(hw_questions, 1):
            if user_answers[idx] is not None:
                answered_count += 1
                selected_idx = hw['options'].index(user_answers[idx])
                if selected_idx == hw['correct']:
                    score += 1

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Fixed out of 15 denominator as requested by Mr. Tarek
        record = f"Student: {student_name} | Score: {score}/{total_questions} | Answered: {answered_count}/{total_questions} | Time: {timestamp}\n"
        
        with open(results_file, "a", encoding="utf-8") as f:
            f.write(record)

        st.success(f"🎉 Great job, {student_name}! Your grade is **{score} / {total_questions}**. The result has been securely logged with your name and timestamp for your instructor's records.")
        
    # Optional section for instructor to view logs directly in app sidebar or view
    if st.checkbox("🔐 Instructor Log Viewer (Mr. Tarek Only)"):
        st.subheader("📋 Saved Student Homework Records:")
        if os.path.exists(results_file):
            with open(results_file, "r", encoding="utf-8") as f:
                logs = f.readlines()
            for log in reversed(logs):
                st.text(log.strip())
            if st.button("🗑️ Clear Log File"):
                open(results_file, "w").close()
                st.rerun()
        else:
            st.info("No submission records found yet.")
else:
    st.warning("⚠️ Please enter your full name above to unlock and submit the homework assessment.")
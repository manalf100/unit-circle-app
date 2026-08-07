import streamlit as st

st.set_page_config(page_title="STEM Trigonometry Exercises", layout="centered")

# Title and Header
st.title("🎯 STEM Trigonometry & Unit Circle Exercises")
st.caption("Designed & Prepared by: Mr. Tarek Shawky")
st.write("---")

# Mode Switcher
mode = st.radio("اختر وضع العرض (Select View Mode):", ["Student Mode (وضع الطالب)", "Teacher Mode (وضع المعلم)"], horizontal=True)

# Question Data
questions = [
    {
        "id": 1,
        "question": "1. What is the exact value of cos(120°)?",
        "options": ["a) 1/2", "b) -1/2", "c) √3/2", "d) -√3/2"],
        "correct": "b) -1/2",
        "hint": "120° is in Quadrant II, where cosine is negative. The reference angle is 180° - 120° = 60°.",
        "solution": "In Quadrant II, cos(θ) < 0. Reference angle = 60°. Since cos(60°) = 1/2, then cos(120°) = -1/2."
    },
    {
        "id": 2,
        "question": "2. If sin(θ) = 0.8 and θ is an acute angle in Quadrant I, what is cos(θ)?",
        "options": ["a) 0.2", "b) 0.6", "c) -0.6", "d) 0.75"],
        "correct": "b) 0.6",
        "hint": "Use the fundamental Pythagorean identity: sin²(θ) + cos²(θ) = 1.",
        "solution": "cos²(θ) = 1 - sin²(θ) = 1 - (0.8)² = 1 - 0.64 = 0.36. Since θ is in Quadrant I, cos(θ) = √0.36 = 0.6."
    },
    {
        "id": 3,
        "question": "3. Which of the following functions is equivalent to 1 / sin(θ)?",
        "options": ["a) cos(θ)", "b) sec(θ)", "c) csc(θ)", "d) cot(θ)"],
        "correct": "c) csc(θ)",
        "hint": "Think about the reciprocal trigonometric functions.",
        "solution": "By definition, the cosecant function csc(θ) is the reciprocal of sin(θ)."
    }
]

# Display Questions
for q in questions:
    st.subheader(f"Question {q['id']}")
    st.write(q["question"])
    
    if mode == "Student Mode (وضع الطالب)":
        user_choice = st.radio(f"Select your answer for Q{q['id']}:", q["options"], key=f"q_{q['id']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"💡 Show Hint Q{q['id']}", key=f"hint_{q['id']}"):
                st.info(f"**Hint:** {q['hint']}")
        with col2:
            if st.button(f"Check Answer Q{q['id']}", key=f"check_{q['id']}"):
                if user_choice == q["correct"]:
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect, try again! ❌")
                    
    else: # Teacher Mode
        st.success(f"**Correct Answer:** {q['correct']}")
        st.info(f"**Explanation & Solution:** {q['solution']}")
        
    st.write("---")
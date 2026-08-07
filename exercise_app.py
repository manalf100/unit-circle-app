import streamlit as st

st.set_page_config(page_title="STEM Trigonometry Exercises", layout="centered")

# Title and Header
st.title("🎯 STEM Trigonometry & Unit Circle Exercises")
st.caption("Designed & Prepared by: Mr. Tarek Shawky")
st.write("---")

# Mode Switcher
mode = st.radio("اختر وضع العرض (Select View Mode):", ["Student Mode (وضع الطالب)", "Teacher Mode (وضع المعلم)"], horizontal=True)

# Full 10 Questions Data
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
    },
    {
        "id": 4,
        "question": "4. What is the radian measure equivalent to 270°?",
        "options": ["a) π/2", "b) π", "c) 3π/2", "d) 2π"],
        "correct": "c) 3π/2",
        "hint": "Multiply the degree measure by (π / 180°).",
        "solution": "270° × (π / 180°) = 270π / 180 = 3π/2 radians."
    },
    {
        "id": 5,
        "question": "5. Which trigonometric ratio corresponds to the x-coordinate of a point on the unit circle?",
        "options": ["a) sin(θ)", "b) cos(θ)", "c) tan(θ)", "d) sec(θ)"],
        "correct": "b) cos(θ)",
        "hint": "On the unit circle, any point P is defined as (x, y) = (cos θ, sin θ).",
        "solution": "The x-coordinate represents cos(θ), and the y-coordinate represents sin(θ)."
    },
    {
        "id": 6,
        "question": "6. What is the value of tan(225°)?",
        "options": ["a) 1", "b) -1", "c) √3", "d) -√3"],
        "correct": "a) 1",
        "hint": "225° is in Quadrant III where tangent is positive. Reference angle = 225° - 180° = 45°.",
        "solution": "In Quadrant III, tan(θ) > 0. Reference angle = 45°. tan(45°) = 1, so tan(225°) = 1."
    },
    {
        "id": 7,
        "question": "7. If tan(θ) = 3/4 and θ is in Quadrant III, what is sin(θ)?",
        "options": ["a) 3/5", "b) -3/5", "c) 4/5", "d) -4/5"],
        "correct": "b) -3/5",
        "hint": "Construct a right triangle or use identities. Remember sine is negative in Quadrant III.",
        "solution": "Opposite = 3, Adjacent = 4, Hypotenuse = √(3² + 4²) = 5. sin(θ) = Opposite/Hypotenuse = 3/5. In Q3, sin(θ) < 0, so sin(θ) = -3/5."
    },
    {
        "id": 8,
        "question": "8. Simplify the expression: sin²(θ) · csc²(θ).",
        "options": ["a) 0", "b) 1", "c) sin(θ)", "d) cos²(θ)"],
        "correct": "b) 1",
        "hint": "Remember that csc(θ) = 1 / sin(θ).",
        "solution": "sin²(θ) · (1 / sin²(θ)) = 1."
    },
    {
        "id": 9,
        "question": "9. What is the domain of the function f(θ) = tan(θ)?",
        "options": ["a) All real numbers", "b) θ ≠ nπ", "c) θ ≠ (2n + 1)π/2", "d) -1 ≤ θ ≤ 1"],
        "correct": "c) θ ≠ (2n + 1)π/2",
        "hint": "tan(θ) = sin(θ) / cos(θ). Identify where the denominator equals zero.",
        "solution": "tan(θ) is undefined where cos(θ) = 0, which occurs at odd multiples of π/2: θ ≠ (2n + 1)π/2."
    },
    {
        "id": 10,
        "question": "10. What is the value of sec(60°)?",
        "options": ["a) 1/2", "b) 2", "c) √2", "d) 2/√3"],
        "correct": "b) 2",
        "hint": "sec(θ) is the reciprocal of cos(θ).",
        "solution": "cos(60°) = 1/2. Therefore, sec(60°) = 1 / cos(60°) = 1 / (1/2) = 2."
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
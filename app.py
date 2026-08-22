import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Math Grade 12: Implicit Differentiation", layout="wide"
)

# Title & Instructor Credit
st.title("Math Grade 12 STEM Mathematics")
st.subheader("Topic: Implicit Differentiation - MCQ Exercises")

st.sidebar.markdown("---")
st.sidebar.markdown("**Prepared by:** Mr. Tarek Shawky")
st.sidebar.markdown("---")

st.write(
    "Welcome, students! Test your skills with the original multiple-choice"
    " questions below."
)
st.markdown("---")

# ==========================================
# PART 1: 10 STEM Exam-Level MCQ Exercises
# ==========================================
st.header("Advanced STEM Exam-Level Exercises (MCQ)")

# Exercise 1
st.markdown("### Exercise 1")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \tan(xy) = x")
selected_ex1 = st.radio(
    "Choose the correct answer for Exercise 1:",
    [
        "A) $\\frac{1 - y \\sec^2(xy)}{x \\sec^2(xy)}$",
        "B) $\\frac{\\sec^2(xy) - 1}{x}$",
        "C) $\\frac{y}{1 - x}$",
        "D) $\\frac{1}{x \\sec^2(xy)}$",
    ],
    key="ex1",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $\\frac{1 - y \\sec^2(xy)}{x \\sec^2(xy)}$")
  st.write(
      "**Explanation:** Differentiating both sides implicitly gives"
      " $\\sec^2(xy) \\cdot (y + x \\frac{dy}{dx}) = 1$. Expanding and solving"
      " for $\\frac{dy}{dx}$ yields the correct option."
  )

# Exercise 2
st.markdown("### Exercise 2")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } x^y = y^x")
selected_ex2 = st.radio(
    "Choose the correct answer for Exercise 2:",
    [
        "A) $\\frac{y(x \\ln y - y)}{x(y \\ln x - x)}$",
        "B) $\\frac{x \\ln x}{y \\ln y}$",
        "C) $\\frac{y}{x}$",
        "D) $\\frac{\\ln y - 1}{\\ln x - 1}$",
    ],
    key="ex2",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $\\frac{y(x \\ln y - y)}{x(y \\ln x - x)}$")
  st.write(
      "**Explanation:** Taking natural logarithms on both sides gives $y \\ln x"
      " = x \\ln y$. Differentiating implicitly and rearranging terms isolates"
      " the derivative."
  )

# Exercise 3
st.markdown("### Exercise 3")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \ln(xy) + 5x = 30")
selected_ex3 = st.radio(
    "Choose the correct answer for Exercise 3:",
    [
        "A) $-y \\left(5 + \\frac{1}{x}\\right)$",
        "B) $-\\frac{1}{5x}$",
        "C) $5 + \\frac{y}{x}$",
        "D) $-\\frac{y}{x}$",
    ],
    key="ex3",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $-y \\left(5 + \\frac{1}{x}\\right)$")
  st.write(
      "**Explanation:** Splitting the logarithm gives $\\ln(x) + \\ln(y) + 5x ="
      " 30$. Differentiating term by term yields $\\frac{1}{x} +"
      " \\frac{1}{y}\\frac{dy}{dx} + 5 = 0$."
  )

# Exercise 4
st.markdown("### Exercise 4")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } e^{x+y} = \sin(xy)")
selected_ex4 = st.radio(
    "Choose the correct answer for Exercise 4:",
    [
        "A) $\\frac{y\\cos(xy) - e^{x+y}}{e^{x+y} - x\\cos(xy)}$",
        "B) $\\frac{e^{x+y}}{\\cos(xy)}$",
        "C) $\\frac{x + y}{1 - x}$",
        "D) $\\frac{\\cos(xy)}{e^{x+y}}$",
    ],
    key="ex4",
)
with st.expander("Show Correct Answer & Solution"):
  st.write(
      "**Correct Answer:** A) $\\frac{y\\cos(xy) - e^{x+y}}{e^{x+y} -"
      " x\\cos(xy)}$"
  )
  st.write(
      "**Explanation:** Apply exponential rule on the left and chain/product"
      " rule on the right, then group $\\frac{dy}{dx}$ terms."
  )

# Exercise 5
st.markdown("### Exercise 5")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } x^2 y^3 - 5xy = 2")
selected_ex5 = st.radio(
    "Choose the correct answer for Exercise 5:",
    [
        "A) $\\frac{5y - 2xy^3}{3x^2y^2 - 5x}$",
        "B) $\\frac{2x + y}{3y^2}$",
        "C) $\\frac{5x}{2y^3}$",
        "D) $\\frac{2xy^3 - 5y}{3x^2y^2}$",
    ],
    key="ex5",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $\\frac{5y - 2xy^3}{3x^2y^2 - 5x}$")
  st.write(
      "**Explanation:** Use the product rule for both terms containing products"
      " of $x$ and $y$, then solve for the derivative."
  )

# Exercise 6
st.markdown("### Exercise 6")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \sin^2(x) + \cos^2(y) = 1")
selected_ex6 = st.radio(
    "Choose the correct answer for Exercise 6:",
    [
        "A) $\\frac{\\sin(2x)}{\\sin(2y)}$",
        "B) $-\\frac{\\cos(x)}{\\sin(y)}$",
        "C) $\\frac{\\cos(2x)}{\\cos(2y)}$",
        "D) $1$",
    ],
    key="ex6",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $\\frac{\\sin(2x)}{\\sin(2y)}$")
  st.write(
      "**Explanation:** Chain rule gives $2\\sin(x)\\cos(x) -"
      " 2\\cos(y)\\sin(y)\\frac{dy}{dx} = 0$, simplifying via double-angle"
      " identities."
  )

# Exercise 7
st.markdown("### Exercise 7")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \sqrt{x} + \sqrt{y} = \sqrt{a}")
selected_ex7 = st.radio(
    "Choose the correct answer for Exercise 7:",
    [
        "A) $-\\sqrt{\\frac{y}{x}}$",
        "B) $\\sqrt{\\frac{x}{y}}$",
        "C) $-\\frac{x}{y}$",
        "D) $\\frac{a}{x+y}$",
    ],
    key="ex7",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $-\\sqrt{\\frac{y}{x}}$")
  st.write(
      "**Explanation:** Differentiating powers $x^{1/2}$ and $y^{1/2}$ directly"
      " leads to the ratio of square roots."
  )

# Exercise 8
st.markdown("### Exercise 8")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } x^3 + y^3 = 3axy")
selected_ex8 = st.radio(
    "Choose the correct answer for Exercise 8:",
    [
        "A) $\\frac{ay - x^2}{y^2 - ax}$",
        "B) $\\frac{x^2 + y^2}{axy}$",
        "C) $\\frac{3x - a}{3y}$",
        "D) $\\frac{y^2 - ax}{ay - x^2}$",
    ],
    key="ex8",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $\\frac{ay - x^2}{y^2 - ax}$")
  st.write(
      "**Explanation:** Differentiate term by term using the product rule on the"
      " right-hand side term $3axy$."
  )

# Exercise 9
st.markdown("### Exercise 9")
st.latex(
    r"\text{Find the slope at } (1,1) \text{ for } 2x^2 + xy - y^2 = 2"
)
selected_ex9 = st.radio(
    "Choose the correct answer for Exercise 9:",
    ["A) $5$", "B) $1$", "C) $-2$", "D) $\\frac{1}{2}$"],
    key="ex9",
)
with st.expander("Show Correct Answer & Solution"):
  st.write("**Correct Answer:** A) $5$")
  st.write(
      "**Explanation:** The general derivative is $\\frac{4x + y}{2y - x}$."
      " Substituting $(1,1)$ gives $\\frac{4(1)+1}{2(1)-1} = 5$."
  )

# Exercise 10
st.markdown("### Exercise 10")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \arcsin(xy) = x^2")
selected_ex10 = st.radio(
    "Choose the correct answer for Exercise 10:",
    [
        "A) $\\frac{2x\\sqrt{1 - x^2y^2} - y}{x}$",
        "B) $\\frac{1}{x \\sqrt{1-x^2}}$",
        "C) $\\frac{2x}{\\sqrt{1-x^2}}$",
        "D) $\\frac{y}{2x}$",
    ],
    key="ex10",
)
with st.expander("Show Correct Answer & Solution"):
  st.write(
      "**Correct Answer:** A) $\\frac{2x\\sqrt{1 - x^2y^2} - y}{x}$"
  )
  st.write(
      "**Explanation:** Apply the inverse sine derivative formula combined with"
      " the product rule for $xy$."
  )

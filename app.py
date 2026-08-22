import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Math Grade 12: Implicit Differentiation", layout="wide"
)

# Title & Instructor Credit
st.title("Math Grade 12 STEM Mathematics")
st.subheader(
    "Topic: Implicit Differentiation - Core Concepts, Examples & Visualization"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Prepared by:** Mr. Tarek Shawky")
st.sidebar.markdown("---")

st.write(
    "Welcome, students! Review the step-by-step examples first, explore the"
    " interactive unit circle module, and then test your skills with the"
    " advanced STEM multiple-choice exercises below."
)
st.markdown("---")

# ==========================================
# PART 1: Step-by-Step Examples
# ==========================================
st.header("1. Step-by-Step Core Examples")

# Example 1
st.markdown("### Example 1: Basic Power & Chain Rule")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } x^3 + y^3 = 6xy")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Differentiate both sides with respect to $x$ term by term."
  )
  st.latex(r"\frac{d}{dx}(x^3) + \frac{d}{dx}(y^3) = \frac{d}{dx}(6xy)")
  st.write(
      "**Step 2:** Apply power rule and chain rule (where $\\frac{d}{dx}(y) ="
      " y'$)."
  )
  st.latex(r"3x^2 + 3y^2 \frac{dy}{dx} = 6(x \frac{dy}{dx} + y \cdot 1)")
  st.write(
      "**Step 3:** Group all terms containing $\\frac{dy}{dx}$ on one side."
  )
  st.latex(r"3y^2 \frac{dy}{dx} - 6x \frac{dy}{dx} = 6y - 3x^2")
  st.write("**Step 4:** Factor out $\\frac{dy}{dx}$ and solve.")
  st.latex(
      r"\frac{dy}{dx} = \frac{6y - 3x^2}{3y^2 - 6x} = \frac{2y - x^2}{y^2 - 2x}"
  )

# Example 2
st.markdown("### Example 2: Trigonometric Implicit Function")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } \sin(y) + x^2 = y")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Differentiate with respect to $x$ using the chain rule."
  )
  st.latex(r"\cos(y) \cdot \frac{dy}{dx} + 2x = \frac{dy}{dx}")
  st.write("**Step 2:** Rearrange terms to isolate $\\frac{dy}{dx}$.")
  st.latex(r"\cos(y) \frac{dy}{dx} - \frac{dy}{dx} = -2x")
  st.write("**Step 3:** Final expression.")
  st.latex(r"\frac{dy}{dx} = \frac{-2x}{\cos(y) - 1}")

# Example 3
st.markdown("### Example 3: Product Rule with Implicit Terms")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } x e^y + y e^x = 10")
with st.expander("Show Step-by-Step Solution"):
  st.write("**Step 1:** Apply product rule on both terms.")
  st.latex(
      r"(1 \cdot e^y + x e^y \frac{dy}{dx}) + (\frac{dy}{dx} e^x + y e^x) = 0"
  )
  st.write("**Step 2:** Collect $\\frac{dy}{dx}$ terms.")
  st.latex(
      r"\frac{dy}{dx}(x e^y + e^x) = -(e^y + y e^x) \implies \frac{dy}{dx} ="
      r" \frac{-(e^y + y e^x)}{x e^y + e^x}"
  )

# Example 4
st.markdown("### Example 4: Rational Implicit Expression")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } \frac{x}{y} = x + y")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Use quotient rule on the left side: $\\frac{1 \cdot y - x"
      " \\frac{dy}{dx}}{y^2} = 1 + \\frac{dy}{dx}$"
  )
  st.write("**Step 2:** Clear denominator and solve for $\\frac{dy}{dx}$.")
  st.latex(r"y - x \frac{dy}{dx} = y^2 + y^2 \frac{dy}{dx}")
  st.latex(r"\frac{dy}{dx} = \frac{y - y^2}{x + y^2}")

# Example 5
st.markdown("### Example 5: Quadratic Mixed Terms")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } x^2 - xy + y^2 = 4")
with st.expander("Show Step-by-Step Solution"):
  st.write("**Step 1:** Differentiate term by term using product rule for $-xy$.")
  st.latex(r"2x - (y + x \frac{dy}{dx}) + 2y \frac{dy}{dx} = 0")
  st.write("**Step 2:** Isolate the derivative.")
  st.latex(
      r"(2y - x) \frac{dy}{dx} = y - 2x \implies \frac{dy}{dx} ="
      r" \frac{y - 2x}{2y - x}"
  )

st.markdown("---")

# ==========================================
# PART 2: Interactive Unit Circle & Tangent
# ==========================================
st.header("2. Interactive Module: Tangent Line to a Circle")

st.sidebar.header("Control Panel")
x_val = st.sidebar.slider("Select x value", -4.99, 4.99, 1.00, 0.01)

y_val = np.sqrt(max(0.0, 25 - x_val**2))

col1, col2 = st.columns(2)

with col1:
  st.subheader("Mathematical Data")
  st.latex(r"x^2 + y^2 = 25")
  st.write(f"**Selected Point (x, y):** ({x_val:.2f}, {y_val:.2f})")

  if y_val != 0:
    dydx = -x_val / y_val
    st.write(f"**Derivative (dy/dx):** {dydx:.2f}")
    st.write(
        f"**Tangent Line Equation:** y - {y_val:.2f} ="
        f" {dydx:.2f}(x - {x_val:.2f})"
    )
  else:
    dydx = None
    st.write("**Derivative (dy/dx):** Undefined (Vertical Tangent)")

with col2:
  st.subheader("Geometric Visualization")
  fig, ax = plt.subplots(figsize=(5, 5))

  theta = np.linspace(0, 2 * np.pi, 200)
  ax.plot(
      5 * np.cos(theta),
      5 * np.sin(theta),
      color="blue",
      linewidth=2,
      label="x^2 + y^2 = 25",
  )
  ax.plot(x_val, y_val, "ro", markersize=8, label="Point P")

  if dydx is not None:
    x_tangent = np.linspace(max(-7.0, x_val - 3), min(7.0, x_val + 3), 100)
    y_tangent = dydx * (x_tangent - x_val) + y_val
    ax.plot(x_tangent, y_tangent, "g--", linewidth=2, label="Tangent Line")

  ax.set_aspect("equal")
  ax.grid(True, linestyle=":", alpha=0.7)
  ax.axhline(0, color="black", linewidth=1)
  ax.axvline(0, color="black", linewidth=1)
  ax.set_xlim(-7, 7)
  ax.set_ylim(-7, 7)
  ax.legend(loc="upper right", fontsize=8)

  st.pyplot(fig)

st.markdown("---")

# ==========================================
# PART 3: 10 STEM Exam-Level Exercises (MCQ)
# ==========================================
st.header("3. Advanced STEM Exam-Level Exercises (MCQ)")
st.write(
    "Challenging multiple-choice problems designed for STEM students. Select"
    " your answer and expand to check the solution."
)

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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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
    index=None,
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

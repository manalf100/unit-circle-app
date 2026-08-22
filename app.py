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
    " advanced STEM guided exercises below."
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
# PART 3: 10 STEM Exam-Level Exercises (Step-by-Step Guided)
# ==========================================
st.header("3. Advanced STEM Exam-Level Exercises")
st.write(
    "Challenging problems designed for STEM students. Expand each exercise to"
    " view the guided step-by-step solution."
)

# Exercise 1
st.markdown("### Exercise 1")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \tan(xy) = x")
with st.expander("Show Step-by-Step Guided Solution - Exercise 1"):
  st.write(
      "**Step 1:** Differentiate both sides with respect to $x$ using chain"
      " rule on $\\tan(xy)$."
  )
  st.latex(r"\sec^2(xy) \cdot \frac{d}{dx}(xy) = 1")
  st.write("**Step 2:** Apply product rule for derivative of $(xy)$.")
  st.latex(r"\sec^2(xy) \cdot \left(y + x \frac{dy}{dx}\right) = 1")
  st.write(
      "**Step 3:** Expand and isolate terms containing $\\frac{dy}{dx}$."
  )
  st.latex(
      r"y \sec^2(xy) + x \sec^2(xy) \frac{dy}{dx} = 1 \implies x \sec^2(xy)"
      r" \frac{dy}{dx} = 1 - y \sec^2(xy)"
  )
  st.write("**Step 4:** Final solution for the derivative.")
  st.latex(r"\frac{dy}{dx} = \frac{1 - y \sec^2(xy)}{x \sec^2(xy)}")

# Exercise 2
st.markdown("### Exercise 2")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } x^y = y^x")
with st.expander("Show Step-by-Step Guided Solution - Exercise 2"):
  st.write(
      "**Step 1:** Take natural logarithm ($\ln$) on both sides to bring"
      " exponents down."
  )
  st.latex(r"y \ln x = x \ln y")
  st.write(
      "**Step 2:** Differentiate both sides implicitly with respect to $x$ using"
      " product rule on both."
  )
  st.latex(
      r"\left(\frac{dy}{dx} \ln x + y \cdot \frac{1}{x}\right) = \left(1 \cdot"
      r" \ln y + x \cdot \frac{1}{y} \frac{dy}{dx}\right)"
  )
  st.write("**Step 3:** Group all $\\frac{dy}{dx}$ terms on one side.")
  st.latex(r"\frac{dy}{dx} \left(\ln x - \frac{x}{y}\right) = \ln y - \frac{y}{x}")
  st.write("**Step 4:** Simplify denominators and solve for $\\frac{dy}{dx}$.")
  st.latex(
      r"\frac{dy}{dx} = \frac{y(x \ln y - y)}{x(y \ln x - x)}"
  )

# Exercise 3
st.markdown("### Exercise 3")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \ln(xy) + 5x = 30")
with st.expander("Show Step-by-Step Guided Solution - Exercise 3"):
  st.write("**Step 1:** Use logarithm properties to split $\\ln(xy)$ first.")
  st.latex(r"\ln(x) + \ln(y) + 5x = 30")
  st.write(
      "**Step 2:** Differentiate each term implicitly with respect to $x$."
  )
  st.latex(r"\frac{1}{x} + \frac{1}{y}\frac{dy}{dx} + 5 = 0")
  st.write("**Step 3:** Isolate the fractional derivative term.")
  st.latex(r"\frac{1}{y}\frac{dy}{dx} = -5 - \frac{1}{x}")
  st.write("**Step 4:** Multiply by $y$ to get final result.")
  st.latex(r"\frac{dy}{dx} = -y \left(5 + \frac{1}{x}\right)")

# Exercise 4
st.markdown("### Exercise 4")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } e^{x+y} = \sin(xy)")
with st.expander("Show Step-by-Step Guided Solution - Exercise 4"):
  st.write("**Step 1:** Differentiate both sides using exponential and chain rules.")
  st.latex(r"e^{x+y} \cdot \left(1 + \frac{dy}{dx}\right) = \cos(xy) \cdot \left(y + x \frac{dy}{dx}\right)")
  st.write("**Step 2:** Distribute terms on both sides.")
  st.latex(r"e^{x+y} + e^{x+y}\frac{dy}{dx} = y\cos(xy) + x\cos(xy)\frac{dy}{dx}")
  st.write("**Step 3:** Collect $\\frac{dy}{dx}$ on the left side.")
  st.latex(r"\frac{dy}{dx} \left(e^{x+y} - x\cos(xy)\right) = y\cos(xy) - e^{x+y}")
  st.write("**Step 4:** Final expression.")
  st.latex(r"\frac{dy}{dx} = \frac{y\cos(xy) - e^{x+y}}{e^{x+y} - x\cos(xy)}")

# Exercise 5
st.markdown("### Exercise 5")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } x^2 y^3 - 5xy = 2")
with st.expander("Show Step-by-Step Guided Solution - Exercise 5"):
  st.write("**Step 1:** Apply product rule for $x^2y^3$ and $-5xy$.")
  st.latex(r"\left(2xy^3 + x^2 \cdot 3y^2 \frac{dy}{dx}\right) - \left(5y + 5x \frac{dy}{dx}\right) = 0")
  st.write("**Step 2:** Group terms with $\\frac{dy}{dx}$.")
  st.latex(r"\frac{dy}{dx} \left(3x^2y^2 - 5x\right) = 5y - 2xy^3")
  st.write("**Step 3:** Divide to get final derivative.")
  st.latex(r"\frac{dy}{dx} = \frac{5y - 2xy^3}{3x^2y^2 - 5x}")

# Exercise 6
st.markdown("### Exercise 6")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \sin^2(x) + \cos^2(y) = 1")
with st.expander("Show Step-by-Step Guided Solution - Exercise 6"):
  st.write("**Step 1:** Apply chain rule to powers of trigonometric functions.")
  st.latex(r"2\sin(x)\cos(x) + 2\cos(y)(-\sin(y))\frac{dy}{dx} = 0")
  st.write("**Step 2:** Use double angle identities: $2\sin(x)\cos(x) = \sin(2x)$.")
  st.latex(r"\sin(2x) - \sin(2y)\frac{dy}{dx} = 0")
  st.write("**Step 3:** Solve for $\\frac{dy}{dx}$.")
  st.latex(r"\frac{dy}{dx} = \frac{\sin(2x)}{\sin(2y)}")

# Exercise 7
st.markdown("### Exercise 7")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \sqrt{x} + \sqrt{y} = \sqrt{a}")
with st.expander("Show Step-by-Step Guided Solution - Exercise 7"):
  st.write("**Step 1:** Convert square roots to fractional exponents ($x^{1/2}$).")
  st.latex(r"\frac{1}{2}x^{-1/2} + \frac{1}{2}y^{-1/2}\frac{dy}{dx} = 0")
  st.write("**Step 2:** Multiply entire equation by $2$ and isolate derivative term.")
  st.latex(r"\frac{1}{\sqrt{y}}\frac{dy}{dx} = -\frac{1}{\sqrt{x}}")
  st.write("**Step 3:** Solve for $\\frac{dy}{dx}$.")
  st.latex(r"\frac{dy}{dx} = -\sqrt{\frac{y}{x}}")

# Exercise 8
st.markdown("### Exercise 8")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } x^3 + y^3 = 3axy")
with st.expander("Show Step-by-Step Guided Solution - Exercise 8"):
  st.write("**Step 1:** Differentiate both sides term by term.")
  st.latex(r"3x^2 + 3y^2\frac{dy}{dx} = 3a\left(y + x\frac{dy}{dx}\right)")
  st.write("**Step 2:** Divide by 3 and expand right side.")
  st.latex(r"x^2 + y^2\frac{dy}{dx} = ay + ax\frac{dy}{dx}")
  st.write("**Step 3:** Group derivative terms and factor out.")
  st.latex(r"\frac{dy}{dx}(y^2 - ax) = ay - x^2")
  st.write("**Step 4:** Final result.")
  st.latex(r"\frac{dy}{dx} = \frac{ay - x^2}{y^2 - ax}")

# Exercise 9
st.markdown("### Exercise 9")
st.latex(r"\text{Find the slope at } (1,1) \text{ for } 2x^2 + xy - y^2 = 2")
with st.expander("Show Step-by-Step Guided Solution - Exercise 9"):
  st.write("**Step 1:** Differentiate implicitly term by term.")
  st.latex(r"4x + (y + x\frac{dy}{dx}) - 2y\frac{dy}{dx} = 0")
  st.write("**Step 2:** Group $\\frac{dy}{dx}$ and find general derivative formula.")
  st.latex(r"\frac{dy}{dx} = \frac{4x + y}{2y - x}")
  st.write("**Step 3:** Substitute point $(x=1, y=1)$ into the derivative.")
  st.latex(r"\left.\frac{dy}{dx}\right|_{(1,1)} = \frac{4(1) + 1}{2(1) - 1} = \frac{5}{1} = 5")

# Exercise 10
st.markdown("### Exercise 10")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ if } \arcsin(xy) = x^2")
with st.expander("Show Step-by-Step Guided Solution - Exercise 10"):
  st.write("**Step 1:** Apply standard derivative formula for inverse sine function.")
  st.latex(r"\frac{1}{\sqrt{1 - (xy)^2}} \cdot \frac{d}{dx}(xy) = 2x")
  st.write("**Step 2:** Apply product rule for $(xy)$.")
  st.latex(r"\frac{1}{\sqrt{1 - x^2y^2}} \cdot \left(y + x\frac{dy}{dx}\right) = 2x")
  st.write("**Step 3:** Multiply both sides by $\\sqrt{1 - x^2y^2}$ and isolate terms.")
  st.latex(r"y + x\frac{dy}{dx} = 2x\sqrt{1 - x^2y^2}")
  st.write("**Step 4:** Final solution for $\\frac{dy}{dx}$.")
  st.latex(r"\frac{dy}{dx} = \frac{2x\sqrt{1 - x^2y^2} - y}{x}")


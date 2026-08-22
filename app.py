import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Math Grade 11: Implicit Differentiation", layout="wide"
)

# Title & Instructor Credit
st.title("Math Grade 11 STEM Mathematics")
st.subheader(
    "Topic: Implicit Differentiation - Core Concepts, Examples & Visualization"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Prepared by:** مستر طارق")
st.sidebar.markdown("---")

st.write(
    "Welcome, students! Review the step-by-step examples first, then explore"
    " the interactive unit circle and tangent line module below."
)
st.markdown("---")

# ==========================================
# PART 1: Step-by-Step Examples
# ==========================================
st.header("1. Step-by-Step Examples")

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

# Sidebar controls for the interactive part
st.sidebar.header("Control Panel")
x_val = st.sidebar.slider("Select x value", -4.99, 4.99, 1.00, 0.01)

# Circle Equation: x^2 + y^2 = 25
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

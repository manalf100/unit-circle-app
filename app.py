import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Math Grade 11: Implicit Differentiation", layout="wide"
)

# Title & Instructor Credit
st.title("Math Grade 11 STEM Mathematics")
st.subheader("Topic: Implicit Differentiation - Step-by-Step Examples")
st.sidebar.markdown("---")
st.sidebar.markdown("**Prepared by:** Mr. Tarek")
st.sidebar.markdown("---")

st.write(
    "Welcome, students! Let's understand implicit differentiation step-by-step"
    " before moving to interactive modules."
)
st.markdown("---")

# Example 1
st.markdown("### Example 1: Basic Power & Chain Rule")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } x^3 + y^3 = 6xy")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Differentiate both sides with respect to $x$ term by term."
  )
  st.latex(r"\frac{d}{dx}(x^3) + \frac{d}{dx}(y^3) = \frac{d}{dx}(6xy)")

  st.write(
      "**Step 2:** Apply power rule and chain rule (remember that $\\frac{d}{dx}(y)"
      "= y'$)."
  )
  st.latex(r"3x^2 + 3y^2 \frac{dy}{dx} = 6(x \frac{dy}{dx} + y \cdot 1)")

  st.write(
      "**Step 3:** Group all terms containing $\\frac{dy}{dx}$ on one side."
  )
  st.latex(r"3y^2 \frac{dy}{dx} - 6x \frac{dy}{dx} = 6y - 3x^2")

  st.write("**Step 4:** Factor out $\\frac{dy}{dx}$ and solve.")
  st.latex(
      r"\frac{dy}{dx} (3y^2 - 6x) = 6y - 3x^2 \implies \frac{dy}{dx} ="
      r" \frac{2y - x^2}{y^2 - 2x}"
  )

# Example 2
st.markdown("### Example 2: Trigonometric Implicit Function")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } \sin(y) + x^2 = y")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Differentiate with respect to $x$ using the chain rule for"
      " $\\sin(y)$."
  )
  st.latex(r"\cos(y) \cdot \frac{dy}{dx} + 2x = \frac{dy}{dx}")

  st.write("**Step 2:** Rearrange terms to isolate $\\frac{dy}{dx}$.")
  st.latex(r"\cos(y) \frac{dy}{dx} - \frac{dy}{dx} = -2x")

  st.write("**Step 3:** Factor and isolate the derivative.")
  st.latex(
      r"\frac{dy}{dx} (\cos(y) - 1) = -2x \implies \frac{dy}{dx} ="
      r" \frac{-2x}{\cos(y) - 1}"
  )

# Example 3
st.markdown("### Example 3: Product Rule with Implicit Terms")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } x e^y + y e^x = 10")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Apply the product rule on both $x e^y$ and $y e^x$."
  )
  st.latex(
      r"(1 \cdot e^y + x e^y \frac{dy}{dx}) + (\frac{dy}{dx} e^x + y e^x) = 0"
  )

  st.write("**Step 2:** Collect $\\frac{dy}{dx}$ terms together.")
  st.latex(
      r"e^y \frac{dy}{dx} + e^x \frac{dy}{dx} = -e^y - y e^x \implies"
      r" \frac{dy}{dx}(x e^y + e^x) = -(e^y + y e^x)"
  )

  st.write("**Step 3:** Final expression for the derivative.")
  st.latex(r"\frac{dy}{dx} = \frac{-(e^y + y e^x)}{x e^y + e^x}")

# Example 4
st.markdown("### Example 4: Rational Implicit Expression")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } \frac{x}{y} = x + y")
with st.expander("Show Step-by-Step Solution"):
  st.write("**Step 1:** Rewrite as $x = y(x + y)$ or differentiate directly.")
  st.write(
      "Using quotient rule on left side: $\\frac{1 \cdot y - x \\frac{dy}{dx}}{y^2}"
      " = 1 + \\frac{dy}{dx}$"
  )

  st.write("**Step 2:** Clear the denominator by multiplying by $y^2$.")
  st.latex(r"y - x \frac{dy}{dx} = y^2 + y^2 \frac{dy}{dx}")

  st.write("**Step 3:** Group and solve for $\\frac{dy}{dx}$.")
  st.latex(
      r"\frac{dy}{dx} (-x - y^2) = y^2 - y \implies \frac{dy}{dx} ="
      r" \frac{y - y^2}{x + y^2}"
  )

# Example 5
st.markdown("### Example 5: Higher-Order Derivative Context")
st.latex(r"\text{Find } \frac{dy}{dx} \text{ for: } x^2 - xy + y^2 = 4")
with st.expander("Show Step-by-Step Solution"):
  st.write(
      "**Step 1:** Differentiate term by term (note product rule for $-xy$)."
  )
  st.latex(r"2x - (1 \cdot y + x \frac{dy}{dx}) + 2y \frac{dy}{dx} = 0")

  st.write("**Step 2:** Simplify and isolate derivative terms.")
  st.latex(r"2x - y - x \frac{dy}{dx} + 2y \frac{dy}{dx} = 0")
  st.latex(r"(2y - x) \frac{dy}{dx} = y - 2x")

  st.write("**Step 3:** Final derivative result.")
  st.latex(r"\frac{dy}{dx} = \frac{y - 2x}{2y - x}")

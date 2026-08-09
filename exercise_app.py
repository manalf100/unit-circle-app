import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعداد الصفحة وتنسيقها
st.set_page_config(page_title="STEM Math - Tarek Shawky", layout="wide")

st.title("🎯 Lesson 1: Six Trig Functions, Unit Circle & Triangle Relations")
st.markdown("### 👨‍🏫 Prepared by: Tarek Shawky")
st.markdown("---")

# ==========================================
# Part 1: Right-Angled Triangle & The Six Trig Functions
# ==========================================
st.header("📐 1. Right-Angled Triangle & The Six Trigonometric Functions")
st.markdown(r"Visualizing the right-angled triangle relations side-by-side with the formulas, connecting $\tan(\theta)$ directly to the **Slope** for STEM questions:")

# استخدام الأعمدة لعرض القوانين بجانب الرسمة مباشرة
col_text, col_plot = st.columns([1.2, 1])

with col_text:
    st.markdown(r"""
    * **$\sin(C) = \frac{\text{Opp}}{\text{Hyp}} = \frac{AB}{AC}$**
    * **$\cos(C) = \frac{\text{Adj}}{\text{Hyp}} = \frac{BC}{AC}$**
    * **$\tan(C) = \frac{\text{Opp}}{\text{Adj}} = \frac{AB}{BC}$** *(Slope / Gradient)*
    
    * **Reciprocals:**
      * $\csc(C) = \frac{1}{\sin(C)}$
      * $\sec(C) = \frac{1}{\cos(C)}$
      * $\cot(C) = \frac{1}{\tan(C)}$
    
    * **Complementary Relations:**
      * $\cos(A) = \sin(C)$
      * $\sin(A) = \cos(C)$
    """)

with col_plot:
    # رسم هندسي دقيق ومنسق للمثلث بجانب القوانين
    fig_tri, ax_tri = plt.subplots(figsize=(4.5, 3.8))
    # رأس القائمة B فوق، C تحت على اليسار، A على اليمين
    ax_tri.plot([0, 4, 0, 0], [0, 0, 3, 0], color='blue', linewidth=2.5)
    ax_tri.text(2, -0.35, 'Adjacent ($BC$)', fontsize=10, ha='center', fontweight='bold', color='darkblue')
    ax_tri.text(-0.45, 1.5, 'Opposite ($AB$)', fontsize=10, va='center', rotation=90, fontweight='bold', color='darkblue')
    ax_tri.text(2.1, 1.7, 'Hypotenuse ($AC$)', fontsize=10, color='red', rotation=37, fontweight='bold')
    ax_tri.text(0.15, 0.2, 'C', fontsize=12, fontweight='bold')
    ax_tri.text(3.7, 0.15, 'A', fontsize=12, fontweight='bold')
    ax_tri.text(0.15, 2.65, 'B', fontsize=12, fontweight='bold')
    ax_tri.set_xlim(-0.8, 4.5)
    ax_tri.set_ylim(-0.6, 3.5)
    ax_tri.axis('off')
    ax_tri.set_title("Right Triangle for Angle C", fontsize=11, fontweight='bold')
    st.pyplot(fig_tri)

st.markdown("---")

# ==========================================
# Part 2: Interactive Unit Circle Visualizer
# ==========================================
st.header("🔵 2. Interactive Unit Circle Visualizer")
st.markdown(r"Exploring coordinates on the Unit Circle where $x = \cos(\theta)$ and $y = \sin(\theta)$ (Identity: $x^2 + y^2 = 1$):")

angle_deg = st.slider("Select Angle (Degrees):", min_value=0, max_value=360, value=75, step=1)
angle_rad = np.radians(angle_deg)

fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.6)

circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2, label=r'Unit Circle ($x^2 + y^2 = 1$)')
ax.add_patch(circle)

x_val = np.cos(angle_rad)
y_val = np.sin(angle_rad)

ax.plot([0, x_val], [0, y_val], color='red', linewidth=2.5, label=f'Radius = 1 (Angle: {angle_deg}°)')
ax.scatter([x_val], [y_val], color='darkred', zorder=5)

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.legend(loc='upper right')
ax.set_title(f"Unit Circle: cos = {x_val:.3f}, sin = {y_val:.3f}")

st.pyplot(fig)

st.markdown(r"""
### 📊 Live Calculated Values for %d°:
* **$x$ ($\cos(\theta)$):** %.4f
* **$y$ ($\sin(\theta)$):** %.4f
* **Fundamental Identity ($x^2 + y^2 = 1$):** %.4f
* **Secant & Cosecant Identities:**
  * $\sec^2(\theta) = 1 + \tan^2(\theta)$
  * $\csc^2(\theta) = 1 + \cot^2(\theta)$
""" % (angle_deg, x_val, y_val, (x_val**2 + y_val**2)))

st.markdown("---")
st.success("Lesson 1 code is fully finalized, clean, and perfectly organized side-by-side.")

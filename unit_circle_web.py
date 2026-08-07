import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. إعدادات الصفحة المخصصة لشاشات الموبايل
st.set_page_config(
    page_title="Unit Circle - Mr. Tarek Shawky",
    page_icon="⭕",
    layout="centered"
)

# 2. الهيدر الرئيسي
st.title("⭕ STEM Interactive Unit Circle")
st.caption("Designed & Prepared by: **Mr. Tarek Shawky**")
st.markdown("---")

# 3. السلايدر التفاعلي للتحكم في الزاوية
angle_deg = st.slider("اختر الزاوية (θ) بالدرجات:", min_value=0.0, max_value=360.0, value=45.0, step=1.0)
rad = np.radians(angle_deg)
x, y = np.cos(rad), np.sin(rad)

# 4. رسم دائرة الوحدة والمثلث
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# رسم الدائرة والمحاور
theta_full = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(theta_full), np.sin(theta_full), color='gray', linestyle='--', linewidth=1.5)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# رسم المتجهات
ax.plot([0, x], [0, y], 'ro-', linewidth=2.5, label='Radius (r=1)')
ax.plot([x, x], [0, y], 'g-', linewidth=2.5, label=f'sin(θ) = {y:.3f}')
ax.plot([0, x], [0, 0], 'b-', linewidth=2.5, label=f'cos(θ) = {x:.3f}')
ax.plot(x, y, 'ro', markersize=8)

# ضبط حدود الرسمة
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_title(f"Angle θ = {angle_deg:.1f}°", fontsize=12, fontweight='bold', color='navy')
ax.legend(loc='upper right', fontsize=8)

# عرض الرسمة
st.pyplot(fig)

# 5. عرض القيم والنسب المثلثية
col1, col2 = st.columns(2)

with col1:
    st.subheader("📐 Trig Functions")
    st.write(f"**$\sin(\\theta)$** = `{y:.3f}`")
    st.write(f"**$\cos(\\theta)$** = `{x:.3f}`")
    
    tan_val = f"{y/x:.3f}" if abs(x) > 1e-4 else "Undefined"
    csc_val = f"{1/y:.3f}" if abs(y) > 1e-4 else "Undefined"
    sec_val = f"{1/x:.3f}" if abs(x) > 1e-4 else "Undefined"
    cot_val = f"{x/y:.3f}" if abs(y) > 1e-4 else "Undefined"
    
    st.write(f"**$\\tan(\\theta)$** = `{tan_val}`")
    st.write(f"**$\\csc(\\theta)$** = `{csc_val}`")
    st.write(f"**$\\sec(\\theta)$** = `{sec_val}`")
    st.write(f"**$\\cot(\\theta)$** = `{cot_val}`")

with col2:
    st.subheader("💡 Identities")
    sin2, cos2 = y**2, x**2
    st.info(f"""
    **$\sin^2(\\theta) + \cos^2(\\theta) = 1$**  
    `{sin2:.3f} + {cos2:.3f} = {sin2+cos2:.3f}`
    
    ---
    **$1 - \sin^2(\\theta) = \cos^2(\\theta)$**  
    `1 - {sin2:.3f} = {cos2:.3f}`
    
    ---
    **$1 - \cos^2(\\theta) = \sin^2(\\theta)$**  
    `1 - {cos2:.3f} = {sin2:.3f}`
    """)

st.caption("© STEM Mathematics Curriculum — Designed by Mr. Tarek Shawky")
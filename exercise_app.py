import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="STEM Unit Circle Master", layout="centered")

# Custom CSS to improve readability and font size
st.markdown("""
    <style>
    .main-title { font-size: 30px !important; font-weight: bold; color: #1f77b4; text-align: center; }
    .author-name { font-size: 22px !important; color: #555; text-align: center; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# Session state management
if 'page' not in st.session_state:
    st.session_state.page = "Lesson"

# Sidebar Navigation
st.sidebar.title("📌 التنقل في الدرس")
page_selection = st.sidebar.radio(
    "الانتقال السريع:",
    ["📘 1. الشرح والتفاعل", "🧬 2. استكشاف المتطابقات", "🎯 3. تمارين الفصل", "📝 4. الواجب المنزلي"]
)

# Logic to handle page navigation
if "1." in page_selection: st.session_state.page = "Lesson"
elif "2." in page_selection: st.session_state.page = "Identities"
elif "3." in page_selection: st.session_state.page = "Exercises"
else: st.session_state.page = "Homework"

# Title Section (Larger for better visibility)
st.markdown('<p class="main-title">⭕ STEM Unit Circle & Trig Functions</p>', unsafe_allow_html=True)
st.markdown('<p class="author-name">Designed & Prepared by: Mr. Tarek Shawky</p>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SECTION 1: INTERACTIVE LESSON
# ==========================================
if st.session_state.page == "Lesson":
    st.subheader("1. Interactive Angle Explorer")
    angle_deg = st.slider("اختر الزاوية بالدرجات (θ):", 0.0, 360.0, 45.0, 1.0)
    angle_rad = np.radians(angle_deg)
    
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    fig, ax = plt.subplots(figsize=(5, 5))
    circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    
    ax.plot([0, x], [0, y], color='red', linewidth=2.5, label='Radius (r=1)')
    ax.plot([x, x], [0, y], color='green', linewidth=2, label=f'sin(θ) = {y:.3f}')
    ax.plot([0, x], [0, 0], color='blue', linewidth=2, label=f'cos(θ) = {x:.3f}')
    ax.plot(x, y, 'ro')

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=8)
    st.pyplot(fig)

# ==========================================
# SECTION 2: IDENTITIES EXPLORER
# ==========================================
elif st.session_state.page == "Identities":
    st.title("🧬 استكشاف المتطابقات (Trig Identities)")
    st.write("هنا نرى كيف ترتبط الدوال المثلثية ببعضها هندسياً:")

    st.subheader("1. متطابقة فيثاغورس (Pythagorean Identity)")
    st.latex(r'''\sin^2(\theta) + \cos^2(\theta) = 1''')
    st.write("بما أن نصف قطر دائرة الوحدة هو 1، فإن المثلث القائم الذي ضلعه `x` (وهو `cos`) و `y` (وهو `sin`) يحقق نظرية فيثاغورس: $x^2 + y^2 = 1^2$")

    st.subheader("2. متطابقات النسب (Quotient & Reciprocal)")
    st.write("العلاقات الأساسية التي تربط الدوال:")
    
    data = {
        "المتطابقة": ["tan(θ)", "cot(θ)", "csc(θ)", "sec(θ)"],
        "القاعدة": ["sin(θ) / cos(θ)", "cos(θ) / sin(θ)", "1 / sin(θ)", "1 / cos(θ)"]
    }
    import pandas as pd
    st.table(pd.DataFrame(data))

# ==========================================
# SECTION 3: CLASS EXERCISES
# ==========================================
elif st.session_state.page == "Exercises":
    st.title("🎯 تمارين الفصل")
    mode = st.radio("وضع العرض:", ["Student Mode (وضع الطالب)", "Teacher Mode (وضع المعلم)"], horizontal=True)
    # (تم اختصار الكود هنا للحفاظ على المساحة، نفس منطق التمارين السابق)
    st.info("استخدم التمارين السابقة للتدريب...")

# ==========================================
# SECTION 4: HOMEWORK
# ==========================================
else:
    st.title("📝 الواجب المنزلي")
    # (تم اختصار الكود هنا للحفاظ على المساحة، نفس منطق الواجب السابق)
    st.info("حل الواجب المخصص...")

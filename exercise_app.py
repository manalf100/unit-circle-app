import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

st.markdown('<div class="portal-title">🏛️ STEM Mathematics Interactive Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="author-name">Designed & Prepared by: Mr. Tarek Shawky</div>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SIDEBAR: GRADE & SEMESTER NAVIGATION
# ==========================================
st.sidebar.title("📚 Academic Navigation")

grade = st.sidebar.selectbox("Select Grade:", ["Grade 10", "Grade 11", "Grade 12"])

if grade in ["Grade 10", "Grade 11"]:
    semester = st.sidebar.selectbox("Select Semester:", ["Semester 1", "Semester 2"])
else:
    semester = "Full Academic Year"
    st.sidebar.info("📌 Grade 12: Continuous Single-Year System")

st.sidebar.write("---")

# ==========================================
# MAIN PORTAL MODES SELECTION
# ==========================================
section_mode = st.sidebar.radio(
    "Portal Modes:",
    [
        "📘 Curriculum & Lessons",
        "🔗 Direct Share Link Generator",
        "🏆 Advanced Challenges (Top Students)",
        "📁 External / Extra PDF Bank"
    ]
)

st.sidebar.write("---")

# ----------------------------------------------------
# 1. CURRICULUM & LESSONS MODE
# ----------------------------------------------------
if section_mode == "📘 Curriculum & Lessons":
    lesson = st.sidebar.selectbox("Select Lesson / Topic:", [
        "1. Six Trigonometric Functions",
        "2. Unit Circle & Trig Ratios",
        "3. Related Angles & Rotation",
        "4. Law of Sine & Cosine",
        "5. Angles of Elevation & Depression",
        "🔥 Full Unit Revision Session"
    ])

    st.markdown(f"### 📌 Current Focus: {lesson}")

    if lesson == "1. Six Trigonometric Functions":
        st.markdown("### 📐 The Six Trigonometric Functions (Foundations)")
        st.write("دراسة وتريف الدوال المثلثية الست (Sine, Cosine, Tangent, Csec, Sec, Cot) في المثلثات القائمة والنسب الأساسية قبل الانتقال لدائرة الوحدة.")
        st.info("🎯 تمرين الكلاس: استنتاج النسب الست لمثلثات معلومة الأضلاع (STEM Rigor Drill).")

    elif lesson == "2. Unit Circle & Trig Ratios":
        st.markdown("### 📘 Interactive Unit Circle Explorer")
        angle_deg = st.slider("Select Angle (Degrees):", 0, 360, 45)
        rad = np.radians(angle_deg)
        x, y = np.cos(rad), np.sin(rad)

        col1, col2 = st.columns([2, 1])
        with col1:
            fig, ax = plt.subplots(figsize=(4, 4))
            circle = plt.Circle((0, 0), 1, fill=False, color='#94A3B8', linestyle='--', linewidth=1.5)
            ax.add_patch(circle)
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.plot([0, x], [0, y], color='#DC2626', linewidth=2, label='Radius = 1')
            ax.plot(x, y, 'ro', markersize=8)
            ax.set_xlim(-1.3, 1.3)
            ax.set_ylim(-1.3, 1.3)
            ax.set_aspect('equal')
            ax.grid(True, linestyle=':', alpha=0.6)
            st.pyplot(fig)

        with col2:
            st.metric("cos(θ)", f"{x:.3f}")
            st.metric("sin(θ)", f"{y:.3f}")

        st.write("---")
        st.markdown("#### 🎯 Class Exercises & Drills (STEM Rigor)")
        st.info("10 أسئلة تطبيقية مكثفة لربط إحداثيات دائرة الوحدة بالقيم المثلثية.")

    elif lesson == "🔥 Full Unit Revision Session":
        st.markdown("## ⚡ Full Unit Revision & Drill Session")
        st.warning("حصة مخصصة بالكامل لـ (حوالي 50 سؤال متنوع / SAT II & AP Style) لفرك أفكار الطلاب وتثبيت المنهج بالكامل!")

# ----------------------------------------------------
# 2. DIRECT SHARE LINK GENERATOR MODE
# ----------------------------------------------------
elif section_mode == "🔗 Direct Share Link Generator":
    st.markdown("### 🔗 Direct Share Link Generator")
    st.write("أداة سريعة لإنشاء وإرسال روابط مباشرة لأي طالب يسألك عن درس أو تمرين معين:")
    
    target_item = st.selectbox("Select Item to Share:", [
        "Lesson 1: Six Trig Functions",
        "Lesson 2: Unit Circle Interactive",
        "Full Revision Session Bank"
    ])
    
    if st.button("Generate Direct Link 🚀"):
        st.success("تم إنشاء الرابط بنجاح! يمكنك نسخه وإرساله للطالب مباشرة عبر واتساب:")
        st.code(f"https://stem-math-portal.streamlit.app/?target={target_item.replace(' ', '_')}", language="text")

# ----------------------------------------------------
# 3. ADVANCED CHALLENGES MODE (Top Students)
# ----------------------------------------------------
elif section_mode == "🏆 Advanced Challenges (Top Students)":
    st.markdown("### 🏆 Advanced Challenges (Very Excellent Students)")
    st.info("هذا القسم مخصص حصرياً للطلبة الفائقين جداً وأصحاب الأسئلة غير التقليدية (Out of the box).")
    
    st.markdown("#### 💡 Challenge Problem #1:")
    st.latex(r"\text{If } \sec(\theta) - \tan(\theta) = p, \text{ prove that } \csc(\theta) = \frac{1 + p^2}{1 - p^2}")
    
    with st.expander("🔍 عرض الحل النموذجي والتوضيح المتقدم"):
        st.success("الخطوات البرهانية الكاملة مع الشرح التحليلي للمتميزين متضمنة العلاقات الهامة بين القواطع والظل.")

# ----------------------------------------------------
# 4. EXTERNAL / EXTRA PDF BANK MODE
# ----------------------------------------------------
else:
    st.markdown("### 📁 External / Extra PDF Bank (شغل حر ووقت إضافي)")
    st.info("مكتبة أوراق العمل الإضافية وملفات الـ PDF الجاهزة للطباعة أو الاستخدام الفوري في أي وقت خارج الحصص الرسمية.")
    
    st.markdown("""
    * 📄 **Extra Worksheet 1:** Six Trig Functions Mastery (PDF) - [Download / Print]
    * 📄 **Extra Worksheet 2:** Unit Circle Advanced Problems (PDF) - [Download / Print]
    * 📄 **Extra Worksheet 3:** Exam Simulation Mock (PDF) - [Download / Print]
    """)

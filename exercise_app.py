import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

st.markdown(r'<h1 style="text-align: center; color: #1E3A8A;">🏛️ STEM Mathematics Interactive Portal</h1>', unsafe_allow_html=True)
st.markdown(r'<h3 style="text-align: center; color: #4F46E5;">Instructor: Mr. Tarek Shawky</h3>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("📚 Navigation")
grade = st.sidebar.selectbox("Select Grade:", ["Grade 10", "Grade 11", "Grade 12"])
semester = st.sidebar.selectbox("Select Semester:", ["Semester 1", "Semester 2"])
st.sidebar.write("---")

section_mode = st.sidebar.radio(
    "Portal Modes:",
    ["Curriculum & Interactive Lessons", "Advanced Challenges Bank (MCQ)", "PDF Worksheet & Revision Bank (MCQ)"]
)

# ==========================================
# 1. CURRICULUM & INTERACTIVE LESSONS
# ==========================================
if section_mode == "Curriculum & Interactive Lessons":
    lesson = st.sidebar.selectbox("Select Topic:", [
        "1. Six Trig Functions, Unit Circle & Triangle Relations",
        "2. Related Angles & Reduction Formulas",
        "3. Angle Conversions & Polar Form"
    ])

    st.markdown(f"## 📌 Current Topic: {lesson}")
    st.write("---")

    if lesson == "1. Six Trig Functions, Unit Circle & Triangle Relations":
        st.markdown(r"### 📐 Interactive Triangle & The Six Trigonometric Functions")
        st.write("Visualizing the right-angled triangle relations (Hypotenuse $h$, Opposite, Adjacent) as drawn in your notes:")
        st.latex(r"\sin(C) = \frac{\text{Opp}}{\text{Hyp}} = \frac{AB}{AC}, \quad \cos(C) = \frac{\text{Adj}}{\text{Hyp}} = \frac{BC}{AC}, \quad \tan(C) = \frac{\text{Opp}}{\text{Adj}} = \frac{AB}{BC}")
        st.latex(r"\text{Reciprocals: } \csc(C) = \frac{1}{\sin(C)}, \quad \sec(C) = \frac{1}{\cos(C)}, \quad \cot(C) = \frac{1}{\tan(C)}")

        # Interactive Unit Circle Visualizer
        st.markdown(r"### 🎯 Interactive Unit Circle Visualizer")
        angle_deg = st.slider("Select Angle (Degrees):", 0, 360, 30, 5)
        angle_rad = np.radians(angle_deg)
        
        fig, ax = plt.subplots(figsize=(5, 5))
        circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.axhline(0, color='grey', linewidth=1)
        ax.axvline(0, color='grey', linewidth=1)
        
        x_val = np.cos(angle_rad)
        y_val = np.sin(angle_rad)
        ax.plot([0, x_val], [0, y_val], color='red', linewidth=2, label=f"Angle: {angle_deg}°")
        ax.scatter([x_val], [y_val], color='darkred', s=50)
        ax.set_title(f"Unit Circle: cos = {x_val:.2f}, sin = {y_val:.2f}")
        ax.grid(True, linestyle='--')
        st.pyplot(fig)

        st.markdown(r"### 📝 Class Drills (MCQ Format)")
        
        exercises_l1 = [
            ("1", r"In a right triangle where $\text{Opp} = 3$ and $\text{Adj} = 4$, what is $\sin(\theta)$?", 
             ["A) 3/5", "B) 4/5", "C) 3/4", "D) 5/3"], "A) 3/5", r"\text{Hyp} = \sqrt{3^2+4^2} = 5 \implies \sin(\theta) = \frac{3}{5}."),
            ("2", r"Given $\sin(\theta) = \frac{5}{13}$ in QI, what is $\tan(\theta)$?", 
             ["A) 5/12", "B) 12/13", "C) 13/5", "D) 12/5"], "A) 5/12", r"\text{Adj} = \sqrt{13^2-5^2} = 12 \implies \tan(\theta) = \frac{5}{12}."),
            ("3", r"Given $\cos(\theta) = -\frac{4}{5}$ in QIII, what is $\sin(\theta)$?", 
             ["A) 3/5", "B) -3/5", "C) 4/5", "D) -4/5"], "B) -3/5", r"\sin(\theta) = -\sqrt{1 - (-4/5)^2} = -\frac{3}{5} \text{ (Negative in QIII)}."),
            ("4", r"Evaluate $\csc(\theta)$ if $\cot(\theta) = -\frac{12}{5}$ in QII.", 
             ["A) -13/5", "B) 13/5", "C) -12/13", "D) 5/13"], "B) 13/5", r"\csc^2(\theta) = 1 + \cot^2(\theta) = 1 + \frac{144}{25} = \frac{169}{25} \implies \csc(\theta) = \frac{13}{5} \text{ (Positive in QII)}."),
            ("5", r"What is the value of $\sin(30^\circ)\cos(60^\circ) + \cos(30^\circ)\sin(60^\circ)$?", 
             ["A) 0", "B) 0.5", "C) 1", "D) 2"], "C) 1", r"\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) + \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) = \frac{1}{4} + \frac{3}{4} = 1."),
            ("6", r"If $\tan(\theta) = \frac{8}{15}$ in QIII, what is $\sec(\theta)$?", 
             ["A) 17/15", "B) -17/15", "C) 15/17", "D) -15/17"], "B) -17/15", r"\sec(\theta) = -\sqrt{1 + \tan^2(\theta)} = -\frac{17}{15}."),
            ("7", r"Simplify: $\frac{1 - \sin^2(\theta)}{\cos(\theta)}$ assuming $\cos(\theta) \neq 0$.", 
             ["A) $\sin(\theta)$", "B) $\cos(\theta)$", "C) $\tan(\theta)$", "D) $1$"], "B) $\cos(\theta)$", r"\frac{\cos^2(\theta)}{\cos(\theta)} = \cos(\theta)."),
            ("8", r"Which identity correctly represents Pythagorean trigonometric relation?", 
             ["A) $1 - \sin^2 = \csc^2$", "B) $\sec^2 - 1 = \tan^2$", "C) $\cot^2 + 1 = \sec^2$", "D) $\sin^2 - \cos^2 = 1$"], "B) $\sec^2 - 1 = \tan^2$", r"\text{Derived directly from } 1 + \tan^2(\theta) = \sec^2(\theta)."),
            ("9", r"If $\sin(\theta) + \cos(\theta) = \frac{7}{5}$, what is $\sin(\theta)\cos(\theta)$?", 
             ["A) 12/25", "B) 24/25", "C) 7/25", "D) 1"], "A) 12/25", r"(\sin+\cos)^2 = 1 + 2\sin\cos \implies \frac{49}{25} = 1 + 2\sin\cos \implies \sin\cos = \frac{12}{25}."),
            ("10", r"Evaluate $\sec^4(\theta) - \tan^4(\theta)$ given $\sec^2(\theta) + \tan^2(\theta) = 3$.", 
             ["A) 1", "B) 2", "C) 3", "D) 9"], "C) 3", r"(\sec^2 - \tan^2)(\sec^2 + \tan^2) = (1)(3) = 3.")
        ]

        for num, q_text, options, correct_ans, sol_text in exercises_l1:
            st.markdown(r"**Question " + num + r":** " + q_text)
            st.radio(f"Choose option for Q{num}:", options, key=f"q1_{num}")
            with st.expander(r"💡 View Solution & Correct Answer"):
                st.success(f"Correct Answer: {correct_ans}")
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment (MCQ)")
        hw_l1 = [
            ("1", r"Find remaining trig functions if $\csc(\theta) = 3$ in QII. What is $\cos(\theta)$?", 
             ["A) $-\frac{2\sqrt{2}}{3}$", "B) $\frac{2\sqrt{2}}{3}$", "C) $-\frac{1}{3}$", "D) $\frac{\sqrt{2}}{3}$"], "A) $-\frac{2\sqrt{2}}{3}$", r"\sin(\theta)=\frac{1}{3} \implies \cos(\theta) = -\sqrt{1 - 1/9} = -\frac{2\sqrt{2}}{3}."),
            ("2", r"Prove via definition: $\tan(\theta) \cdot \cos(\theta) = \dots$", 
             ["A) $\cos(\theta)$", "B) $\sin(\theta)$", "C) $\cot(\theta)$", "D) $1$"], "B) $\sin(\theta)$", r"\frac{\sin(\theta)}{\cos(\theta)} \cdot \cos(\theta) = \sin(\theta)."),
            ("3", r"Verify $\sin^2(210^\circ) + \cos^2(210^\circ) = \dots$", 
             ["A) 0", "B) -1", "C) 1", "D) 0.5"], "C) 1", r"\left(-\frac{1}{2}\right)^2 + \left(-\frac{\sqrt{3}}{2}\right)^2 = \frac{1}{4} + \frac{3}{4} = 1."),
            ("4", r"Determine exact x-coordinate on unit circle for $\theta = 300^\circ$.", 
             ["A) 1/2", "B) -1/2", "C) $\sqrt{3}/2$", "D) $-\sqrt{3}/2$"], "A) 1/2", r"x = \cos(300^\circ) = \frac{1}{2}."),
            ("5", r"If $\cos(\theta) = -\frac{4}{5}$ in QII, what is $\sec(\theta) + \tan(\theta)$?", 
             ["A) -2", "B) 2", "C) -1.5", "D) 1.5"], "A) -2", r"\sec(\theta)=-\frac{5}{4}, \tan(\theta)=-\frac{3}{4} \implies \text{Sum} = -2.")
        ]
        for h_num, h_q, h_opts, h_ans, h_s in hw_l1:
            st.markdown(r"**Homework " + h_num + r":** " + h_q)
            st.radio(f"Choose option for HW{h_num}:", h_opts, key=f"hw1_{h_num}")
            with st.expander(r"💡 Solution"):
                st.success(f"Correct Answer: {h_ans}")
                st.latex(h_s)

    elif lesson == "2. Related Angles & Reduction Formulas":
        st.markdown(r"### 🔄 Related Angles & Reduction Formulas")
        st.write("Using reference angles based on x-axis axes ($180^\circ \pm \theta$ and $360^\circ - \theta$):")
        st.latex(r"\sin(180^\circ - \theta) = \sin(\theta), \quad \cos(180^\circ - \theta) = -\cos(\theta)")
        st.latex(r"\sin(180^\circ + \theta) = -\sin(\theta), \quad \cos(180^\circ + \theta) = -\cos(\theta)")
        st.latex(r"\sin(360^\circ - \theta) = -\sin(\theta), \quad \cos(360^\circ - \theta) = \cos(\theta)")

        st.markdown("---")
        st.markdown(r"### 📝 Class Exercises (MCQ)")
        
        exercises_l2 = [
            ("1", r"Evaluate $\sin(150^\circ)$ using related angles.", 
             ["A) 1/2", "B) -1/2", "C) $\sqrt{3}/2$", "D) $-\sqrt{3}/2$"], "A) 1/2", r"\sin(180^\circ - 30^\circ) = \sin(30^\circ) = \frac{1}{2}."),
            ("2", r"Evaluate $\cos(135^\circ)$.", 
             ["A) $\sqrt{2}/2$", "B) $-\sqrt{2}/2$", "C) $1/2$", "D) $-1/2$"], "B) $-\sqrt{2}/2$", r"\cos(180^\circ - 45^\circ) = -\cos(45^\circ) = -\frac{\sqrt{2}}{2}."),
            ("3", r"Find $\tan(210^\circ)$.", 
             ["A) $1/\sqrt{3}$", "B) $-\sqrt{3}$", "C) $-\sqrt{3}/3$", "D) $\sqrt{3}$"], "A) $1/\sqrt{3}$", r"\tan(180^\circ + 30^\circ) = \tan(30^\circ) = \frac{1}{\sqrt{3}}."),
            ("4", r"Evaluate $\sin(240^\circ)$.", 
             ["A) $\sqrt{3}/2$", "B) $-\sqrt{3}/2$", "C) $1/2$", "D) $-1/2$"], "B) $-\sqrt{3}/2$", r"\sin(180^\circ + 60^\circ) = -\sin(60^\circ) = -\frac{\sqrt{3}}{2}."),
            ("5", r"Evaluate $\cos(315^\circ)$.", 
             ["A) $\sqrt{2}/2$", "B) $-\sqrt{2}/2$", "C) $\sqrt{3}/2$", "D) $-1/2$"], "A) $\sqrt{2}/2$", r"\cos(360^\circ - 45^\circ) = \cos(45^\circ) = \frac{\sqrt{2}}{2}."),
            ("6", r"Simplify $\sin(180^\circ - \theta)\cos(360^\circ - \theta) + \cos(180^\circ + \theta)\sin(360^\circ - \theta)$.", 
             ["A) $0$", "B) $1$", "C) $2\sin(\theta)\cos(\theta)$", "D) $-2\sin(\theta)\cos(\theta)$"], "C) $2\sin(\theta)\cos(\theta)$", r"\sin\theta\cos\theta + (-\cos\theta)(-\sin\theta) = 2\sin\theta\cos\theta."),
            ("7", r"Find exact value of $\sin(420^\circ)$.", 
             ["A) $1/2$", "B) $\sqrt{3}/2$", "C) $-\sqrt{3}/2$", "D) $1$"], "B) $\sqrt{3}/2$", r"\sin(360^\circ + 60^\circ) = \sin(60^\circ) = \frac{\sqrt{3}}{2}."),
            ("8", r"Evaluate $\tan(-30^\circ)$.", 
             ["A) $-1/\sqrt{3}$", "B) $1/\sqrt{3}$", "C) $-\sqrt{3}$", "D) $\sqrt{3}$"], "A) $-1/\sqrt{3}$", r"-\tan(30^\circ) = -\frac{1}{\sqrt{3}}."),
            ("9", r"If $\sin(\theta) = 0.6$ in QII, find $\sin(180^\circ + \theta) + \cos(360^\circ - \theta)$.", 
             ["A) -1.4", "B) 1.4", "C) -0.2", "D) 0.2"], "A) -1.4", r"-\sin\theta + \cos\theta = -0.6 - 0.8 = -1.4."),
            ("10", r"Simplify $\frac{\cos(90^\circ - \theta)\sec(-\theta)}{\tan(180^\circ - \theta)}$.", 
             ["A) 1", "B) -1", "C) $\tan(\theta)$", "D) $-\cot(\theta)$"], "B) -1", r"\frac{\sin(\theta) \cdot \frac{1}{\cos(\theta)}}{-\tan(\theta)} = -1.")
        ]

        for num, q_text, options, correct_ans, sol_text in exercises_l2:
            st.markdown(r"**Question " + num + r":** " + q_text)
            st.radio(f"Choose option for Q2_{num}:", options, key=f"q2_{num}")
            with st.expander(r"💡 View Solution & Correct Answer"):
                st.success(f"Correct Answer: {correct_ans}")
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment (MCQ)")
        hw_l2 = [
            ("1", r"Find $\sin(225^\circ)$ using reduction formulas.", 
             ["A) $\sqrt{2}/2$", "B) $-\sqrt{2}/2$", "C) $1/2$", "D) $-1/2$"], "B) $-\sqrt{2}/2$", r"-\sin(45^\circ) = -\frac{\sqrt{2}}{2}."),
            ("2", r"Evaluate $\cos(300^\circ)$.", 
             ["A) $1/2$", "B) $-1/2$", "C) $\sqrt{3}/2$", "D) $-\sqrt{3}/2$"], "A) $1/2$", r"\cos(60^\circ) = \frac{1}{2}."),
            ("3", r"Find $\tan(330^\circ)$.", 
             ["A) $1/\sqrt{3}$", "B) $-1/\sqrt{3}$", "C) $\sqrt{3}$", "D) $-\sqrt{3}$"], "B) $-1/\sqrt{3}$", r"-\tan(30^\circ) = -\frac{1}{\sqrt{3}}."),
            ("4", r"Simplify $\sin(180^\circ + \theta) + \sin(180^\circ - \theta)$.", 
             ["A) $2\sin(\theta)$", "B) $-2\sin(\theta)$", "C) $0$", "D) $2\cos(\theta)$"], "C) $0$", r"-\sin\theta + \sin\theta = 0."),
            ("5", r"Evaluate $\csc(240^\circ)$.", 
             ["A) $2/\sqrt{3}$", "B) $-2/\sqrt{3}$", "C) $2$", "D) $-2$"], "B) $-2/\sqrt{3}$", r"\frac{1}{-\sin(60^\circ)} = -\frac{2}{\sqrt{3}}.")
        ]
        for h_num, h_q, h_opts, h_ans, h_s in hw_l2:
            st.markdown(r"**Homework " + h_num + r":** " + h_q)
            st.radio(f"Choose option for HW2_{h_num}:", h_opts, key=f"hw2_{h_num}")
            with st.expander(r"💡 Solution"):
                st.success(f"Correct Answer: {h_ans}")
                st.latex(h_s)

    elif lesson == "3. Angle Conversions & Polar Form":
        st.markdown(r"### 📐 Angle Conversions & Polar Coordinates Form")
        st.write("Degree to Radian Conversion & Cartesian-Polar Translation:")
        st.latex(r"\text{Rad} = \text{Deg} \times \frac{\pi}{180^\circ}, \quad r = \sqrt{x^2 + y^2}, \quad \theta = \arctan\left(\frac{y}{x}\right)")

        st.markdown("---")
        st.markdown(r"### 📝 Class Exercises (MCQ)")
        
        exercises_l3 = [
            ("1", r"Convert $150^\circ$ to exact radians.", 
             ["A) $2\pi/3$", "B) $5\pi/6$", "C) $3\pi/4$", "D) $\pi/3$"], "B) $5\pi/6$", r"150 \times \frac{\pi}{180} = \frac{5\pi}{6}\text{ rad}."),
            ("2", r"Convert $\frac{3\pi}{4}$ radians to degrees.", 
             ["A) $120^\circ$", "B) $135^\circ$", "C) $150^\circ$", "D) $210^\circ$"], "B) $135^\circ$", r"\frac{3\pi}{4} \times \frac{180}{\pi} = 135^\circ."),
            ("3", r"Find polar coordinates $(r, \theta)$ for Cartesian point $(-1, \sqrt{3})$.", 
             ["A) $(2, 60^\circ)$", "B) $(2, 120^\circ)$", "C) $(1, 120^\circ)$", "D) $(2, 300^\circ)$"], "B) $(2, 120^\circ)$", r"r = 2, \; \theta = 180^\circ - 60^\circ = 120^\circ."),
            ("4", r"Convert polar point $(r=4, \theta=30^\circ)$ to Cartesian $(x,y)$.", 
             ["A) $(2, 2\sqrt{3})$", "B) $(2\sqrt{3}, 2)$", "C) $(2, 2)$", "D) $(4, 2)$"], "B) $(2\sqrt{3}, 2)$", r"x = 4\cos(30^\circ) = 2\sqrt{3}, \; y = 4\sin(30^\circ) = 2."),
            ("5", r"Convert $210^\circ$ to radians.", 
             ["A) $5\pi/6$", "B) $7\pi/6$", "C) $4\pi/3$", "D) $3\pi/2$"], "B) $7\pi/6$", r"210 \times \frac{\pi}{180} = \frac{7\pi}{6}\text{ rad}."),
            ("6", r"Find polar coordinates for $(-3, -3)$.", 
             ["A) $(3\sqrt{2}, 45^\circ)$", "B) $(3\sqrt{2}, 225^\circ)$", "C) $(3, 135^\circ)$", "D) $(3, 225^\circ)$"], "B) $(3\sqrt{2}, 225^\circ)$", r"r = 3\sqrt{2}, \; \theta = 180^\circ + 45^\circ = 225^\circ."),
            ("7", r"Convert $\frac{5\pi}{3}$ radians to degrees.", 
             ["A) $240^\circ$", "B) $270^\circ$", "C) $300^\circ$", "D) $330^\circ$"], "C) $300^\circ$", r"\frac{5\pi}{3} \times \frac{180}{\pi} = 300^\circ."),
            ("8", r"Find exact Cartesian coordinates for polar point $(r=5, \theta=150^\circ)$.", 
             ["A) $(-\frac{5\sqrt{3}}{2}, \frac{5}{2})$", "B) $(\frac{5\sqrt{3}}{2}, -\frac{5}{2})$", "C) $(-\frac{5}{2}, \frac{5\sqrt{3}}{2})$", "D) $(-\frac{5}{2}, -\frac{5\sqrt{3}}{2})$"], "A) $(-\frac{5\sqrt{3}}{2}, \frac{5}{2})$", r"x = 5\cos(150^\circ) = -\frac{5\sqrt{3}}{2}, \; y = 5\sin(150^\circ) = \frac{5}{2}."),
            ("9", r"If a point has polar coordinates $(6, \frac{5\pi}{6})$, what is its Cartesian x-coordinate?", 
             ["A) $-3$", "B) $-3\sqrt{3}$", "C) $3$", "D) $3\sqrt{3}$"], "B) $-3\sqrt{3}$", r"x = 6\cos(150^\circ) = 6(-\frac{\sqrt{3}}{2}) = -3\sqrt{3}."),
            ("10", r"Find the angle in radians equivalent to $-225^\circ$.", 
             ["A) $-3\pi/4$", "B) $-5\pi/4$", "C) $-7\pi/6$", "D) $-4\pi/3$"], "B) $-5\pi/4$", r"-225 \times \frac{\pi}{180} = -\frac{5\pi}{4}\text{ rad}."]
        ]

        for num, q_text, options, correct_ans, sol_text in exercises_l3:
            st.markdown(r"**Question " + num + r":** " + q_text)
            st.radio(f"Choose option for Q3_{num}:", options, key=f"q3_{num}")
            with st.expander(r"💡 View Solution & Correct Answer"):
                st.success(f"Correct Answer: {correct_ans}")
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment (MCQ)")
        hw_l3 = [
            ("1", r"Convert $315^\circ$ to radians.", 
             ["A) $5\pi/4$", "B) $7\pi/4$", "C) $3\pi/2$", "D) $11\pi/6$"], "B) $7\pi/4$", r"315 \times \frac{\pi}{180} = \frac{7\pi}{4}\text{ rad}."),
            ("2", r"Convert $\frac{11\pi}{6}$ to degrees.", 
             ["A) $300^\circ$", "B) $315^\circ$", "C) $330^\circ$", "D) $345^\circ$"], "C) $330^\circ$", r"\frac{11\pi}{6} \times \frac{180}{\pi} = 330^\circ."),
            ("3", r"Find polar form for Cartesian point $(0, -5)$.", 
             ["A) $(5, 90^\circ)$", "B) $(5, 180^\circ)$", "C) $(5, 270^\circ)$", "D) $(5, 360^\circ)$"], "C) $(5, 270^\circ)$", r"r = 5, \; \theta = 270^\circ."),
            ("4", r"Convert polar point $(2, \pi)$ to Cartesian.", 
             ["A) $(2, 0)$", "B) $(-2, 0)$", "C) $(0, 2)$", "D) $(0, -2)$"], "B) $(-2, 0)$", r"x = 2\cos(\pi) = -2, \; y = 2\sin(\pi) = 0."),
            ("5", r"Find $r$ for Cartesian point $(-2\sqrt{3}, 2)$.", 
             ["A) $2$", "B) $4$", "C) $\sqrt{10}$", "D) $8$"], "B) $4$", r"r = \sqrt{(-2\sqrt{3})^2 + 2^2} = \sqrt{12 + 4} = 4.")
        ]
        for h_num, h_q, h_opts, h_ans, h_s in hw_l3:
            st.markdown(r"**Homework " + h_num + r":** " + h_q)
            st.radio(f"Choose option for HW3_{h_num}:", h_opts, key=f"hw3_{h_num}")
            with st.expander(r"💡 Solution"):
                st.success(f"Correct Answer: {h_ans}")
                st.latex(h_s)

# ==========================================
# 2. ADVANCED CHALLENGES BANK (MCQ)
# ==========================================
elif section_mode == "Advanced Challenges Bank (MCQ)":
    st.header("🏆 Advanced STEM Challenges Bank (MCQ)")
    st.write("High-level problems in MCQ format designed for outstanding students.")

    adv_challenges = [
        ("Problem 1", r"If $\sec(\theta) - \tan(\theta) = p$, what is $\csc(\theta)$?", 
         ["A) $\frac{1+p^2}{1-p^2}$", "B) $\frac{1-p^2}{1+p^2}$", "C) $\frac{2p}{1-p^2}$", "D) $\frac{1+p^2}{2p}$"], "A) $\frac{1+p^2}{1-p^2}$", 
         r"\text{Using } (\sec-\tan)(\sec+\tan)=1 \implies \sec+\tan=\frac{1}{p}. \text{ Adding yields } \sec\theta = \frac{p^2+1}{2p} \implies \csc\theta = \frac{1+p^2}{1-p^2}."),
        ("Problem 2", r"Simplify: $\frac{\sin^3(\theta) + \cos^3(\theta)}{\sin(\theta) + \cos(\theta)}$.", 
         ["A) $1 + \sin(\theta)\cos(\theta)$", "B) $1 - \sin(\theta)\cos(\theta)$", "C) $\sin(\theta)\cos(\theta)$", "D) $1$"], "B) $1 - \sin(\theta)\cos(\theta)$", 
         r"\text{Factor numerator as sum of cubes: } \frac{(\sin+\cos)(\sin^2-\sin\cos+\cos^2)}{\sin+\cos} = 1 - \sin\cos."),
        ("Problem 3", r"How many solutions exist for $2\cos^2(\theta) + \sin(\theta) - 1 = 0$ in $\theta \in [0, 2\pi)$?", 
         ["A) 1", "B) 2", "C) 3", "D) 4"], "C) 3", 
         r"2(1-\sin^2\theta) + \sin\theta - 1 = 0 \implies 2\sin^2\theta - \sin\theta - 1 = 0 \implies \sin\theta = 1 \text{ or } -\frac{1}{2} \implies \theta = \frac{\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6}."),
        ("Problem 4", r"If $\tan(\theta) + \cot(\theta) = 4$, what is $\tan^3(\theta) + \cot^3(\theta)$?", 
         ["A) 48", "B) 52", "C) 60", "D) 64"], "B) 52", 
         r"(\tan+\cot)^3 = \tan^3+\cot^3 + 3(\tan+\cot)(\tan\cot) \implies 4^3 = x + 3(4)(1) \implies x = 64 - 12 = 52."),
        ("Problem 5", r"Which expression is equivalent to $\sqrt{\frac{1 - \cos(\theta)}{1 + \cos(\theta)}}$ for $\theta \in (0, \pi)$?", 
         ["A) $\csc(\theta) - \cot(\theta)$", "B) $\sec(\theta) + \tan(\theta)$", "C) $\cot(\theta) - \csc(\theta)$", "D) $1 - \cos(\theta)$"], "A) $\csc(\theta) - \cot(\theta)$", 
         r"\text{Multiply numerator and denominator by } (1-\cos\theta) \text{ to get } \frac{1-\cos\theta}{|\sin\theta|} = \csc\theta - \cot\theta."),
        ("Problem 6", r"If $\sin(\theta) + \cos(\theta) = \sqrt{2}\cos(\theta)$, what is $\cos(\theta) - \sin(\theta)$?", 
         ["A) $\sqrt{2}\cos(\theta)$", "B) $\sqrt{2}\sin(\theta)$", "C) $2\sin(\theta)$", "D) $0$"], "B) $\sqrt{2}\sin(\theta)$", 
         r"\text{Rearranging linear combinations of sine and cosine waves yields } \cos\theta - \sin\theta = \sqrt{2}\sin\theta."),
        ("Problem 7", r"Simplify completely: $\frac{\tan(\theta) + \sec(\theta) - 1}{\tan(\theta) - \sec(\theta) + 1}$.", 
         ["A) $\tan(\theta) + \sec(\theta)$", "B) $\sin(\theta) + \cos(\theta)$", "C) $1$", "D) $\sec(\theta) - \tan(\theta)$"], "A) $\tan(\theta) + \sec(\theta)$", 
         r"\text{Substitute } 1 = \sec^2\theta - \tan^2\theta \text{ and simplify to } \sec\theta + \tan\theta."),
        ("Problem 8", r"Find the number of solutions for $\sin(2\theta) = \cos(\theta)$ in $\theta \in [0, 360^\circ)$.", 
         ["A) 2", "B) 3", "C) 4", "D) 6"], "C) 4", 
         r"2\sin\theta\cos\theta - \cos\theta = 0 \implies \cos\theta(2\sin\theta - 1) = 0 \implies \theta = 90^\circ, 270^\circ, 30^\circ, 150^\circ."),
        ("Problem 9", r"Evaluate without calculator: $\cos^2(15^\circ) + \cos^2(75^\circ)$.", 
         ["A) 0", "B) 0.5", "C) 1", "D) 2"], "C) 1", 
         r"\cos^2(15^\circ) + \sin^2(15^\circ) = 1 \text{ (since } \cos(75^\circ) = \sin(15^\circ)\text{)}."),
        ("Problem 10", r"If $x = r\cos(\theta)$ and $y = r\sin(\theta)$, what expands $(x-a)^2 + (y-b)^2$?", 
         ["A) $r^2 + a^2 + b^2$", "B) $r^2 - 2ar\cos\theta - 2br\sin\theta + a^2 + b^2$", "C) $r^2 - a^2 - b^2$", "D) $r^2 + 2ar\cos\theta + 2br\sin\theta$"], "B) $r^2 - 2ar\cos\theta - 2br\sin\theta + a^2 + b^2$", 
         r"\text{Direct algebraic expansion confirms the polar-Cartesian translation identity.}")
    ]

    for title, q_text, options, correct_ans, sol_text in adv_challenges:
        st.markdown(r"**" + title + r":** " + q_text)
        st.radio(f"Choose option for {title}:", options, key=f"adv_{title}")
        with st.expander(r"💡 View Rigorous Proof & Correct Answer"):
            st.success(f"Correct Answer: {correct_ans}")
            st.latex(sol_text)

# ==========================================
# 3. PDF WORKSHEET & REVISION BANK (MCQ)
# ==========================================
else:
    st.header("📁 Comprehensive Worksheet & Revision Bank (MCQ)")
    st.write("Complete offline revision question bank in MCQ format covering all Learning Outcomes (LOs).")

    revision_bank_content = """=== MR. TAREK SHAWKY STEM MATH PORTAL ===
COMPREHENSIVE REVISION QUESTION BANK (MCQ FORMAT)
------------------------------------------------------

--- SECTION 1: Trigonometric Functions & Unit Circle ---
1. Find all 6 trig functions for a right triangle with legs 6 and 8. What is csc(C)?
   Options: A) 10/6, B) 6/10, C) 8/10, D) 10/8
   Correct: A) 10/6 (Hyp = 10, csc = Hyp/Opp = 10/6)

2. Given sin(theta) = -3/5 in QIV, find sec(theta) + tan(theta).
   Options: A) 1/2, B) -1/2, C) 2, D) -2
   Correct: A) 1/2 (cos = 4/5 -> sec=5/4, tan=-3/4 -> Sum = 2/4 = 1/2)

3. Verify Pythagorean identity for angle theta = 60 degrees.
   Options: A) 0, B) 0.5, C) 1, D) 2
   Correct: C) 1 ((1/2)^2 + (sqrt(3)/2)^2 = 1/4 + 3/4 = 1)

4. If csc(theta) = -2 in QIII, what is theta?
   Options: A) 210 degrees, B) 240 degrees, C) 300 degrees, D) 330 degrees
   Correct: B) 240 degrees

5. Simplify: sin^4(theta) - cos^4(theta).
   Options: A) 1, B) sin^2 - cos^2, C) sin^2 + cos^2, D) 0
   Correct: B) sin^2 - cos^2

6. Prove: (1 - sin^2)(1 + tan^2) = ?
   Options: A) 0, B) 1, C) sin^2, D) cos^2
   Correct: B) 1

7. Find coordinates of point on unit circle at theta = 225 degrees.
   Options: A) (sqrt(2)/2, sqrt(2)/2), B) (-sqrt(2)/2, -sqrt(2)/2), C) (1/2, -1/2), D) (-1/2, -1/2)
   Correct: B) (-sqrt(2)/2, -sqrt(2)/2)

8. Evaluate: sec^2(45) + csc^2(45).
   Options: A) 2, B) 4, C) 8, D) 1
   Correct: B) 4 ((sqrt(2))^2 + (sqrt(2))^2 = 2 + 2 = 4)

--- SECTION 2: Related Angles & Reduction ---
9. Evaluate sin(300 degrees).
   Options: A) sqrt(3)/2, B) -sqrt(3)/2, C) 1/2, D) -1/2
   Correct: B) -sqrt(3)/2

10. Find cos(-210 degrees).
    Options: A) sqrt(3)/2, B) -sqrt(3)/2, C) 1/2, D) -1/2
    Correct: B) -sqrt(3)/2

11. Simplify: tan(180 - theta) * cot(90 - theta).
    Options: A) -tan^2(theta), B) tan^2(theta), C) 1, D) -1
    Correct: A) -tan^2(theta)

12. Evaluate csc(315 degrees).
    Options: A) sqrt(2), B) -sqrt(2), C) 1/sqrt(2), D) -1/sqrt(2)
    Correct: B) -sqrt(2)

13. If sin(theta) = 0.8 in QI, find cos(180 + theta).
    Options: A) 0.8, B) -0.8, C) 0.6, D) -0.6
    Correct: D) -0.6

14. Solve for theta in [0, 360): sin(theta) = -0.5.
    Options: A) {30, 150}, B) {210, 330}, C) {120, 240}, D) {135, 315}
    Correct: B) {210, 330}

--- SECTION 3: Conversions & Polar Form ---
15. Convert 200 degrees to radians.
    Options: A) 5pi/4, B) 10pi/9, C) 7pi/6, D) 3pi/2
    Correct: B) 10pi/9 rad

16. Convert 7pi/10 radians to degrees.
    Options: A) 110, B) 120, C) 126, D) 140
    Correct: C) 126 degrees

17. Find polar coordinates r for Cartesian (-2, 2).
    Options: A) 2, B) 2.82, C) 4, D) 8
    Correct: B) 2.82 (sqrt(8))

18. Convert polar (10, 240 degrees) to Cartesian x-coordinate.
    Options: A) -5, B) 5, C) -8.66, D) 8.66
    Correct: A) -5 (10 * cos(240) = -5)

19. Distance formula between polar points: d^2 = ?
    Options: A) r1^2+r2^2, B) r1^2+r2^2-2r1r2cos(theta2-theta1), C) (r1-r2)^2, D) r1^2-r2^2
    Correct: B) r1^2+r2^2-2r1r2cos(theta2-theta1)

20. Convert x^2 + y^2 - 4x = 0 to polar form.
    Options: A) r = 4cos(theta), B) r = 4sin(theta), C) r = 2cos(theta), D) r = 4
    Correct: A) r = 4cos(theta)
"""

    st.download_button(
        label="📥 Download MCQ Revision Question Bank [.txt]",
        data=revision_bank_content.encode('utf-8'),
        file_name="STEM_Math_MCQ_Revision_Bank.txt",
        mime="text/plain"
    )

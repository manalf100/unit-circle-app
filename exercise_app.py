import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="STEM Math Portal - Mr. Tarek Shawky", layout="centered")

st.markdown(r'<h1 style="text-align: center; color: #1E3A8A;">🏛️ STEM Mathematics Interactive Portal</h1>', unsafe_allow_html=True)
st.markdown(r'<h3 style="text-align: center; color: #4F46E5;">Instructor: Mr. Tarek Shawky</h3>', unsafe_allow_html=True)
st.write("---")

# ==========================================
# SIDEBAR NAVIGATION (Protected for Teacher)
# ==========================================
st.sidebar.title("📚 Navigation")
grade = st.sidebar.selectbox("Select Grade:", ["Grade 10", "Grade 11", "Grade 12"])
semester = st.sidebar.selectbox("Select Semester:", ["Semester 1", "Semester 2"])
st.sidebar.write("---")

section_mode = st.sidebar.radio(
    "Portal Modes:",
    ["Curriculum & Lessons", "Advanced Challenges Bank", "PDF Worksheet & Revision Bank"]
)

# ==========================================
# 1. CURRICULUM & LESSONS MODE
# ==========================================
if section_mode == "Curriculum & Lessons":
    lesson = st.sidebar.selectbox("Select Topic:", [
        "1. Six Trig Functions, Unit Circle & Identities",
        "2. Related Angles & Reduction Formulas",
        "3. Angle Conversions & Polar Form"
    ])

    st.markdown(f"## 📌 Current Topic: {lesson}")
    st.write("---")

    if lesson == "1. Six Trig Functions, Unit Circle & Identities":
        st.markdown(r"### 📐 Part A: The Six Trigonometric Functions & Right Triangles")
        st.write("In a right-angled triangle (Hypotenuse $h$, Opposite, Adjacent):")
        st.latex(r"\sin(C) = \frac{\text{Opp}}{\text{Hyp}} = \frac{AB}{AC}, \quad \cos(C) = \frac{\text{Adj}}{\text{Hyp}} = \frac{BC}{AC}, \quad \tan(C) = \frac{\text{Opp}}{\text{Adj}} = \frac{AB}{BC}")
        st.write("Reciprocal Trigonometric Functions:")
        st.latex(r"\csc(C) = \frac{1}{\sin(C)}, \quad \sec(C) = \frac{1}{\cos(C)}, \quad \cot(C) = \frac{1}{\tan(C)}")

        st.markdown(r"### 📘 Part B: The Unit Circle & Fundamental Identities")
        st.write("On the unit circle ($r = 1$), any point on the circumference satisfies:")
        st.latex(r"x = \cos(\theta), \quad y = \sin(\theta)")
        st.latex(r"\text{Pythagorean Identity: } \sin^2(\theta) + \cos^2(\theta) = 1")
        st.latex(r"\sec^2(\theta) = \tan^2(\theta) + 1, \quad \csc^2(\theta) = \cot^2(\theta) + 1")

        st.markdown("---")
        st.markdown(r"### 📝 Class Drills & Exercises")
        
        exercises_l1 = [
            ("1", r"In a right triangle where $\text{Opp} = 3$ and $\text{Adj} = 4$, find $\sin(\theta)$ and $\cos(\theta)$.", r"\text{Hyp} = 5, \quad \sin(\theta) = \frac{3}{5}, \quad \cos(\theta) = \frac{4}{5}"),
            ("2", r"Given $\sin(\theta) = \frac{5}{13}$ in QI, find $\tan(\theta)$ and $\sec(\theta)$.", r"\text{Adj} = 12, \quad \tan(\theta) = \frac{5}{12}, \quad \sec(\theta) = \frac{13}{12}"),
            ("3", r"Given $\cos(\theta) = -\frac{4}{5}$ in QIII, evaluate $\sin(\theta)$ and $\tan(\theta)$.", r"\sin(\theta) = -\frac{3}{5}, \quad \tan(\theta) = \frac{3}{4}"),
            ("4", r"Evaluate $\csc(\theta)$ if $\cot(\theta) = -\frac{12}{5}$ in QII.", r"\csc(\theta) = \frac{13}{5} \text{ (Positive in QII)}"),
            ("5", r"Find the value of $\sin(30^\circ)\cos(60^\circ) + \cos(30^\circ)\sin(60^\circ)$.", r"\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) + \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) = 1"),
            ("6", r"If $\tan(\theta) = \frac{8}{15}$ in QIII, evaluate $\csc(\theta) + \sec(\theta)$.", r"\csc(\theta) = -\frac{17}{8}, \, \sec(\theta) = -\frac{17}{15} \implies \text{Sum} = -\frac{391}{120}"),
            ("7", r"Simplify: $\frac{1 - \sin^2(\theta)}{\cos(\theta)}$ assuming $\cos(\theta) \neq 0$.", r"\frac{\cos^2(\theta)}{\cos(\theta)} = \cos(\theta)"),
            ("8", r"Prove the identity: $\sec^2(\theta) - 1 = \tan^2(\theta)$.", r"\text{From } 1 + \tan^2(\theta) = \sec^2(\theta) \implies \text{Result follows directly.}"),
            ("9", r"If $\sin(\theta) + \cos(\theta) = \frac{7}{5}$, find $\sin(\theta)\cos(\theta)$.", r"(\sin+\cos)^2 = 1 + 2\sin\cos \implies \frac{49}{25} = 1 + 2\sin\cos \implies \sin\cos = \frac{12}{25}"),
            ("10", r"Evaluate $\sec^4(\theta) - \tan^4(\theta)$ given $\sec^2(\theta) + \tan^2(\theta) = 3$.", r"(\sec^2 - \tan^2)(\sec^2 + \tan^2) = (1)(3) = 3")
        ]

        for num, q_text, sol_text in exercises_l1:
            st.markdown(r"**Question " + num + r":** " + q_text)
            with st.expander(r"💡 View Solution for Question " + num):
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment")
        hw_l1 = [
            ("1", r"Find remaining trig functions if $\csc(\theta) = 3$ in QII.", r"\sin(\theta)=\frac{1}{3}, \cos(\theta)=-\frac{2\sqrt{2}}{3}, \tan(\theta)=-\frac{\sqrt{2}}{4}"),
            ("2", r"Prove that $\tan(\theta) \cdot \cos(\theta) = \sin(\theta)$ using definitions.", r"\frac{\sin}{\cos} \cdot \cos = \sin \quad \checkmark"),
            ("3", r"Verify $\sin^2(210^\circ) + \cos^2(210^\circ) = 1$.", r"\left(-\frac{1}{2}\right)^2 + \left(-\frac{\sqrt{3}}{2}\right)^2 = \frac{1}{4} + \frac{3}{4} = 1"),
            ("4", r"Determine exact coordinates on unit circle for $\theta = 300^\circ$.", r"x = \frac{1}{2}, \; y = -\frac{\sqrt{3}}{2}"),
            ("5", r"If $\cos(\theta) = -\frac{4}{5}$ and $\theta$ in QII, find $\sec(\theta) + \tan(\theta)$.", r"\sec(\theta)=-\frac{5}{4}, \tan(\theta)=-\frac{3}{4} \implies \text{Sum} = -2")
        ]
        for h_num, h_q, h_s in hw_l1:
            st.markdown(r"**Homework " + h_num + r":** " + h_q)
            with st.expander(r"💡 Solution for Homework " + h_num):
                st.latex(h_s)

    elif lesson == "2. Related Angles & Reduction Formulas":
        st.markdown(r"### 🔄 Related Angles & Reduction Formulas")
        st.write("Using reference angles based on x-axis axes ($180^\circ \pm \theta$ and $360^\circ - \theta$):")
        st.latex(r"\sin(180^\circ - \theta) = \sin(\theta), \quad \cos(180^\circ - \theta) = -\cos(\theta)")
        st.latex(r"\sin(180^\circ + \theta) = -\sin(\theta), \quad \cos(180^\circ + \theta) = -\cos(\theta)")
        st.latex(r"\sin(360^\circ - \theta) = -\sin(\theta), \quad \cos(360^\circ - \theta) = \cos(\theta)")

        st.markdown("---")
        st.markdown(r"### 📝 Class Exercises")
        
        exercises_l2 = [
            ("1", r"Evaluate $\sin(150^\circ)$ using related angles.", r"\sin(180^\circ - 30^\circ) = \sin(30^\circ) = \frac{1}{2}"),
            ("2", r"Evaluate $\cos(135^\circ)$.", r"\cos(180^\circ - 45^\circ) = -\cos(45^\circ) = -\frac{\sqrt{2}}{2}"),
            ("3", r"Find $\tan(210^\circ)$.", r"\tan(180^\circ + 30^\circ) = \tan(30^\circ) = \frac{1}{\sqrt{3}}"),
            ("4", r"Evaluate $\sin(240^\circ)$.", r"\sin(180^\circ + 60^\circ) = -\sin(60^\circ) = -\frac{\sqrt{3}}{2}"),
            ("5", r"Evaluate $\cos(315^\circ)$.", r"\cos(360^\circ - 45^\circ) = \cos(45^\circ) = \frac{\sqrt{2}}{2}"),
            ("6", r"Simplify $\sin(180^\circ - \theta)\cos(360^\circ - \theta) + \cos(180^\circ + \theta)\sin(360^\circ - \theta).$", r"\sin(\theta)\cos(\theta) + (-\cos(\theta))(-\sin(\theta)) = 2\sin(\theta)\cos(\theta)"),
            ("7", r"Find exact value of $\sin(420^\circ)$.", r"\sin(360^\circ + 60^\circ) = \sin(60^\circ) = \frac{\sqrt{3}}{2}"),
            ("8", r"Evaluate $\tan(-30^\circ)$.", r"-\tan(30^\circ) = -\frac{1}{\sqrt{3}}"),
            ("9", r"If $\sin(\theta) = 0.6$ in QII, find $\sin(180^\circ + \theta) + \cos(360^\circ - \theta)$.", r"-\sin(\theta) + \cos(\theta) = -0.6 - 0.8 = -1.4"),
            ("10", r"Simplify $\frac{\cos(90^\circ - \theta)\sec(-\theta)}{\tan(180^\circ - \theta)}.$", r"\frac{\sin(\theta) \cdot \frac{1}{\cos(\theta)}}{-\tan(\theta)} = -1")
        ]

        for num, q_text, sol_text in exercises_l2:
            st.markdown(r"**Question " + num + r":** " + q_text)
            with st.expander(r"💡 View Solution for Question " + num):
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment")
        hw_l2 = [
            ("1", r"Find $\sin(225^\circ)$ using reduction formulas.", r"-\sin(45^\circ) = -\frac{\sqrt{2}}{2}"),
            ("2", r"Evaluate $\cos(300^\circ)$.", r"\cos(60^\circ) = \frac{1}{2}"),
            ("3", r"Find $\tan(330^\circ)$.", r"-\tan(30^\circ) = -\frac{1}{\sqrt{3}}"),
            ("4", r"Simplify $\sin(180^\circ + \theta) + \sin(180^\circ - \theta)$.", r"-\sin\theta + \sin\theta = 0"),
            ("5", r"Evaluate $\csc(240^\circ)$.", r"\frac{1}{-\sin(60^\circ)} = -\frac{2}{\sqrt{3}}")
        ]
        for h_num, h_q, h_s in hw_l2:
            st.markdown(r"**Homework " + h_num + r":** " + h_q)
            with st.expander(r"💡 Solution for Homework " + h_num):
                st.latex(h_s)

    elif lesson == "3. Angle Conversions & Polar Form":
        st.markdown(r"### 📐 Angle Conversions & Polar Coordinates Form")
        st.write("Degree to Radian Conversion:")
        st.latex(r"180^\circ = \pi \text{ rad} \implies \text{Rad} = \text{Deg} \times \frac{\pi}{180^\circ}")
        st.write("Polar Form vs Cartesian Form:")
        st.latex(r"r = \sqrt{x^2 + y^2}, \quad \theta = \arctan\left(\frac{y}{x}\right)")
        st.latex(r"x = r\cos(\theta), \quad y = r\sin(\theta)")

        st.markdown("---")
        st.markdown(r"### 📝 Class Exercises")
        
        exercises_l3 = [
            ("1", r"Convert $150^\circ$ to exact radians.", r"150 \times \frac{\pi}{180} = \frac{5\pi}{6}\text{ rad}"),
            ("2", r"Convert $\frac{3\pi}{4}$ radians to degrees.", r"\frac{3\pi}{4} \times \frac{180}{\pi} = 135^\circ"),
            ("3", r"Find polar coordinates $(r, \theta)$ for Cartesian point $(-1, \sqrt{3})$.", r"r = 2, \; \theta = 120^\circ \text{ (QII)}"),
            ("4", r"Convert polar point $(r=4, \theta=30^\circ)$ to Cartesian $(x,y)$.", r"x = 4\cos(30^\circ) = 2\sqrt{3}, \; y = 4\sin(30^\circ) = 2"),
            ("5", r"Convert $210^\circ$ to radians.", r"\frac{7\pi}{6}\text{ rad}"),
            ("6", r"Find polar coordinates for $(-3, -3)$.", r"r = 3\sqrt{2}, \; \theta = 225^\circ"),
            ("7", r"Convert $\frac{5\pi}{3}$ radians to degrees.", r"300^\circ"),
            ("8", r"Find exact Cartesian coordinates for polar point $(r=5, \theta=150^\circ)$.", r"x = -\frac{5\sqrt{3}}{2}, \; y = \frac{5}{2}"),
            ("9", r"If a point has polar coordinates $(6, \frac{5\pi}{6})$, find its Cartesian form.", r"x = -3\sqrt{3}, \; y = 3"),
            ("10", r"Find the angle in radians equivalent to $-225^\circ$.", r"-\frac{5\pi}{4}\text{ rad}")
        ]

        for num, q_text, sol_text in exercises_l3:
            st.markdown(r"**Question " + num + r":** " + q_text)
            with st.expander(r"💡 View Solution for Question " + num):
                st.latex(sol_text)

        st.markdown("---")
        st.markdown("### 🏠 Homework Assignment")
        hw_l3 = [
            ("1", r"Convert $315^\circ$ to radians.", r"\frac{7\pi}{4}\text{ rad}"),
            ("2", r"Convert $\frac{11\pi}{6}$ to degrees.", r"330^\circ"),
            ("3", r"Find polar form for $(0, -5)$.", r"r = 5, \; \theta = 270^\circ"),
            ("4", r"Convert polar point $(2, \pi)$ to Cartesian.", r"x = -2, \; y = 0"),
            ("5", r"Find $r$ and $\theta$ for $(-2\sqrt{3}, 2)$.", r"r = 4, \; \theta = 150^\circ")
        ]
        for h_num, h_q, h_s in hw_l3:
            st.markdown(r"**Homework " + h_num + r":** " + h_q)
            with st.expander(r"💡 Solution for Homework " + h_num):
                st.latex(h_s)

# ==========================================
# 2. ADVANCED CHALLENGES BANK
# ==========================================
elif section_mode == "Advanced Challenges Bank":
    st.header("🏆 Advanced STEM Challenges Bank")
    st.write("Exclusive high-level problem bank designed for outstanding students.")

    adv_challenges = [
        ("Problem 1", r"If $\sec(\theta) - \tan(\theta) = p$, prove that $\csc(\theta) = \frac{1 + p^2}{1 - p^2}$.", 
         r"\text{Using } (\sec-\tan)(\sec+\tan)=1 \implies \sec+\tan=\frac{1}{p}. \text{ Adding yields } \sec\theta = \frac{p^2+1}{2p} \implies \csc\theta = \frac{1+p^2}{1-p^2}."),
        ("Problem 2", r"Prove the identity: $\frac{\sin^3(\theta) + \cos^3(\theta)}{\sin(\theta) + \cos(\theta)} = 1 - \sin(\theta)\cos(\theta)$.", 
         r"\text{Factor numerator as sum of cubes: } \frac{(\sin+\cos)(\sin^2-\sin\cos+\cos^2)}{\sin+\cos} = 1 - \sin\cos."),
        ("Problem 3", r"Solve for $\theta \in [0, 2\pi)$: $2\cos^2(\theta) + \sin(\theta) - 1 = 0$.", 
         r"2(1-\sin^2\theta) + \sin\theta - 1 = 0 \implies 2\sin^2\theta - \sin\theta - 1 = 0 \implies \sin\theta = 1 \text{ or } -\frac{1}{2} \implies \theta = \frac{\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6}."),
        ("Problem 4", r"If $\tan(\theta) + \cot(\theta) = 4$, find $\tan^3(\theta) + \cot^3(\theta)$.", 
         r"(\tan+\cot)^3 = \tan^3+\cot^3 + 3(\tan+\cot)(\tan\cot) \implies 4^3 = x + 3(4)(1) \implies x = 64 - 12 = 52."),
        ("Problem 5", r"Prove: $\sqrt{\frac{1 - \cos(\theta)}{1 + \cos(\theta)}} = |\csc(\theta) - \cot(\theta)|$ for $\theta \neq n\pi$.", 
         r"\text{Multiply numerator and denominator by } (1-\cos\theta) \text{ to get } \frac{1-\cos\theta}{|\sin\theta|} = |\csc\theta - \cot\theta|."),
        ("Problem 6", r"If $\sin(\theta) + \cos(\theta) = \sqrt{2}\cos(\theta)$, prove that $\cos(\theta) - \sin(\theta) = \sqrt{2}\sin(\theta)$.", 
         r"\text{Square both sides or use linear combinations of sine and cosine waves.}"),
        ("Problem 7", r"Simplify completely: $\frac{\tan(\theta) + \sec(\theta) - 1}{\tan(\theta) - \sec(\theta) + 1}$.", 
         r"\text{Substitute } 1 = \sec^2\theta - \tan^2\theta \text{ and simplify to } \frac{1+\sin\theta}{\cos\theta} = \sec\theta + \tan\theta."),
        ("Problem 8", r"Find all values of $\theta \in [0, 360^\circ)$ where $\sin(2\theta) = \cos(\theta)$.", 
         r"2\sin\theta\cos\theta - \cos\theta = 0 \implies \cos\theta(2\sin\theta - 1) = 0 \implies \theta = 90^\circ, 270^\circ, 30^\circ, 150^\circ."),
        ("Problem 9", r"Evaluate without calculator: $\cos^2(15^\circ) + \cos^2(75^\circ)$.", 
         r"\cos^2(15^\circ) + \sin^2(15^\circ) = 1 \text{ (since } \cos(75^\circ) = \sin(15^\circ)\text{)}."),
        ("Problem 10", r"If $x = r\cos(\theta)$ and $y = r\sin(\theta)$, prove that $(x-a)^2 + (y-b)^2 = r^2 - 2ar\cos\theta - 2br\sin\theta + a^2 + b^2$.", 
         r"\text{Direct algebraic expansion confirms the polar-Cartesian translation identity.}")
    ]

    for title, q_text, sol_text in adv_challenges:
        st.markdown(r"**" + title + r":** " + q_text)
        with st.expander(r"💡 View Rigorous Proof / Solution"):
            st.latex(sol_text)

# ==========================================
# 3. PDF WORKSHEET & REVISION BANK
# ==========================================
else:
    st.header("📁 Comprehensive Worksheet & Revision Bank")
    st.write("Complete offline revision question bank covering all Learning Outcomes (LOs) with full step-by-step solutions.")

    revision_bank_content = """=== MR. TAREK SHAWKY STEM MATH PORTAL ===
COMPREHENSIVE REVISION QUESTION BANK
------------------------------------------------------

--- SECTION 1: Trigonometric Functions & Unit Circle ---
1. Find all 6 trig functions for a right triangle with legs 6 and 8.
   Solution: Hyp = 10, sin=6/10, cos=8/10, tan=6/8, csc=10/6, sec=10/8, cot=8/6.
2. Given sin(theta) = -3/5 in QIV, find sec(theta) + tan(theta).
   Solution: cos(theta) = 4/5 -> sec=5/4, tan=-3/4 -> Sum = 2/4 = 1/2.
3. Verify Pythagorean identity for angle theta = 60 degrees.
   Solution: (1/2)^2 + (sqrt(3)/2)^2 = 1/4 + 3/4 = 1.
4. If csc(theta) = -2 in QIII, find exact angle and other functions.
   Solution: theta = 240 degrees, cos = -1/2, sin = -1/2, etc.
5. Simplify: sin^4(theta) - cos^4(theta).
   Solution: (sin^2 - cos^2)(sin^2 + cos^2) = sin^2 - cos^2 = 2sin^2 - 1.
6. Prove: (1 - sin^2)(1 + tan^2) = 1.
   Solution: cos^2 * sec^2 = cos^2 * (1/cos^2) = 1.
7. Find coordinates of point on unit circle at theta = 225 degrees.
   Solution: (-sqrt(2)/2, -sqrt(2)/2).
8. Evaluate: sec^2(45^\circ) + csc^2(45^\circ).
   Solution: (sqrt(2))^2 + (sqrt(2))^2 = 2 + 2 = 4.

--- SECTION 2: Related Angles & Reduction ---
9. Evaluate sin(300 degrees).
   Solution: -sin(60) = -sqrt(3)/2.
10. Find cos(-210 degrees).
    Solution: cos(150 degrees) = -sqrt(3)/2.
11. Simplify: tan(180 - theta) * cot(90 - theta).
    Solution: (-tan theta) * (tan theta) = -tan^2 theta.
12. Evaluate csc(315 degrees).
    Solution: -sqrt(2).
13. If sin(theta) = 0.8 in QI, find sin(180 - theta) and cos(180 + theta).
    Solution: sin = 0.8, cos = -0.6.
14. Solve for theta in [0, 360): sin(theta) = -0.5.
    Solution: 210 degrees, 330 degrees.

--- SECTION 3: Conversions & Polar Form ---
15. Convert 200 degrees to radians.
    Solution: 10pi / 9 rad.
16. Convert 7pi/10 radians to degrees.
    Solution: 126 degrees.
17. Find polar coordinates for Cartesian (-2, 2).
    Solution: r = 2.82, theta = 135 degrees.
18. Convert polar (10, 240 degrees) to Cartesian.
    Solution: x = -5, y = -5.83.
19. Find distance between two polar points (r1, theta1) and (r2, theta2) using law of cosines.
    Solution: d = sqrt(r1^2 + r2^2 - 2r1r2 cos(theta2 - theta1)).
20. Advanced Polar conversion test: Convert x^2 + y^2 - 4x = 0 to polar form.
    Solution: r = 4 cos(theta).
"""

    st.download_button(
        label="📥 Download Complete Revision Question Bank [.txt]",
        data=revision_bank_content.encode('utf-8'),
        file_name="STEM_Math_Comprehensive_Revision_Bank.txt",
        mime="text/plain"
    )

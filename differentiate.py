import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# تعريف الأمثلة الخمسة مع تعديل الرموز لنقطتين (:) بدلاً من الأسهم
examples = [
    {
        "title": "Example 1: Addition & Subtraction (Circle)",
        "expr": "x^2 + y^2 = 25",
        "type": "circle",
        "steps": [
            "Step 1: Identify equation : x^2 + y^2 = 25",
            "Step 2: Differentiate w.r.t x : d/dx(x^2) + d/dx(y^2) = 0",
            "Step 3: Apply Chain Rule : 2x + 2y * (dy/dx) = 0",
            "Step 4: Solve for dy/dx : dy/dx = -x / y"
        ]
    },
    {
        "title": "Example 2: Multiplication (Product Rule)",
        "expr": "x * y = 6",
        "type": "text",
        "steps": [
            "Step 1: Given equation : x * y = 6",
            "Step 2: Apply Product Rule : (d/dx[x])*y + x*(d/dx[y]) = 0",
            "Step 3: Evaluate derivatives : 1*y + x * (dy/dx) = 0",
            "Step 4: Solve for dy/dx : dy/dx = -y / x"
        ]
    },
    {
        "title": "Example 3: Division (Quotient Rule)",
        "expr": "x / y = 4",
        "type": "text",
        "steps": [
            "Step 1: Given equation : x / y = 4 (or x = 4y)",
            "Step 2: Differentiate both sides : d/dx[x] = d/dx[4y]",
            "Step 3: Apply derivative : 1 = 4 * (dy/dx)",
            "Step 4: Solve for dy/dx : dy/dx = 1 / 4"
        ]
    },
    {
        "title": "Example 4: Natural Logarithm (ln)",
        "expr": "ln(y) + x = 5",
        "type": "text",
        "steps": [
            "Step 1: Given equation : ln(y) + x = 5",
            "Step 2: Differentiate w.r.t x : d/dx[ln(y)] + d/dx[x] = 0",
            "Step 3: Apply Chain Rule for ln : (1/y) * (dy/dx) + 1 = 0",
            "Step 4: Solve for dy/dx : dy/dx = -y"
        ]
    },
    {
        "title": "Example 5: Exponential (x * e^y = 10)",
        "expr": "x * e^y = 10",
        "type": "text",
        "steps": [
            "Step 1: Given equation : x * e^y = 10",
            "Step 2: Apply Product Rule : (d/dx[x])*e^y + x*(d/dx[e^y]) = 0",
            "Step 3: Evaluate : 1*e^y + x * e^y * (dy/dx) = 0",
            "Step 4: Solve for dy/dx : dy/dx = -1 / x"
        ]
    }
]

current_ex_idx = 0
current_step_idx = 0

# إعداد الرسمة والشاشة
fig, ax = plt.subplots(figsize=(9, 8))
plt.subplots_adjust(left=0.1, bottom=0.32, right=0.9, top=0.85)

# بيانات الدائرة للمثال الأول
theta_vals = np.linspace(0, 2 * np.pi, 400)
X_circle = 5 * np.cos(theta_vals)
Y_circle = 5 * np.sin(theta_vals)

line_circle, = ax.plot(X_circle, Y_circle, color='blue', linewidth=2)
point, = ax.plot([], [], 'ro', markersize=8)
tangent_line, = ax.plot([], [], color='red', linestyle='--', linewidth=2)

# عناصر التحكم (السلايدر)
ax_slider = plt.axes([0.15, 0.22, 0.7, 0.03])
slider = Slider(ax_slider, 'Point Position', 0, 2 * np.pi, valinit=0.7)

def update_slider(val):
    if current_ex_idx == 0:
        angle = slider.val
        px = 5 * np.cos(angle)
        py = 5 * np.sin(angle)
        point.set_data([px], [py])
        slope = -px / py if py != 0 else float('inf')
        x_tan = np.linspace(px - 2, px + 2, 100)
        y_tan = slope * (x_tan - px) + py
        tangent_line.set_data(x_tan, y_tan)
        fig.canvas.draw_idle()

slider.on_changed(update_slider)

# مربعات النصوص والعنوان
title_text = ax.text(0.5, 0.92, "", transform=ax.transAxes, fontsize=13, fontweight='bold', ha='center', color='navy')
step_box = ax.text(0.05, 0.83, "", transform=ax.transAxes, fontsize=9.5, 
                   verticalalignment='top', linespacing=1.6,
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, pad=0.8))

def update_display():
    ex = examples[current_ex_idx]
    title_text.set_text(f"{ex['title']}\nEquation : {ex['expr']}")
    visible_steps = ex['steps'][:current_step_idx+1]
    step_box.set_text("\n\n".join(visible_steps) if visible_steps else "Press 'Next Step'...")
    
    if ex['type'] == 'circle':
        line_circle.set_visible(True)
        point.set_visible(True)
        tangent_line.set_visible(True)
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax_slider.set_visible(True)
        slider.ax.set_visible(True)
        update_slider(slider.val)
    else:
        line_circle.set_visible(False)
        point.set_visible(False)
        tangent_line.set_visible(False)
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.grid(False)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.set_xticks([])
        ax.set_yticks([])
        ax_slider.set_visible(False)
        slider.ax.set_visible(False)
        
    fig.canvas.draw_idle()

# أزرار التنقل
ax_btn_step = plt.axes([0.35, 0.14, 0.3, 0.06])
btn_step = Button(ax_btn_step, 'Next Step', color='lightgoldenrodyellow', hovercolor='0.9')

ax_btn_next_ex = plt.axes([0.35, 0.05, 0.3, 0.06])
btn_next_ex = Button(ax_btn_next_ex, 'Next Example (1/5)', color='lightblue', hovercolor='0.9')

def on_next_step(event):
    global current_step_idx
    ex = examples[current_ex_idx]
    if current_step_idx < len(ex['steps']) - 1:
        current_step_idx += 1
    else:
        current_step_idx = 0
    update_display()

def on_next_example(event):
    global current_ex_idx, current_step_idx
    current_ex_idx = (current_ex_idx + 1) % len(examples)
    current_step_idx = 0
    btn_next_ex.label.set_text(f'Next Example ({current_ex_idx+1}/5)')
    update_display()

btn_step.on_clicked(on_next_step)
btn_next_ex.on_clicked(on_next_example)

update_display()
plt.show()

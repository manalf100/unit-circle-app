import tkinter as tk
from tkinter import messagebox
import csv
import datetime

# 15 سؤالاً حقيقياً من امتحانات المدارس المتقدمة والأنظمة العالمية للـ STEM (Implicit Differentiation)
homework_questions = [
    {
        "q": "1. If x^2 + y^2 = 25, find the value of dy/dx at the point (3, 4).",
        "options": ["-3/4", "-4/3", "3/4", "4/3"],
        "answer": "-3/4"
    },
    {
        "q": "2. Find dy/dx for the curve x^3 + y^3 = 6xy.",
        "options": ["(2y - x^2)/(y^2 - 2x)", "(2x - y^2)/(x^2 - 2y)", "(y - x^2)/(y^2 - x)", "(x^2 - y)/(x - y^2)"],
        "answer": "(2y - x^2)/(y^2 - 2x)"
    },
    {
        "q": "3. If sin(x + y) = y cos(x), what is dy/dx?",
        "options": [
            "(y sin(x) + cos(x+y)) / (cos(x+y) - cos(x))",
            "(cos(x+y) - y sin(x)) / (cos(x) - cos(x+y))",
            "sin(x+y) / cos(x)",
            "y cos(x) / sin(x)"
        ],
        "answer": "(cos(x+y) - y sin(x)) / (cos(x) - cos(x+y))"
    },
    {
        "q": "4. Find the slope of the tangent line to x^y = y^x at the point (1, 1).",
        "options": ["0", "1", "-1", "Undefined"],
        "answer": "1"
    },
    {
        "q": "5. Given ln(xy) + x + y = 5, find dy/dx in terms of x and y.",
        "options": ["-y(1+x)/(x(1+y))", "-(1+x)/(1+y)", "x/y", "-y/x"],
        "answer": "-y(1+x)/(x(1+y))"
    },
    {
        "q": "6. Find dy/dx for the exponential implicit relation e^(xy) + x^2 - y^2 = 10.",
        "options": [
            "(2x + y e^(xy)) / (2y - x e^(xy))",
            "(-2x - y e^(xy)) / (2y - x e^(xy))",
            "(2x - y e^(xy)) / (2y + x e^(xy))",
            "(y e^(xy) - 2x) / (2y + x e^(xy))"
        ],
        "answer": "(-2x - y e^(xy)) / (2y - x e^(xy))"
    },
    {
        "q": "7. If x^2 + y^2 = 25, find the second derivative d^2y/dx^2 at the point (3, 4).",
        "options": ["-25/16", "-25/64", "5/4", "-16/25"],
        "answer": "-25/64"
    },
    {
        "q": "8. Find the slope of the tangent to the curve tan(y) = x y at the origin (0, 0).",
        "options": ["0", "1", "-1", "Infinity"],
        "answer": "0"
    },
    {
        "q": "9. If (x - y)/(x + y) = x/2, find the derivative dy/dx.",
        "options": ["(x - 2y)/x", "(2x - y)/x", "(y - 2x)/x", "(x + 2y)/x"],
        "answer": "(y - 2x)/x"
    },
    {
        "q": "10. For the relation x^3 y^3 - y = x, evaluate dy/dx.",
        "options": [
            "(1 + 3x^2 y^3) / (3x^3 y^2 - 1)",
            "(1 - 3x^2 y^3) / (3x^3 y^2 - 1)",
            "(3x^2 y^3 - 1) / (1 - 3x^3 y^2)",
            "(1 + 3x^2 y^3) / (1 - 3x^3 y^2)"
        ],
        "answer": "(1 - 3x^2 y^3) / (3x^3 y^2 - 1)"
    },
    {
        "q": "11. If x^4 + y^4 = 17, find dy/dx at the point (1, 2).",
        "options": ["-1/8", "-1/2", "1/8", "1/2"],
        "answer": "-1/8"
    },
    {
        "q": "12. Find dy/dx if x^3 + 3xy + y^3 = 5.",
        "options": [
            "-(x^2 + y) / (x + y^2)",
            "(x^2 + y) / (x + y^2)",
            "-(x + y^2) / (x^2 + y)",
            "(x + y^2) / (x^2 + y)"
        ],
        "answer": "-(x^2 + y) / (x + y^2)"
    },
    {
        "q": "13. Given y = sin(xy), find the expression for dy/dx.",
        "options": [
            "y cos(xy) / (1 - x cos(xy))",
            "-y cos(xy) / (1 - x cos(xy))",
            "x cos(xy) / (1 - y cos(xy))",
            "1 / (1 - xy)"
        ],
        "answer": "y cos(xy) / (1 - x cos(xy))"
    },
    {
        "q": "14. If x^2 y + y^2 x = 6, find the value of dy/dx at the point (2, 1).",
        "options": ["-4/5", "-5/4", "4/5", "5/4"],
        "answer": "-5/4"
    },
    {
        "q": "15. Find dy/dx for the curve sqrt(x) + sqrt(y) = 5 at the point (9, 16).",
        "options": ["-4/3", "-3/4", "4/3", "3/4"],
        "answer": "-4/3"
    }
]

class HomeworkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MR/Tarek Shawky")
        self.root.geometry("750x580")
        
        self.current_q = 0
        self.student_name = ""
        self.user_answers = [None] * len(homework_questions)
        
        self.create_name_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_name_screen(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)
        
        tk.Label(frame, text="STEM Grade 12 - Assessment", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(frame, text="Please enter your full name to start the exam:", font=("Arial", 12)).pack(pady=5)
        
        self.name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=10)
        
        btn = tk.Button(frame, text="Start Assessment", font=("Arial", 12), command=self.start_quiz)
        btn.pack(pady=10)

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Name is required to proceed!")
            return
        self.student_name = name
        self.show_question()

    def show_question(self):
        self.clear_window()
        
        q_data = homework_questions[self.current_q]
        
        top_frame = tk.Frame(self.root, padx=10, pady=10)
        top_frame.pack(fill="x")
        
        tk.Label(top_frame, text=f"Student: {self.student_name}", font=("Arial", 10, "bold")).pack(side="left")
        tk.Label(top_frame, text=f"Question {self.current_q + 1} of {len(homework_questions)}", font=("Arial", 10, "bold")).pack(side="right")
        
        q_frame = tk.Frame(self.root, padx=20, pady=10)
        q_frame.pack(fill="both", expand=True)
        
        tk.Label(q_frame, text=q_data["q"], font=("Arial", 12, "bold"), wraplength=700, justify="left").pack(anchor="w", pady=10)
        
        self.selected_option = tk.StringVar()
        if self.user_answers[self.current_q] is not None:
            self.selected_option.set(self.user_answers[self.current_q])
            
        for opt in q_data["options"]:
            rb = tk.Radiobutton(q_frame, text=opt, variable=self.selected_option, value=opt, font=("Arial", 11), anchor="w")
            rb.pack(anchor="w", pady=6)
            
        nav_frame = tk.Frame(self.root, padx=20, pady=15)
        nav_frame.pack(fill="x")
        
        if self.current_q > 0:
            tk.Button(nav_frame, text="Previous", font=("Arial", 11), width=10, command=self.prev_question).pack(side="left")
            
        if self.current_q < len(homework_questions) - 1:
            tk.Button(nav_frame, text="Next", font=("Arial", 11), width=10, command=self.next_question).pack(side="right")
        else:
            tk.Button(nav_frame, text="Submit", font=("Arial", 11, "bold"), width=12, command=self.submit_quiz).pack(side="right")

    def save_answer(self):
        self.user_answers[self.current_q] = self.selected_option.get()

    def next_question(self):
        self.save_answer()
        self.current_q += 1
        self.show_question()

    def prev_question(self):
        self.save_answer()
        self.current_q -= 1
        self.show_question()

    def submit_quiz(self):
        self.save_answer()
        
        score = 0
        for i, q in enumerate(homework_questions):
            if self.user_answers[i] == q["answer"]:
                score += 1
                
        filename = f"exam_results_{self.student_name.replace(' ', '_')}.csv"
        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Student Name", "Date/Time", "Score", f"Out of {len(homework_questions)}"])
                writer.writerow([self.student_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), score, len(homework_questions)])
                writer.writerow([])
                writer.writerow(["Q#", "Selected Answer", "Correct Answer", "Result"])
                for i, q in enumerate(homework_questions):
                    user_ans = self.user_answers[i] if self.user_answers[i] else "No Answer"
                    correct_ans = q["answer"]
                    res = "Correct" if user_ans == correct_ans else "Incorrect"
                    writer.writerow([i+1, user_ans, correct_ans, res])
        except Exception as e:
            print("Error saving file:", e)
            
        self.clear_window()
        
        result_frame = tk.Frame(self.root, padx=20, pady=20)
        result_frame.pack(expand=True)
        
        tk.Label(result_frame, text="Exam Submitted Successfully!", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(result_frame, text=f"Student: {self.student_name}", font=("Arial", 12)).pack(pady=5)
        tk.Label(result_frame, text=f"Final Score: {score} / {len(homework_questions)}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(result_frame, text=f"Results saved securely to: '{filename}'", font=("Arial", 10)).pack(pady=5)
        
        tk.Button(result_frame, text="Close", font=("Arial", 12), width=15, command=self.root.destroy).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeworkApp(root)
    root.mainloop()
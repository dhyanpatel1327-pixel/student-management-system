import tkinter as tk
from tkinter import messagebox, ttk

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()
    
    if name == "" or roll == "" or marks == "":
        messagebox.showerror("Error", "Sabhi fields bharo!")
        return
    
    marks = float(marks)
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 45:
        grade = "C"
    else:
        grade = "Fail"
    
    students.append({"name": name, "roll": roll, "marks": marks, "grade": grade})
    table.insert("", "end", values=(roll, name, marks, grade))
    
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"{name} add ho gaya! Grade: {grade}")

def delete_student():
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error", "Pehle ek student select karo!")
        return
    table.delete(selected)
    messagebox.showinfo("Deleted", "Student delete ho gaya!")

def show_topper():
    if len(students) == 0:
        messagebox.showerror("Error", "Koi student nahi hai!")
        return
    topper = max(students, key=lambda x: x["marks"])
    messagebox.showinfo("🏆 Topper", f"Name: {topper['name']}\nMarks: {topper['marks']}\nGrade: {topper['grade']}")

# Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")
root.configure(bg="#1e1e2e")

# Title
tk.Label(root, text="Student Management System", font=("Arial", 18, "bold"),
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

tk.Label(frame, text="Name:", bg="#1e1e2e", fg="white").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, width=20)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Roll No:", bg="#1e1e2e", fg="white").grid(row=1, column=0, padx=5, pady=5)
roll_entry = tk.Entry(frame, width=20)
roll_entry.grid(row=1, column=1, padx=5)

tk.Label(frame, text="Marks:", bg="#1e1e2e", fg="white").grid(row=2, column=0, padx=5, pady=5)
marks_entry = tk.Entry(frame, width=20)
marks_entry.grid(row=2, column=1, padx=5)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Student", bg="#a6e3a1", fg="black",
          command=add_student, width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Delete Student", bg="#f38ba8", fg="black",
          command=delete_student, width=15).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Show Topper 🏆", bg="#fab387", fg="black",
          command=show_topper, width=15).grid(row=0, column=2, padx=10)

# Table
cols = ("Roll", "Name", "Marks", "Grade")
table = ttk.Treeview(root, columns=cols, show="headings", height=10)
for col in cols:
    table.heading(col, text=col)
    table.column(col, width=130)
table.pack(pady=10)

root.mainloop()

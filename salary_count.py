import tkinter as tk
from tkinter import messagebox

def calculate_new_salary():
    try:
        current_salary = float(entry_salary.get())
        percentage_hike = float(entry_percentage.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numerical values for salary and percentage.")
        return

    if current_salary < 0 or percentage_hike < 0:
        messagebox.showerror("Error", "Salary and percentage hike should be non-negative.")
        return

    new_salary = current_salary + (current_salary * (percentage_hike / 100))
    result_text = f"Your new salary after a {percentage_hike}% hike will be: {new_salary}"
    messagebox.showinfo("Result", result_text)

# Create main window
app = tk.Tk()
app.title("Salary Calculator")

# Set the window size and position it at (20, 20) with padding
app.geometry("400x250+20+20")

# Add a background color
app.configure(bg="#f0f0f0")

# Create and place widgets with some styling
label_salary = tk.Label(app, text="Enter your current salary:", font=("Helvetica", 12), bg="#f0f0f0")
label_salary.pack()

entry_salary = tk.Entry(app, font=("Helvetica", 12))
entry_salary.pack()

label_percentage = tk.Label(app, text="Enter the percentage hike:", font=("Helvetica", 12), bg="#f0f0f0")
label_percentage.pack()

entry_percentage = tk.Entry(app, font=("Helvetica", 12))
entry_percentage.pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate_new_salary, font=("Helvetica", 12), bg="#4CAF50", fg="white")
calculate_button.pack()

# Start the main event loop
app.mainloop()

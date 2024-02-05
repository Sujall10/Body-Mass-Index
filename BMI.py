import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        messagebox.showinfo("BMI Result", "Your BMI is: {:.2f}".format(bmi))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

def set_widget_style(widget, style_name):
    style = ThemedStyle(root)
    style.set_theme(theme_name="plastik")
    style.configure(style_name, padding=6, relief="flat", background="#4CAF50", foreground="black")
    widget.configure(style=style_name)

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
root.configure(bg="#EFEFEF")

label_weight = tk.Label(root, text="Enter Weight (kg):", bg="#EFEFEF")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

label_height = tk.Label(root, text="Enter Height (m):", bg="#EFEFEF")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=20)
set_widget_style(calculate_button, "TButton")

root.mainloop()

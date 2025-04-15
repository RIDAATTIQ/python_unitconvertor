import tkinter as tk

def km_to_miles():
    try:
        km = float(entry.get())
        miles = km * 0.621371
        result_label.config(text=f"{km} km = {miles:.2f} miles")
    except ValueError:
        result_label.config(text="❌ Please enter a valid number")

def c_to_f():
    try:
        c = float(entry.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"{c}°C = {f:.2f}°F")
    except ValueError:
        result_label.config(text="❌ Please enter a valid number")

def f_to_c():
    try:
        f = float(entry.get())
        c = (f - 32) * 5/9
        result_label.config(text=f"{f}°F = {c:.2f}°C")
    except ValueError:
        result_label.config(text="❌ Please enter a valid number")

# 🪄 GUI setup
root = tk.Tk()
root.title("Unit Converter 💫")
root.geometry("400x300")
root.configure(bg="#f2f2f2")  # light background

title_label = tk.Label(root, text="✨ Unit Converter ✨", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333")
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
entry.pack(pady=10)

# 💡 Buttons
btn_km = tk.Button(root, text="Kilometers to Miles", font=("Helvetica", 12), command=km_to_miles, bg="#add8e6", width=25)
btn_km.pack(pady=5)

btn_c = tk.Button(root, text="Celsius to Fahrenheit", font=("Helvetica", 12), command=c_to_f, bg="#90ee90", width=25)
btn_c.pack(pady=5)

btn_f = tk.Button(root, text="Fahrenheit to Celsius", font=("Helvetica", 12), command=f_to_c, bg="#ffb6c1", width=25)
btn_f.pack(pady=5)

# ✅ Result
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f2f2f2", fg="#444")
result_label.pack(pady=20)

root.mainloop()

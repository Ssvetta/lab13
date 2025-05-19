import tkinter as tk
from tkinter import messagebox
import math

def calculate_sum():
    try:
        x = float(entry_x.get())
        result = 0
        for k in range(1, 10):  # Сумуємо від k=1 до 9
            term = (math.sin(2 * k * x) + 0.2) / (2 * k + 5)
            result += term
        label_result.config(text=f"Результат: {result:.4f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть дійсне число для x.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Виникла помилка: {e}")

root = tk.Tk()
root.title("Обчислення суми (Варіант 5)")
root.geometry("300x150")

label_x = tk.Label(root, text="Введіть значення x:")
label_x.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

button_calculate = tk.Button(root, text="Обчислити суму", command=calculate_sum)
button_calculate.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

label_result = tk.Label(root, text="Результат:")
label_result.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.grid_columnconfigure(1, weight=1)#великий стовпець

root.mainloop()

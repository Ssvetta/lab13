import tkinter as tk
from math import sqrt, tan
def calculate_function(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        ctg_c = 1 / tan(c)
        result = ctg_c + sqrt(c / b + a)

        label_result.config(text=f"Результат: {result:.4f}")
    except Exception as e:
        label_result.config(text=f"Помилка: {e}")

root = tk.Tk()
root.title("Обчислення функції")
root.geometry("450x400")
root.configure(bg="#f2f2f2")

# Фото
photo = tk.PhotoImage(file="лаб13.png")
photo = photo.subsample(4, 4)
label_image = tk.Label(root, image=photo, bg="#f2f2f2")
label_image.grid(row=0, column=0, columnspan=2, pady=10)
# Поля вводу
tk.Label(root, text="Введіть значення a:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_a = tk.Entry(root, width=20)
entry_a.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Введіть значення b:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_b = tk.Entry(root, width=20)
entry_b.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Введіть значення c:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_c = tk.Entry(root, width=20)
entry_c.grid(row=3, column=1, padx=10, pady=5)

# Кнопка
button_calc = tk.Button(root, text="Обчислити f", command=calculate_function)
button_calc.grid(row=4, column=0, columnspan=2, pady=10)

# Результат
label_result = tk.Label(root, text="Результат:", bg="#f2f2f2", font=("Arial", 12))
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

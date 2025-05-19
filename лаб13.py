import tkinter as tk
from math import sqrt

def calculate_all(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Півпериметр і площа
        p = (a+b+c)/2
        s = sqrt(p*(p - a)*(p - b)*(p - c))

        # Радіус вписаного кола
        r = (2 * s) / (a + b + c)

        # Медіана до сторони b
        m = 0.5 * sqrt(2*a**2+2*c**2-b**2)

        label_result.config(text=f"Радіус вписаного кола: {r:.2f}\nМедіана до сторони a: {m:.2f}")
    except Exception as e:
        label_result.config(text=f"Помилка: {e}")

root = tk.Tk()
root.title("Радіус вписаного кола і медіана")
root.geometry("500x420")
root.configure(bg="lavender")

# Фото
photo = tk.PhotoImage(file="лрр13.png")
photo = photo.subsample(2, 2)
label_image = tk.Label(root, image=photo)
label_image.place(x=50, y=10)

# Поля вводу
tk.Label(root, text="Сторона a:").place(x=50, y=130)
entry_a = tk.Entry(root)
entry_a.place(x=150, y=130)

tk.Label(root, text="Сторона b:").place(x=50, y=170)
entry_b = tk.Entry(root)
entry_b.place(x=150, y=170)

tk.Label(root, text="Сторона c:").place(x=50, y=210)
entry_c = tk.Entry(root)
entry_c.place(x=150, y=210)

# Кнопка
button = tk.Button(root, text="Обчислити", command=calculate_all)
button.place(x=200, y=260)

# Вивід результату
label_result = tk.Label(root, text="", font=("Arial", 12), justify="left")
label_result.place(x=100, y=310)

root.mainloop()

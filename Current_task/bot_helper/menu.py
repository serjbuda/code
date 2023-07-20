import tkinter as tk

# функция, вызываемая при нажатии на кнопку "Activate"
def activate():
    print("Кнопка 'Activate' нажата.")

# функция, вызываемая при наведении курсора на кнопку "Exit"
def exit_hover(event):
    exit_button.config(fg="red")

# функция, вызываемая при убирании курсора с кнопки "Exit"
def exit_unhover(event):
    exit_button.config(fg="black")

# функция, вызываемая при нажатии на кнопку "Exit"
def exit_app():
    print("Кнопка 'Exit' нажата.")
    root.destroy()

# создаем главное окно
root = tk.Tk()
root.title("B0tHe1Per")
root.geometry("700x1000")
root.configure(bg="black")

# добавляем надпись "B0tHe1Per" в центр сверху
label = tk.Label(root, text="B0tHe1Per", font=("Arial", 36), fg="white", bg="black")
label.pack(pady=50)

# добавляем кнопку "Activate" ниже надписи
activate_button = tk.Button(root, text="Activate", font=("Arial", 24), command=activate)
activate_button.pack(pady=50)

# добавляем кнопку "Exit" еще ниже
exit_button = tk.Button(root, text="Exit", font=("Arial", 24), command=exit_app)
exit_button.pack(pady=50)

# наводим и убираем курсор на кнопку "Exit"
exit_button.bind("<Enter>", exit_hover)
exit_button.bind("<Leave>", exit_unhover)

# запускаем цикл обработки событий
root.mainloop()

import tkinter as tk

# функция, вызываемая при нажатии на кнопку "Activate"
def activate():
    # удаляем кнопки
    activate_button.destroy()
    exit_button.destroy()

    # добавляем консоль
    console = tk.Text(root, fg="white", bg="black", font=("Arial", 14))
    console.pack(fill=tk.BOTH, expand=True)
    console.focus_set()

    # добавляем обработчик событий на нажатие клавиш
    console.bind("<Return>", process_command)

# функция для обработки команд пользователя
def process_command(event):
    command = console.get("end-1c linestart", "end-1c lineend")
    console.delete("end-1c linestart", "end-1c lineend")

    if command.lower() == "exit":
        root.destroy()
    else:
        console.insert(tk.END, f">>> {command}\n")

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
exit_button = tk.Button(root, text="Exit", font=("Arial", 24), command=root.destroy)
exit_button.pack(pady=50)

# наводим и убираем курсор на кнопку "Exit"
exit_button.bind("<Enter>", lambda event: exit_button.config(fg="red"))
exit_button.bind("<Leave>", lambda event: exit_button.config(fg="black"))

# запускаем цикл обработки событий
root.mainloop()

import sys
import os
# Добавляем корневую директорию проекта в PYTHONPATH, чтобы Python мог находить модули
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем функцию set_alarm из модуля alarm, который находится в директории src
from src.alarm import set_alarm


import os
import threading
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from src.alarm import set_alarm


def start_alarm(date_entry, hour_combobox, minute_combobox, sound_var):
    """Функция для начала работы будильника."""
    date = date_entry.get()
    time_ = f"{hour_combobox.get()}:{minute_combobox.get()}"
    sound_file = sound_var.get()

    alarm_datetime = f"{date} {time_}"

    # Отображаем сообщение, что будильник установлен
    messagebox.showinfo("Будильник", f"Будильник установлен на {alarm_datetime}")

    # Запускаем будильник в отдельном потоке
    threading.Thread(
        target=set_alarm,
        args=(alarm_datetime, sound_file)
    ).start()


def create_gui():
    """Создание графического интерфейса для будильника."""
    root = tk.Tk()
    root.title("Будильник")

    # Устанавливаем размер окна
    window_width = 500
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")

    # Отключаем возможность изменения размера окна
    root.resizable(False, False)

    # Устанавливаем окно в центре экрана
    position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Определяем абсолютный путь к изображениям и звукам
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "../assets/images/cat.jpeg")

    # Загрузка и установка фонового изображения
    background_image = Image.open(image_path)
    background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Метки и поля для ввода даты и времени
    tk.Label(
        root, text="Дата:", font=("Helvetica", 14), bg="#ffea00"
    ).grid(row=0, column=0, pady=10)
    date_entry = DateEntry(root, font=("Helvetica", 14), date_pattern='dd.mm.yyyy')
    date_entry.grid(row=0, column=1, pady=10)

    tk.Label(
        root, text="Время:", font=("Helvetica", 14), bg="#ffea00"
    ).grid(row=1, column=0, pady=10)

    # Комбинированные боксы для выбора часа и минуты
    hour_combobox = tk.ttk.Combobox(
        root, values=[f"{i:02d}" for i in range(24)], width=5, font=("Helvetica", 14)
    )
    hour_combobox.set("00")
    hour_combobox.grid(row=1, column=1, pady=10, sticky="w")

    minute_combobox = tk.ttk.Combobox(
        root, values=[f"{i:02d}" for i in range(60)], width=5, font=("Helvetica", 14)
    )
    minute_combobox.set("00")
    minute_combobox.grid(row=1, column=1, pady=10, sticky="e")

    # Радиокнопки для выбора звукового файла
    tk.Label(
        root, text="Выберите звук:", font=("Helvetica", 14), bg="#ffe9b9"
    ).grid(row=2, column=0, columnspan=2, pady=10)
    sound_var = tk.StringVar(value=os.path.join(base_dir, "../assets/sounds/Morning.mp3"))

    tk.Radiobutton(
        root, text="Morning", variable=sound_var, value=os.path.join(base_dir, "../assets/sounds/Morning.mp3"),
        font=("Helvetica", 12), bg="#ffe9b9", activebackground="#d3d3d3"
    ).grid(row=3, column=0, sticky="w", padx=50)

    tk.Radiobutton(
        root, text="Sherlock", variable=sound_var, value=os.path.join(base_dir, "../assets/sounds/Sherlock.mp3"),
        font=("Helvetica", 12), bg="#ffe9b9", activebackground="#d3d3d3"
    ).grid(row=4, column=0, sticky="w", padx=50)

    tk.Radiobutton(
        root, text="Spring", variable=sound_var, value=os.path.join(base_dir, "../assets/sounds/Spring.mp3"),
        font=("Helvetica", 12), bg="#ffe9b9", activebackground="#d3d3d3"
    ).grid(row=5, column=0, sticky="w", padx=50)

    # Кнопка для установки будильника
    tk.Button(
        root, text="Установить будильник",
        command=lambda: start_alarm(date_entry, hour_combobox, minute_combobox, sound_var),
        font=("Helvetica", 14), bg="#b34d00", fg="white",
        activebackground="#4682B4", activeforeground="white", borderwidth=0
    ).grid(row=6, column=0, columnspan=2, pady=20)

    # Запускаем основной цикл приложения
    root.mainloop()


if __name__ == "__main__":
    create_gui()

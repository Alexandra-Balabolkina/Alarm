from datetime import datetime, timedelta
import time
import pygame
from tkinter import messagebox


def play_sound(sound_file):
    """Функция для воспроизведения звука с использованием pygame."""
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def set_alarm(alarm_datetime, sound_file, snooze_minutes=3):
    """Функция установки будильника с возможностью отсрочки."""
    alarm_time = datetime.strptime(alarm_datetime, "%d.%m.%Y %H:%M")
    while True:
        current_time = datetime.now()
        if current_time >= alarm_time:
            try:
                play_sound(sound_file)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось воспроизвести звук: {e}")

            snooze_option = messagebox.askquestion(
                "Будильник",
                "Просыпайтесь! Отложить будильник на 3 минуты?"
            )
            if snooze_option == 'yes':
                alarm_time = datetime.now() + timedelta(minutes=snooze_minutes)
            else:
                break
        time.sleep(10)

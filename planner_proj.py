import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pygame  # برای پخش صدا

# فایل ذخیره‌سازی
SAVE_FILE = "planner_data.txt"

# مقداردهی اولیه pygame
pygame.mixer.init()

# تابع برای پخش صدای کلیک
def play_click_sound(button_sound=True):
    sound_file = "bib3.mp3" if button_sound else "bib2.mp3"
    if os.path.exists(sound_file):
        pygame.mixer.Sound(sound_file).play()

# تابع برای بارگذاری داده‌ها از فایل
def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# تابع برای ذخیره داده‌ها در فایل
def save_data():
    with open(SAVE_FILE, "w") as file:
        file.write("\n".join(tasks))

# اضافه کردن کار جدید
def add_task():
    play_click_sound()
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_data()

# حذف کار انتخابی
def delete_task():
    play_click_sound()
    selected = task_list.curselection()
    if selected:
        task = task_list.get(selected)
        tasks.remove(task)
        task_list.delete(selected)
        save_data()

# تیک زدن یا انجام کار
def mark_done():
    play_click_sound()
    selected = task_list.curselection()
    if selected:
        task = task_list.get(selected)
        tasks[selected[0]] = f"✔️ {task}" if not task.startswith("✔️") else task.replace("✔️ ", "")
        task_list.delete(selected)
        task_list.insert(selected, tasks[selected[0]])
        save_data()

# رابط گرافیکی اصلی
root = tk.Tk()
root.title("Cute Planner")
root.geometry("800x600")

# بک‌گراند
bg_image = Image.open("D:\\New folder (2) - Copy\\photos\\999.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# لیست کارها
tasks = load_data()

task_frame = tk.Frame(root, bg="#d0f0c0", bd=2)
task_frame.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.7)

task_list = tk.Listbox(task_frame, font=("Segoe Print", 14), bg="#f0fff0", fg="#004d00", selectbackground="#98fb98")
task_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

for task in tasks:
    task_list.insert(tk.END, task)

# ورودی متن
task_entry = tk.Entry(root, font=("Segoe Print", 14, "bold"), bg="#ffffff", bd=2)
task_entry.place(relx=0.05, rely=0.82, relwidth=0.6, height=40)

# دکمه‌ها
button_frame = tk.Frame(root, bg="#98fb98", bd=2)
button_frame.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.7)

button_style = ttk.Style()
button_style.configure("TButton", font=("Segoe Print", 10, "bold"), padding=10)

add_button = ttk.Button(button_frame, text="➕", command=add_task, style="TButton")
add_button.pack(pady=20)

delete_button = ttk.Button(button_frame, text="🗑️", command=delete_task, style="TButton")
delete_button.pack(pady=20)

done_button = ttk.Button(button_frame, text="✔️", command=mark_done, style="TButton")
done_button.pack(pady=20)

# افزودن رویداد کلیک برای سایر بخش‌ها
def on_any_click(event):
    play_click_sound(button_sound=False)

root.bind_all("<Button-1>", on_any_click)
root.iconbitmap('D:\\New folder (2) - Copy\\photos\\22.ico')

# راه‌اندازی برنامه
root.mainloop()

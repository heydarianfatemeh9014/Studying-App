from tkinter import *
from time import sleep
from PIL import Image, ImageTk
import pygame
# تنظیمات اصلی
from random import*

staroot = Tk()
staroot.title('Pomodoro Timer')
staroot.config(bg='#FCE4EC')
staroot.resizable(False, False)
staroot.geometry('650x450+300+40')
staroot.iconbitmap('D:\\New folder (2) - Copy\\photos\\22.ico')
def back():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib2.mp3")
    pygame.mixer.music.play()
    staroot.destroy()
    import start_proj
back_bt = Button(staroot, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=0, y=0)
# تنظیمات تصویر پس‌زمینه
bg_image = Image.open("D:\\New folder (2) - Copy\\photos\\bg2.jpg")
bg_image = bg_image.resize((650, 450))
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = Label(staroot, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# متغیرهای تایمر
work_time = 25 * 60  # 25 دقیقه کار
short_break = 5 * 60  # 5 دقیقه استراحت کوتاه
long_break = 15 * 60  # 15 دقیقه استراحت بلند
time_remaining = work_time
current_mode = "Work"  # حالت اولیه

def update_timer():
    import pygame
    global time_remaining, current_mode
    if time_remaining > 0:
        minutes = time_remaining // 60
        seconds = time_remaining % 60
        clock_lbl.config(text=f"{minutes:02}:{seconds:02}")
        time_remaining -= 1
        staroot.after(1000, update_timer)
    else:
        play_sound()
        if current_mode == "Work":
            start_break(short_break)
        elif current_mode == "Short Break":
            start_work()
        elif current_mode == "Long Break":
            show_end_popup()

def start_work():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib4.mp3")
    pygame.mixer.music.play()
    global time_remaining, current_mode
    time_remaining = work_time
    current_mode = "Work"
    show_info_popup("Time to work! Stay focused. 😊")
    update_timer()

def start_break(duration):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib3.mp3")
    pygame.mixer.music.play()
    global time_remaining, current_mode
    time_remaining = duration
    current_mode = "Short Break" if duration == short_break else "Long Break"
    show_info_popup("Take a short break! Relax. 💤")
    update_timer()

def show_info_popup(message):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib4.mp3")
    pygame.mixer.music.play()
    colo = choice(['#F0E89A','#B5F08F','#F0D192'])
    im = choice(['D:\\New folder (2) - Copy\\photos\\11.png','D:\\New folder (2) - Copy\\photos\\22.png','D:\\New folder (2) - Copy\\photos\\33.png','D:\\New folder (2) - Copy\\photos\\44.png'])
    popup = Toplevel(staroot)
    popup.title("Reminder")
    popup.geometry("400x200")
    popup.config(bg=colo)
    
    icon_img = Image.open(im)
    icon_img = icon_img.resize((75, 75))
    icon_photo = ImageTk.PhotoImage(icon_img)
    icon_label = Label(popup, image=icon_photo, bg=colo)
    icon_label.image = icon_photo
    icon_label.pack(pady=10)

    msg_label = Label(popup, text=message, font=("Segoe Print", 12, "bold"), bg=colo, fg="#4D7B40")
    msg_label.pack(pady=10)

    ok_button = Button(popup, text="OK", font=("Segoe Print", 12, "bold"), bg=colo, fg="white", command=popup.destroy)
    ok_button.pack(pady=10)

def show_end_popup():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib4.mp3")
    pygame.mixer.music.play()
    colo = choice(['#F0E89A','#B5F08F','#F0D192'])
    im =choice(['D:\\New folder (2) - Copy\\photos\\11.png','D:\\New folder (2) - Copy\\photos\\22.png','D:\\New folder (2) - Copy\\photos\\33.png','D:\\New folder (2) - Copy\\photos\\44.png'])

    popup = Toplevel(staroot)
    popup.title("Congratulations!")
    popup.geometry("400x200")
    popup.config(bg=colo)
    icon_img = Image.open(im)
    icon_img = icon_img.resize((85, 85))
    icon_photo = ImageTk.PhotoImage(icon_img)
    icon_label = Label(popup, image=icon_photo, bg=colo)
    icon_label.image = icon_photo
    icon_label.pack(pady=10)

    msg_label = Label(popup, text="Great job! You've completed your session. 🎉", 
                      font=("Segoe Print", 12, "bold"), bg=colo, fg="#D81B60")
    msg_label.pack(pady=10)

    ok_button = Button(popup, text="OK", font=("Segoe Print", 12, "bold"), bg=colo, fg="white", command=popup.destroy)
    ok_button.pack(pady=10)

def play_sound():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib4.mp3")
    pygame.mixer.music.play()
    pygame.mixer.init()
    pygame.mixer.music.load("222.mp3")
    pygame.mixer.music.play()

# ویجت‌ها
clock_lbl = Label(staroot, bg='#DCE7C5', fg='#688F4B', font=('Segoe Print', 30, 'bold'), text="25:00")
clock_lbl.place(x=250, y=150)

start_button = Button(staroot, text="Start", font=('Segoe Print', 15, 'bold'), bg='#548E62', fg='white', command=start_work)
start_button.place(x=275, y=300)

staroot.mainloop()

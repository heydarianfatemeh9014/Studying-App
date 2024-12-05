from tkinter import *
from tkinter import font
from calendar import monthrange, month_name
from datetime import date
from PIL import Image, ImageTk
from random import choice

# تنظیمات اصلی
calr = Tk()
calr.title('Calendar Window')
calr.config(bg='#FCE4EC')
calr.resizable(False, False)
calr.geometry('500x500+300+40')
calr.iconbitmap('D:\\New folder (2) - Copy\\photos\\22.ico')

# تاریخ فعلی
current_date = date.today()
current_month = current_date.month
current_year = current_date.year
 
# تنظیمات فونت و رنگ‌ها
font_title = ('CommercialScript Bt', 28, 'bold')
font_days = ('CommercialScript Bt', 15, 'bold')

# لیست رنگ‌ها و پس‌زمینه‌ها
color_palettes = [
    ['#66BB6A', '#FFB74D', '#FFEB3B', '#FFD54F'],  # سبز و زرد کیوت
    ['#9C27B0', '#F06292', '#FF7043', '#DCE775'],
    ['#2196F3', '#4CAF50', '#FFC107', '#FF5722'],
    ['#E91E63', '#FF9800', '#8BC34A', '#00BCD4']
]

backgrounds = ['D:\\New folder (2) - Copy\\photos\\cute_yellow.png', 'D:\\New folder (2) - Copy\\photos\\cute_blue.png', 'D:\\New folder (2) - Copy\\photos\\cute_green.png', 'D:\\New folder (2) - Copy\\photos\\cute_brown.png']

# انتخاب رنگ‌ها و پس‌زمینه به صورت تصادفی
current_palette = choice(color_palettes)
current_background = choice(backgrounds)

# پس‌زمینه تقویم
bg_image = Image.open(current_background)
bg_image = bg_image.resize((500, 500))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = Label(calr, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# تابع برای تغییر رنگ‌ها و پس‌زمینه
def change_theme():
    global current_palette, bg_image, current_background
    current_palette = choice(color_palettes)
    current_background = choice(backgrounds)
    bg_image = Image.open(current_background)
    bg_image = bg_image.resize((500, 500))
    bg_image = ImageTk.PhotoImage(bg_image)
    bg_label.config(image=bg_image)

# تابع برای به‌روزرسانی تقویم
def update_calendar(month, year):
    change_theme()
    for widget in frame_days.winfo_children():
        widget.destroy()

    title_label.config(text=f"{month_name[month]} {year}", fg=current_palette[0])

    days_in_month = monthrange(year, month)[1]
    first_day_of_month = monthrange(year, month)[0]

    for i, day in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        Label(frame_days, text=day, font=font_days, fg=current_palette[1]).grid(row=0, column=i, pady=5)

    row = 1
    col = first_day_of_month

    for day in range(1, days_in_month + 1):
        color = current_palette[2] if col in [5, 6] else current_palette[0]
        if day == current_date.day and month == current_month and year == current_year:
            lbl = Label(frame_days, text=day, font=font_days, fg='white', bg=current_palette[3], width=4, height=2)
        else:
            lbl = Label(frame_days, text=day, font=font_days, fg=color, width=4, height=2)

        lbl.grid(row=row, column=col, padx=2, pady=2)

        col += 1
        if col > 6:
            col = 0
            row += 1

# توابع برای تغییر ماه
def previous_month():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib2.mp3")
    pygame.mixer.music.play()
    global current_month, current_year
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    update_calendar(current_month, current_year)

def next_month():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib2.mp3")
    pygame.mixer.music.play()
    global current_month, current_year
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
    update_calendar(current_month, current_year)

# ساخت اجزای تقویم
title_label = Label(calr, text="", font=font_title)
title_label.pack(pady=10)

frame_days = Frame(calr)
frame_days.pack(pady=10)

btn_prev = Button(calr, text="\u25C0", command=previous_month, bg=current_palette[1], fg='white', font=font_days, width=5)
btn_prev.place(x=50, y=450)

btn_next = Button(calr, text="\u25B6", command=next_month, bg=current_palette[1], fg='white', font=font_days, width=5)
btn_next.place(x=400, y=450)
# دکمه برای بازگشت
def back():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib2.mp3")
    pygame.mixer.music.play()
    calr.destroy()
    from start_proj import staroot
back_bt = Button(calr, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=0, y=0)
# نمایش تقویم برای ماه فعلی
update_calendar(current_month, current_year)

calr.mainloop()

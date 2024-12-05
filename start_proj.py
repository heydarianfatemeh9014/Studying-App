from tkinter import *
from PIL import Image, ImageTk
import pygame

staroot = Tk()
staroot.title('Study App')
staroot.config(bg='#94C973')
staroot.resizable(False, False)
staroot.geometry('500x500+300+40')
def tips():
    pygame.mixer.init()
    pygame.mixer.music.load("bib3.mp3")
    pygame.mixer.music.play()
    staroot.destroy()
    
    
    import tips_study

def cal():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib3.mp3")
    pygame.mixer.music.play()
    staroot.destroy()
    
    
    import calendar_proj
def plan():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib3.mp3")
    pygame.mixer.music.play()
    staroot.destroy()
    
    
    import planner_proj

bg_image = Image.open("D:\\New folder (2) - Copy\\photos\\greeen.jpg")

bg_image = bg_image.resize((500, 500))  # Resizing the image to fit the window

bg_image = ImageTk.PhotoImage(bg_image)  # Converting the image to a format usable in Tkinter


bg_label = Label(staroot, image=bg_image)

bg_label.place(relwidth=1, relheight=1)  # Expanding the label to cover the entire window
staroot.iconbitmap('D:\\New folder (2) - Copy\\photos\\22.ico')


def back():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib2.mp3")
    pygame.mixer.music.play()
    staroot.destroy()
    import main
back_bt = Button(staroot, activeforeground='pink', activebackground='red', fg='red', bg='pink', text='Back', font=('Segoe Print', 14, 'bold'), command=back).place(x=180, y=240)
btn_tips = Button(staroot, activebackground='#528041', activeforeground='#D7F3AC', bg='#D7F3AC', fg='#528041', text='Study Techniques', font=('Segoe Print', 14, 'bold'), command=tips).place(x=0, y=0)
btn_cal = Button(staroot, activebackground='#D7F3AC', activeforeground='#528041', bg='#528041', fg='#D7F3AC', text='Calendar', font=('Segoe Print', 14, 'bold'), command=cal).place(x=180, y=80)
btn_plan = Button(staroot, activebackground='#4F681A', activeforeground='#FAF795', bg='#FAF795', fg='#4F681A', text='Planner', font=('Segoe Print', 14, 'bold'), command=plan).place(x=0, y=160)

staroot.mainloop()


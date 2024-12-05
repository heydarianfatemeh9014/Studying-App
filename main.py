


from tkinter import *

from PIL import Image, ImageTk

def start():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("bib4.mp3")
    pygame.mixer.music.play()
    root.destroy()
    import start_proj  # Importing the function that will be executed on button click

root = Tk()  # Creating the main window
root.title('Study App')  # Setting the title of the window

root.config(bg='#94C973')  # Configuring the background color
root.iconbitmap('D:\\New folder (2) - Copy\\photos\\22.ico')

root.resizable(False, False)  # Disabling window resizing

root.geometry('800x400+300+40')  # Setting the dimensions and position of the window

bg_image = Image.open("D:\\New folder (2) - Copy\\photos\\grbg2.png")

bg_image = bg_image.resize((800, 400))  # Resizing the image to fit the window

bg_image = ImageTk.PhotoImage(bg_image)  # Converting the image to a format usable in Tkinter


bg_label = Label(root, image=bg_image)

bg_label.place(relwidth=1, relheight=1)  # Expanding the label to cover the entire window



btn_start = Button(root, activebackground='#7E8C69', activeforeground='#D3D9A7', bg='#F4E891', fg='#F5AE59', text='Start now!', font=('Segoe Print', 14, 'bold'), command=start).place(x=580, y=120)

root.mainloop()  # Starting the Tkinter event loop
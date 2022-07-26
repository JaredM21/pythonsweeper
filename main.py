from tkinter import *
import settings

root = Tk()
# Sets Window Settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEGHT}')
root.title('PySweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', #TODO Change Later
    width=1920,
    height=270
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    bg = 'blue',
    width=360,
    height=810
)
left_frame.place(x=0, y=270)

#Runs Window
root.mainloop()
import customtkinter as Ctk
from tkinter import *


Homepage= Ctk.CTk()

Ctk.set_appearance_mode('light')
Homepage.geometry("{0}x{1}+0+0".format(Homepage.winfo_screenwidth(), Homepage.winfo_screenheight()))
screen_width = Homepage.winfo_screenwidth()
screen_height = Homepage.winfo_screenheight()


def change_status():
    Change= Ctk.CTk()

Mymenue= Menu(Homepage)
Mymenue.add_command(label="Change Status", command=change_status)

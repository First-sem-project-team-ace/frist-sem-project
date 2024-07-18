from tkinter import *

import customtkinter 
from PIL import Image

def register_page():

 app= customtkinter.CTk()
 
 customtkinter.set_appearance_mode('light')
 # app.geometry("1300x700")
 
 app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
 screen_width= app.winfo_screenwidth()
 screen_height= app.winfo_screenheight()
 
 frame= customtkinter.CTkFrame(master=app, width=screen_width, height=screen_height,bg_color="white",fg_color="#614BD4")
 frame.place(relx=0,rely=0)
 
 Linear_image = customtkinter.CTkImage(light_image=Image.open('Linear.png'),
                                   size=(screen_width,screen_height))
 
 Linear_image_label=customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
 Linear_image_label.place(x=0,y=0)
 
 
 Hostel_label= customtkinter.CTkLabel(master=frame, text="Griha Hostel", font=("helvetica", 40, "bold"), text_color="white",fg_color="#46358D")
 Hostel_label.place(relx=0.01,rely=0.05)
 
 Creatacc_label=customtkinter.CTkLabel(master=frame,text="Create Account",font=("helvetica", 40), text_color="white",fg_color="#5E4EA1")
 Creatacc_label.place(relx=0.42,rely=0.1)
 
 
 name_entry= customtkinter.CTkEntry(master=app,placeholder_text="Name of student", width=1500,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 name_entry.place(relx=0.1,rely=0.2)
 
 
 email_entry= customtkinter.CTkEntry(master=app,placeholder_text="Enter Your Email Address", width=1500,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 email_entry.place(relx=0.1,rely=0.275)
 
 
 number_entry1= customtkinter.CTkEntry(master=app,placeholder_text="+977", width=200,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 number_entry1.place(relx=0.1,rely=0.350)
 
 
 number_entry2= customtkinter.CTkEntry(master=app,placeholder_text="Enter Your Number", width=1200,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 number_entry2.place(relx=0.255,rely=0.350)
 
 
 number_entry3= customtkinter.CTkEntry(master=app,placeholder_text="+977", width=200,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 number_entry3.place(relx=0.1,rely=0.425)
 
 
 number_entry4= customtkinter.CTkEntry(master=app,placeholder_text="Enter Your Emergency Contact Details", width=1200,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 number_entry4.place(relx=0.255,rely=0.425)
 
 guardian_entry= customtkinter.CTkEntry(master=app, width=1500,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 guardian_entry.place(relx=0.1,rely=0.5)
   
 
 address_entry1= customtkinter.CTkEntry(master=app, width=1500,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 address_entry1.place(relx=0.1,rely=0.650)
 
 
 address_entry2= customtkinter.CTkEntry(master=app, width=1500,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 address_entry2.place(relx=0.1,rely=0.725)
 
 
 proceed_btn= customtkinter.CTkButton(master=app,text="Proceed", width=400,height=50, fg_color="#614BD4", text_color="white", corner_radius=10, bg_color="#796cb2")
 proceed_btn.place(relx=0.255,rely=0.875)
 
 back_btn= customtkinter.CTkButton(master=app,text="Back" ,width=400,height=50, fg_color="#D9D9D9", text_color="white", corner_radius=10, bg_color="#796cb2")
 back_btn.place(relx=0.5,rely=0.875)
 
 residental_label=customtkinter.CTkLabel(master=app,text="Residential Address",font=("helvetica", 40), text_color="white",fg_color="#5E4EA1")
 residental_label.place(relx=0.42,rely=0.575)
 
 
 app.mainloop()
 
if __name__ == "__main__":
    register_page()
 
 
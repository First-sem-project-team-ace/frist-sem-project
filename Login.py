from tkinter import *

import customtkinter 
from PIL import Image



app= customtkinter.CTk()

customtkinter.set_appearance_mode('light')
# app.geometry("1300x700")

app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
screen_width= app.winfo_screenwidth()
screen_height= app.winfo_screenheight()



def hygiene():
    print("")

def comfort():
    print("")

def security():
    print("")

def login():
    print(" Login button is clicked")

def register():
    print("Clicked")




frame= customtkinter.CTkFrame(master=app, width=screen_width, height=screen_height,bg_color="white",fg_color="#614BD4")
frame.place(relx=0,rely=0)

Linear_image = customtkinter.CTkImage(light_image=Image.open('Screenshot 2024-07-10 091838.png'),
                                  size=(1366, 770))

Linear_image_label=customtkinter.CTkLabel(master=frame, image=Linear_image)
Linear_image_label.place(x=0,y=0)

Hostel_label= customtkinter.CTkLabel(master=frame, text="Griha Hostel", font=("helvetica", 20, "bold"), text_color="white",fg_color="#6455A6")
Hostel_label.place(relx=0.01,rely=0.05)


Headline_label= customtkinter.CTkLabel(master=frame, text="YOUR HOME AWAY", font=("helvetica", 30, "bold"), bg_color="white",fg_color="#9489C1", text_color="white")
Headline_label.place(relx=0.01,rely=0.13)

Headline_label1= customtkinter.CTkLabel(master=frame, text="FROM HOME", font=("helvetica", 30, "bold"), bg_color="white", fg_color='#9489C1', text_color="white")
Headline_label1.place(relx=0.01,rely=0.17)

Subheadline_label= customtkinter.CTkLabel(master=frame, text="Experience Comfort In Every Corner", font=("helvetica", 14,"italic"), fg_color="#614BD4", text_color="white")
Subheadline_label.place(relx=0.03,rely=0.23)


my_image = customtkinter.CTkImage(light_image=Image.open('Hostel.jpg'),
                                  size=(1366, 400))

my_label= customtkinter.CTkLabel(master=frame,image=my_image )
my_label.place(relx=0,rely=0.45)

Login_frame= customtkinter.CTkFrame(master=app, fg_color="white", width=300, height=300)
Login_frame.place(relx=0.7,rely=0.1)

Login_welcome= Label(master=Login_frame, text="Welcome to Griha Hostel", fg="black", bg="white")
Login_welcome.place(relx=0.3, rely=0)

Login_label=Label(master=Login_frame, text="Log In", font="bold, 25", bg="white", fg="#614BD4")
Login_label.place(relx=0.1, rely=0.1)

email_label= Label(master=Login_frame, text="Email:", bg="white", fg="black", font="20")
email_label.place(relx=0.03,rely=0.3)
password_label= Label(master=Login_frame, text="Password:", bg="white", fg="Black", font="20")
password_label.place(relx=0.03, rely=0.4)


email_entry= customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
email_entry.place(relx=0.3,rely=0.3)
password_entry= customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
password_entry.place(relx=0.3, rely=0.4)

Btn_login= customtkinter.CTkButton(master=Login_frame, text="Login",width=90, fg_color="#614BD4", text_color="white")
Btn_login.place(relx=0.65, rely=0.6)


app.mainloop()



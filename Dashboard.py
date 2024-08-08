# from tkinter import *

# import customtkinter 
# from PIL import Image
# import Login
# import Register


# app= customtkinter.CTk()

# customtkinter.set_appearance_mode('light')
# # app.geometry("1300x700")

# app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
# screen_width= app.winfo_screenwidth()
# screen_height= app.winfo_screenheight()



# def hygiene():
#     print("")

# def comfort():
#     print("")

# def security():
#     print("")

# def login():
#        app.destroy()  # Destroy the main application window
#        Login.login_page()

# def register():
#     app.destroy()
#     Register.register_page()




# frame= customtkinter.CTkFrame(master=app, width=screen_width, height=screen_height,bg_color="white",fg_color="#614BD4")
# frame.place(relx=0,rely=0)

# Linear_image = customtkinter.CTkImage(light_image=Image.open('Linear.png'),
#                                   size=(screen_width,screen_height))

# Linear_image_label=customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
# Linear_image_label.place(x=0,y=0)

# Hostel_label= customtkinter.CTkLabel(master=frame, text="Griha Hostel", font=("helvetica", 40, "bold"), text_color="white")
# Hostel_label.place(relx=0.01,rely=0.05)

# Login_btn= customtkinter.CTkButton(master=frame, text="Log In",command=login, fg_color="gray", text_color="white", border_color="black", border_width=2)
# Login_btn.place(relx=0.88,rely=0.05)

# Register_btn= customtkinter.CTkButton(master=frame, text="Register",command= register,fg_color="gray", text_color="white", border_color="black", border_width=2 )
# Register_btn.place(relx=0.77,rely=0.05)


# Headline_label= customtkinter.CTkLabel(master=frame, text="YOUR HOME AWAY", font=("helvetica", 50, "bold"), bg_color="white",fg_color="#8074B6", text_color="white")
# Headline_label.place(relx=0.01,rely=0.13)

# Headline_label1= customtkinter.CTkLabel(master=frame, text="FROM HOME", font=("helvetica", 50, "bold"), bg_color="white", fg_color='#867bb8', text_color="white")
# Headline_label1.place(relx=0.01,rely=0.19)

# Subheadline_label= customtkinter.CTkLabel(master=frame, text="Experience Comfort In Every Corner", font=("helvetica", 20,"italic"), fg_color="#867bb8", text_color="white")
# Subheadline_label.place(relx=0.01,rely=0.25)


# my_image = customtkinter.CTkImage(light_image=Image.open('Hostel.jpg'),
#                                   size=(screen_width,400))

# my_label= customtkinter.CTkLabel(master=frame,image=my_image, text="")
# my_label.place(relx=0,rely=0.6)



# Button_frame= customtkinter.CTkFrame(master=app, width=1120, height=60, fg_color="#FEC8C8",
#                                       corner_radius=10 , bg_color="#B7B0D6")
# Button_frame.place(relx=0.19,rely=0.35)



# hygiene_btn= customtkinter.CTkButton(master=Button_frame, text="Hygiene", command=hygiene, 
#                                      fg_color="white", bg_color="#FEC8C8", text_color="black",
#                                        corner_radius=10, width=320, height=45, font=('calibri',20))
# hygiene_btn.place(x=20,y=9)

# #comfort button

# comfort_btn= customtkinter.CTkButton(master=Button_frame, text="Comfort",command=comfort, bg_color="#FEC8C8", 
#                                      fg_color="white", text_color="#614BD4", corner_radius=10, width=320, height=45,
#                                      font=('calibri',20))
# comfort_btn.place(x=400,y=9)

# #logo
# Comfort_image = customtkinter.CTkImage(light_image=Image.open('comfort.png'),
#                                   size=(30, 30))
# Comfort_image_label= customtkinter.CTkLabel(master=Button_frame, image=Comfort_image, text="")
# Comfort_image_label.place(x=400,y=14)

# #security button

# security_btn= customtkinter.CTkButton(master=Button_frame, text="Security", command=security, bg_color="#FEC8C8",
#                                       fg_color="white", text_color="black", corner_radius=10, width=320, height=45
#                                       , font=('calibri',20))
# security_btn.place(x=780,y=9)

# #logo

# # add `from PIL import Image` on top
# security_image = customtkinter.CTkImage(light_image=Image.open('security.png'),
#                                   size=(30, 30))
# security_image_label= customtkinter.CTkLabel(master=Button_frame, image=security_image, text="")
# security_image_label.place(x=730,y=14)









# app.mainloop()  


import tkinter as tk
import customtkinter as CTk
from PIL import Image
import Login
import Register
from ttkbootstrap.constants import *
import ttkbootstrap as tb

app = CTk.CTk()

CTk.set_appearance_mode("light")
# app.geometry("1300x700")

app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


def hygiene():
    hygine_frame= CTk.CTkFrame(master=app, height=400, width=328, fg_color="#9CD9E4",corner_radius=15)
    hygine_frame.place(relx=0.22, rely=0.4085)

    hygine_label=CTk.CTkLabel(master=hygine_frame, text="Hygiene", font=("bold",25), text_color="black")
    hygine_label.place(relx=0.05, rely=0.05)

    Content_label= CTk.CTkLabel(master=hygine_frame, text=" At Griha Hostel, we prioritize the\n health and well-being of our\n residents by maintaining the highest\n standards of hygiene throughout\n our facilities. We believe that a\n clean and sanitary environment is\n essential for the comfort and\n safety of our guests. Our\n comprehensive hygiene practices\n are designed to provide a\n welcoming and healthy living\n space for everyone.", justify= LEFT,
                                text_color="black", font=("bold",20))
    Content_label.place(relx=0.01, rely=0.15)

    def back():
      

        hygine_frame.destroy()
       
        

    Exit_button= CTk.CTkButton(master=hygine_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)



def comfort():
    comfort_frame= CTk.CTkFrame(master=app, height=400, width=328, fg_color="#9CD9E4",corner_radius=15)
    comfort_frame.place(relx=0.415, rely=0.4085)

    comfort_label=CTk.CTkLabel(master=comfort_frame, text="Comfort", font=("bold",25), text_color="black")
    comfort_label.place(relx=0.05, rely=0.05)

    Content_label= CTk.CTkLabel(master=comfort_frame, text=" At Griha Hostel, we are dedicated\n to providing a comfortable and cozy\n environment for all our residents.\n Our aim is to create a home away\n from home where everyone feels\n relaxed and at ease. From well-\n furnished rooms to thoughtfully\n designed common areas,every\n aspect of our hostel is geared\n towards ensuring maximum comfort\n and convenience for our guests.", justify= LEFT,
                                text_color="black", font=("bold",20))
    Content_label.place(relx=0.01, rely=0.15)

    def back():
      

        comfort_frame.destroy()
       
        

    Exit_button= CTk.CTkButton(master=comfort_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)


def security():
    Security_frame= CTk.CTkFrame(master=app, height=400, width=328, fg_color="#9CD9E4",corner_radius=15)
    Security_frame.place(relx=0.615, rely=0.4085)

    Security_label=CTk.CTkLabel(master=Security_frame, text="Security", font=("bold",25), text_color="black")
    Security_label.place(relx=0.05, rely=0.05)

    Content_label= CTk.CTkLabel(master=Security_frame, text=" At Griha Hostel, the safety and\n security of our residents is our top\n priority. We have implemented\n comprehensive security measures to\n create a safe living environment\n where everyone can feel protected and\n secure. From advanced surveillance systems\n to strict access controls,\n every aspect of our security\n infrastructure is designed to provide\n peace of mind to our guests.", justify= LEFT,
                                text_color="black", font=("bold",20))
    Content_label.place(relx=0.01, rely=0.15)

    def back():
      

        Security_frame.destroy()
       
        

    Exit_button= CTk.CTkButton(master=Security_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)


def login():
    app.destroy()  # Destroy the main application window
    Login.login_page()


def register():
    app.destroy()
    Register.Register_page()


frame = CTk.CTkFrame(
    master=app,
    width=screen_width,
    height=screen_height,
    fg_color="transparent",
)

frame.place(relx=0, rely=0)

Linear_image = CTk.CTkImage(
    light_image=Image.open(
        r"images\\linear homepage backgroud.png"
    ),
    size=(screen_width, screen_height),
)

Linear_image_label = CTk.CTkLabel(master=frame, image=Linear_image, text="")
Linear_image_label.place(x=0, y=0)


# Hostel_label = customtkinter.CTkLabel(
#     master=frame,
#     text="Griha Hostel",
#     font=("helvetica", 40, "bold"),
#     text_color="white",
#     fg_color="#2B0A78",
    
# )
# Hostel_label.place(relx=0.01, rely=0.05)

Login_btn = CTk.CTkButton(
    master=frame,
    text="Log In",
    command=login,
    fg_color="gray",
    text_color="white",
    border_color="black",
    border_width=2,
)
Login_btn.place(relx=0.88, rely=0.05)

Register_btn = CTk.CTkButton(
    master=frame,
    text="Register",
    command=register,
    fg_color="gray",
    text_color="white",
    border_color="black",
    border_width=2,
)
Register_btn.place(relx=0.77, rely=0.05)

# Headline_label = customtkinter.CTkLabel(
#     master=frame,
#     text="YOUR HOME AWAY",
#     font=("helvetica", 50, "bold"),
#     fg_color="transparent",
#     bg_color="transparent",
#     text_color="white",
# )
# Headline_label.place(relx=0.01, rely=0.13)

# Headline_label1 = tk.Label(
#     master=frame,
#     text="FROM HOME",
#     font=("helvetica", 50, "bold"),
#     fg="white"
    
    
# )
# Headline_label1.place(relx=0.01, rely=0.19)

# Subheadline_label = customtkinter.CTkLabel(
#     master=frame,
#     text="Experience Comfort In Every Corner",
#     font=("helvetica", 20, "italic"),
#     fg_color="transparent",
#     bg_color="transparent",
#     text_color="white",
# )
# Subheadline_label.place(relx=0.01, rely=0.25)

my_image = CTk.CTkImage(
    light_image=Image.open(
        r"images\\Hostel.jpg"
    ),
    size=(screen_width, 400),
)

my_label = CTk.CTkLabel(master=frame, image=my_image, text="")
my_label.place(relx=0, rely=0.6)

Button_frame = CTk.CTkFrame(
    master=app,
    width=1120,
    height=60,
    fg_color="#FEC8C8",
    corner_radius=10,
    bg_color="#B7B0D6",
)

Button_frame.place(relx=0.21, rely=0.4)

hygiene_btn = CTk.CTkButton(
    master=Button_frame,
    text="Hygiene",
    command=hygiene,
    fg_color="white",
    bg_color="#FEC8C8",
    text_color="#534D4D",
    corner_radius=10,
    width=320,
    height=45,
    font=("calibri", 25),
)
hygiene_btn.place(x=20, y=9)

comfort_btn = CTk.CTkButton(
    master=Button_frame,
    text="Comfort",
    command=comfort,
    bg_color="#FEC8C8",
    fg_color="white",
    text_color="#534D4D",
    corner_radius=10,
    width=320,
    height=45,
    font=("calibri", 25),
)
comfort_btn.place(x=400, y=9)

Comfort_image = CTk.CTkImage(
    light_image=Image.open(
        r"images\\comfort.png"
    ),
    size=(30, 30),
)

Comfort_image_label = CTk.CTkLabel(
    master=Button_frame, image=Comfort_image, text=""
)
Comfort_image_label.place(x=400, y=14)

security_btn = CTk.CTkButton(
    master=Button_frame,
    text="Security",
    command=security,
    bg_color="#FEC8C8",
    fg_color="white",
    text_color="#534D4D",
    corner_radius=10,
    width=320,
    height=45,
    font=("calibri", 25),
)
security_btn.place(x=780, y=9)

security_image = CTk.CTkImage(
    light_image=Image.open(
        r"images\\security.png"
    ),
    size=(30, 30),
)

security_image_label = CTk.CTkLabel(
    master=Button_frame, image=security_image, text=""
)
security_image_label.place(x=780, y=14)

app.mainloop()

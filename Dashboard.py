from tkinter import *

import customtkinter 
from PIL import Image
import Login
import Register


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
       app.destroy()  # Destroy the main application window
       Login.login_page()

def register():
    app.destroy()
    Register.register_page()




frame= customtkinter.CTkFrame(master=app, width=screen_width, height=screen_height,bg_color="white",fg_color="#614BD4")
frame.place(relx=0,rely=0)

Linear_image = customtkinter.CTkImage(light_image=Image.open('Linear.png'),
                                  size=(screen_width,screen_height))

Linear_image_label=customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
Linear_image_label.place(x=0,y=0)

Hostel_label= customtkinter.CTkLabel(master=frame, text="Griha Hostel", font=("helvetica", 40, "bold"), text_color="white")
Hostel_label.place(relx=0.01,rely=0.05)

Login_btn= customtkinter.CTkButton(master=frame, text="Log In",command=login, fg_color="gray", text_color="white", border_color="black", border_width=2)
Login_btn.place(relx=0.88,rely=0.05)

Register_btn= customtkinter.CTkButton(master=frame, text="Register",command= register,fg_color="gray", text_color="white", border_color="black", border_width=2 )
Register_btn.place(relx=0.77,rely=0.05)


Headline_label= customtkinter.CTkLabel(master=frame, text="YOUR HOME AWAY", font=("helvetica", 50, "bold"), bg_color="white",fg_color="#8074B6", text_color="white")
Headline_label.place(relx=0.01,rely=0.13)

Headline_label1= customtkinter.CTkLabel(master=frame, text="FROM HOME", font=("helvetica", 50, "bold"), bg_color="white", fg_color='#867bb8', text_color="white")
Headline_label1.place(relx=0.01,rely=0.19)

Subheadline_label= customtkinter.CTkLabel(master=frame, text="Experience Comfort In Every Corner", font=("helvetica", 20,"italic"), fg_color="#867bb8", text_color="white")
Subheadline_label.place(relx=0.01,rely=0.25)


my_image = customtkinter.CTkImage(light_image=Image.open('Hostel.jpg'),
                                  size=(screen_width,400))

my_label= customtkinter.CTkLabel(master=frame,image=my_image, text="")
my_label.place(relx=0,rely=0.6)



Button_frame= customtkinter.CTkFrame(master=app, width=1120, height=60, fg_color="#FEC8C8",
                                      corner_radius=10 , bg_color="#B7B0D6")
Button_frame.place(relx=0.19,rely=0.35)



hygiene_btn= customtkinter.CTkButton(master=Button_frame, text="Hygiene", command=hygiene, 
                                     fg_color="white", bg_color="#FEC8C8", text_color="black",
                                       corner_radius=10, width=320, height=45, font=('calibri',20))
hygiene_btn.place(x=20,y=9)

#comfort button

comfort_btn= customtkinter.CTkButton(master=Button_frame, text="Comfort",command=comfort, bg_color="#FEC8C8", 
                                     fg_color="white", text_color="#614BD4", corner_radius=10, width=320, height=45,
                                     font=('calibri',20))
comfort_btn.place(x=400,y=9)

#logo
Comfort_image = customtkinter.CTkImage(light_image=Image.open('comfort.png'),
                                  size=(30, 30))
Comfort_image_label= customtkinter.CTkLabel(master=Button_frame, image=Comfort_image, text="")
Comfort_image_label.place(x=400,y=14)

#security button

security_btn= customtkinter.CTkButton(master=Button_frame, text="Security", command=security, bg_color="#FEC8C8",
                                      fg_color="white", text_color="black", corner_radius=10, width=320, height=45
                                      , font=('calibri',20))
security_btn.place(x=780,y=9)

#logo

# add `from PIL import Image` on top
security_image = customtkinter.CTkImage(light_image=Image.open('security.png'),
                                  size=(30, 30))
security_image_label= customtkinter.CTkLabel(master=Button_frame, image=security_image, text="")
security_image_label.place(x=730,y=14)









app.mainloop()
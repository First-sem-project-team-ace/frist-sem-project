from tkinter import *
import customtkinter
from PIL import Image
import Login

app = customtkinter.CTk()

customtkinter.set_appearance_mode('light')
app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

def hygiene():
    print("Hygiene button pressed")

def comfort():
    print("Comfort button pressed")

def security():
    print("Security button pressed")

def login():
    app.destroy()  # Destroy the main application window
    Login.login_page()

frame = customtkinter.CTkFrame(master=app, width=screen_width, height=screen_height, bg_color="white", fg_color="#614BD4")
frame.place(relx=0, rely=0)

Linear_image = customtkinter.CTkImage(light_image=Image.open('Linear.png'), size=(screen_width, screen_height))
Linear_image_label = customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
Linear_image_label.place(x=0, y=0)

Hostel_label = customtkinter.CTkLabel(master=frame, text="Griha Hostel", font=("helvetica", 20, "bold"), text_color="white", fg_color="#544499")
Hostel_label.place(relx=0.01, rely=0.05)

Login_btn = customtkinter.CTkButton(master=frame, text="Log In", fg_color="gray", text_color="white", border_color="black", border_width=2, command=login)
Login_btn.place(relx=0.88, rely=0.05)

Register_btn = customtkinter.CTkButton(master=frame, text="Register", fg_color="gray", text_color="white", border_color="black", border_width=2)
Register_btn.place(relx=0.77, rely=0.05)

Headline_label = customtkinter.CTkLabel(master=frame, text="YOUR HOME AWAY", font=("helvetica", 30, "bold"), bg_color="white", fg_color="#8074B6", text_color="white")
Headline_label.place(relx=0.01, rely=0.13)

Headline_label1 = customtkinter.CTkLabel(master=frame, text="FROM HOME", font=("helvetica", 30, "bold"), bg_color="white", fg_color='#9489C1', text_color="white")
Headline_label1.place(relx=0.01, rely=0.17)

Subheadline_label = customtkinter.CTkLabel(master=frame, text="Experience Comfort In Every Corner", font=("helvetica", 14, "italic"), fg_color="#614BD4", text_color="white")
Subheadline_label.place(relx=0.03, rely=0.23)

my_image = customtkinter.CTkImage(light_image=Image.open('Hostel.jpg'), size=(screen_width, 400))
my_label = customtkinter.CTkLabel(master=frame, image=my_image, text="")
my_label.place(relx=0, rely=0.45)

Button_frame = customtkinter.CTkFrame(master=app, width=1000, height=60, fg_color="#FEC8C8", corner_radius=10, bg_color="white")
Button_frame.place(relx=0.1, rely=0.4)

hygiene_btn = customtkinter.CTkButton(master=Button_frame, text="Hygiene", command=hygiene, fg_color="white", bg_color="#FEC8C8", text_color="black", corner_radius=10, width=320, height=45, font=('calibri', 20))
hygiene_btn.place(x=10, y=9)

comfort_btn = customtkinter.CTkButton(master=Button_frame, text="Comfort", command=comfort, bg_color="gray", fg_color="white", text_color="#614BD4", corner_radius=10, width=320, height=45, font=('calibri', 20))
comfort_btn.place(x=340, y=9)

Comfort_image = customtkinter.CTkImage(light_image=Image.open('comfort.png'), size=(30, 30))
Comfort_image_label = customtkinter.CTkLabel(master=Button_frame, image=Comfort_image, text="")
Comfort_image_label.place(x=400, y=14)

security_btn = customtkinter.CTkButton(master=Button_frame, text="Security", command=security, bg_color="gray", fg_color="white", text_color="black", corner_radius=10, width=320, height=45, font=('calibri', 20))
security_btn.place(x=670, y=9)

Security_image = customtkinter.CTkImage(light_image=Image.open('security.png'), size=(30, 30))
Security_image_label = customtkinter.CTkLabel(master=Button_frame, image=Security_image, text="")
Security_image_label.place(x=750, y=14)

app.mainloop()

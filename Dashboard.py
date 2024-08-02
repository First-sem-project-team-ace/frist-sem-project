from tkinter import *
import customtkinter
from PIL import Image



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
    import Login
    Login.login_page()

def register():
    app.destroy()
    import Register


frame = customtkinter.CTkFrame(master=app, width=screen_width, height=screen_height, bg_color="white", fg_color="#614BD4")
frame.place(relx=0, rely=0)

Linear_image = customtkinter.CTkImage(light_image=Image.open('images\\Dashboard_label.png'), size=(screen_width, screen_height))
Linear_image_label = customtkinter.CTkLabel(master=frame, image=Linear_image, text="")
Linear_image_label.place(x=0, y=0)


Login_btn = customtkinter.CTkButton(master=frame, text="Log In", fg_color="gray", text_color="white", border_color="black", border_width=2, command=login)
Login_btn.place(relx=0.88, rely=0.05)

Register_btn = customtkinter.CTkButton(master=frame, text="Register", fg_color="gray", text_color="white", border_color="black", border_width=2,
                                       command=register)
Register_btn.place(relx=0.77, rely=0.05)


my_image = customtkinter.CTkImage(light_image=Image.open('images\\Hostel.jpg'), size=(screen_width, 280))
my_label = customtkinter.CTkLabel(master=frame, image=my_image, text="")
my_label.place(relx=0, rely=0.621)

Button_frame = customtkinter.CTkFrame(master=app, width=1000, height=60, fg_color="#FEC8C8", corner_radius=10, bg_color="white")
Button_frame.place(relx=0.1, rely=0.4)

hygiene_btn = customtkinter.CTkButton(master=Button_frame, text="Hygiene", command=hygiene, fg_color="white", bg_color="#FEC8C8", text_color="black", corner_radius=10, width=320, height=45, font=('calibri', 20))
hygiene_btn.place(x=10, y=9)

Comfort_image = customtkinter.CTkImage(light_image=Image.open('images\\comfort.png'), size=(30, 30))
Security_image = customtkinter.CTkImage(light_image=Image.open('images\\security.png'), size=(30, 30))

comfort_btn = customtkinter.CTkButton(master=Button_frame, text="Comfort", command=comfort, bg_color="gray", 
                                      fg_color="white", text_color="#614BD4", corner_radius=10, width=320, 
                                      height=45, font=('calibri', 20), image=Comfort_image)
comfort_btn.place(x=340, y=9)

security_btn = customtkinter.CTkButton(master=Button_frame, text="Security", command=security, bg_color="gray",
                                       fg_color="white", text_color="black", corner_radius=10, width=320, 
                                       height=45, font=('calibri', 20), image=Security_image)
security_btn.place(x=670, y=9)


def about():

    
    About_frame= customtkinter.CTkFrame(master=app, height=300, width=500, fg_color="#42ABC7")
    About_frame.place(relx=0.6, rely=0.15)

    About_label=customtkinter.CTkLabel(master=About_frame, text="About us", font=("bold",25), text_color="white")
    About_label.place(relx=0.05, rely=0.15)

    Content_label= customtkinter.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \ncomfortable living environment for\n students abd professionals.With\n modern amenities and facilities,and a\n supportive community,Griha hostel\n ensures a home-like experience away\n from home.", justify= LEFT,
                                text_color="white", font=("bold",20))
    Content_label.place(relx=0.1, rely=0.25)

    def back():

        About_frame.destroy()
        

    Exit_button= customtkinter.CTkButton(master=About_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)

What_btn= customtkinter.CTkButton(master=app,text="?", bg_color="#3FB5CB",fg_color="#3FB5CB",width=50, text_color="black",
                        corner_radius=80, font=("bold", 20), command=about)
What_btn.place(relx=0.7, rely=0.05)


app.mainloop()


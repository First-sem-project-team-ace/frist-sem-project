from tkinter import *
import customtkinter
from PIL import Image



app = customtkinter.CTk()

customtkinter.set_appearance_mode('light')
app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

def hygiene():
    global hygiene_frame

    hygiene_btn.configure(fg_color="#9CD9E4")
    hygiene_frame= customtkinter.CTkFrame(master=app, width=320, height=200, fg_color="#9CD9E4")
    hygiene_frame.place(relx=0.11, rely=0.46)

    back_btn=customtkinter.CTkButton(master=hygiene_frame, text="X", width=20, height=10 ,command=hygiene_back)
    back_btn.place(relx=0.9, rely=0.02)

    hygiene_label=customtkinter.CTkLabel(master=hygiene_frame, text="At Griha Hostel, we prioritize the health and well-\n being of our residents by maintaining the highest \n standards of hygiene throughout our facilities.\n We believe that a clean and sanitary environment \n is essential for the comfort and safety of our\n guests. Our comprehensive hygiene practices are\n designed to provide a welcoming and healthy\n living space for everyone.",
                                         font=("bold",14), text_color="black", justify=LEFT)
    hygiene_label.place(relx=0 ,rely=0.14)

def hygiene_back():
        hygiene_frame.destroy()

def comfort():
    global comfort_frame

    comfort_btn.configure(fg_color="#9CD9E4")
    comfort_frame= customtkinter.CTkFrame(master=app, width=320, height=200, fg_color="#9CD9E4")
    comfort_frame.place(relx=0.35, rely=0.46)

    back_btn=customtkinter.CTkButton(master=comfort_frame, text="X", width=20, height=10 ,command=comfort_back)
    back_btn.place(relx=0.9, rely=0.02)

    hygiene_label=customtkinter.CTkLabel(master=comfort_frame, text="At Griha Hostel, we are dedicated to providing a \n comfortable and cozy environment for all our \n residents. Our aim is to create a home away \n from home where everyone feels relaxed and at \n ease. From well-furnished rooms to thoughtfully \n  designed common areas, every aspect of our \n  hostel is geared towards ensuring maximum \ncomfort and convenience for our guests.",
                                         font=("bold",14), text_color="black", justify=LEFT)
    hygiene_label.place(relx=0 ,rely=0.14)

def comfort_back():
        comfort_frame.destroy()

def security():
    global security_frame

    security_btn.configure(fg_color="#9CD9E4")
    security_frame= customtkinter.CTkFrame(master=app, width=320, height=200, fg_color="#9CD9E4")
    security_frame.place(relx=0.59, rely=0.46)

    back_btn=customtkinter.CTkButton(master=security_frame, text="X", width=20, height=10 ,command=security_back)
    back_btn.place(relx=0.9, rely=0.02)

    hygiene_label=customtkinter.CTkLabel(master=security_frame, text="At Griha Hostel, the safety and security of our \n residents is our top priority. We have \nimplemented comprehensive security measures \nto create a safe living environment where\n everyone can feel protected and secure. From \nadvanced surveillance systems to strict access \ncontrols, every aspect of our security \ninfrastructure is designed to provide peace of \nmind to our guests.",
                                         font=("bold",14), text_color="black", justify=LEFT)
    hygiene_label.place(relx=0 ,rely=0.14)

def security_back():
        security_frame.destroy()



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

    Content_label= customtkinter.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \n comfortable living environment for\n students abd professionals.With\n modern amenities and facilities,and a\n supportive community,Griha hostel\n ensures a home-like experience away\n from home.", justify= LEFT,
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


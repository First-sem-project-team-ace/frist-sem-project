from tkinter import *
import customtkinter
from PIL import Image
from tkinter import messagebox


import sqlite3

# def login_page():
#     login_window = customtkinter.CTk()
#     login_window.title("Login")

#     customtkinter.set_appearance_mode('light')
#     screen_width = login_window.winfo_screenwidth()
#     screen_height = login_window.winfo_screenheight()
#     login_window.geometry(f"{screen_width}x{screen_height}+0+0")

#     frame = customtkinter.CTkFrame(master=login_window, width=screen_width, height=screen_height, bg_color="white", fg_color="#614BD4")
#     frame.place(relx=0, rely=0)

#     Linear_image = customtkinter.CTkImage(light_image=Image.open('images\\linear homepage backgroud.png'), size=(screen_width,screen_height))
#     Linear_image_label = customtkinter.CTkLabel(master=frame, image=Linear_image,text="")
#     Linear_image_label.place(x=0, y=0)

#     my_image = customtkinter.CTkImage(light_image=Image.open('images\\Hostel.jpg'), size=(screen_width, 400))
#     my_label = customtkinter.CTkLabel(master=frame, image=my_image,text="")
#     my_label.place(relx=0, rely=0.6)

#     Login_frame = customtkinter.CTkFrame(master=login_window, fg_color="white", width=300, height=300)
#     Login_frame.place(relx=0.7, rely=0.1)

#     Login_welcome = Label(master=Login_frame, text="Welcome to Griha Hostel", fg="black", bg="white")
#     Login_welcome.place(relx=0.3, rely=0)

#     Login_label = Label(master=Login_frame, text="Log In", font=("bold", 25), bg="white", fg="#614BD4")
#     Login_label.place(relx=0.1, rely=0.1)

#     email_label = Label(master=Login_frame, text="Email:", bg="white", fg="black", font=("20"))
#     email_label.place(relx=0.03, rely=0.3)
#     password_label = Label(master=Login_frame, text="Password:", bg="white", fg="Black", font=("20"))
#     password_label.place(relx=0.03, rely=0.4)

#     email_entry = customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
#     email_entry.place(relx=0.3, rely=0.3)
#     password_entry = customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white", show="*")
#     password_entry.place(relx=0.3, rely=0.4)

#     def show_pass():
#         if show_password_var.get() == 1:
#             password_entry.configure(show="")
#         else:
#             password_entry.configure(show="*")

#     show_password_var = IntVar()
#     chk = Checkbutton(master=Login_frame, text="Show password", variable=show_password_var, onvalue=1, offvalue=0, command=show_pass)
#     chk.place(relx=0.5, rely=0.5)

#     Btn_login = customtkinter.CTkButton(master=Login_frame, text="Login", width=90, fg_color="#614BD4", text_color="white")
#     Btn_login.place(relx=0.65, rely=0.6)

#     login_window.mainloop()

# if __name__ == "__main__":
#     login_page()



def login_page():
    login_window = customtkinter.CTk()
    login_window.title("Login")

    customtkinter.set_appearance_mode('light')
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    login_window.geometry(f"{screen_width}x{screen_height}+0+0")
    def login():
        global username
        conn = sqlite3.connect("hostel.db")
        c = conn.cursor()
    
        username = username_entry.get()
        password = password_entry.get()
    
        if not username or not password:
            messagebox.showerror("Error", "Please fill in both username and password")
            return
        c.execute("SELECT password FROM hostel WHERE username=?", (username,))
        result = c.fetchone()
            
        if username == "ram" and password == "1":
           login_window.destroy()
           import homepage
    

        elif result:
            stored_password = result[0]
            if stored_password == password:
                login_window.destroy()
    
                shared_state=username
                import student_homepage
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid username")
    
        conn.close()
        
    

    frame = customtkinter.CTkFrame(master=login_window, width=screen_width, height=screen_height, bg_color="white", fg_color="#614BD4")
    frame.place(relx=0, rely=0)
    
    
    
    Linear_image = customtkinter.CTkImage(light_image=Image.open('images\\linear homepage backgroud.png'), size=(screen_width,screen_height))
    Linear_image_label = customtkinter.CTkLabel(master=frame, image=Linear_image,text="")
    Linear_image_label.place(x=0, y=0)
    
    
    my_image = customtkinter.CTkImage(light_image=Image.open('images\\Hostel.jpg'), size=(screen_width, 400))
    my_label = customtkinter.CTkLabel(master=frame, image=my_image,text="")
    my_label.place(relx=0, rely=0.6)

    Login_frame = customtkinter.CTkFrame(master=login_window, fg_color="white", width=300, height=300)
    Login_frame.place(relx=0.7, rely=0.1)

    Login_welcome = Label(master=Login_frame, text="Welcome to Griha Hostel", fg="black", bg="white")
    Login_welcome.place(relx=0.3, rely=0)

    Login_label = Label(master=Login_frame, text="Log In", font=("bold", 25), bg="white", fg="#614BD4")
    Login_label.place(relx=0.1, rely=0.1)

    username_label = Label(master=Login_frame, text="Username:", bg="white", fg="black", font=("20"))
    username_label.place(relx=0.03, rely=0.3)
    password_label = Label(master=Login_frame, text="Password:", bg="white", fg="Black", font=("20"))
    password_label.place(relx=0.03, rely=0.4)
    username_entry = customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white")
    username_entry.place(relx=0.3, rely=0.3)
    password_entry = customtkinter.CTkEntry(master=Login_frame, width=200, fg_color="gray", text_color="white", corner_radius=10, bg_color="white", show="*")
    password_entry.place(relx=0.3, rely=0.4)


    def show_pass():
        if show_password_var.get() == 1:
            password_entry.configure(show="")
        else:
            password_entry.configure(show="*")

    show_password_var = IntVar()
    chk = Checkbutton(master=Login_frame, text="Show password", variable=show_password_var, onvalue=1, offvalue=0, command=show_pass)
    chk.place(relx=0.5, rely=0.5)

    Btn_login = customtkinter.CTkButton(master=Login_frame, text="Login", width=90, fg_color="#614BD4", 
                                        command=login,text_color="white")
    Btn_login.place(relx=0.65, rely=0.6)
    
    
    def forgot_password():
        login_window.destroy()
        import Forgotpass
                
    forgot_password_btn = customtkinter.CTkButton(master=Login_frame, text="Forgot Password?", width=120, fg_color="#42ABC7", 
                                                      command=forgot_password, text_color="white")
    forgot_password_btn.place(relx=0.05, rely=0.6)

    def about():
   
       
       About_frame= customtkinter.CTkFrame(master=login_window, height=300, width=500, fg_color="#42ABC7")
       About_frame.place(relx=0.3, rely=0.2)
   
       About_label=customtkinter.CTkLabel(master=About_frame, text="About us", font=("bold",25), text_color="white")
       About_label.place(relx=0.05, rely=0.15)
   
       Content_label= customtkinter.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \ncomfortable living environment for\n students abd professionals.With\n modern amenities and facilities,and a\n supportive community,Griha hostel\n ensures a home-like experience away\n from home.", justify= LEFT,
                                   text_color="white", font=("bold",20))
       Content_label.place(relx=0.1, rely=0.25)

       def back():

        About_frame.destroy()
        

       Exit_button= customtkinter.CTkButton(master=About_frame, text="X", command=back, width=30)
       Exit_button.place(relx=0.9, rely=0.05)   

    What_btn= customtkinter.CTkButton(master=frame,text="?", bg_color="#3FB5CB",fg_color="#3FB5CB",width=50, text_color="black",
                           corner_radius=80, font=("bold", 20), command=about)
    What_btn.place(relx=0.7, rely=0.05)

    login_window.mainloop()
    
login_page()







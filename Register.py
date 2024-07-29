import customtkinter as Ctk
from tkinter import *
from tkinter import font
from PIL import Image
import Login

def Register_page():

  Registerpage= Ctk.CTk()
  
  
  Ctk.set_appearance_mode('light')
  Registerpage.geometry("{0}x{1}+0+0".format(Registerpage.winfo_screenwidth(), Registerpage.winfo_screenheight()))
  screen_width = Registerpage.winfo_screenwidth()
  screen_height = Registerpage.winfo_screenheight()
  Registerpage.configure(bg_color="white")

  def login():

    Registerpage.destroy()
    Login.login_page()
  
  
  
  # add `from PIL import Image` on top
  Hostel_image = Ctk.CTkImage(light_image=Image.open('images\\HostelImage.jpg'),
                                    size=(500, screen_height))
  
  # add `from PIL import Image` on top
  Hostel_logo = Ctk.CTkImage(light_image=Image.open('images\\Hostel_logo.png'),
                                    size=(50, 40))
  
  Image_label= Ctk.CTkLabel(master=Registerpage, text="", image=Hostel_image)
  Image_label.place(relx=0, rely=0)
  
  Main_label= Ctk.CTkLabel(master=Registerpage, text="Griha Hostel", text_color="#323F76", font=("bold",35))
  Main_label.place(relx=0.6, rely=0.05)
  
  Logo_label= Ctk.CTkLabel(master=Registerpage, text="", image=Hostel_logo, fg_color="black", width=30, corner_radius=80,
                           bg_color="white")
  Logo_label.place(relx=0.55, rely=0.05)
  
  
  Create_account_label= Ctk.CTkLabel(master=Registerpage, text="Create a new account", font=("bold", 25),text_color="#323F76")
  Create_account_label.place(relx=0.4, rely=0.2)
  
  Username_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Username*", border_color="light gray",width=650, height=40, corner_radius=15)
  Username_entry.place(relx=0.4, rely=0.25)
  
  First_name_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="First Name*", border_color="light gray", width=300, height=40, corner_radius=15)
  First_name_entry.place(relx=0.4, rely=0.33)
  
  Last_name_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Last Name*", border_color="light gray", width=300, height=40, corner_radius=15)
  Last_name_entry.place(relx=0.65, rely=0.33)
  
  Password_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Password", border_color="light gray", width=300, height=40, corner_radius=15)
  Password_entry.place(relx=0.4, rely=0.41)
  
  Confirm_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Confirm password", border_color="light gray", width=300, height=40,corner_radius=15)
  Confirm_entry.place(relx=0.65, rely=0.41)
  
  Gender_label= Ctk.CTkLabel(master=Registerpage, text="Gender", font=("bold", 25),text_color="#323F76")
  Gender_label.place(relx=0.4, rely=0.5)
  
  var= IntVar()
  
  Male_button= Ctk.CTkRadioButton(master=Registerpage, text="Male", font=("bold",20), text_color="#323F76",
                                  variable=var, value=1)
  Male_button.place(relx=0.42, rely=0.55)
  
  Female_button= Ctk.CTkRadioButton(master=Registerpage, text="Female", font=("bold",20),text_color="#323F76",
                                    variable=var, value=2)
  Female_button.place(relx=0.55, rely=0.55)
  
  Non_binary= Ctk.CTkRadioButton(master=Registerpage, text="Non-Binary", font=("bold",20), text_color="#323F76",
                                 variable=var, value=3)
  Non_binary.place(relx=0.67, rely=0.55)
  
  Security_label= Ctk.CTkLabel(master=Registerpage, text="Security question:",font=("bold",25), text_color="#323F76")
  Security_label.place(relx=0.4, rely=0.63)
  
  Father_name_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Your Father Name*", width=300, height=40,
                                  border_color="light gray", corner_radius=15)
  Father_name_entry.place(relx=0.4, rely=0.7)
  
  Fathers_phone_number_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="His Phone Number", width=300, height=40, 
                                           corner_radius=15, border_color="light gray")
  
  Fathers_phone_number_entry.place(relx=0.65, rely=0.7)
  
  Sign_up_button= Ctk.CTkButton(master=Registerpage, text="Sign up", font=('bold',35), fg_color="#333D7A", text_color="white", 
                                corner_radius=15,width=650, height=40)
  Sign_up_button.place(relx=0.4, rely=0.78)
  
  Login_btn= Ctk.CTkButton(master=Registerpage, text="Already have an account? Login!", text_color="#E3A2CA", fg_color="#ebebeb", 
                           font=("bold",15), command=login)
  Login_btn.place(relx=0.4, rely=0.85)
  
  
  
   
  
  
  Registerpage.mainloop()

  if __name__ == "__main__":
    Register_page()

  
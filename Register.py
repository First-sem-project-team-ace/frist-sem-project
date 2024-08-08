import customtkinter as Ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import sqlite3



Registerpage= Ctk.CTk()

conn= sqlite3.connect("hostel.db")
c= conn.cursor()
c.execute(

    """CREATE TABLE IF NOT EXISTS hostel(
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        fav_food TEXT,
        pet_name TEXT,
        password TEXT


        )"""

)
conn.commit()
conn.close()

def sign_up():
    
    if Password_entry.get()!=Confirm_entry.get():
      messagebox.showerror("Error","Password did not match")

    elif Username_entry.get()=="":
       messagebox.showinfo("Username","Please fill your username")
       
    elif First_name_entry.get()=="":
       messagebox.showinfo("First Name","Plese fill your first name")

    elif Last_name_entry.get()=="":
       messagebox.showinfo("Last Name","Plese fill your last name")

    elif Password_entry.get()=="":
       messagebox.showinfo("Password","Plese fill your password")

    elif Confirm_entry.get()=="":
       messagebox.showinfo("Confirm Password","Plese fill your confirm password")

    elif Fav_food_entry.get()=="":
       messagebox.showinfo("Favrouite Food","Plese fill your favroutie food")

    elif Pet_name_entry.get()=="":
       messagebox.showinfo("Pet Name","Plese fill your pet name")
          

    
    else:
      conn= sqlite3.connect("hostel.db")
      c= conn.cursor()
      c.execute(
         "INSERT INTO hostel(username,first_name,last_name,gender,fav_food,pet_name,password) VALUES(?,?,?,?,?,?,?)",
         (Username_entry.get(), First_name_entry.get(),Last_name_entry.get(),get_gender(),Fav_food_entry.get(),Pet_name_entry.get(), Password_entry.get()),
  
      )
  
     
      conn.commit()
      conn.close()
  
      login()

  



Ctk.set_appearance_mode('light')
Registerpage.geometry("{0}x{1}+0+0".format(Registerpage.winfo_screenwidth(), Registerpage.winfo_screenheight()))
screen_width = Registerpage.winfo_screenwidth()
screen_height = Registerpage.winfo_screenheight()
Registerpage.configure(bg_color="white")

def login():
  Registerpage.destroy()
  import Login
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

def get_gender():
  if var.get()==1:
     return "Male"
  elif var.get()==2:
     return "Female"
  else:
     return "Non-Binary"

Non_binary= Ctk.CTkRadioButton(master=Registerpage, text="Non-Binary", font=("bold",20), text_color="#323F76",
                               variable=var, value=3)
Non_binary.place(relx=0.67, rely=0.55)

Security_label= Ctk.CTkLabel(master=Registerpage, text="Security question:",font=("bold",25), text_color="#323F76")
Security_label.place(relx=0.4, rely=0.63)

Fav_food_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Your Favourite Food*", width=300, height=40,
                                border_color="light gray", corner_radius=15)
Fav_food_entry.place(relx=0.4, rely=0.7)

Pet_name_entry= Ctk.CTkEntry(master=Registerpage, placeholder_text="Your First Pet Name", width=300, height=40, 
                                         corner_radius=15, border_color="light gray")

Pet_name_entry.place(relx=0.65, rely=0.7)

Sign_up_button= Ctk.CTkButton(master=Registerpage, text="Sign up", font=('bold',35), fg_color="#333D7A", text_color="white", 
                              corner_radius=15,width=650, height=40, command=sign_up)
Sign_up_button.place(relx=0.4, rely=0.78)

Login_btn= Ctk.CTkButton(master=Registerpage, text="Already have an account? Login!", text_color="#E3A2CA", fg_color="#ebebeb", 
                         font=("bold",15), command=login)
Login_btn.place(relx=0.4, rely=0.85)



 


Registerpage.mainloop()



  
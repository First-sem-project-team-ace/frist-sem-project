import customtkinter as Ctk
import tkinter as tk
from PIL import Image



def profile():
        
        
          
        Profilepage= Ctk.CTk()
        Ctk.set_appearance_mode('light')
        Profilepage.geometry("{0}x{1}+0+0".format(Profilepage.winfo_screenwidth(), Profilepage.winfo_screenheight()))
        screen_width = Profilepage.winfo_screenwidth()
        screen_height = Profilepage.winfo_screenheight()
        Profile_page_frame= Ctk.CTkFrame(master=Profilepage, width=screen_width, height=screen_height, fg_color="#A7DCF5")
        Profile_page_frame.place(relx=0, rely=0)

        Update_profile_label= Ctk.CTkLabel(master=Profile_page_frame, text="Update Profile", text_color="#CD1818", font=("bold",35))
        Update_profile_label.place(relx=0.5, rely=0.05)


        Name_label= Ctk.CTkLabel(master=Profile_page_frame, text="Name:", text_color="black", font=("bold", 25))
        Name_label.place(relx=0.15, rely=0.2)

        Email_label= Ctk.CTkLabel(master=Profile_page_frame, text="Email:", text_color="Black",font=("bold",25))
        Email_label.place(relx=0.15, rely=0.3)

        Guardian_name_label= Ctk.CTkLabel(master=Profile_page_frame, text="Guardian's Name:", text_color="black", font=("bold",25))
        Guardian_name_label.place(relx=0.15, rely=0.4)

        Contact_no_label= Ctk.CTkLabel(master=Profile_page_frame, text="Contact No:", text_color="Black", font=("bold",25))
        Contact_no_label.place(relx=0.15, rely=0.5)

        Emergency_contact_label= Ctk.CTkLabel(master=Profile_page_frame, text="Emergency Contact no:", text_color="Black", font=("bold",25))
        Emergency_contact_label.place(relx=0.15, rely=0.6)

        Name_entry= Ctk.CTkEntry(master=Profile_page_frame, width=500, height=40)
        Name_entry.place(relx=0.4, rely=0.2)

        Email_entry= Ctk.CTkEntry(master=Profile_page_frame, width=500, height=40)
        Email_entry.place(relx=0.4, rely=0.3)

        Gurdian_name_entry= Ctk.CTkEntry(master=Profile_page_frame, width=500, height=40)
        Gurdian_name_entry.place(relx=0.4, rely=0.4)

        Contact_entry= Ctk.CTkEntry(master=Profile_page_frame, width=500, height=40)
        Contact_entry.place(relx=0.4, rely=0.5)

        Emergency_contact_entry= Ctk.CTkEntry(master=Profile_page_frame, width=500, height=40)
        Emergency_contact_entry.place(relx=0.4, rely=0.6)


        Profilepage.mainloop()

if __name__ == "__main__":
    profile()
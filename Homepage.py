import customtkinter as Ctk
from tkinter import *
from PIL import Image
from datetime import datetime
from tkinter import messagebox
import sqlite3
from Login import username


Homepage= Ctk.CTk()

Ctk.set_appearance_mode('light')
Homepage.geometry("{0}x{1}+0+0".format(Homepage.winfo_screenwidth(), Homepage.winfo_screenheight()))
screen_width = Homepage.winfo_screenwidth()
screen_height = Homepage.winfo_screenheight()

current_frame = None


    
def logout_system():
    
    Homepage.destroy()
    import Dashboard


def show_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = frame
    current_frame.place(relx=0.2, rely=0.14)
   

global Change_btn
global Menu_frame
global menu
menu_button=[]
button_color={}

def dashboard():
   
   
   dashboard_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100), fg_color="#EDF1F5")
   dashboard_frame.place(relx=0, rely=0.13)


   profile_frame= Ctk.CTkFrame(master=Homepage,width=250, height= 130, fg_color="white")
   profile_frame.place(relx=0, rely=0.13)

   profile_label= Ctk.CTkLabel(master=profile_frame, text=username)
   profile_label.place(relx=0.4, rely=0.4)

   # add `from PIL import Image` on top
   Profile_account_image = Ctk.CTkImage(light_image=Image.open('images\\profile.png'),
                                     size=(50, 50))

   profile_image_label= Ctk.CTkLabel(master=profile_frame, text="", image=Profile_account_image)
   profile_image_label.place(relx=0.1, rely=0.2)

   def menu():
    
     global Menu_frame
     global Change_btn, Change_frame
     global menu_button, button_color
   
     def menu_collapse():
         Menu_frame.destroy()
         Toggle_btn.configure(text="☰", command=menu)
         
   
   
     Menu_frame = Ctk.CTkFrame(master=dashboard_frame, width=250, height=screen_height, bg_color="white", fg_color="white")
     Menu_frame.place(relx=0, rely=0.2)

     # add `from PIL import Image` on top
     alert_image = Ctk.CTkImage(light_image=Image.open('images\\alert.png'),
                                       size=(30, 30))
     
     # add `from PIL import Image` on top
     speaker_image = Ctk.CTkImage(light_image=Image.open('images\\speaker.png'),
                                       size=(30, 30))
     invoice_image = Ctk.CTkImage(light_image=Image.open('images\\invoice.png'),
                                       size=(30, 30))
     emergency_image = Ctk.CTkImage(light_image=Image.open('images\\emergency.png'),
                                       size=(30, 30))
     setting_image = Ctk.CTkImage(light_image=Image.open('images\\setting.png'),
                                       size=(30, 30))
   
   
     
     Change_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Change Status", text_color="black", command=lambda: toggle_button("Change Status",change),
                        image=alert_image)
     Change_btn.place(relx=0, rely=0)
   
     Notice_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Notice", text_color="black", command=lambda: toggle_button("Notice",notice), 
                        image=speaker_image)
     Notice_btn.place(relx=0, rely=0.1) 
   
     Invoice_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Invoice", text_color="black", command=lambda: toggle_button("Invoice",invoice), 
                        image=invoice_image)
     Invoice_btn.place(relx=0, rely=0.2)
   
     Complaint_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Complaint", text_color="black", command=lambda: toggle_button("Complaint",complaint))
     Complaint_btn.place(relx=0, rely=0.3)
   
     Emergency_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Emergency Contact", text_color="black", command= lambda: toggle_button("Emergency Contact",emergency), 
                        image=emergency_image)
     Emergency_btn.place(relx=0, rely=0.4)
   
     Setting_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Setting", text_color="black", command=lambda: toggle_button("Setting", setting), image=setting_image)
     Setting_btn.place(relx=0, rely=0.5)
   
     menu_button=[Change_btn,Notice_btn,Invoice_btn, Complaint_btn,Emergency_btn, Setting_btn]
     button_color={btn.cget("text"): False for btn in menu_button}
   
     
   
     Toggle_btn.configure(text="X", command=menu_collapse)
   
   
   def reset_all_btn():
      for btn in menu_button:
         btn.configure(fg_color="#3FB5CB")
         button_color[btn.cget("text")]=False
   
   def toggle_button(button_name, frame_function):
       if button_color[button_name]:
           reset_all_btn()
           button_color[button_name] = False
       else:
           reset_all_btn()
           for btn in menu_button:
               if btn.cget("text") == button_name:
                   btn.configure(fg_color="#1AD8E4")
                   button_color[btn.cget("text")] = True
       show_frame(frame_function())
   
   
   def change():
      
      global Change_btn
   
      global Change_frame
      Change_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100))
      Change_frame.place(relx=0.2, rely=0)

      ChangeRoom_btn= Ctk.CTkButton(master=Change_frame, text="Change room", width=250, height=100, fg_color="#585454", bg_color="white",
                                font=("bold",20))
      ChangeRoom_btn.place(relx=0.15, rely=0.2)
   
      swap_btn= Ctk.CTkButton(master=Change_frame, text="Swap Bed", width=250, height=100, fg_color="#585454",  bg_color="white",
                                font=("bold",20))
      swap_btn.place(relx=0.55, rely=0.2)
   
      Room_upgrade= Ctk.CTkButton(master=Change_frame, text="Room Upgrade", width=250, height=100, fg_color="#585454", bg_color="white", 
                                font=("bold",20))
      Room_upgrade.place(relx=0.15, rely=0.4)
   
      occupancy_btn= Ctk.CTkButton(master=Change_frame, text="Occupancy Status", width=250, height=100, fg_color="#585454", bg_color="white", 
                                font=("bold",20))
      occupancy_btn.place(relx=0.55, rely=0.4)
   
      Change_btn.configure(fg_color="gray")
   
      # add `from PIL import Image` on top
      oldnew_image = Ctk.CTkImage(light_image=Image.open('images\\oldnew.png'),
                                        size=(300, 200))
      oldnew_label= Ctk.CTkLabel(master=Change_frame, image=oldnew_image,text="" )
      oldnew_label.place(relx=0.3,rely=0.65)
   
      Go_room_btn= Ctk.CTkButton(master=Change_frame, text="Go To Room Details", fg_color="dark blue", bg_color="white",
                                 corner_radius=10, height=50, width=150, command=room)
      Go_room_btn.place(relx=0.65, rely=0.75)
   
      return Change_frame
   
   
   def notice():
      Notice_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5", corner_radius=20)
      Notice_frame.place(relx=0.25, rely=0)
   
      Cont_frame= Ctk.CTkFrame(master=Notice_frame, width=(screen_width-500), height=(400), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
      Cont_frame.place(relx=0.1, rely=0.2)
   
      Feature_label= Ctk.CTkLabel(master=Notice_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
      Feature_label.place (relx=0, rely=0.05)
   
      Notice_label= Ctk.CTkLabel(master=Cont_frame, text="Notices:", text_color="black", font=("bold",25))
      Notice_label.place(relx=0.02, rely=0.05)
      return Notice_frame
   
   
   def invoice():
       Invoice_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
       Invoice_frame.place(relx=0.25, rely=0)
   
       Cont_frame= Ctk.CTkFrame(master=Invoice_frame, width=(screen_width-500), height=(400), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
       Cont_frame.place(relx=0.1, rely=0.2)
   
       Feature_label= Ctk.CTkLabel(master=Invoice_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
       Feature_label.place (relx=0, rely=0.05)
   
    
   
       Invoice_label= Ctk.CTkLabel(master=Cont_frame, text="INVOICE:", font=("bold", 25), text_color="black")
       Invoice_label.place(relx=0.05, rely=0.1)
   
    #    current_month = datetime.now().strftime("%B")

       Month_amount_label= Ctk.CTkLabel(master=Cont_frame, text="Month\t\t\t\tAmount")
       Month_amount_label.place(relx=0.1, rely=0.2)

       Proceed_button= Ctk.CTkButton(master=Cont_frame, text="Proceed to pay", font=("bold", 20), fg_color="#17EBAB")
       Proceed_button.place(relx=0.7, rely=0.92)

   
       return Invoice_frame
   
   def complaint():
      
       Complaint_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
       Complaint_frame.place(relx=0.25, rely=0)
   
   
       Cont_frame= Ctk.CTkFrame(master=Complaint_frame, width=(screen_width-500), height=(400), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
       Cont_frame.place(relx=0.1, rely=0.2)
   
       Feature_label= Ctk.CTkLabel(master=Complaint_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
       Feature_label.place (relx=0, rely=0.05)
   
    
   
       Complaint_label= Ctk.CTkLabel(master=Cont_frame, text="Complaint:", font=("bold", 25), text_color="black")
       Complaint_label.place(relx=0.05, rely=0.05)
   
       Subject_label= Ctk.CTkLabel(master=Cont_frame, text="Subject:", font=("bold",20))
       Subject_label.place(relx=0.1, rely=0.15)
   
       Subject_entry= Ctk.CTkEntry(master=Cont_frame, placeholder_text="Write your subject here",
       width=400, placeholder_text_color="black", fg_color="#EDF1F5")
       Subject_entry.place(relx=0.2, rely=0.15)
   
       Complaint_text = Text(master=Cont_frame, height=15, width=85, wrap=WORD, bg='#EDF1F5', fg='black')
       Complaint_text.place(relx=0.1, rely=0.3)

       submit_button= Ctk.CTkButton(master=Cont_frame, text="Submit Complain", font=("bold", 20), fg_color="#17EBAB")
       submit_button.place(relx=0.7, rely=0.92)
   
       return Complaint_frame
   
   def emergency():
   
      Emergency_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100), fg_color="#EDF1F5")
      Emergency_frame.place(relx=0.25, rely=0)
   
   
      Feature_label= Ctk.CTkLabel(master=Emergency_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
      Feature_label.place (relx=0, rely=0.05)

      
      Cont_frame= Ctk.CTkFrame(master=Emergency_frame, width=(screen_width-500), height=(400), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
      Cont_frame.place(relx=0.1, rely=0.2)

      Contact_label= Ctk.CTkLabel(master=Cont_frame, text="Contacts:", font=("bold", 25), text_color="black")
      Contact_label.place(relx=0.05, rely=0.05)

      Header_label= Ctk.CTkLabel(master=Cont_frame, text="Relation \t\t\t\t Number", text_color="black", font=("bold", 25))
      Header_label.place(relx=0.18, rely=0.25)

      Father_contact= Ctk.CTkLabel(master=Cont_frame, text="Father \t\t\t\t +977-98XXXXXXXX",font=("bold", 20) )
      Father_contact.place(relx=0.2, rely=0.4)
      
      Mother_contact= Ctk.CTkLabel(master=Cont_frame, text="Mother \t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Mother_contact.place(relx=0.2, rely=0.55)

      Police_contace= Ctk.CTkLabel(master=Cont_frame, text="Police \t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Police_contace.place(relx=0.2, rely=0.7)
      
      Warden_contact= Ctk.CTkLabel(master=Cont_frame, text="Warden \t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Warden_contact.place(relx=0.2, rely=0.85)
      

   
      return Emergency_frame
   
   def setting():
      
      global Cont_frame
      global Setting_frame
      global Search_entry
      Setting_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
      Setting_frame.place(relx=0.25, rely=0)
   
      Cont_frame= Ctk.CTkFrame(master=Setting_frame, width=(screen_width-500), height=(400), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
      Cont_frame.place(relx=0.1, rely=0.2)
   
      Feature_label= Ctk.CTkLabel(master=Setting_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
      Feature_label.place (relx=0.05, rely=0.05)
   
      Notice_label= Ctk.CTkLabel(master=Cont_frame, text="Setting:", text_color="black", font=("bold",25))
      Notice_label.place(relx=0.05, rely=0.1)
   
      Search_entry= Ctk.CTkEntry(master=Cont_frame, placeholder_text="Search setting", width=300, height=30,text_color="black",fg_color="#EDF1F5")
      Search_entry.place(relx=0.3, rely=0.2)



      # add `from PIL import Image` on top

      # add `from PIL import Image` on top
      search_image = Ctk.CTkImage(light_image=Image.open('images\\search.png'),
                                        size=(15, 15))
      contact_image = Ctk.CTkImage(light_image=Image.open('images\\contact.png'),
                                        size=(20, 20))
      
      account_image = Ctk.CTkImage(light_image=Image.open('images\\account.png'),
                                        size=(20, 20))
      logout_image = Ctk.CTkImage(light_image=Image.open('images\\logout.png'),
                                        size=(20, 20))
      
      Search_btn= Ctk.CTkButton(master=Search_entry, image=search_image, text="", fg_color="#EDF1F5", width=100, height=10,
                                 border_color="light gray", command= search)
      Search_btn.place(relx=0.7, rely=0.1)

   
   
      Profile_btn= Ctk.CTkButton(master=Cont_frame, text="Profile", width=400, height=30,fg_color="#EDF1F5", text_color="black",
                                 anchor=W, image=account_image, command=profile)
      Profile_btn.place(relx=0.15, rely=0.4)
   
      Change_passoword_btn= Ctk.CTkButton(master=Cont_frame, text="Change Password", width=400, height=30, text_color="black",
                                              image=notification_image, fg_color="#EDF1F5", anchor=W, command=change_pass)
      Change_passoword_btn.place(relx=0.15, rely=0.5)
   
      Update_contact_btn= Ctk.CTkButton(master=Cont_frame, text="Update contact", width=400, height=30, fg_color="#EDF1F5", text_color="black",
                                         anchor=W, image=contact_image, command=update_contact)
      Update_contact_btn.place(relx=0.15, rely=0.6)
   
      Logout_btn= Ctk.CTkButton(master=Cont_frame, text="Log out", width=400, height=30, fg_color="#EDF1F5", text_color="black",
                                        anchor=W, image=logout_image, command=logout)
      Logout_btn.place(relx=0.15, rely=0.7)

      return Setting_frame
   

   

   def profile():
        
        global Cont_frame
        global Profile_page_frame
          
        Profile_page_frame= Ctk.CTkFrame(master=Cont_frame, width=screen_width, height=screen_height, fg_color="#A7DCF5")
        Profile_page_frame.place(relx=0, rely=0)

        Update_profile_label= Ctk.CTkLabel(master=Profile_page_frame, text="Update Profile", text_color="#CD1818", font=("bold",20))
        Update_profile_label.place(relx=0.3, rely=0.01)


        Name_label= Ctk.CTkLabel(master=Profile_page_frame, text="Name:", text_color="black", font=("bold", 20))
        Name_label.place(relx=0.05, rely=0.1)

        Email_label= Ctk.CTkLabel(master=Profile_page_frame, text="Email:", text_color="Black",font=("bold",20))
        Email_label.place(relx=0.05, rely=0.18)

        Guardian_name_label= Ctk.CTkLabel(master=Profile_page_frame, text="Guardian's Name:", text_color="black", font=("bold",20))
        Guardian_name_label.place(relx=0.05, rely=0.26)

        Contact_no_label= Ctk.CTkLabel(master=Profile_page_frame, text="Contact No:", text_color="Black", font=("bold",20))
        Contact_no_label.place(relx=0.05, rely=0.34)

        Emergency_contact_label= Ctk.CTkLabel(master=Profile_page_frame, text="Emergency Contact no:", text_color="Black", font=("bold",20))
        Emergency_contact_label.place(relx=0.05, rely=0.42)

        Name_entry= Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
        Name_entry.place(relx=0.25, rely=0.1)

        Email_entry= Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
        Email_entry.place(relx=0.25, rely=0.18)

        Gurdian_name_entry= Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
        Gurdian_name_entry.place(relx=0.25, rely=0.26)

        Contact_entry= Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
        Contact_entry.place(relx=0.25, rely=0.34)

        Emergency_contact_entry= Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
        Emergency_contact_entry.place(relx=0.25, rely=0.42)

        Submit_btn= Ctk.CTkButton(master=Profile_page_frame, text="Submit", fg_color="#3FB5CB")
        Submit_btn.place(relx=0.5, rely=0.48)

         # add `from PIL import Image` on top
        Back_image = Ctk.CTkImage(light_image=Image.open('images\\back.png'),
                                          size=(30, 30))

        Back_btn= Ctk.CTkButton(master=Profile_page_frame, text="", image=Back_image, fg_color="#A7DCF5", command=profile_back)
        Back_btn.place(relx=0.01,rely=0.01)


        return Profile_page_frame
   
   def profile_back():
       
       
       Profile_page_frame.destroy()

   def change_pass():
       
       global Cont_frame
       global change_pass_page_frame

       change_pass_page_frame= Ctk.CTkFrame(master=Cont_frame, width=screen_width, height=screen_height, fg_color="#A7DCF5")
       change_pass_page_frame.place(relx=0, rely=0)   
       change_pass_label= Ctk.CTkLabel(master=change_pass_page_frame, text="Change Password", text_color="#CD1818", font=("bold",20))
       change_pass_label.place(relx=0.3, rely=0.01)   
       Old_pass_label= Ctk.CTkLabel(master=change_pass_page_frame, text="Old Password:", text_color="black", font=("bold", 20))
       Old_pass_label.place(relx=0.05, rely=0.1)   
       new_pass_label= Ctk.CTkLabel(master=change_pass_page_frame, text="New Password:", text_color="Black",font=("bold",20))
       new_pass_label.place(relx=0.05, rely=0.18)   
       confirm_pass_label= Ctk.CTkLabel(master=change_pass_page_frame, text="Confirm New Password:", text_color="black", font=("bold",20))
       confirm_pass_label.place(relx=0.05, rely=0.26)   


       Old_pass_entry= Ctk.CTkEntry(master=change_pass_page_frame, width=350, height=40)
       Old_pass_entry.place(relx=0.25, rely=0.1)   
       New_pass_entry= Ctk.CTkEntry(master=change_pass_page_frame, width=350, height=40)
       New_pass_entry.place(relx=0.25, rely=0.18)   
       Confirm_pass_entry= Ctk.CTkEntry(master=change_pass_page_frame, width=350, height=40)
       Confirm_pass_entry.place(relx=0.25, rely=0.26)

       Attempt_label= Ctk.CTkLabel(master=change_pass_page_frame, text="Attempt Securiy Question", text_color="black",
                                    font=("bold",20))
       Attempt_label.place(relx=0.2, rely=0.34)

       Favourite_food_label= Ctk.CTkLabel(master=change_pass_page_frame, text="Favourite Food:", font=("bold",20))
       Favourite_food_label.place(relx=0.13, rely=0.38)
       First_pet_name_label= Ctk.CTkLabel(master=change_pass_page_frame, text="First pet name:", font=("bold",20))
       First_pet_name_label.place(relx=0.13, rely=0.42)

       Favourite_food_entry= Ctk.CTkEntry(master=change_pass_page_frame, width=250, height=30)
       Favourite_food_entry.place(relx=0.25, rely=0.38)
       First_pet_name_entry= Ctk.CTkEntry(master=change_pass_page_frame, width=250, height=30)
       First_pet_name_entry.place(relx=0.25,rely=0.42)

       Update_btn= Ctk.CTkButton(master=change_pass_page_frame, text="Update", font=("bold",25), fg_color="#3FB5CB",
                                 text_color="black")
       Update_btn.place(relx=0.5, rely=0.45)

       Back_image = Ctk.CTkImage(light_image=Image.open('images\\back.png'),
                                          size=(30, 30))

       Back_btn= Ctk.CTkButton(master=change_pass_page_frame, text="", image=Back_image, fg_color="#A7DCF5", command=change_pass_back)
       Back_btn.place(relx=0.01,rely=0.01)
   
   def change_pass_back():
       global change_pass_page_frame
       
       change_pass_page_frame.destroy()

   def update_contact():
       global Cont_frame
       global update_contact_frame

       update_contact_frame=Ctk.CTkFrame(master=Cont_frame, width=screen_height, height=screen_height, fg_color="#A7DCF5")
       update_contact_frame.place(relx=0, rely=0)

       update_contact_label= Ctk.CTkLabel(master=update_contact_frame, text="Update contact", text_color="#CD1818", font=("bold",20))
       update_contact_label.place(relx=0.4, rely=0.01)   
       Father_contact_label= Ctk.CTkLabel(master=update_contact_frame, text="Father's contact no:", text_color="black", font=("bold", 20))
       Father_contact_label.place(relx=0.05, rely=0.1)   
       Mother_contact_label= Ctk.CTkLabel(master=update_contact_frame, text="Mother's contact no:", text_color="Black",font=("bold",20))
       Mother_contact_label.place(relx=0.05, rely=0.18)  

       Father_contact_entry= Ctk.CTkEntry(master=update_contact_frame, width=350, height=40)
       Father_contact_entry.place(relx=0.35, rely=0.1)   
       Mother_contact_entry= Ctk.CTkEntry(master=update_contact_frame, width=350, height=40)
       Mother_contact_entry.place(relx=0.35, rely=0.18)  
       
       Update_btn= Ctk.CTkButton(master=update_contact_frame, text="Update", font=("bold",25), fg_color="#3FB5CB",
                                 text_color="black")
       Update_btn.place(relx=0.6, rely=0.3)

       Back_image = Ctk.CTkImage(light_image=Image.open('images\\back.png'),
                                          size=(30, 30))

       Back_btn= Ctk.CTkButton(master=update_contact_frame, text="", image=Back_image, fg_color="#A7DCF5", command=update_contact_back)
       Back_btn.place(relx=0.01,rely=0.01)


   def update_contact_back():
       global update_contact_frame

       update_contact_frame.destroy()

   def logout():
       
       global Cont_frame
       global logout_frame

       logout_frame= Ctk.CTkFrame(master=Cont_frame, width=screen_width, height=screen_height, fg_color="#A7DCF5") 
       logout_frame.place(relx=0, rely=0)

       # add `from PIL import Image` on top
       Logout_image = Ctk.CTkImage(light_image=Image.open('images\\Tussinajao.png'),
                                         size=(400, 400))
       Logout_image_label= Ctk.CTkLabel(master=logout_frame, text="", image=Logout_image)
       Logout_image_label.place(relx=0, rely=0)

       Logout_label= Ctk.CTkLabel(master=logout_frame, text="Log Out", text_color="#CD1818", font=("bold",25))
       Logout_label.place(relx=0.4,rely=0.05)

       Question_label= Ctk.CTkLabel(master=logout_frame, text="Are you sure you want to Log Out?",text_color="black",
                                    font=("bold",20))
       Question_label.place(relx=0.35, rely=0.17)

       Option_frame= Ctk.CTkFrame(master=logout_frame, width=200, height=40)
       Option_frame.place(relx=0.38, rely=0.24)

       Logout_btn= Ctk.CTkButton(master=Option_frame, text="Log out", fg_color="#D9D9D9", width=100, height=40,text_color="black",
                                 command=logout_system)
       Logout_btn.place(relx=0, rely=0)

       Stay_btn= Ctk.CTkButton(master=Option_frame,text="Stay", fg_color="#3FB5CB", width= 100, height=40, text_color="black",
                               command=stay)
       Stay_btn.place(relx=0.5, rely=0)


   def stay():
       global logout_frame

       logout_frame.destroy()


   def search():
       
       global Search_entry

       value = Search_entry.get()
       
       if value.lower() in ["profile", "update profile"]:
           return profile()
       elif value.lower() in ["password", "change password"]:
           return change_pass()
       elif value.lower() in ["contact", "update contact"]:
           return update_contact()
       elif value.lower() in ["log out", "logout"]:
           return logout()
       else:
           return messagebox.showinfo("Info", "Invalid Search")
       
       

   
       

       
       



      
   
   menu()
   toggle_button("Change Status", change)

   return dashboard_frame
   
   

def room():

    Menu_frame.destroy()
    current_frame.destroy()

    room_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100) )
    room_frame.place(relx=0, rely=0.13)

   # add `from PIL import Image` on top
    Background_image = Ctk.CTkImage(light_image=Image.open('images\\Screenshot 2024-07-18 141337.png'),
                                     size=(screen_width, screen_height))
   
    image_label=Ctk.CTkLabel(master=room_frame, image=Background_image, text="")
    image_label.place(relx=0, rely=0)

    # add `from PIL import Image` on top
    Room_image = Ctk.CTkImage(light_image=Image.open('images\\Room_image.png'),
                                      size=((screen_width-100), 300))
    
    Room_image_label= Ctk.CTkLabel(master=room_frame, image=Room_image, text="")
    Room_image_label.place(relx=0, rely=0.5)
  

    Occupied_frame= Ctk.CTkFrame(master=room_frame,width=200, height=70, fg_color="dark blue", corner_radius=15)
    Occupied_frame.place(relx=0.01, rely=0.23)
    Occupied_label= Ctk.CTkLabel(master=Occupied_frame, text="Occupied", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    Occupied_label.place(relx=0.3, rely=0.01)
    Occupied_num= Ctk.CTkLabel(master=Occupied_frame, text="50", text_color="white", fg_color="dark blue",
                               width=30, height=30, font=("bold", 30))
    Occupied_num.place(relx=0.3, rely=0.4)

    vacant_frame= Ctk.CTkFrame(master=room_frame,width=200, height=70, fg_color="dark blue", corner_radius=15)
    vacant_frame.place(relx=0.2, rely=0.23)
    vacant_label= Ctk.CTkLabel(master=vacant_frame, text="Vacant", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    vacant_label.place(relx=0.3, rely=0.01)
    vacant_num= Ctk.CTkLabel(master=vacant_frame, text="15", text_color="white", fg_color="dark blue",
                               width=30, height=30, font=("bold", 30))
    vacant_num.place(relx=0.3, rely=0.4)

    tenant_frame= Ctk.CTkFrame(master=room_frame,width=200, height=70, fg_color="dark blue", corner_radius=15)
    tenant_frame.place(relx=0.4, rely=0.23)
    tenant_label= Ctk.CTkLabel(master=tenant_frame, text="Tenant", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    tenant_label.place(relx=0.3, rely=0.01)
    tenant_num= Ctk.CTkLabel(master=tenant_frame, text="100", text_color="white", fg_color="dark blue",
                               width=30, height=30, font=("bold", 30))
    tenant_num.place(relx=0.3, rely=0.4)

    ac_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=70, fg_color="dark blue", corner_radius=15)
    ac_room_frame.place(relx=0.01, rely=0.4)
    ac_room_label= Ctk.CTkLabel(master=ac_room_frame, text="Ac room", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    ac_room_label.place(relx=0.3, rely=0.01)
    ac_room_num= Ctk.CTkLabel(master=ac_room_frame, text="20", text_color="white", fg_color="dark blue",
                               width=30, height=30, font=("bold", 30))
    ac_room_num.place(relx=0.3, rely=0.4)

    normal_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=70, fg_color="dark blue", corner_radius=15)
    normal_room_frame.place(relx=0.2, rely=0.4)
    normal_room_label= Ctk.CTkLabel(master=normal_room_frame, text="Normal", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    normal_room_label.place(relx=0.3, rely=0.01)
    normal_room_num= Ctk.CTkLabel(master=normal_room_frame, text="30", text_color="white", fg_color="dark blue",
                               width=30, height=30, font=("bold", 30))
    normal_room_num.place(relx=0.3, rely=0.4)

    return room_frame

def special_req():

    Menu_frame.destroy()
    current_frame.destroy()

    special_req_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100) )
    special_req_frame.place(relx=0, rely=0.13)

    #Leave Request Frame

    Leave_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=300, fg_color="#3FB5CB")
    Leave_frame.place(relx=0.05, rely=0.01)

    Request_label=Ctk.CTkLabel(master=Leave_frame, text="Request to leave", text_color="White", font=("bold",25))
    Request_label.place(relx=0.01, rely=0.05)

    Reason_text= Text(master=Leave_frame, width=50, height=5, wrap=WORD, bg="#1AD8E4")
    Reason_text.place(relx=0, rely=0.18)

    Days_label= Ctk.CTkLabel(master=Leave_frame, text="Days to take leave:", font=("bold",15))
    Days_label.place(relx=0.05, rely=0.5)

    Days_entry= Ctk.CTkEntry(master=Leave_frame, width=100, height=30, fg_color="#1AD8E4" )
    Days_entry.place(relx=0.45, rely=0.5)

    Question_label= Ctk.CTkLabel(master=Leave_frame, text="Did you inform your parents?", text_color="black", font=("bold",15))
    Question_label.place(relx=0.05, rely=0.65)

    Yes_no_var= IntVar()

    Yes_radio_button= Ctk.CTkRadioButton(master=Leave_frame, text="Yes", variable=Yes_no_var,value=1)
    Yes_radio_button.place(relx=0.65, rely=0.66)

    No_radio_button= Ctk.CTkRadioButton(master=Leave_frame, text="No", variable=Yes_no_var, value=2)
    No_radio_button.place(relx=0.65, rely=0.75)

    Submit_btn= Ctk.CTkButton(master=Leave_frame, text="Submit", fg_color="#1AD8E4", text_color="black", font=("bold",20))
    Submit_btn.place(relx=0.3, rely=0.85)


     #Meal Preference Frame
    Meal_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=300, fg_color="#3FB5CB")
    Meal_frame.place(relx=0.38, rely=0.01)

    Meal_label=Ctk.CTkLabel(master=Meal_frame, text="Meal Preferences", text_color="White", font=("bold",25))
    Meal_label.place(relx=0.01, rely=0.05)

    Iam_label= Ctk.CTkLabel(master=Meal_frame, text="I am:", text_color="black", font=("bold",15))
    Iam_label.place(relx=0.05, rely=0.2)

    Veg_nonveg_var= IntVar()

    Veg_radio_button= Ctk.CTkRadioButton(master=Meal_frame, text="Veg", variable=Veg_nonveg_var,value=1)
    Veg_radio_button.place(relx=0.25, rely=0.21)

    Non_veg_radio_button= Ctk.CTkRadioButton(master=Meal_frame, text="Non-veg", variable=Veg_nonveg_var, value=2)
    Non_veg_radio_button.place(relx=0.25, rely=0.3)

    Submit_btn= Ctk.CTkButton(master=Meal_frame, text="Submit", fg_color="#1AD8E4", text_color="black", font=("bold",15))
    Submit_btn.place(relx=0.4, rely=0.4)

    Egg_paneer_label= Ctk.CTkLabel(master=Meal_frame, text="Egg/Paneer", text_color="black", font=("bold",15))
    Egg_paneer_label.place(relx=0.05, rely=0.55)

    Egg_paneer_var= IntVar()

    Egg_radio_button= Ctk.CTkRadioButton(master=Meal_frame, text="Egg", variable=Egg_paneer_var,value=1)
    Egg_radio_button.place(relx=0.3, rely=0.6)

    Paneer_radio_button= Ctk.CTkRadioButton(master=Meal_frame, text="Paneer", variable=Egg_paneer_var, value=2)
    Paneer_radio_button.place(relx=0.3, rely=0.7)

    Change_preference_btn= Ctk.CTkButton(master=Meal_frame, text="Change", fg_color="#1AD8E4", text_color="black", font=("bold",15))
    Change_preference_btn.place(relx=0.3, rely=0.8)

    #Event Request Frame

    Event_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=300, fg_color="#3FB5CB")
    Event_frame.place(relx=0.7, rely=0.01)

    Event_label=Ctk.CTkLabel(master=Event_frame, text="Event Request", text_color="White", font=("bold",25))
    Event_label.place(relx=0.01, rely=0.05)

    Catagory_label= Ctk.CTkLabel(master=Event_frame, text="Catagory:", text_color="black", font=("bold",15))
    Catagory_label.place(relx=0.05, rely=0.2)

    catagory_var= IntVar()

    Education_radio_button= Ctk.CTkRadioButton(master=Event_frame, text="Education", variable=catagory_var,value=1)
    Education_radio_button.place(relx=0.25, rely=0.21)

    Games_radio_button= Ctk.CTkRadioButton(master=Event_frame, text="Mobile Games", variable=catagory_var, value=2)
    Games_radio_button.place(relx=0.25, rely=0.3)

    Sports_radio_button= Ctk.CTkRadioButton(master=Event_frame, text="Sports", variable=catagory_var,value=3)
    Sports_radio_button.place(relx=0.25, rely=0.39)

    Other_radio_button= Ctk.CTkRadioButton(master=Event_frame, text="Others", variable=catagory_var, value=4)
    Other_radio_button.place(relx=0.25, rely=0.48)

    Title_label= Ctk.CTkLabel(master=Event_frame, text="Specify the title", font=("bold",15))
    Title_label.place(relx=0.05, rely=0.56)

    Title_text= Text(master=Event_frame, width=50, height=3, wrap=WORD, bg="#1AD8E4")
    Title_text.place(relx=0, rely=0.65)

    Event_request_btn= Ctk.CTkButton(master=Event_frame, text="Request", fg_color=("#1AD8E4"), text_color="black")
    Event_request_btn.place(relx=0.35, rely=0.85)


    #Maintenace Request Frame

    Maintenance_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=250, fg_color="#3FB5CB")
    Maintenance_frame.place(relx=0.05, rely=0.5)

    Miantenance_label=Ctk.CTkLabel(master=Maintenance_frame, text="Maintenacne Request", text_color="White", font=("bold",25))
    Miantenance_label.place(relx=0.01, rely=0.05)

    Specify_label= Ctk.CTkLabel(master=Maintenance_frame, text="Specify what happened", font=("bold",15))
    Specify_label.place(relx=0.05, rely=0.2)

    Maintenance_text= Text(master=Maintenance_frame, width=50, height=5, wrap=WORD, bg="#1AD8E4")
    Maintenance_text.place(relx=0, rely=0.3)

    Maintenance_btn= Ctk.CTkButton(master=Maintenance_frame, text="Submit", fg_color="#1AD8E4", text_color="black")
    Maintenance_btn.place(relx=0.3, rely=0.7)





    







def about():

    
    About_frame= Ctk.CTkFrame(master=Homepage, height=300, width=500, fg_color="#42ABC7")
    About_frame.place(relx=0.6, rely=0.15)

    About_label=Ctk.CTkLabel(master=About_frame, text="About us", font=("bold",25), text_color="white")
    About_label.place(relx=0.05, rely=0.15)

    Content_label= Ctk.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \ncomfortable living environment for\n students abd professionals.With\n modern amenities and facilities,and a\n supportive community,Griha hostel\n ensures a home-like experience away\n from home.", justify= LEFT,
                                text_color="white", font=("bold",20))
    Content_label.place(relx=0.1, rely=0.25)

    def back():
      

        About_frame.destroy()
       
        

    Exit_button= Ctk.CTkButton(master=About_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)


    


Top_frame= Frame(master=Homepage, width=screen_width, height=100, bg="#3FB5CB", highlightbackground="black", highlightthickness=1,highlightcolor="red")
Top_frame.place(relx=0, rely=0)

Toggle_btn= Ctk.CTkButton(master=Top_frame, text="☰", font=("bold", 20), corner_radius=0,fg_color="#3FB5CB", bg_color="#5c54a4", command=dashboard)
Toggle_btn.place(relx=0.2, rely=0.05)

Hostel_label = Ctk.CTkLabel(master=Top_frame, text="Griha Hostel", font=("helvetica", 25, "bold"), text_color="white")
Hostel_label.place(relx=0.01, rely=0.05)

Lbl1= Ctk.CTkLabel(master=Top_frame, text="Hi, there", font=("helvetica", 15) , text_color="white")
Lbl1.place(relx=0.01, rely=0.29)

# add `from PIL import Image` on top
dashboard_image = Ctk.CTkImage(light_image=Image.open('images\\dashboard.png'),
                                  size=(20, 20))

Dashboard_btn= Ctk.CTkButton(master=Top_frame, text="Dashboard", text_color="black",font=("bold",15), fg_color="#3FB5CB",
                             command= dashboard, image=dashboard_image)
Dashboard_btn.place(relx=0.35, rely=0.4)

Room_btn= Ctk.CTkButton(master=Top_frame, text="Rooms", text_color="black", font=("bold",15),fg_color="#3FB5CB",
                         command=room)
Room_btn.place(relx=0.48, rely=0.4)

Special_req_btn= Ctk.CTkButton(master=Top_frame, text="Special Request", text_color="black", font=("bold",15),fg_color="#3FB5CB",
                               command= special_req)
Special_req_btn.place(relx=0.62, rely=0.4)

# add `from PIL import Image` on top
notification_image = Ctk.CTkImage(light_image=Image.open('images\\notification.png'),
                                  size=(20, 20))

# add `from PIL import Image` on top
calendar_image = Ctk.CTkImage(light_image=Image.open('images\\calendar.png'),
size=(20, 20))

# add `from PIL import Image` on top
profile_image = Ctk.CTkImage(light_image=Image.open('images\\profile.png'),
                                  size=(20, 20))

Notification_btn= Ctk.CTkButton(master=Top_frame, text="",fg_color="#3FB5CB", bg_color="#3FB5CB", corner_radius=80, 
                                width=40, image=notification_image)
Notification_btn.place(relx=0.75, rely=0.4)

Calender_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#3FB5CB",fg_color="#3FB5CB", 
                            corner_radius=80, width=30, image=calendar_image)
Calender_btn.place(relx=0.8, rely=0.4)

What_btn= Ctk.CTkButton(master=Top_frame,text="?", bg_color="#3FB5CB",fg_color="#3FB5CB",width=50, text_color="black",
                        corner_radius=80, font=("bold", 20), command=about)
What_btn.place(relx=0.85, rely=0.4)

Profile_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#3FB5CB",fg_color="#3FB5CB", width=40,
                           corner_radius=80, image=profile_image)
Profile_btn.place(relx=0.9, rely=0.4)

top_button=[Dashboard_btn,Room_btn,Special_req_btn]
button_color={btn.cget("text"): False for btn in top_button}


dashboard()




Homepage.mainloop()
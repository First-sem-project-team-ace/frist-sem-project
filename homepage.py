import customtkinter as Ctk
from tkinter import *
from PIL import Image
from datetime import datetime
from tkinter import messagebox
from Login import username
import sqlite3 





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
    current_frame.place(relx=0.2, rely=0.095)
   

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

   def menu():
    
     global Menu_frame
     global Change_btn
     global menu_button, button_color
   
     def menu_collapse():
         Menu_frame.destroy()
         Toggle_btn.configure(text="☰", command=menu)
         
   
   
     Menu_frame = Ctk.CTkFrame(master=Homepage, width=385, height=screen_height, bg_color="white", fg_color="white")
     Menu_frame.place(relx=0, rely=0.095)

     ownername_label=Ctk.CTkLabel(master=Menu_frame,text="Giriraj Rawat",font=("bold", 25),text_color="black",fg_color="white")
     ownername_label.place(relx=0.4,rely=0.1)
  
     ownerid_label=Ctk.CTkLabel(master=Menu_frame,text="id_no:0000001",font=("bold", 20),text_color="black",fg_color="white")
     ownerid_label.place(relx=0.4,rely=0.15)
  
  
     owner_image=Ctk.CTkImage(light_image=Image.open("images\\Owner_Profile.png"),
                           size=(73, 79) )
     owner_label= Ctk.CTkLabel(master=Menu_frame, image=owner_image,text="" )
     owner_label.place(relx=0.1,rely=0.1)

     # add `from PIL import Image` on top
     alert_image = Ctk.CTkImage(light_image=Image.open('images\\alert.png'),
                                       size=(30, 30))
     
     # add `from PIL import Image` on top
     speaker_image = Ctk.CTkImage(light_image=Image.open('images\\speaker.png'),
                                       size=(30, 30))
    
     emergency_image = Ctk.CTkImage(light_image=Image.open('images\\emergency.png'),
                                       size=(30, 30))
     setting_image = Ctk.CTkImage(light_image=Image.open('images\\setting.png'),
                                       size=(30, 30))
   
   
     
   
     Appeared_btn= Ctk.CTkButton(master=Menu_frame, width=385, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Appeared Request", text_color="black", command=lambda: toggle_button("Appeared Request",Appeared), 
                        image=speaker_image,compound=LEFT)
     Appeared_btn.place(relx=0, rely=0.4) 
   
     Report_btn= Ctk.CTkButton(master=Menu_frame, width=385, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Reports and Analytics", text_color="black", command=lambda: toggle_button("Reports and Analytics",Report), 
                        image=alert_image,compound=LEFT)
     Report_btn.place(relx=0, rely=0.3)
   
    
   
     Emergency_btn= Ctk.CTkButton(master=Menu_frame, width=385, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Emergency Contact", text_color="black", command= lambda: toggle_button("Emergency Contact",emergency), 
                        image=emergency_image,compound=LEFT)
     Emergency_btn.place(relx=0, rely=0.5)
   
     Setting_btn= Ctk.CTkButton(master=Menu_frame, width=385, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Setting", text_color="black", command=lambda: toggle_button("Setting", setting), image=setting_image,compound=LEFT)
     Setting_btn.place(relx=0, rely=0.6)
   
     menu_button=[Appeared_btn,Report_btn, Emergency_btn, Setting_btn]
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
   
   
   def Report():
     Report_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
     Report_frame.place(relx=0.25, rely=0.95)
   
     Expense_label=Ctk.CTkLabel(master=Report_frame,text="Expenses", text_color="black", font=("bold",25))
     Expense_label.place(relx=0,rely=0)
     
     
     
     
     expense_frame=Ctk.CTkFrame(master=Report_frame,width=(screen_width-1600),height=(100),fg_color="#3FB5CB",corner_radius=10,bg_color="white")
     expense_frame.place(relx=0.3,rely=0.05)
     
     
     
     
     expense_label=Ctk.CTkLabel(master=expense_frame,text="Total Expense", text_color="black", font=("bold",20))
     expense_label.place(relx=0.03,rely=0.0)
     
     
     expense1_label=Ctk.CTkLabel(master=expense_frame,text="NRs. 52,00,000", text_color="white", font=("bold",30))
     expense1_label.place(relx=0.05,rely=0.5)
     
     
     
     furniture_frame=Ctk.CTkFrame(master=Report_frame,width=(screen_width-1600),height=(100),fg_color="#3FB5CB",corner_radius=10,bg_color="white")
     furniture_frame.place(relx=0.6,rely=0.05)
     
     furniture_label=Ctk.CTkLabel(master=furniture_frame,text="Furnitures and other Repairings", text_color="white", font=("bold",20))
     furniture_label.place(relx=0.03,rely=0.0)
     
     furniture1_label=Ctk.CTkLabel(master=furniture_frame,text="NRs. 15,60,000", text_color="#FFE605", font=("bold",30))
     furniture1_label.place(relx=0.05,rely=0.5)
     
     
     food_frame=Ctk.CTkFrame(master=Report_frame,width=(screen_width-1600),height=(100),fg_color="#3FB5CB",corner_radius=10,bg_color="white")
     food_frame.place(relx=0.3,rely=0.2)
     
     
     food_label=Ctk.CTkLabel(master=food_frame,text="Fooding and Laundry", text_color="white", font=("bold",20))
     food_label.place(relx=0.03,rely=0.0)
     
     food1_label=Ctk.CTkLabel(master=food_frame,text="NRs. 26,00,000", text_color="#00FFF5", font=("bold",30))
     food1_label.place(relx=0.05,rely=0.5)
     
     
     payment_frame=Ctk.CTkFrame(master=Report_frame,width=(screen_width-1600),height=(100),fg_color="#3FB5CB",corner_radius=10,bg_color="white")
     payment_frame.place(relx=0.6,rely=0.2)
     
     pay_label=Ctk.CTkLabel(master=payment_frame,text="Outstanding Payment", text_color="white", font=("bold",20))
     pay_label.place(relx=0.03,rely=0.0)
     
      
     pay1_label=Ctk.CTkLabel(master=payment_frame,text="NRs. 10,40,000", text_color="#FF05C8", font=("bold",30))
     pay1_label.place(relx=0.05,rely=0.5)
      
     
     
     Cont_frame= Ctk.CTkFrame(master=Report_frame, width=(screen_width-650), height=(200), fg_color="#3FB5CB", corner_radius=10, bg_color="white")
     Cont_frame.place(relx=0.01, rely=0.4)
     
     
     
     
     Complaint_label=Ctk.CTkLabel(master=Cont_frame,text="Complaints", text_color="white", font=("bold",25))
     Complaint_label.place(relx=0,rely=0)
     
     
     
     
     
     color_frame=Ctk.CTkFrame(master=Cont_frame,width=(screen_width-1650),height=(70),fg_color="white",corner_radius=10,bg_color="#3FB5CB")
     color_frame.place(relx=0.03,rely=0.4)
     
     
     
     
     color_label=Ctk.CTkLabel(master=color_frame,text="70%", text_color="black",width=(200),height=(70), font=("bold",25),fg_color="#A6DBCB",bg_color="#3FB5CB",corner_radius=10)
     color_label.place(relx=0.0,rely=0.0)
     
     
     
     
     color1_label=Ctk.CTkLabel(master=color_frame,text="30%", text_color="black",width=(100),height=(70), font=("bold",25),fg_color="#EEBFBF",bg_color="#3FB5CB")
     color1_label.place(relx=0.7,rely=0.0)
     
     
     
     
     fees_frame=Ctk.CTkFrame(master=Cont_frame,width=(screen_width-1650),height=(70),fg_color="black",corner_radius=10,bg_color="#3FB5CB")
     fees_frame.place(relx=0.27,rely=0.4)
     
     
     
     
     
     fees_label=Ctk.CTkLabel(master=fees_frame,text="Total Fees", text_color="white", font=("bold",15))
     fees_label.place(relx=0.05,rely=0.0)
     
     
     
     
     fees1_label=Ctk.CTkLabel(master=fees_frame,text="NRs.420,000", text_color="white", font=("bold",25))
     fees1_label.place(relx=0.05,rely=0.4)
     
     
     
     
     Collected_frame=Ctk.CTkFrame(master=Cont_frame,width=(screen_width-1650),height=(70),fg_color="black",corner_radius=10,bg_color="#3FB5CB")
     Collected_frame.place(relx=0.52,rely=0.4)
     
     
     
     
     collected_label=Ctk.CTkLabel(master=Collected_frame,text="Collected", text_color="white", font=("bold",15))
     collected_label.place(relx=0.05,rely=0.0)
     
     
     
     
     collected1_label=Ctk.CTkLabel(master=Collected_frame,text="NRs.", text_color="white", font=("bold",25))
     collected1_label.place(relx=0.05,rely=0.4)
     
     
     
     
     collected2_label=Ctk.CTkLabel(master=Collected_frame,text="294,000", text_color="#A6DBCB", font=("bold",25))
     collected2_label.place(relx=0.3,rely=0.4)
     
     
     
     
     dues_frame=Ctk.CTkFrame(master=Cont_frame,width=(screen_width-1650),height=(70),fg_color="black",corner_radius=10,bg_color="#3FB5CB")
     dues_frame.place(relx=0.77,rely=0.4) 
     
     
     
     
     dues_label=Ctk.CTkLabel(master=dues_frame,text="Dues", text_color="white", font=("bold",15))
     dues_label.place(relx=0.05,rely=0.0)
     
     
     
     
     dues1_label=Ctk.CTkLabel(master=dues_frame,text="NRs.", text_color="white", font=("bold",25))
     dues1_label.place(relx=0.05,rely=0.4)
     
     
     
     
     dues2_label=Ctk.CTkLabel(master=dues_frame,text="126,000", text_color="#EEBFBF", font=("bold",25))
     dues2_label.place(relx=0.3,rely=0.4)
     
     
     
     
     graph_image=Ctk.CTkImage(light_image=Image.open('images\\graph image.png'),
                                     size=(800, 300))
     graph_image_label=Ctk.CTkLabel(master=Report_frame,text="",image=graph_image)
     graph_image_label.place(relx=0.1, rely=0.65)
     
     
     piechart_image=Ctk.CTkImage(light_image=Image.open("images\\piechart.png"),size=(300,300))
     piechart_image_label=Ctk.CTkLabel(master=Report_frame,text="",image=piechart_image)
     piechart_image_label.place(relx=0.05,rely=0.05)
     
     return Report_frame


   def Appeared():
      Appeared_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5", corner_radius=20)
      Appeared_frame.place(relx=0.25, rely=0)
   
      Cont_frame= Ctk.CTkFrame(master=Appeared_frame, width=(screen_width-800), height=(600), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
      Cont_frame.place(relx=0.1, rely=0.2)
   
      Feature_label= Ctk.CTkLabel(master=Appeared_frame, text="Feature: We offer our honerable student to change their status such as room, bed,occupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
      Feature_label.place (relx=0, rely=0.05)
   
      Notice_label= Ctk.CTkLabel(master=Cont_frame, text="Notices:", text_color="black", font=("bold",25))
      Notice_label.place(relx=0.02, rely=0.05)
      return Appeared_frame
   
   
  
   
  
   
   def emergency():
   
      Emergency_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100), fg_color="#EDF1F5")
      Emergency_frame.place(relx=0.25, rely=0)
   
   
      Feature_label= Ctk.CTkLabel(master=Emergency_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
      Feature_label.place (relx=0, rely=0.05)

      
      Cont_frame= Ctk.CTkFrame(master=Emergency_frame, width=(screen_width-800), height=(600), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
      Cont_frame.place(relx=0.1, rely=0.2)

      Contact_label= Ctk.CTkLabel(master=Cont_frame, text="Contacts:", font=("bold", 25), text_color="black")
      Contact_label.place(relx=0.05, rely=0.05)

      Header_label= Ctk.CTkLabel(master=Cont_frame, text="Relation \t\t\t\t Number", text_color="black", font=("bold", 25))
      Header_label.place(relx=0.18, rely=0.20)

      Father_contact= Ctk.CTkLabel(master=Cont_frame, text="Canteen \t\t\t\t\t +977-98XXXXXXXX",font=("bold", 20) )
      Father_contact.place(relx=0.2, rely=0.35)
      
      Mother_contact= Ctk.CTkLabel(master=Cont_frame, text="Electrician \t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Mother_contact.place(relx=0.2, rely=0.45)

      Police_contace= Ctk.CTkLabel(master=Cont_frame, text="Police \t\t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Police_contace.place(relx=0.2, rely=0.55)
      
      Ambulance_contact= Ctk.CTkLabel(master=Cont_frame, text="Ambulance \t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Ambulance_contact.place(relx=0.2, rely=0.65)
      
      
      Fire_contact= Ctk.CTkLabel(master=Cont_frame, text="Fire Helper \t\t\t\t +977-98XXXXXXXX",font=("bold", 20))
      Fire_contact.place(relx=0.2, rely=0.75)
      

   
      return Emergency_frame
   
   def setting():
      
      global Cont_frame
      global Setting_frame
      Setting_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
      Setting_frame.place(relx=0.25, rely=0)
   
      Cont_frame= Ctk.CTkFrame(master=Setting_frame, width=(screen_width-800), height=(600), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
      Cont_frame.place(relx=0.1, rely=0.2)
   
      Feature_label= Ctk.CTkLabel(master=Setting_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                  justify= LEFT,text_color="black", font=("bold",25))
      Feature_label.place (relx=0.05, rely=0.05)
   
      Notice_label= Ctk.CTkLabel(master=Cont_frame, text="Setting:", text_color="black", font=("bold",25))
      Notice_label.place(relx=0.05, rely=0.1)
   
      Search_entry= Ctk.CTkEntry(master=Cont_frame, placeholder_text="Search setting", width=300, height=30,text_color="black",fg_color="#EDF1F5")
      Search_entry.place(relx=0.3, rely=0.2)

      # add `from PIL import Image` on top
      contact_image = Ctk.CTkImage(light_image=Image.open('images\\contact.png'),
                                        size=(20, 20))
      
      account_image = Ctk.CTkImage(light_image=Image.open('images\\account.png'),
                                        size=(20, 20))
      logout_image = Ctk.CTkImage(light_image=Image.open('images\\logout.png'),
                                        size=(20, 20))

   
   
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


   
      
   
   menu()
   
   toggle_button("Reports and Analytics", Report)
   
   return dashboard_frame
   
   
def get_total_room():
    conn= sqlite3.connect("hostel.db")
    c= conn.cursor()
    c.execute("SELECT total_room FROM room")
    count=c.fetchone()
    conn.close()
    return count
def room():
    
    conn= sqlite3.connect("hostel.db")
    c= conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS room(
        total_room INTEGER)""")
    
    # Insert initial quantities only if the table is empty
    c.execute("SELECT COUNT(*) FROM room")
    if c.fetchone()[0] == 0:
        c.execute("""
            INSERT INTO room (total_room)
            VALUES (?)
        """, (50,))

    conn.commit()
    conn.close()
    
    total_room=get_total_room()



    Menu_frame.destroy()
    current_frame.destroy()

    room_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100) )
    room_frame.place(relx=0, rely=0.095)



    # add `from PIL import Image` on top
    Room_image = Ctk.CTkImage(light_image=Image.open('images\\Room_image.png'),
                                      size=((screen_width), 500))
    
    Room_image_label= Ctk.CTkLabel(master=room_frame, image=Room_image, text="")
    Room_image_label.place(relx=0, rely=0.5)
    
    
    Room1_frame= Ctk.CTkFrame(master=room_frame,width=300, height=70, fg_color="#3FB5CB", corner_radius=15)
    Room1_frame.place(relx=0.09, rely=0.07)
    Room1_label= Ctk.CTkLabel(master=Room1_frame, text="Total Rooms", text_color="white", font=("bold",30),
                                 width=30, height=30, corner_radius=0)
    Room1_label.place(relx=0.05, rely=0.2)
    Room1_num= Ctk.CTkLabel(master=Room1_frame, text=f"{total_room}", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    Room1_num.place(relx=0.7, rely=0.2)
    
    
    addRoom_btn= Ctk.CTkButton(master=room_frame,  text="+Add Room", text_color="white", font=("bold",30),  width=300, height=70, fg_color="#3FB5CB", corner_radius=15,command=add_room)
    addRoom_btn.place(relx=0.39, rely=0.07)
    
    
    
    totalroom_label= Ctk.CTkLabel(master=room_frame, text="Total Rooms", text_color="Black", font=("bold",25),
                                 width=30, height=30, corner_radius=0)
    totalroom_label.place(relx=0.45, rely=0.3)
    
    
    
    def create_pie_chart(canvas, center_x, center_y, outer_radius, inner_radius, data, colors):
     total = sum(data)
     start_angle = 0

     for i, value in enumerate(data):
        extent = value / total * 360
        end_angle = start_angle + extent

        # Draw the outer arc for the pie slice
        canvas.create_arc(center_x - outer_radius, center_y - outer_radius,
                          center_x + outer_radius, center_y + outer_radius,
                          start=start_angle, extent=extent,
                          fill=colors[i], outline="black", width=2)

        start_angle = end_angle

    # Draw the inner circle to create a donut shape
     canvas.create_oval(center_x - inner_radius, center_y - inner_radius,
                       center_x + inner_radius, center_y + inner_radius,
                       fill="lightgray", outline="black", width=2)

    # Add the percentage text in the center
     percentage_text = "50"
     canvas.create_text(center_x, center_y, text=percentage_text, font=('Helvetica', 24, 'bold'), fill="black")
     
         # Create a canvas to draw the pie chart
    canvas = Ctk.CTkCanvas(master=room_frame, width=200, height=200, bg='#D9D9D9', highlightthickness=0)
    canvas.place(relx=0.55, rely=0.29)

    # Data for the pie chart
    data = [180, 30]
    colors = ["#FFEB3B", "#FF4081"]

    # Draw the pie chart
    create_pie_chart(canvas, 100, 120, 70, 50, data, colors)

    
    
    
   

    
    
    
    Occupied_frame= Ctk.CTkFrame(master=room_frame,width=200, height=100, fg_color="#3FB5CB", corner_radius=15)
    Occupied_frame.place(relx=0.09, rely=0.2)
    Occupied_label= Ctk.CTkLabel(master=Occupied_frame, text="Occupied", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    Occupied_label.place(relx=0.3, rely=0.01)
    Occupied_num= Ctk.CTkLabel(master=Occupied_frame, text="50", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    Occupied_num.place(relx=0.3, rely=0.4)

    vacant_frame= Ctk.CTkFrame(master=room_frame,width=200, height=100, fg_color="#3FB5CB", corner_radius=15)
    vacant_frame.place(relx=0.29, rely=0.2)
    vacant_label= Ctk.CTkLabel(master=vacant_frame, text="Vacant", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    vacant_label.place(relx=0.3, rely=0.01)
    vacant_num= Ctk.CTkLabel(master=vacant_frame, text="15", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    vacant_num.place(relx=0.3, rely=0.4)

    tenant_frame= Ctk.CTkFrame(master=room_frame,width=200, height=100, fg_color="#3FB5CB", corner_radius=15)
    tenant_frame.place(relx=0.49, rely=0.2)
    tenant_label= Ctk.CTkLabel(master=tenant_frame, text="Tenant", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    tenant_label.place(relx=0.3, rely=0.01)
    tenant_num= Ctk.CTkLabel(master=tenant_frame, text="100", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    tenant_num.place(relx=0.3, rely=0.4)

    ac_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=65, fg_color="#3FB5CB", corner_radius=15)
    ac_room_frame.place(relx=0.09, rely=0.4)
    ac_room_label= Ctk.CTkLabel(master=ac_room_frame, text="Ac room", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    ac_room_label.place(relx=0.1, rely=0.01)
    ac_room_num= Ctk.CTkLabel(master=ac_room_frame, text="20", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 25))
    ac_room_num.place(relx=0.4, rely=0.4)

    normal_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=65, fg_color="#3FB5CB", corner_radius=15)
    normal_room_frame.place(relx=0.29, rely=0.4)
    normal_room_label= Ctk.CTkLabel(master=normal_room_frame, text="Normal room", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    normal_room_label.place(relx=0.1, rely=0.01)
    normal_room_num= Ctk.CTkLabel(master=normal_room_frame, text="30", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 25))
    normal_room_num.place(relx=0.4, rely=0.4)
    
      # Furniture frame

    Furniture_frame= Ctk.CTkFrame(master= room_frame, width=350, height=450, fg_color="#555252", corner_radius=5)
    Furniture_frame.place(relx=0.7, rely=0.1)

    Furniture_label= Ctk.CTkLabel(master=Furniture_frame, text="Furniture", text_color="White", font=("bold",25))
    Furniture_label.place(relx=0.05, rely=0.03)

    Celing_fan_label= Ctk.CTkLabel(master=Furniture_frame, text="Celing fan \t\t 50", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    Celing_fan_label.place(relx=0.1, rely=0.1)

    table_label= Ctk.CTkLabel(master=Furniture_frame, text="Table \t\t\t 15", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    table_label.place(relx=0.1, rely=0.2)

    chairs_label= Ctk.CTkLabel(master=Furniture_frame, text="Chairs \t\t\t 20", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    chairs_label.place(relx=0.1, rely=0.3)

    bed_label= Ctk.CTkLabel(master=Furniture_frame, text="Beds \t\t\t 50", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    bed_label.place(relx=0.1, rely=0.4)

    cupboard_label= Ctk.CTkLabel(master=Furniture_frame, text="Cupboard \t\t 30", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    cupboard_label.place(relx=0.1, rely=0.5)

    tea_table_label= Ctk.CTkLabel(master=Furniture_frame, text="Tea Table \t\t 10", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    tea_table_label.place(relx=0.1, rely=0.6)

    shoes_rack_label= Ctk.CTkLabel(master=Furniture_frame, text="Shoes Rack \t\t 45", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    shoes_rack_label.place(relx=0.1, rely=0.7)

    Claim_btn= Ctk.CTkButton(master=Furniture_frame, text="Claim Furniture", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#3FB5CB", width=100,height=40, command=claim_furniture)
    Claim_btn.place(relx=0.3, rely=0.8)
    

    return room_frame

def add_room():
       
       global Floor_entry
       global Room_entry
       global Block_entry
       room_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100) )
       room_frame.place(relx=0, rely=0.13)
   
       # add `from PIL import Image` on top
       Room_image = Ctk.CTkImage(light_image=Image.open('images\\Room_image.png'),
                                         size=(screen_width, 300))
       
       Room_image_label= Ctk.CTkLabel(master=room_frame, image=Room_image, text="")
       Room_image_label.place(relx=0, rely=0.5)
   
       Total_room_frame= Ctk.CTkFrame(master=room_frame, width=200, height=70, fg_color="#3FB5CB", corner_radius=15)
       Total_room_frame.place(relx=0.01, rely=0.1)
       Total_room_label= Ctk.CTkLabel(master=Total_room_frame, text="Total Rooms \t 50", text_color="white", font=("bold",15))
       Total_room_label.place(relx=0.1, rely=0.3)
     
   
       Occupied_frame= Ctk.CTkFrame(master=room_frame,width=200, height=85, fg_color="#3FB5CB", corner_radius=15)
       Occupied_frame.place(relx=0.01, rely=0.23)
       Occupied_label= Ctk.CTkLabel(master=Occupied_frame, text="Occupied", text_color="yellow", font=("bold",15),
                                    width=30, height=30, corner_radius=0)
       Occupied_label.place(relx=0.3, rely=0.01)
       Occupied_num= Ctk.CTkLabel(master=Occupied_frame, text="50", text_color="yellow", fg_color="#3FB5CB",
                                  width=30, height=30, font=("bold", 30))
       Occupied_num.place(relx=0.3, rely=0.4)
   
       ac_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=60, fg_color="#3FB5CB", corner_radius=15)
       ac_room_frame.place(relx=0.01, rely=0.4)
       ac_room_label= Ctk.CTkLabel(master=ac_room_frame, text="Ac room", text_color="white", font=("bold",15),
                                    width=30, height=30, corner_radius=0)
       ac_room_label.place(relx=0.3, rely=0.01)
       ac_room_num= Ctk.CTkLabel(master=ac_room_frame, text="20", text_color="white", fg_color="#3FB5CB",
                                  width=30, height=30, font=("bold", 30))
       ac_room_num.place(relx=0.3, rely=0.4)


       change_room_frame= Ctk.CTkFrame(master=room_frame, width=600, height=250, fg_color="#3FB5CB", corner_radius=10)
       change_room_frame.place(relx=0.2, rely=0.1)

       Change_room_label=Ctk.CTkLabel(master=change_room_frame, text="Change Room", text_color="white", font=("bold",25))
       Change_room_label.place(relx=0.3, rely=0.1)

       Change_to_label=Ctk.CTkLabel(master=change_room_frame, text="Change To:", text_color=("White"), font=('bold',20))
       Change_to_label.place(relx=0.3, rely=0.3)

       Block_label= Ctk.CTkLabel(master=change_room_frame, text="Block:",text_color="White", font=("bold",20))
       Block_label.place(relx=0.25, rely=0.45)

       Floor_label= Ctk.CTkLabel(master=change_room_frame, text="Floor:",text_color="White", font=("bold",20))
       Floor_label.place(relx=0.25, rely=0.6)

       Room_label= Ctk.CTkLabel(master=change_room_frame, text="Room no:",text_color="White", font=("bold",20))
       Room_label.place(relx=0.25, rely=0.75)

       Block_entry= Ctk.CTkEntry(master=change_room_frame, text_color="black", width=50)
       Block_entry.place(relx=0.4, rely=0.45)

       Floor_entry= Ctk.CTkEntry(master=change_room_frame,text_color="black", width=50)
       Floor_entry.place(relx=0.4, rely=0.6)

       Room_entry= Ctk.CTkEntry(master=change_room_frame,text_color="black", width=50)
       Room_entry.place(relx=0.4, rely=0.75)

       Request_btn= Ctk.CTkButton(master=change_room_frame, text="Request to change", width=100, height=40, corner_radius=10,
                                  fg_color="#1AD8E4", text_color="black", command=change_room_request)
       Request_btn.place(relx=0.5, rely=0.8)


       # Furniture frame
   
       Furniture_frame= Ctk.CTkFrame(master= room_frame, width=350, height=450, fg_color="#555252", corner_radius=5)
       Furniture_frame.place(relx=0.7, rely=0.1)
   
       Furniture_label= Ctk.CTkLabel(master=Furniture_frame, text="Furniture", text_color="White", font=("bold",25))
       Furniture_label.place(relx=0.05, rely=0.03)
   
       Celing_fan_label= Ctk.CTkLabel(master=Furniture_frame, text="Celing fan \t\t 50", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       Celing_fan_label.place(relx=0.1, rely=0.1)
   
       table_label= Ctk.CTkLabel(master=Furniture_frame, text="Table \t\t\t 15", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       table_label.place(relx=0.1, rely=0.2)
   
       chairs_label= Ctk.CTkLabel(master=Furniture_frame, text="Chairs \t\t\t 20", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       chairs_label.place(relx=0.1, rely=0.3)
   
       bed_label= Ctk.CTkLabel(master=Furniture_frame, text="Beds \t\t\t 50", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       bed_label.place(relx=0.1, rely=0.4)
   
       cupboard_label= Ctk.CTkLabel(master=Furniture_frame, text="Cupboard \t\t 30", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       cupboard_label.place(relx=0.1, rely=0.5)
   
       tea_table_label= Ctk.CTkLabel(master=Furniture_frame, text="Tea Table \t\t 10", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       tea_table_label.place(relx=0.1, rely=0.6)
   
       shoes_rack_label= Ctk.CTkLabel(master=Furniture_frame, text="Shoes Rack \t\t 45", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       shoes_rack_label.place(relx=0.1, rely=0.7)
   
       Claim_btn= Ctk.CTkButton(master=Furniture_frame, text="Claim Furniture", text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#3FB5CB", width=100,height=40, command=claim_furniture)
       Claim_btn.place(relx=0.3, rely=0.8)

def change_room_request():
 if Block_entry.get()=="":
    messagebox.showinfo("Entry","Please fill the block no")
 elif Floor_entry.get()=="":
    messagebox.showinfo("Entry","Please fill the floor")
 elif Room_entry.get()=="":
     messagebox.showinfo("Entry","Please fill the Room no")
 else:
     conn= sqlite3.connect("hostel.db")
     c= conn.cursor()
     c.execute("""
        UPDATE room
        SET total_room=total_room+?
    """, (1))

    # Commit the changes and close the connection
     conn.commit()
     conn.close()

     messagebox.showinfo("Success","Room added successfully")
     room()

def claim_furniture():

    global Celing_fan_entry
    global chairs_entry
    global table_entry
    global bed_entry
    global shoes_rack_entry
    global tea_table_entry
    global cupboard_entry

    room_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100) )
    room_frame.place(relx=0, rely=0.13)

    # add `from PIL import Image` on top
    Room_image = Ctk.CTkImage(light_image=Image.open('images\\Room_image.png'),
                                      size=(screen_width, 300))
    
    Room_image_label= Ctk.CTkLabel(master=room_frame, image=Room_image, text="")
    Room_image_label.place(relx=0, rely=0.5)

    Total_room_frame= Ctk.CTkFrame(master=room_frame, width=200, height=70, fg_color="#3FB5CB", corner_radius=15)
    Total_room_frame.place(relx=0.01, rely=0.1)
    Total_room_label= Ctk.CTkLabel(master=Total_room_frame, text="Total Rooms \t 50", text_color="white", font=("bold",15))
    Total_room_label.place(relx=0.1, rely=0.3)

    #Change room button

    Change_room_button= Ctk.CTkButton(master=room_frame, width=200, height=70, text="Change room", text_color="white",
                                      font=("bold",15), fg_color="#3FB5CB", corner_radius=15, command=add_room)
    Change_room_button.place(relx=0.25, rely=0.1)

  

    Occupied_frame= Ctk.CTkFrame(master=room_frame,width=200, height=85, fg_color="#3FB5CB", corner_radius=15)
    Occupied_frame.place(relx=0.01, rely=0.23)
    Occupied_label= Ctk.CTkLabel(master=Occupied_frame, text="Occupied", text_color="yellow", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    Occupied_label.place(relx=0.3, rely=0.01)
    Occupied_num= Ctk.CTkLabel(master=Occupied_frame, text="50", text_color="yellow", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    Occupied_num.place(relx=0.3, rely=0.4)

    vacant_frame= Ctk.CTkFrame(master=room_frame,width=200, height=85, fg_color="#3FB5CB", corner_radius=15)
    vacant_frame.place(relx=0.2, rely=0.23)
    vacant_label= Ctk.CTkLabel(master=vacant_frame, text="Vacant", text_color="#FF05C8", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    vacant_label.place(relx=0.3, rely=0.01)
    vacant_num= Ctk.CTkLabel(master=vacant_frame, text="15", text_color="#FF05C8", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    vacant_num.place(relx=0.3, rely=0.4)

    tenant_frame= Ctk.CTkFrame(master=room_frame,width=200, height=85, fg_color="#3FB5CB", corner_radius=15)
    tenant_frame.place(relx=0.4, rely=0.23)
    tenant_label= Ctk.CTkLabel(master=tenant_frame, text="Tenant", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    tenant_label.place(relx=0.3, rely=0.01)
    tenant_num= Ctk.CTkLabel(master=tenant_frame, text="100", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    tenant_num.place(relx=0.3, rely=0.4)

    ac_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=60, fg_color="#3FB5CB", corner_radius=15)
    ac_room_frame.place(relx=0.01, rely=0.4)
    ac_room_label= Ctk.CTkLabel(master=ac_room_frame, text="Ac room", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    ac_room_label.place(relx=0.3, rely=0.01)
    ac_room_num= Ctk.CTkLabel(master=ac_room_frame, text="20", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    ac_room_num.place(relx=0.3, rely=0.4)

    normal_room_frame= Ctk.CTkFrame(master=room_frame,width=200, height=60, fg_color="#3FB5CB", corner_radius=15)
    normal_room_frame.place(relx=0.2, rely=0.4)
    normal_room_label= Ctk.CTkLabel(master=normal_room_frame, text="Normal", text_color="white", font=("bold",15),
                                 width=30, height=30, corner_radius=0)
    normal_room_label.place(relx=0.3, rely=0.01)
    normal_room_num= Ctk.CTkLabel(master=normal_room_frame, text="30", text_color="white", fg_color="#3FB5CB",
                               width=30, height=30, font=("bold", 30))
    normal_room_num.place(relx=0.3, rely=0.4)


    claim_furniture_frame= Ctk.CTkFrame(master=room_frame, width=400, height=300, fg_color="#3FB5CB", corner_radius=10)
    claim_furniture_frame.place(relx=0.68, rely=0.1)

    claim_furniture_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Claim Furniture", text_color="White", font=("bold",25))
    claim_furniture_label.place(relx=0.3, rely=0.05)

    Celing_fan_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Celing fan", text_color="white",font=("bold",15),
                                   corner_radius=15)
    Celing_fan_label.place(relx=0.1, rely=0.15)

    table_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Table", text_color="white",font=("bold",15),
                                   corner_radius=15)
    table_label.place(relx=0.1, rely=0.25)

    chairs_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Chairs", text_color="white",font=("bold",15),
                                   corner_radius=15)
    chairs_label.place(relx=0.1, rely=0.35)

    bed_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Beds", text_color="white",font=("bold",15),
                                   corner_radius=15)
    bed_label.place(relx=0.1, rely=0.45)

    cupboard_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Cupboard", text_color="white",font=("bold",15),
                                   corner_radius=15)
    cupboard_label.place(relx=0.1, rely=0.55)

    tea_table_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Tea Table", text_color="white",font=("bold",15),
                                   corner_radius=15)
    tea_table_label.place(relx=0.1, rely=0.65)

    shoes_rack_label= Ctk.CTkLabel(master=claim_furniture_frame, text="Shoes Rack", text_color="white",font=("bold",15),
                                   corner_radius=15)
    shoes_rack_label.place(relx=0.1, rely=0.75)


    Celing_fan_entry= Ctk.CTkEntry(master=claim_furniture_frame,font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    Celing_fan_entry.place(relx=0.5, rely=0.15)

    table_entry= Ctk.CTkEntry(master=claim_furniture_frame,font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    table_entry.place(relx=0.5, rely=0.25)

    chairs_entry= Ctk.CTkEntry(master=claim_furniture_frame,font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    chairs_entry.place(relx=0.5, rely=0.35)

    bed_entry= Ctk.CTkEntry(master=claim_furniture_frame, font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    bed_entry.place(relx=0.5, rely=0.45)

    cupboard_entry= Ctk.CTkEntry(master=claim_furniture_frame, font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    cupboard_entry.place(relx=0.5, rely=0.55)

    tea_table_entry= Ctk.CTkEntry(master=claim_furniture_frame, font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    tea_table_entry.place(relx=0.5, rely=0.65)

    shoes_rack_entry= Ctk.CTkEntry(master=claim_furniture_frame,font=("bold",15), width=80, placeholder_text="Qnt", fg_color="#D9D9D9",
                                   corner_radius=15)
    shoes_rack_entry.place(relx=0.5, rely=0.75)

    request_btn= Ctk.CTkButton(master=claim_furniture_frame, text="Request", text_color="black", fg_color="#1AD8E4",width=100, height=40,
                               command= claim_furniture_request)
    request_btn.place(relx=0.75, rely=0.5)

def claim_furniture_request():

    if Celing_fan_entry.get()=="":
        messagebox.showinfo("Info","Please fill the ceiling fan quantity")
    elif table_entry.get()=="":
         messagebox.showinfo("Info","Please fill the table quantity")
    elif chairs_entry.get()=="":
         messagebox.showinfo("Info","Please fill the chairs quantity")
    elif bed_entry.get()=="":
         messagebox.showinfo("Info","Please fill the bed quantity")    
    elif cupboard_entry.get()=="":
         messagebox.showinfo("Info","Please fill the cupboard quantity")
    elif tea_table_entry.get()=="":
         messagebox.showinfo("Info","Please fill the tea table quantity")
    elif shoes_rack_entry.get()=="":
         messagebox.showinfo("Info","Please fill the shoe rack quantity")

    else:
         try:
        # Get the requested quantities from the user
            fan = Celing_fan_entry.get()
            table = (table_entry.get())
            chair = chairs_entry.get()
            bed = bed_entry.get()
            teatable = tea_table_entry.get()
            shoerack = shoes_rack_entry.get()
            cupboard = cupboard_entry.get()
    
            # Connect to the database
            conn = sqlite3.connect("hostel.db")
            c = conn.cursor()
    
            # Update the quantities in the furniture table
            c.execute("""
                UPDATE furniture
                SET fan = fan + ?, [table] = [table] + ?, chair = chair + ?, bed = bed + ?, teatable = teatable + ?, shoerack = shoerack + ?, cupboard = cupboard + ?
            """, (fan, table, chair, bed, teatable, shoerack, cupboard))
    
            # Commit the changes and close the connection
            conn.commit()
            conn.close()
    
            # Clear the entry fields
            Celing_fan_entry.delete(0, 'end')
            table_entry.delete(0, 'end')
            chairs_entry.delete(0, 'end')
            bed_entry.delete(0, 'end')
            tea_table_entry.delete(0, 'end')
            shoes_rack_entry.delete(0, 'end')
            cupboard_entry.delete(0, 'end')
    
            # Display a success message
            messagebox.showinfo("Success", "Furniture added successfully!")
    
            room()
    
         except Exception as e:
            # Display an error message if the database is locked
            if str(e) == "database is locked":
                messagebox.showerror("Error", "The database is currently locked. Please try again later.")
            else:
                # Display the original error message for other types of OperationalErrors
                messagebox.showerror("Error", str(e))
    
    
    
    

def special_req():
    
    
    conn= sqlite3.connect("hostel.db")
    c= conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS update_notice(
        notice TEXT)""")
    conn.close()
    

    Menu_frame.destroy()
    current_frame.destroy()

    special_req_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100) )
    special_req_frame.place(relx=0, rely=0.095)

    #Update Notice
    global Reason_text
    updatenotice_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=300, fg_color="#3FB5CB")
    updatenotice_frame.place(relx=0.05, rely=0.01)

    notice_label=Ctk.CTkLabel(master=updatenotice_frame, text="Update Notice", text_color="White", font=("bold",25))
    notice_label.place(relx=0.01, rely=0.05)

    Reason_text= Text(master=updatenotice_frame,width=50, height=10, wrap=WORD, bg="#1AD8E4")
    Reason_text.place(relx=0, rely=0.18)


    Submit_btn= Ctk.CTkButton(master=updatenotice_frame, text="Submit", fg_color="#1AD8E4", text_color="black", font=("bold",20),
                              command= notice_update)
    Submit_btn.place(relx=0.3, rely=0.85)


     #Meal Preference Frame
    Meal_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=300, fg_color="#3FB5CB")
    Meal_frame.place(relx=0.38, rely=0.01)

    Meal_label=Ctk.CTkLabel(master=Meal_frame, text="Change Meal Routine", text_color="White", font=("bold",25))
    Meal_label.place(relx=0.01, rely=0.05)

    Iam_label= Ctk.CTkLabel(master=Meal_frame, text="Are you sure you want to change meal routine?", text_color="black", font=("bold",15))
    Iam_label.place(relx=0.05, rely=0.2)

   



    Yes_No_var= IntVar()

    Yes_radio_button= Ctk.CTkRadioButton(master=Meal_frame, text="Yes", variable=Yes_No_var,value=1)
    Yes_radio_button.place(relx=0.35, rely=0.4)

    No_radio_button= Ctk.CTkRadioButton(master=Meal_frame, text="No", variable=Yes_No_var, value=2)
    No_radio_button.place(relx=0.35, rely=0.5)

    Change_preference_btn= Ctk.CTkButton(master=Meal_frame, text="Go to Meal Routine", fg_color="#1AD8E4", text_color="black", font=("bold",15))
    Change_preference_btn.place(relx=0.3, rely=0.7)

    #Event Announcment Frame

    Event_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=300, fg_color="#3FB5CB")
    Event_frame.place(relx=0.7, rely=0.01)

    Event_label=Ctk.CTkLabel(master=Event_frame, text="Event Announcement", text_color="White", font=("bold",25))
    Event_label.place(relx=0.01, rely=0.05)

    Catagory_label= Ctk.CTkLabel(master=Event_frame, text="Category:", text_color="black", font=("bold",15))
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
    
    
    date_label=Ctk.CTkLabel(master=Event_frame,text="Date:",font=("bold",15))
    date_label.place(relx=0.52,rely=0.48)
    
    Date_text= Text(master=Event_frame, width=13, height=2, wrap=WORD, bg="#1AD8E4")
    Date_text.place(relx=0.65, rely=0.48)

    Title_label= Ctk.CTkLabel(master=Event_frame, text="Specify the title", font=("bold",15))
    Title_label.place(relx=0.05, rely=0.56)

    Title_text= Text(master=Event_frame, width=50, height=3, wrap=WORD, bg="#1AD8E4")
    Title_text.place(relx=0, rely=0.65)

    Event_submmit_btn= Ctk.CTkButton(master=Event_frame, text="Submmit", fg_color=("#1AD8E4"), text_color="black")
    Event_submmit_btn.place(relx=0.35, rely=0.85)


    #Maintenace Request Frame

    Maintenance_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=250, fg_color="#3FB5CB")
    Maintenance_frame.place(relx=0.05, rely=0.5)

    Miantenance_label=Ctk.CTkLabel(master=Maintenance_frame, text="Maintainance Notice", text_color="White", font=("bold",25))
    Miantenance_label.place(relx=0.01, rely=0.05)

    Specify_label= Ctk.CTkLabel(master=Maintenance_frame, text="Specify what happened", font=("bold",15))
    Specify_label.place(relx=0.05, rely=0.2)

    Maintenance_text= Text(master=Maintenance_frame, width=50, height=5, wrap=WORD, bg="#1AD8E4")
    Maintenance_text.place(relx=0, rely=0.3)

    Maintenance_btn= Ctk.CTkButton(master=Maintenance_frame, text="Submit", fg_color="#1AD8E4", text_color="black")
    Maintenance_btn.place(relx=0.3, rely=0.7)
    
def notice_update():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    notice = Reason_text.get("1.0","end-1c").strip()  # Remove leading and trailing whitespace
    c.execute("INSERT INTO update_notice(notice) VALUES(?)", (notice,))
    
    messagebox.showinfo("Info","Your notice has been updated")
    
    conn.commit()
    conn.close()


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




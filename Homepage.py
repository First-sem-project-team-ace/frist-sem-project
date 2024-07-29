import customtkinter as Ctk
from tkinter import *
from PIL import Image
from datetime import datetime



Homepage= Ctk.CTk()

Ctk.set_appearance_mode('light')
Homepage.geometry("{0}x{1}+0+0".format(Homepage.winfo_screenwidth(), Homepage.winfo_screenheight()))
screen_width = Homepage.winfo_screenwidth()
screen_height = Homepage.winfo_screenheight()

current_frame = None


    
    

def logout():
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

   def menu():
    
     global Menu_frame
     global Change_btn
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
      contact_image = Ctk.CTkImage(light_image=Image.open('images\\contact.png'),
                                        size=(20, 20))
      
      account_image = Ctk.CTkImage(light_image=Image.open('images\\account.png'),
                                        size=(20, 20))
      logout_image = Ctk.CTkImage(light_image=Image.open('images\\logout.png'),
                                        size=(20, 20))

   
   
      Account_btn= Ctk.CTkButton(master=Cont_frame, text="Account", width=400, height=30,fg_color="#EDF1F5", text_color="black",
                                 anchor=W, image=account_image)
      Account_btn.place(relx=0.15, rely=0.4)
   
      Setting_notification_btn= Ctk.CTkButton(master=Cont_frame, text="Notification", width=400, height=30, text_color="black",
                                              image=notification_image, fg_color="#EDF1F5", anchor=W)
      Setting_notification_btn.place(relx=0.15, rely=0.5)
   
      Update_contact_btn= Ctk.CTkButton(master=Cont_frame, text="Update contact", width=400, height=30, fg_color="#EDF1F5", text_color="black",
                                         anchor=W, image=contact_image)
      Update_contact_btn.place(relx=0.15, rely=0.6)
   
      Logout_btn= Ctk.CTkButton(master=Cont_frame, text="Log out", width=400, height=30, fg_color="#EDF1F5", text_color="black",
                                        anchor=W, image=logout_image, command=logout)
      Logout_btn.place(relx=0.15, rely=0.7)
   
   
      return Setting_frame
   
   menu()

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

    special_req_frame= Ctk.CTkFrame(master=Homepage, width=screen_height, height=(screen_height-100) )
    special_req_frame.place(relx=0, rely=0.1)


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
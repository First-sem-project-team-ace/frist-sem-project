import customtkinter as Ctk
from tkinter import *
from PIL import Image
from datetime import datetime



Homepage= Ctk.CTk()

Ctk.set_appearance_mode('light')
Homepage.geometry("{0}x{1}+0+0".format(Homepage.winfo_screenwidth(), Homepage.winfo_screenheight()))
screen_width = Homepage.winfo_screenwidth()
screen_height = Homepage.winfo_screenheight()

Linear_image = Ctk.CTkImage(light_image=Image.open('C:\\Users\\User\\OneDrive\\Desktop\\Project\\Linear.png'), size=(screen_width, screen_height))
Linear_image_label = Ctk.CTkLabel(master=Homepage, image=Linear_image, text="")
Linear_image_label.place(x=0, y=0)


current_frame = None

def show_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = frame
    current_frame.place(relx=0.2, rely=0.135)
   

global Change_btn
global Menu_frame
menu_button=[]
button_color={}
def menu():
  global Menu_frame
  global Change_btn
  global menu_button, button_color

  def menu_collapse():
      Menu_frame.destroy()
      Toggle_btn.configure(text="☰", command=menu)
      


  Menu_frame = Ctk.CTkFrame(master=Homepage, width=250, height=screen_height, bg_color="white", fg_color="#9F96C8")
  Menu_frame.place(relx=0, rely=0.3)


  
  Change_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="dark blue", corner_radius=10, bg_color="#9F96C8", font=("bold",15),
                     text="Change Status", text_color="white", command=lambda: toggle_button("Change Status",change))
  Change_btn.place(relx=0, rely=0)

  Notice_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="dark blue", corner_radius=10, bg_color="#9F96C8", font=("bold",15),
                     text="Notice", text_color="white", command=lambda: toggle_button("Notice",notice))
  Notice_btn.place(relx=0, rely=0.1) 

  Invoice_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="dark blue", corner_radius=10, bg_color="#9F96C8", font=("bold",15),
                     text="Invoice", text_color="white", command=lambda: toggle_button("Invoice",invoice))
  Invoice_btn.place(relx=0, rely=0.2)

  Complaint_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="dark blue", corner_radius=10, bg_color="#9F96C8", font=("bold",15),
                     text="Complaint", text_color="white", command=lambda: toggle_button("Complaint",complaint))
  Complaint_btn.place(relx=0, rely=0.3)

  Emergency_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="dark blue", corner_radius=10, bg_color="#9F96C8", font=("bold",15),
                     text="Emergency Contact", text_color="white", command= lambda: toggle_button("Emergency Contact",emergency))
  Emergency_btn.place(relx=0, rely=0.4)

  Setting_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="dark blue", corner_radius=10, bg_color="#9F96C8", font=("bold",15),
                     text="Setting", text_color="white", command=lambda: toggle_button("Setting", setting))
  Setting_btn.place(relx=0, rely=0.5)

  menu_button=[Change_btn,Notice_btn,Invoice_btn, Complaint_btn,Emergency_btn, Setting_btn, Room_btn]
  button_color={btn.cget("text"): False for btn in menu_button}

  

  Toggle_btn.configure(text="X", command=menu_collapse)


def reset_all_btn():
   for btn in menu_button:
      btn.configure(fg_color="dark blue")
      button_color[btn.cget("text")]=False

def toggle_button(button_name, frame_function):
    if button_color[button_name]:
        reset_all_btn()
        button_color[button_name] = False
    else:
        reset_all_btn()
        for btn in menu_button:
            if btn.cget("text") == button_name:
                btn.configure(fg_color="gray")
                button_color[btn.cget("text")] = True
    show_frame(frame_function())


def change():
   
   global Change_btn

   
   Change_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100))
   Change_frame.place(relx=0.2, rely=0.35)

   Hmepage_background = Ctk.CTkImage(light_image=Image.open('Homepage_background.png'),
                                       size=(screen_width-350, screen_height-100))
   Homepage_image_label= Ctk.CTkLabel(master=Change_frame, image=Hmepage_background,bg_color="transparent", text="")
   Homepage_image_label.place(relx=0, rely=0)


   Feature_label= Ctk.CTkLabel(master=Change_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                               justify= LEFT,text_color="white", font=("bold",25), fg_color="#b4acd4")
   Feature_label.place (relx=0.05, rely=0.05)

   ChangeRoom_btn= Ctk.CTkButton(master=Change_frame, text="Change room", width=250, height=100, fg_color="#585454", bg_color="white",
                             font=("bold",20))
   ChangeRoom_btn.place(relx=0.15, rely=0.3)

   swap_btn= Ctk.CTkButton(master=Change_frame, text="Swap Bed", width=250, height=100, fg_color="#585454",  bg_color="white",
                             font=("bold",20))
   swap_btn.place(relx=0.55, rely=0.3)

   Room_upgrade= Ctk.CTkButton(master=Change_frame, text="Room Upgrade", width=250, height=100, fg_color="#585454", bg_color="white", 
                             font=("bold",20))
   Room_upgrade.place(relx=0.15, rely=0.5)

   occupancy_btn= Ctk.CTkButton(master=Change_frame, text="Occupancy Status", width=250, height=100, fg_color="#585454", bg_color="white", 
                             font=("bold",20))
   occupancy_btn.place(relx=0.55, rely=0.5)

   Change_btn.configure(fg_color="gray")

   # add `from PIL import Image` on top
   oldnew_image = Ctk.CTkImage(light_image=Image.open('oldnew.png'),
                                     size=(300, 200))
   oldnew_label= Ctk.CTkLabel(master=Change_frame, image=oldnew_image,text="" )
   oldnew_label.place(relx=0.3,rely=0.65)

   Go_room_btn= Ctk.CTkButton(master=Change_frame, text="Go To Room Details", fg_color="dark blue", bg_color="white",
                              corner_radius=10, height=50, width=150)
   Go_room_btn.place(relx=0.65, rely=0.75)

    
   
   
  
   return Change_frame


def notice():
   Notice_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-200), fg_color="white")
   Notice_frame.place(relx=0.2, rely=0.35)

   Hmepage_background = Ctk.CTkImage(light_image=Image.open('Homepage_background.png'),
                                       size=(screen_width-350, screen_height-100))
   Homepage_image_label= Ctk.CTkLabel(master=Notice_frame, image=Hmepage_background,bg_color="transparent", text="")
   Homepage_image_label.place(relx=0, rely=0)

   Feature_frame= Ctk.CTkFrame(master=Notice_frame, width=(screen_width-350), height= 100 , fg_color="#8c7cbc")
   Feature_frame.place(relx=0, rely=0)

   Cont_frame= Ctk.CTkFrame(master=Notice_frame, width=(screen_width-500), height=(400), fg_color="#8377b8", corner_radius=10, bg_color="white")
   Cont_frame.place(relx=0.07, rely=0.3)

   Feature_label= Ctk.CTkLabel(master=Feature_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                               justify= LEFT,text_color="white", font=("bold",25))
   Feature_label.place (relx=0.05, rely=0.05)

   Notice_label= Ctk.CTkLabel(master=Cont_frame, text="Notices:", text_color="white", font=("bold",25), fg_color="#8377b8")
   Notice_label.place(relx=0.05, rely=0.1)
   return Notice_frame


def invoice():
    Invoice_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-200), fg_color="#746cb4")
    Invoice_frame.place(relx=0.2, rely=0.35)

    Hmepage_background = Ctk.CTkImage(light_image=Image.open('Homepage_background.png'),
                                        size=(screen_width-350, screen_height-100))
    Homepage_image_label= Ctk.CTkLabel(master=Invoice_frame, image=Hmepage_background,bg_color="transparent", text="")
    Homepage_image_label.place(relx=0, rely=0)

    Feature_frame= Ctk.CTkFrame(master=Invoice_frame, width=(screen_width-350), height= 100 , fg_color="#8c7cbc")
    Feature_frame.place(relx=0, rely=0)

    Cont_frame= Ctk.CTkFrame(master=Invoice_frame, width=(screen_width-500), height=(400), fg_color="#8377b8", corner_radius=10, bg_color="white")
    Cont_frame.place(relx=0.07, rely=0.3)

    Feature_label= Ctk.CTkLabel(master=Feature_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                               justify= LEFT,text_color="white", font=("bold",25))
    Feature_label.place (relx=0.05, rely=0.05)

 

    Invoice_label= Ctk.CTkLabel(master=Cont_frame, text="INVOICE:", font=("bold", 25), text_color="white")
    Invoice_label.place(relx=0.05, rely=0.1)

    current_month = datetime.now().strftime("%B")

    Month_label=Ctk.CTkLabel(master=Cont_frame, text=f"{current_month} month", font=("bold", 25), text_color="white")
    Month_label.place(relx=0.4, rely=0.2)

    return Invoice_frame

def complaint():
   
    Complaint_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-200), fg_color="#746cb4")
    Complaint_frame.place(relx=0.2, rely=0.35)

    Hmepage_background = Ctk.CTkImage(light_image=Image.open('Homepage_background.png'),
                                        size=(screen_width-350, screen_height-100))
    Homepage_image_label= Ctk.CTkLabel(master=Complaint_frame, image=Hmepage_background,bg_color="transparent", text="")
    Homepage_image_label.place(relx=0, rely=0)

    Feature_frame= Ctk.CTkFrame(master=Complaint_frame, width=(screen_width-350), height= 100 , fg_color="#8c7cbc")
    Feature_frame.place(relx=0, rely=0)

    Cont_frame= Ctk.CTkFrame(master=Complaint_frame, width=(screen_width-500), height=(400), fg_color="#8377b8", corner_radius=10, bg_color="white")
    Cont_frame.place(relx=0.07, rely=0.3)

    Feature_label= Ctk.CTkLabel(master=Feature_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                               justify= LEFT,text_color="white", font=("bold",25))
    Feature_label.place (relx=0.05, rely=0.05)

 

    Complaint_label= Ctk.CTkLabel(master=Cont_frame, text="Complaint:", font=("bold", 25), text_color="white")
    Complaint_label.place(relx=0.05, rely=0.05)

    Subject_label= Ctk.CTkLabel(master=Cont_frame, text="Subject:", font=("bold",20))
    Subject_label.place(relx=0.1, rely=0.15)

    Subject_entry= Ctk.CTkEntry(master=Cont_frame, placeholder_text="Write your subject here",
    width=400, placeholder_text_color="white", fg_color="gray")
    Subject_entry.place(relx=0.2, rely=0.15)

    Complaint_text = Text(master=Cont_frame, height=15, width=85, wrap=WORD, bg='gray', fg='white')
    Complaint_text.place(relx=0.1, rely=0.3)

    return Complaint_frame

def emergency():

   Emergency_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100), fg_color="#746cb4")
   Emergency_frame.place(relx=0.2, rely=0.35)

   Hmepage_background = Ctk.CTkImage(light_image=Image.open('Homepage_background.png'),
                                       size=(screen_width-350, screen_height-100))
   Homepage_image_label= Ctk.CTkLabel(master=Emergency_frame, image=Hmepage_background,bg_color="transparent", text="")
   Homepage_image_label.place(relx=0, rely=0)

   Feature_frame= Ctk.CTkFrame(master=Emergency_frame, width=(screen_width-350), height= 100 , fg_color="#8c7cbc")
   Feature_frame.place(relx=0, rely=0)

   Feature_label= Ctk.CTkLabel(master=Feature_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                               justify= LEFT,text_color="white", font=("bold",25))
   Feature_label.place (relx=0.05, rely=0.05)

   Change_btn= Ctk.CTkButton(master=Emergency_frame, text="Contact Numbers", width=250, height=100, fg_color="#4B3A91", bg_color="white",
                             font=("bold",20))
   Change_btn.place(relx=0.15, rely=0.3)

   swap_btn= Ctk.CTkButton(master=Emergency_frame, text="Health issues", width=250, height=100, fg_color="#4B3A91", bg_color="white",
                             font=("bold",20))
   swap_btn.place(relx=0.55, rely=0.3)

   Room_upgrade= Ctk.CTkButton(master=Emergency_frame, text="Personal Contacts", width=250, height=100, fg_color="#4B3A91", bg_color="white",
                             font=("bold",20))
   Room_upgrade.place(relx=0.15, rely=0.6)

   occupancy_btn= Ctk.CTkButton(master=Emergency_frame, text="Emergency \nprocedures", width=250, height=100, fg_color="#4B3A91", bg_color="white",
                             font=("bold",20))
   occupancy_btn.place(relx=0.55, rely=0.6)
  
   return Emergency_frame

def setting():
   Setting_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-200), fg_color="white")
   Setting_frame.place(relx=0.2, rely=0.35)

   Hmepage_background = Ctk.CTkImage(light_image=Image.open('Homepage_background.png'),
                                       size=(screen_width-350, screen_height-100))
   Homepage_image_label= Ctk.CTkLabel(master=Setting_frame, image=Hmepage_background,bg_color="transparent", text="")
   Homepage_image_label.place(relx=0, rely=0)

   Feature_frame= Ctk.CTkFrame(master=Setting_frame, width=(screen_width-350), height= 100 , fg_color="#8c7cbc")
   Feature_frame.place(relx=0, rely=0)

   Cont_frame= Ctk.CTkFrame(master=Setting_frame, width=(screen_width-500), height=(400), fg_color="#8377b8", corner_radius=10, bg_color="white")
   Cont_frame.place(relx=0.07, rely=0.3)

   Feature_label= Ctk.CTkLabel(master=Feature_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                               justify= LEFT,text_color="white", font=("bold",25))
   Feature_label.place (relx=0.05, rely=0.05)

   Notice_label= Ctk.CTkLabel(master=Cont_frame, text="Setting", text_color="white", font=("bold",25), fg_color="#8377b8")
   Notice_label.place(relx=0.05, rely=0.1)

   Search_entry= Ctk.CTkEntry(master=Cont_frame, placeholder_text="Search setting", width=300, height=30,text_color="white",fg_color="#555252")
   Search_entry.place(relx=0.3, rely=0.2)

   Account_btn= Ctk.CTkButton(master=Cont_frame, text="Account", width=400, height=30,fg_color="#555252",
                              anchor=W)
   Account_btn.place(relx=0.15, rely=0.4)

   Setting_notification_btn= Ctk.CTkButton(master=Cont_frame, text="Notification", width=400, height=30, 
                                           image=notification_image, fg_color="#555252", anchor=W)
   Setting_notification_btn.place(relx=0.15, rely=0.5)

   Update_password_btn= Ctk.CTkButton(master=Cont_frame, text="Update password", width=400, height=30, fg_color="#555252",
                                      anchor=W)
   Update_password_btn.place(relx=0.15, rely=0.6)

   Change_contact_btn= Ctk.CTkButton(master=Cont_frame, text="Change contact", width=400, height=30, fg_color="#555252",
                                     anchor=W)
   Change_contact_btn.place(relx=0.15, rely=0.7)







   return Setting_frame


def room():

    
    global Menu_frame
    global current_frame

    Menu_frame.destroy()
    current_frame.destroy()
    room_frame= Ctk.CTkFrame(master=Homepage, width=screen_height, height=(screen_height-100) )
    room_frame.place(relx=0, rely=0.1)

    # add `from PIL import Image` on top
    Room_background = Ctk.CTkImage(light_image=Image.open('Room_background.png'),
                                      size=(screen_width, (screen_height-100)))
    
    Room_background_label= Ctk.CTkLabel(master=room_frame, image=Room_background, text="")
    Room_background_label.place(relx=0, rely=0)

    # Total_room_lbl=Ctk.CTkLabel(master=Homepage)


    return room_frame





Top_frame= Frame(master=Homepage, width=screen_width, height=100, bg="#746cb4", highlightbackground="black", highlightthickness=1,highlightcolor="red")
Top_frame.place(relx=0, rely=0)

Toggle_btn= Ctk.CTkButton(master=Top_frame, text="☰", font=("bold", 20), corner_radius=0, fg_color="#746cb4", bg_color="#5c54a4", command=menu)
Toggle_btn.place(relx=0.2, rely=0.05)

Hostel_label = Ctk.CTkLabel(master=Top_frame, text="Griha Hostel", font=("helvetica", 25, "bold"), text_color="white", fg_color="#746cb4")
Hostel_label.place(relx=0.01, rely=0.05)

Lbl1= Ctk.CTkLabel(master=Top_frame, text="Hi, there", font=("helvetica", 15) , text_color="white", fg_color="#746cb4" )
Lbl1.place(relx=0.01, rely=0.29)

Dashboard_btn= Ctk.CTkButton(master=Top_frame, text="Dashboard", fg_color="#746cb4", font=("bold",15),command=menu)
Dashboard_btn.place(relx=0.35, rely=0.4)

Room_btn= Ctk.CTkButton(master=Top_frame, text="Rooms", fg_color="#746cb4", font=("bold",15),
                         command=lambda: toggle_button("Rooms", room))
Room_btn.place(relx=0.48, rely=0.4)

Special_req_btn= Ctk.CTkButton(master=Top_frame, text="Special Request", fg_color="#746cb4", font=("bold",15))
Special_req_btn.place(relx=0.62, rely=0.4)

# add `from PIL import Image` on top
notification_image = Ctk.CTkImage(light_image=Image.open('notification.png'),
                                  size=(20, 20))

# add `from PIL import Image` on top
calendar_image = Ctk.CTkImage(light_image=Image.open('calendar.png'),
size=(20, 20))

# add `from PIL import Image` on top
profile_image = Ctk.CTkImage(light_image=Image.open('profile.png'),
                                  size=(20, 20))

Notification_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#746cb4", corner_radius=80, 
                                width=40, image=notification_image)
Notification_btn.place(relx=0.75, rely=0.4)

Calender_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#746cb4", 
                            corner_radius=80, width=30, image=calendar_image)
Calender_btn.place(relx=0.8, rely=0.4)

What_btn= Ctk.CTkButton(master=Top_frame,text="?", bg_color="#746cb4",width=50, text_color="purple",
                        corner_radius=80, font=("bold", 20))
What_btn.place(relx=0.85, rely=0.4)

Profile_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#746cb4", width=40,
                           corner_radius=80, image=profile_image)
Profile_btn.place(relx=0.9, rely=0.4)



menu()




Homepage.mainloop()
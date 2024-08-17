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

conn= sqlite3.connect("hostel.db")
c=conn.cursor()


    
def logout_system():
    
    Homepage.destroy()
    import Login
    Login.login_page()


def show_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = frame
    current_frame.place(relx=0.2, rely=0.14)
   

global Status_btn
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
     global Status_btn, Change_frame
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
     complaint_image = Ctk.CTkImage(light_image=Image.open('images\\complaint.png'),
                                       size=(30, 30))
    
   
     
     Status_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Status", text_color="black", command=lambda: toggle_button("Status",status),
                        image=alert_image)
     Status_btn.place(relx=0, rely=0)
   
     Notice_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Notice", text_color="black", command=lambda: toggle_button("Notice",notice), 
                        image=speaker_image)
     Notice_btn.place(relx=0, rely=0.1) 
   
     Invoice_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Invoice", text_color="black", command=lambda: toggle_button("Invoice",invoice), 
                        image=invoice_image)
     Invoice_btn.place(relx=0, rely=0.2)
   
     Complaint_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Complaint", text_color="black", command=lambda: toggle_button("Complaint",complaint), image=complaint_image)
     Complaint_btn.place(relx=0, rely=0.3)
   
     Emergency_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Emergency Contact", text_color="black", command= lambda: toggle_button("Emergency Contact",emergency), 
                        image=emergency_image)
     Emergency_btn.place(relx=0, rely=0.4)
   
     Setting_btn= Ctk.CTkButton(master=Menu_frame, width=250, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Setting", text_color="black", command=lambda: toggle_button("Setting", setting), image=setting_image)
     Setting_btn.place(relx=0, rely=0.5)
   
     menu_button=[Status_btn,Notice_btn,Invoice_btn, Complaint_btn,Emergency_btn, Setting_btn]
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
   
   
   def status():
      
      global Change_btn
   
      global Change_frame
      Change_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-100), height=(screen_height-100), fg_color="#EDF1F5")
      Change_frame.place(relx=0.2, rely=0)

      Status_label= Ctk.CTkLabel(master=Change_frame, text="Status", text_color="#1AD8E4", font=("bold",25))
      Status_label.place(relx=0.01, rely=0.01)

      Subtitle_label= Ctk.CTkLabel(master=Change_frame, text="A quick data overview of the Status.", text_color="#1AD8E4",font=("bold",15))
      Subtitle_label.place(relx=0.01, rely=0.05)

      # Overall Status Frame

      Overall_status_frame= Ctk.CTkFrame(master=Change_frame, width=240, height=180, fg_color="white", border_color="#01A768", border_width=1)
      Overall_status_frame.place(relx=0.01, rely=0.1)

      Overall_status_label= Ctk.CTkLabel(master=Overall_status_frame, text="Overall Status", text_color="#1AD8E4", font=("bold",20))
      Overall_status_label.place(relx=0.25, rely=0.35)

      Good_label= Ctk.CTkLabel(master=Overall_status_frame, text="Good", font=("bold",15), text_color="#1AD8E4")
      Good_label.place(relx=0.38, rely=0.55)

      Detailed_status_report_btn= Ctk.CTkButton(master=Overall_status_frame, text="View Detailed Report", text_color="#1AD8E4", 
                                         width=240, height=40, fg_color="#8FEDF3", border_color="#01A768", border_width=1,
                                         corner_radius=0)
      Detailed_status_report_btn.place(relx=0, rely=0.78)

      #Joined date frame

      Joined_frame= Ctk.CTkFrame(master=Change_frame, width=240, height=180, fg_color="white", border_color="#FED600", border_width=1)
      Joined_frame.place(relx=0.23, rely=0.1)

      Joined_date_label= Ctk.CTkLabel(master=Joined_frame, text="Joined Date", text_color="#1AD8E4", font=("bold",20))
      Joined_date_label.place(relx=0.25, rely=0.35)

      date_label= Ctk.CTkLabel(master=Joined_frame, text="Jan 2024", font=("bold",15), text_color="#1AD8E4")
      date_label.place(relx=0.3, rely=0.55)

      Detailed_joined_report_btn= Ctk.CTkButton(master=Joined_frame, text="View Detailed Report", text_color="#1AD8E4", 
                                         width=240, height=40, fg_color="#F3E8AD", border_color="#FED600", border_width=1,
                                         corner_radius=0)
      Detailed_joined_report_btn.place(relx=0, rely=0.78)

      # Paid up frame

      Paid_frame= Ctk.CTkFrame(master=Change_frame, width=240, height=180, fg_color="white", border_color="#03A9F5", border_width=1)
      Paid_frame.place(relx=0.44, rely=0.1)

      Paid_label= Ctk.CTkLabel(master=Paid_frame, text="Paid Up-To", text_color="#1AD8E4", font=("bold",20))
      Paid_label.place(relx=0.25, rely=0.35)

      Remaining_label= Ctk.CTkLabel(master=Paid_frame, text="3 month remaining", font=("bold",15), text_color="#1AD8E4")
      Remaining_label.place(relx=0.25, rely=0.55)

      Detailed_Paid_report_btn= Ctk.CTkButton(master=Paid_frame, text="View Detailed Report", text_color="#1AD8E4", 
                                         width=240, height=40, fg_color="#8FEDF3", border_color="#03A9F5", border_width=1,
                                         corner_radius=0)
      Detailed_Paid_report_btn.place(relx=0, rely=0.78)      


      #Disciplinary act frame
      
      Disciplinary_frame= Ctk.CTkFrame(master=Change_frame, width=240, height=180, fg_color="white", border_color="#F0483E", border_width=1)
      Disciplinary_frame.place(relx=0.65, rely=0.1)

      Disciplinary_label= Ctk.CTkLabel(master=Disciplinary_frame, text="Discipinary", text_color="#1AD8E4", font=("bold",20))
      Disciplinary_label.place(relx=0.25, rely=0.35)

      Complaint_found_label= Ctk.CTkLabel(master=Disciplinary_frame, text="Found Complaints", font=("bold",15), text_color="#1AD8E4")
      Complaint_found_label.place(relx=0.25, rely=0.55)

      Detailed_disciplinary_report_btn= Ctk.CTkButton(master=Disciplinary_frame, text="View Detailed Report", text_color="#1AD8E4", 
                                         width=240, height=40, fg_color="#ECC3C1", border_color="#F0483E", border_width=1,
                                         corner_radius=0)
      Detailed_disciplinary_report_btn.place(relx=0, rely=0.78)

      # Second frame

      Second_frame= Ctk.CTkFrame(master=Change_frame, width=screen_width, height=(screen_height-300), fg_color="white")
      Second_frame.place(relx=0, rely=0.4)


      # Routine Frame

      Routine_frame= Ctk.CTkFrame(master=Second_frame, width=500, height=150, fg_color="white", border_color="#1D242E", border_width=1)
      Routine_frame.place(relx=0.01, rely=0.01)

      Routine2_frame= Ctk.CTkFrame(master=Routine_frame, width=500, height=50, fg_color="white", border_color="#1D242E", border_width=1,
                                   corner_radius=0)
      Routine2_frame.place(relx=0, rely=0)

      Routine_label= Ctk.CTkLabel(master=Routine2_frame, text="Routine", text_color="#1AD8E4", font=("bold", 20))
      Routine_label.place(relx=0.05, rely=0.3)

      Configuration_btn= Ctk.CTkButton(master=Routine2_frame, text="Go to configuration", text_color="#1AD8E4", font=("bold",15),
                                       fg_color="white", command=room)
      Configuration_btn.place(relx=0.55, rely=0.3)

      label4= Ctk.CTkLabel(master=Routine_frame, text="4", font=("bold",35), text_color="#1AD8E4")
      label4.place(relx=0.1, rely=0.4)

      Special_food_label= Ctk.CTkLabel(master=Routine_frame, text="Special Food Days",text_color="#1AD8E4", font=("bold",15))
      Special_food_label.place(relx=0.1, rely=0.7)

      label2= Ctk.CTkLabel(master=Routine_frame, text="2", font=("bold",35), text_color="#1AD8E4")
      label2.place(relx=0.7, rely=0.4)

      Laundry_label= Ctk.CTkLabel(master=Routine_frame, text="Laundry Days", text_color="#1AD8E4", font=("bold", 15))
      Laundry_label.place(relx=0.7, rely=0.7)

      # Quick report frame

      Quick_report_frame= Ctk.CTkFrame(master=Second_frame, width=500, height=150, fg_color="white", border_color="#1D242E",
                                       border_width=1)

      Quick_report_frame.place(relx=0.4, rely=0.01)

      Report2_frame= Ctk.CTkFrame(master=Quick_report_frame, width=500, height=50, fg_color="white", border_color="#1D242E", border_width=1,
                                  corner_radius=0)
      Report2_frame.place(relx=0, rely=0)

      Reprot_label= Ctk.CTkLabel(master=Report2_frame, text="Quick report", font=("bold",20), text_color="#1AD8E4")
      Reprot_label.place(relx=0.05,rely=0.3)


      Lable0= Ctk.CTkLabel(master=Quick_report_frame, text="0", font=("bold",35), text_color="#1AD8E4")
      Lable0.place(relx=0.1, rely=0.4)

      NO_disciplinary_label= Ctk.CTkLabel(master=Quick_report_frame, text="No Disciplinary Acts Found", text_color="#1AD8E4", font=("bold",15))
      NO_disciplinary_label.place(relx=0.1, rely=0.65)

      Month_lable= Ctk.CTkLabel(master=Quick_report_frame, text="8", font=("bold",35), text_color="#1AD8E4")
      Month_lable.place(relx=0.7, rely= 0.4)

      Staying_label= Ctk.CTkLabel(master=Quick_report_frame, text="Staying from past", text_color="#1AD8E4", font=("bold",15))
      Staying_label.place(relx=0.7, rely=0.65)


      # My room frame

      My_room_frame= Ctk.CTkFrame(master=Change_frame, width=500, height=150, fg_color="white", border_color="#1D242E", border_width=1)
      My_room_frame.place(relx=0.01, rely=0.65)

      My_room_frame2= Ctk.CTkFrame(master=My_room_frame, width=500, height=50, fg_color="white", border_color="#1D242E", border_width=1,
                                   corner_radius=0)
      My_room_frame2.place(relx=0, rely=0)

      My_room_label= Ctk.CTkLabel(master=My_room_frame2, text="My Room", text_color="#1AD8E4", font=("bold",20))
      My_room_label.place(relx=0.05, rely=0.3)

      My_room_configuration= Ctk.CTkButton(master=My_room_frame2, text="Go To Configuration", text_color="#1AD8E4", font=("bold",15),
                                           fg_color="white")
      My_room_configuration.place(relx=0.65, rely=0.3)

      Lable04= Ctk.CTkLabel(master=My_room_frame, text="04", font=("bold",35), text_color="#1AD8E4")
      Lable04.place(relx=0.1, rely=0.4)

      Total_bed_label= Ctk.CTkLabel(master=My_room_frame, text="Total No Of Beds", text_color="#1AD8E4", font=("bold",15))
      Total_bed_label.place(relx=0.1, rely=0.65)

      Label204= Ctk.CTkLabel(master=My_room_frame, text="04", text_color="#1AD8E4", font=("bold",35))
      Label204.place(relx=0.7, rely=0.4)
      
      Total_inmates_label= Ctk.CTkLabel(master=My_room_frame, text="Total no of inmates", text_color="#1AD8E4", font=("bold",15))
      Total_inmates_label.place(relx=0.7, rely=0.65)


   
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

      def display_notices():
          c.execute("SELECT * FROM update_notice")
          data = c.fetchall()
          
          x = 0.15
          y = 0.1
          for i, row in enumerate(data):
              label = Ctk.CTkLabel(master=Cont_frame, text=row[0], width=500, height=40, fg_color="#1AD8E4")  
              label.place(relx=x, rely=y)    
              y += 0.15  # increment y for each label
      
      display_notices()
      

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

       first_frame= Ctk.CTkFrame(master=Cont_frame, width=500, height=60, fg_color="#EDF1F5", corner_radius=15, border_color="black", 
                                 border_width=1)
       first_frame.place(relx=0.25, rely=0.2)
   


       Month_amount_label= Ctk.CTkLabel(master=first_frame, text="Month\t\t\tAmount", font=("bold",25))
       Month_amount_label.place(relx=0.1, rely=0.2)

       Proceed_button= Ctk.CTkButton(master=Cont_frame, text="Proceed to pay", font=("bold", 20), fg_color="#17EBAB")
       Proceed_button.place(relx=0.7, rely=0.92)

   
       return Invoice_frame
   
   def complaint():
       
       global Complaint_text
       global Subject_entry


       c.execute("""CREATE TABLE IF NOT EXISTS complaint(
                 
                 subject TEXT,
                 complaint TEXT
                 )
                 
                 """)
       
      
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

       submit_button= Ctk.CTkButton(master=Cont_frame, text="Submit Complain", font=("bold", 20), fg_color="#17EBAB",
                                    command=get_Complaint)
       submit_button.place(relx=0.7, rely=0.92)
   
       return Complaint_frame
   
   def get_Complaint():
       

       c.execute(" INSERT INTO complaint(subject,complaint) VALUES(?,?)",
                 (Subject_entry.get(), Complaint_text.get("1.0","end-1c")))
       
       messagebox.showinfo("Info","Your Complaint has been successfully submitted")

       conn.commit()
       

       Subject_entry.delete(0,END)
       Complaint_text.delete("1.0","end-1c")
       

       

   
   def emergency():
      

       c.execute("SELECT father_contact, mother_contact FROM profile WHERE username=?", (username,))
       result = c.fetchone()
      
       
       father_number = mother_number = "No contact"
       
       if result:
           father_number, mother_number = result
       
       Emergency_frame = Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100), fg_color="#EDF1F5")
       Emergency_frame.place(relx=0.25, rely=0)
       
       Feature_label = Ctk.CTkLabel(master=Emergency_frame, text="Feature: We offer our honerable student to change their status such as room, bed,\noccupancy and so on", 
                                    justify=LEFT, text_color="black", font=("bold", 25))
       Feature_label.place(relx=0, rely=0.05)
       
       Cont_frame = Ctk.CTkFrame(master=Emergency_frame, width=(screen_width-500), height=(400), fg_color="#A7DCF5", corner_radius=10, bg_color="white")
       Cont_frame.place(relx=0.1, rely=0.2)
       
       Contact_label = Ctk.CTkLabel(master=Cont_frame, text="Contacts:", font=("bold", 25), text_color="black")
       Contact_label.place(relx=0.05, rely=0.05)
       
       Header_label = Ctk.CTkLabel(master=Cont_frame, text="Relation \t\t\t\t Number", text_color="black", font=("bold", 25))
       Header_label.place(relx=0.18, rely=0.25)
       
       Father_contact = Ctk.CTkLabel(master=Cont_frame, text="Father \t\t\t\t +977-{}".format(father_number), font=("bold", 20))
       Father_contact.place(relx=0.2, rely=0.4)
       
       Mother_contact = Ctk.CTkLabel(master=Cont_frame, text="Mother \t\t\t\t +977-{}".format(mother_number), font=("bold", 20))
       Mother_contact.place(relx=0.2, rely=0.55)
       
       Police_contace = Ctk.CTkLabel(master=Cont_frame, text="Police \t\t\t\t 100", font=("bold", 20))
       Police_contace.place(relx=0.2, rely=0.7)
       
       Warden_contact = Ctk.CTkLabel(master=Cont_frame, text="Warden \t\t\t\t +977-984561287", font=("bold", 20))
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

    c.execute("""CREATE TABLE IF NOT EXISTS profile(
                name TEXT,
                email TEXT,
                gurdian TEXT,
                contact TEXT,
                emergency_contact TEXT,
                username TEXT,
                father_contact TEXT,
                mother_contact
              
                )""")
    conn.commit()
    

    global Cont_frame
    global Profile_page_frame
    global Name_entry
    global Email_entry
    global Gurdian_name_entry
    global Contact_entry
    global Emergency_contact_entry

    Profile_page_frame = Ctk.CTkFrame(master=Cont_frame, width=screen_width, height=screen_height, fg_color="#A7DCF5")
    Profile_page_frame.place(relx=0, rely=0)

    Update_profile_label = Ctk.CTkLabel(master=Profile_page_frame, text="Update Profile", text_color="#CD1818", font=("bold", 20))
    Update_profile_label.place(relx=0.3, rely=0.01)

    Name_label = Ctk.CTkLabel(master=Profile_page_frame, text="Name:", text_color="black", font=("bold", 20))
    Name_label.place(relx=0.05, rely=0.1)

    Email_label = Ctk.CTkLabel(master=Profile_page_frame, text="Email:", text_color="Black", font=("bold", 20))
    Email_label.place(relx=0.05, rely=0.18)

    Guardian_name_label = Ctk.CTkLabel(master=Profile_page_frame, text="Guardian's Name:", text_color="black", font=("bold", 20))
    Guardian_name_label.place(relx=0.05, rely=0.26)

    Contact_no_label = Ctk.CTkLabel(master=Profile_page_frame, text="Contact No:", text_color="Black", font=("bold", 20))
    Contact_no_label.place(relx=0.05, rely=0.34)

    Emergency_contact_label = Ctk.CTkLabel(master=Profile_page_frame, text="Emergency Contact no:", text_color="Black", font=("bold", 20))
    Emergency_contact_label.place(relx=0.05, rely=0.42)

    Name_entry = Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
    Name_entry.place(relx=0.25, rely=0.1)

    Email_entry = Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
    Email_entry.place(relx=0.25, rely=0.18)

    Gurdian_name_entry = Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
    Gurdian_name_entry.place(relx=0.25, rely=0.26)

    Contact_entry = Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
    Contact_entry.place(relx=0.25, rely=0.34)

    Emergency_contact_entry = Ctk.CTkEntry(master=Profile_page_frame, width=350, height=40)
    Emergency_contact_entry.place(relx=0.25, rely=0.42)

    Submit_btn = Ctk.CTkButton(master=Profile_page_frame, text="Submit", fg_color="#3FB5CB", command=update_add)
    Submit_btn.place(relx=0.5, rely=0.48)

    Back_image = Ctk.CTkImage(light_image=Image.open('images\\back.png'), size=(30, 30))
    Back_btn = Ctk.CTkButton(master=Profile_page_frame, text="", image=Back_image, fg_color="#A7DCF5", command=profile_back)
    Back_btn.place(relx=0.01, rely=0.01)

    c.execute("SELECT * FROM profile WHERE username=?", (username,))
    row = c.fetchone()
    if row is None:
        # If the profile is empty, insert the user's information
        c.execute("INSERT INTO profile (name, email, gurdian, contact, emergency_contact, username) VALUES (?, ?, ?, ?, ?, ?)",
                  (Name_entry.get(), Email_entry.get(), Gurdian_name_entry.get(), Contact_entry.get(), Emergency_contact_entry.get(), username))
        conn.commit()
    

    return Profile_page_frame


   def update_add():

     c.execute(
        """UPDATE profile SET
        name= :Uname,
        email = :Uemail,
        gurdian= :Ugurdian,
        contact= :Ucontact,
        emergency_contact= :Uemergency
        WHERE username= :Username""",
        {
            "Uname": Name_entry.get(),
            "Uemail": Email_entry.get(),
            "Ugurdian": Gurdian_name_entry.get(),
            "Ucontact": Contact_entry.get(),
            "Uemergency": Emergency_contact_entry.get(),
            "Username": username
        },
    )
     conn.commit()
    
     messagebox.showinfo("Info", "Your profile has been updated successfully")

       
    
   
   def profile_back():
       
       
       Profile_page_frame.destroy()

   def change_pass():
       
       global Cont_frame
       global change_pass_page_frame
       global Old_pass_entry
       global New_pass_entry
       global Confirm_pass_entry
       global First_pet_name_entry
       global Favourite_food_entry

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
                                 text_color="black", command=update_password)
       Update_btn.place(relx=0.5, rely=0.45)

       Back_image = Ctk.CTkImage(light_image=Image.open('images\\back.png'),
                                          size=(30, 30))

       Back_btn= Ctk.CTkButton(master=change_pass_page_frame, text="", image=Back_image, fg_color="#A7DCF5", command=change_pass_back)
       Back_btn.place(relx=0.01,rely=0.01)
   
   def update_password():

    
    # Get the old password from the database
    c.execute("SELECT password FROM hostel WHERE username=?", (username,))
    old_password = c.fetchone()[0]
    
    # Check if the old password matches the one entered
    if Old_pass_entry.get() == old_password:
        # Check if the new password and confirm password match
        if New_pass_entry.get() == Confirm_pass_entry.get():
            # Update the password
            c.execute("UPDATE hostel SET password=? WHERE username=?", (New_pass_entry.get(), username))
            conn.commit()
           
            messagebox.showinfo("Info", "Password updated successfully")
            Old_pass_entry.delete(0,END)
            New_pass_entry.delete(0,END)
            Confirm_pass_entry.delete(0,END)
            First_pet_name_entry.delete(0,END)
            Favourite_food_entry.delete(0,END)

        else:
            messagebox.showerror("Error", "New password and confirm password do not match")
    else:
        messagebox.showerror("Error", "Old password is incorrect")

       
   
   def change_pass_back():
       global change_pass_page_frame
       
       change_pass_page_frame.destroy()

   def update_contact():
       global Cont_frame
       global update_contact_frame
       global Father_contact_entry
       global Mother_contact_entry

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
                                 text_color="black", command=contact_update)
       Update_btn.place(relx=0.6, rely=0.3)

       Back_image = Ctk.CTkImage(light_image=Image.open('images\\back.png'),
                                          size=(30, 30))

       Back_btn= Ctk.CTkButton(master=update_contact_frame, text="", image=Back_image, fg_color="#A7DCF5", command=update_contact_back)
       Back_btn.place(relx=0.01,rely=0.01)


       c.execute("SELECT * FROM profile WHERE username=?", (username,))
       row = c.fetchone()
       if row is None:
           # If the profile is empty, insert the user's information
           c.execute("INSERT INTO profile (father_contact,mother_contact) VALUES (?, ?)",
                     (Father_contact_entry.get(),Mother_contact_entry.get()))
           conn.commit()
       

   def contact_update():
       
     conn = sqlite3.connect("hostel.db")
     c = conn.cursor()
     c.execute(
        """UPDATE profile SET
        father_contact= :Ufather_contact,
        mother_contact= :Umother_contact
        WHERE username= :Username""",
        {
            "Ufather_contact":Father_contact_entry.get(),
            "Umother_contact": Mother_contact_entry.get(),
            "Username": username
        },
    )
     conn.commit()
     
     messagebox.showinfo("Info", "Your contact info has been updated successfully")
   
       


       



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
   toggle_button("Status", status)

   return dashboard_frame
   
def database(): 
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()

    # Create the furniture table
    c.execute("""
        CREATE TABLE IF NOT EXISTS furniture (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fan INTEGER,
            [table] INTEGER,
            chair INTEGER,
            bed INTEGER,
            teatable INTEGER,
            shoerack INTEGER,
            cupboard INTEGER,
            quantity INTEGER
        )
    """)

    # Insert initial quantities only if the table is empty
    c.execute("SELECT COUNT(*) FROM furniture")
    if c.fetchone()[0] == 0:
        c.execute("""
            INSERT INTO furniture (fan, [table], chair, bed, teatable, shoerack, cupboard, quantity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (50, 50, 50, 50, 50, 50, 50, 50))

    conn.commit()
   
    

def get_furniture_counts():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    c.execute("SELECT fan, [table], chair, bed, teatable, shoerack, cupboard FROM furniture")
    counts = c.fetchone()
   
    return counts


def room():

    global fan, table, chair, bed, teatable, shoerack, cupboard 
    fan, table, chair, bed, teatable, shoerack, cupboard = get_furniture_counts()

    global Celing_fan_label
    global table_label
    global chairs_label
    global bed_label
    global cupboard_label
    global tea_table_label
    global shoes_rack_label

    database()



# Connect to the database
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    
    # Create the furniture table
    c.execute("""
        CREATE TABLE IF NOT EXISTS furniture (
            id  PRIMARY KEY,
            fan ,
            [table] ,
            chair ,
            bed ,
            teatable ,
            shoerack ,
            cupboard ,
            quantity 
        )
    """) 


    # Insert the initial quantities into the table
    c.execute("""
        INSERT INTO furniture (fan, [table], chair, bed, teatable, shoerack, cupboard, quantity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (50, 50, 50, 50, 50, 50, 50, 50))


    c.execute("SELECT fan, [table],chair,bed,teatable,shoerack,cupboard FROM furniture")
    quant=c.fetchone()
    conn.commit()
   

    fan,table,chair,bed,teatable,shoerack,cupboard=quant

    Menu_frame.destroy()
    current_frame.destroy()

    room_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height-100))
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
                                      font=("bold",15), fg_color="#3FB5CB", corner_radius=15, command=change_room)
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


    # Furniture frame

    Furniture_frame= Ctk.CTkFrame(master= room_frame, width=350, height=450, fg_color="#555252", corner_radius=5)
    Furniture_frame.place(relx=0.7, rely=0.1)

    Furniture_label= Ctk.CTkLabel(master=Furniture_frame, text="Furniture", text_color="White", font=("bold",25))
    Furniture_label.place(relx=0.05, rely=0.03)

    Celing_fan_label= Ctk.CTkLabel(master=Furniture_frame, text="Celing fan \t\t {}".format(fan), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    Celing_fan_label.place(relx=0.1, rely=0.1)

    table_label= Ctk.CTkLabel(master=Furniture_frame, text="Table \t\t\t {}".format(table), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    table_label.place(relx=0.1, rely=0.2)

    chairs_label= Ctk.CTkLabel(master=Furniture_frame, text="Chairs \t\t\t {}".format(chair), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    chairs_label.place(relx=0.1, rely=0.3)

    bed_label= Ctk.CTkLabel(master=Furniture_frame, text="Beds \t\t\t {}".format(bed), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    bed_label.place(relx=0.1, rely=0.4)

    cupboard_label= Ctk.CTkLabel(master=Furniture_frame, text="Cupboard \t\t {}".format(cupboard), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    cupboard_label.place(relx=0.1, rely=0.5)

    tea_table_label= Ctk.CTkLabel(master=Furniture_frame, text="Tea Table \t\t {}".format(teatable), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    tea_table_label.place(relx=0.1, rely=0.6)

    shoes_rack_label= Ctk.CTkLabel(master=Furniture_frame, text="Shoes Rack \t\t {}".format(shoerack), text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#202020")
    shoes_rack_label.place(relx=0.1, rely=0.7)

    Claim_btn= Ctk.CTkButton(master=Furniture_frame, text="Claim Furniture", text_color="white",font=("bold",15),
                                   corner_radius=15, fg_color="#3FB5CB", width=100,height=40, command=claim_furniture)
    Claim_btn.place(relx=0.3, rely=0.8)

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
    canvas.place(relx=0.55, rely=0.2)

    # Data for the pie chart
    data = [180, 30]
    colors = ["#FFEB3B", "#FF4081"]

    # Draw the pie chart
    create_pie_chart(canvas, 100, 120, 70, 50, data, colors)



   

    return room_frame

def change_room():
       
       conn= sqlite3.connect("hostel.db")
       c= conn.cursor()
       c.execute("""CREATE TABLE IF NOT EXISTS change_room(
                 
                 block TEXT,
                 floor TEXT,
                 room_no TEXT,
                 username TEXT)""")
       conn.commit()
      
       
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
   
       Celing_fan_label= Ctk.CTkLabel(master=Furniture_frame, text="Celing fan \t\t {}".format(fan), text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       Celing_fan_label.place(relx=0.1, rely=0.1)
   
       table_label= Ctk.CTkLabel(master=Furniture_frame, text="Table \t\t\t {}".format(table), text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       table_label.place(relx=0.1, rely=0.2)
   
       chairs_label= Ctk.CTkLabel(master=Furniture_frame, text="Chairs \t\t\t {}".format(chair), text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       chairs_label.place(relx=0.1, rely=0.3)
   
       bed_label= Ctk.CTkLabel(master=Furniture_frame, text="Beds \t\t\t {}".format(bed), text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       bed_label.place(relx=0.1, rely=0.4)
   
       cupboard_label= Ctk.CTkLabel(master=Furniture_frame, text="Cupboard \t\t {}".format(cupboard), text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       cupboard_label.place(relx=0.1, rely=0.5)
   
       tea_table_label= Ctk.CTkLabel(master=Furniture_frame, text="Tea Table \t\t {}".format(teatable), text_color="white",font=("bold",15),
                                      corner_radius=15, fg_color="#202020")
       tea_table_label.place(relx=0.1, rely=0.6)
   
       shoes_rack_label= Ctk.CTkLabel(master=Furniture_frame, text="Shoes Rack \t\t {}".format(shoerack), text_color="white",font=("bold",15),
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
      
    # Get the requested quantities from the user
    fan = int(Celing_fan_entry.get())
    table = int(table_entry.get())
    chair = int(chairs_entry.get())
    bed = int(bed_entry.get())
    teatable = int(tea_table_entry.get())
    shoerack = int(shoes_rack_entry.get())
    cupboard = int(cupboard_entry.get())

    # Connect to the database
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()

    # Insert the request into the furniture_request table
    c.execute("INSERT INTO furniture_request(fan,[table],chair,bed,teatable,shoerack,cupboard,username) VALUES(?,?,?,?,?,?,?,?)",
              (fan, table, chair, bed, teatable, shoerack, cupboard, username))

    # Update the quantities in the furniture table
    c.execute("""
        UPDATE furniture
        SET fan = fan - ?, [table] = [table] - ?, chair = chair - ?, bed = bed - ?, teatable = teatable - ?, shoerack = shoerack - ?, cupboard = cupboard - ?, quantity = quantity - ?
    """, (fan, table, chair, bed, teatable, shoerack, cupboard, fan + table + chair + bed + teatable + shoerack + cupboard))

    # Commit the changes and close the connection
    conn.commit()
   

    # Clear the entry fields
    Celing_fan_entry.delete(0, END)
    table_entry.delete(0, END)
    chairs_entry.delete(0, END)
    bed_entry.delete(0, END)
    tea_table_entry.delete(0, END)
    shoes_rack_entry.delete(0, END)
    cupboard_entry.delete(0, END)

    # Display a success message
    messagebox.showinfo("Success", "Your request has been sent")
def claim_furniture():

    global Celing_fan_entry
    global chairs_entry
    global table_entry
    global bed_entry
    global shoes_rack_entry
    global tea_table_entry
    global cupboard_entry


    conn= sqlite3.connect("hostel.db")
    c= conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS furniture_request(
              
                 [fan] INT,
                 [table] INT,
                 [bed] INT,
                 [chair] INT,
                 [cupboard] INT,
                 [teatable] INT,
                 [shoerack] INT,
                 username TEXT
              )""")
    
    conn.commit()
   

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
                                      font=("bold",15), fg_color="#3FB5CB", corner_radius=15, command=change_room)
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
    canvas = Ctk.CTkCanvas(master=room_frame, width=175, height=200, bg='#D9D9D9', highlightthickness=0)
    canvas.place(relx=0.55, rely=0.2)

    # Data for the pie chart
    data = [180, 30]
    colors = ["#FFEB3B", "#FF4081"]

    # Draw the pie chart
    create_pie_chart(canvas, 100, 120, 70, 50, data, colors)


def claim_furniture_request():
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

        # Insert the request into the furniture_request table
        c.execute("INSERT INTO furniture_request(fan, [table], chair, bed, teatable, shoerack, cupboard, username) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (fan, table, chair, bed, teatable, shoerack, cupboard, username))

        # Update the quantities in the furniture table
        c.execute("""
            UPDATE furniture
            SET fan = fan - ?, [table] = [table] - ?, chair = chair - ?, bed = bed - ?, teatable = teatable - ?, shoerack = shoerack - ?, cupboard = cupboard - ?
        """, (fan, table, chair, bed, teatable, shoerack, cupboard))

        # Commit the changes and close the connection
        conn.commit()
       

        # Clear the entry fields
        Celing_fan_entry.delete(0, 'end')
        table_entry.delete(0, 'end')
        chairs_entry.delete(0, 'end')
        bed_entry.delete(0, 'end')
        tea_table_entry.delete(0, 'end')
        shoes_rack_entry.delete(0, 'end')
        cupboard_entry.delete(0, 'end')

        # Display a success message
        messagebox.showinfo("Success", "Furniture request submitted successfully!")

        room()

    except Exception as e:
        # Display an error message if the database is locked
        if str(e) == "database is locked":
            messagebox.showerror("Error", "The database is currently locked. Please try again later.")
        else:
            # Display the original error message for other types of OperationalErrors
            messagebox.showerror("Error", str(e))


             
            



def special_req():

    c.execute("""CREATE TABLE IF NOT EXISTS special_request(
              Leave_reason TEXT,
              days TEXT,
              informed TEXT,
              maintenance TEXT,
              event TEXT,
              catagory TEXT,
              username TEXT)""")
    
    conn.commit()

    Menu_frame.destroy()
    current_frame.destroy()
    global Reason_text
    global Days_entry
    global Title_text
    global Maintenance_text
    global permission
    global get_event
    

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
    
    def permission():
        if Yes_no_var.get()==1:
            return "Yes"
        elif Yes_no_var.get()==2:
            return "No"
        

    Submit_btn= Ctk.CTkButton(master=Leave_frame, text="Submit", fg_color="#1AD8E4", text_color="black", font=("bold",20),
                              command=request)
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

    def get_event():
        if catagory_var.get()==1:
            return "Education"
        elif catagory_var.get()==2:
            return "Mobile games"
        elif catagory_var.get()==3:
            return "Sports"
        elif catagory_var.get()==3:
            return "Other"           
    

    Event_request_btn= Ctk.CTkButton(master=Event_frame, text="Request", fg_color=("#1AD8E4"), text_color="black",
                                     command=request)
    Event_request_btn.place(relx=0.35, rely=0.85)


    #Maintenace Request Frame

    Maintenance_frame= Ctk.CTkFrame(master=special_req_frame, width=350, height=250, fg_color="#3FB5CB")
    Maintenance_frame.place(relx=0.05, rely=0.5)

    Mainntenance_label=Ctk.CTkLabel(master=Maintenance_frame, text="Maintenacne Request", text_color="White", font=("bold",25))
    Mainntenance_label.place(relx=0.01, rely=0.05)

    Specify_label= Ctk.CTkLabel(master=Maintenance_frame, text="Specify what happened", font=("bold",15))
    Specify_label.place(relx=0.05, rely=0.2)

    Maintenance_text= Text(master=Maintenance_frame, width=50, height=5, wrap=WORD, bg="#1AD8E4")
    Maintenance_text.place(relx=0, rely=0.3)

    Maintenance_btn= Ctk.CTkButton(master=Maintenance_frame, text="Submit", fg_color="#1AD8E4", text_color="black",
                                   command=request)
    Maintenance_btn.place(relx=0.3, rely=0.7)

def request():
    c.execute("INSERT INTO special_request(Leave_reason,days,informed,maintenance,event,catagory,username) VALUES(?,?,?,?,?,?,?)",
              (Reason_text.get("1.0","end-1c"),Days_entry.get(),permission(),Maintenance_text.get("1.0","end-1c"),get_event(),Title_text.get("1.0","end-1c"),username))
    
    messagebox.showinfo("Info","Your request has been submitted successfully")
    conn.commit()


pop_up_frame = None

def popup(frame_name):
    global pop_up_frame
    if pop_up_frame:
        pop_up_frame.destroy()
    pop_up_frame = Ctk.CTkFrame(master=Homepage, height=320, width=500, fg_color="#42ABC7", corner_radius=15, bg_color="#D9D9D9")
    pop_up_frame.place(relx=0.6, rely=0.15)
    if frame_name == "notification":
        notification()
    elif frame_name == "about":
        about()
    elif frame_name == "profile":
        profile()
    return pop_up_frame


#About frame


def about():
    

    About_frame= Ctk.CTkFrame(master=pop_up_frame, height=320, width=500, fg_color="#42ABC7", corner_radius=15, bg_color="white")
    About_frame.place(relx=0, rely=0)


    About_label=Ctk.CTkLabel(master=About_frame, text="About us", font=("bold",25), text_color="white")
    About_label.place(relx=0.05, rely=0.15)


    Content_label= Ctk.CTkLabel(master=About_frame, text="Griha hostel offers a welcoming and \ncomfortable living environment for\n students abd professionals.With\n modern amenities and facilities,and a\n supportive community,Griha hostel\n ensures a home-like experience away\n from home.", justify= LEFT,
                                text_color="white", font=("bold",20))
    Content_label.place(relx=0.1, rely=0.25)

    Exit_button= Ctk.CTkButton(master=About_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)


def notification():

    Notification_frame= Ctk.CTkFrame(master=pop_up_frame, height=300, width=500, fg_color="#42ABC7", corner_radius=15, bg_color="white")
    Notification_frame.place(relx=0, rely=0)


    Notification_label= Ctk.CTkLabel(master=Notification_frame, text="Notification", font=("bold",20), text_color="light gray")
    Notification_label.place(relx=0.05, rely=0.05)

    #first frame

    first_notice_frame= Ctk.CTkFrame(master=Notification_frame, width=500, height=60, fg_color="#BDA4A4",border_color="light gray",
                                     border_width=1, corner_radius=0)
    first_notice_frame.place(relx=0, rely=0.2)
    first_notice_lable= Ctk.CTkLabel(master=first_notice_frame, text=("Notice has been added by admin to the system, please check."),
                                     font=("bold",15), text_color="black", image=profile_image, compound=LEFT)
    first_notice_lable.place(relx=0.05, rely=0.2)

  # second frame

    second_notice_frame= Ctk.CTkFrame(master=Notification_frame, width=500, height=60, fg_color="#BDA4A4",border_color="light gray",
                                     border_width=1, corner_radius=0)
    second_notice_frame.place(relx=0, rely=0.4)
    second_notice_lable= Ctk.CTkLabel(master=second_notice_frame, text=("The meal Routine has been changed by admin."),
                                     font=("bold",15), text_color="black", image=profile_image, compound=LEFT)
    second_notice_lable.place(relx=0.05, rely=0.2)

# third frame

    third_notice_frame= Ctk.CTkFrame(master=Notification_frame, width=500, height=60, fg_color="#BDA4A4",border_color="light gray",
                                     border_width=1, corner_radius=0)
    third_notice_frame.place(relx=0, rely=0.6)
    third_notice_lable= Ctk.CTkLabel(master=third_notice_frame, text=("Furniture has been added to the hostel.Please claim."),
                                     font=("bold",15), text_color="black", image=profile_image, compound=LEFT)
    third_notice_lable.place(relx=0.05, rely=0.2)

#fourth frame

    fourth_notice_frame= Ctk.CTkFrame(master=Notification_frame, width=500, height=60, fg_color="#BDA4A4",border_color="light gray",
                                     border_width=1, corner_radius=0)
    fourth_notice_frame.place(relx=0, rely=0.8)
    fourth_notice_lable= Ctk.CTkLabel(master=fourth_notice_frame, text=("Your ID has been varified successfully."),
                                     font=("bold",15), text_color="black", image=profile_image, compound=LEFT)
    fourth_notice_lable.place(relx=0.05, rely=0.2)

    def back():
     
        pop_up_frame.destroy()


    Exit_button= Ctk.CTkButton(master=Notification_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)

    #profile frame

def profile():

    c.execute("SELECT email,gurdian,contact,emergency_contact FROM profile WHERE username=?",(username,))
    cont= c.fetchone()

    email,gurdian,contact,emergency=cont


    Name_label= Ctk.CTkLabel(pop_up_frame, text=username, font=("bold",20),text_color="white")
    Name_label.place(relx=0.3, rely=0.15)
    Email_label=Ctk.CTkLabel(pop_up_frame,text=f"Email:  {email}",font=("bold",20),text_color="white")
    Email_label.place(relx=0.3,rely=0.25)
    Gurdain_label= Ctk.CTkLabel(pop_up_frame, text=f"Gurdain: {gurdian}",font=("bold",20),text_color="white")
    Gurdain_label.place(relx=0.3,rely=0.35)
    Contact_label= Ctk.CTkLabel(pop_up_frame, text=f"Contact: {contact}",font=("bold",20),text_color="white")
    Contact_label.place(relx=0.3,rely=0.45)
    Emergency_contact_label= Ctk.CTkLabel(pop_up_frame, text=f"Emergency Contact: {emergency}",font=('bold',20),text_color="white")
    Emergency_contact_label.place(relx=0.3,rely=0.55)
    Exit_button= Ctk.CTkButton(master=pop_up_frame, text="X", command=back, width=30)
    Exit_button.place(relx=0.9, rely=0.05)

def back():
     
    pop_up_frame.destroy()

    




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
                                width=40, image=notification_image, command= lambda: popup("notification"))
Notification_btn.place(relx=0.75, rely=0.4)

Calender_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#3FB5CB",fg_color="#3FB5CB", 
                            corner_radius=80, width=30, image=calendar_image)
Calender_btn.place(relx=0.8, rely=0.4)

What_btn= Ctk.CTkButton(master=Top_frame,text="?", bg_color="#3FB5CB",fg_color="#3FB5CB",width=50, text_color="black",
                        corner_radius=80, font=("bold", 20), command=lambda:popup("about"))
What_btn.place(relx=0.85, rely=0.4)

Profile_btn= Ctk.CTkButton(master=Top_frame, text="", bg_color="#3FB5CB",fg_color="#3FB5CB", width=40,
                           corner_radius=80, image=profile_image, command=lambda:popup("profile"))
Profile_btn.place(relx=0.9, rely=0.4)

top_button=[Dashboard_btn,Room_btn,Special_req_btn]
button_color={btn.cget("text"): False for btn in top_button}


dashboard()




Homepage.mainloop()
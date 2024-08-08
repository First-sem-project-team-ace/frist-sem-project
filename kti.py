




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

def show_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = frame
    current_frame.place(relx=0.2, rely=0.095)
   

global Change_btn

menu_button=[]
button_color={}

def dashboard():
   
   dashboard_frame= Ctk.CTkFrame(master=Homepage, width=screen_width, height=(screen_height), fg_color="#EDF1F5")
   dashboard_frame.place(relx=0, rely=0.095)

   Top_frame= Frame(master=Homepage, width=screen_width, height=100, bg="#EDF1F5", highlightbackground="black", highlightthickness=1,highlightcolor="red")
   Top_frame.place(relx=0, rely=0)
    

   def menu():
    
     global Menu_frame
     
     global menu_button, button_color
   

   
   
     
     Menu_frame = Ctk.CTkFrame(master=Homepage, width=385, height=screen_height, bg_color="white", fg_color="#3FAEFF")
     Menu_frame.place(relx=0, rely=0.0)

     ownername_label=Ctk.CTkLabel(master=Menu_frame,text="Giriraj Rawat",font=("bold", 25),text_color="black",fg_color="white")
     ownername_label.place(relx=0.4,rely=0.1)
  
     ownerid_label=Ctk.CTkLabel(master=Menu_frame,text="id_no:0000001",font=("bold", 20),text_color="black",fg_color="white")
     ownerid_label.place(relx=0.4,rely=0.15)
  
  
     owner_image=Ctk.CTkImage(light_image=Image.open("Owner_Profile.png"),
                           size=(73, 79) )
     owner_label= Ctk.CTkLabel(master=Menu_frame, image=owner_image,text="" )
     owner_label.place(relx=0.1,rely=0.1)

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
   
   
     
   
     Appeared_btn= Ctk.CTkButton(master=Menu_frame, width=385, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Appeared Request", text_color="black", command=lambda: toggle_button("Appeared Request",Appeared), 
                        image=speaker_image,compound=LEFT)
     Appeared_btn.place(relx=0, rely=0.4) 
   
     Report_btn= Ctk.CTkButton(master=Menu_frame, width=385, height=60, fg_color="#3FB5CB", corner_radius=10, bg_color="white", font=("bold",15),
                        text="Learning", text_color="black", command=lambda: toggle_button("Learning",Learning), 
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
   
   

   def Learning():
     Report_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
     Report_frame.place(relx=0.25, rely=0.95)
     
     Search_entry= Ctk.CTkEntry(master=Report_frame, placeholder_text="Search setting", width=300, height=30,text_color="black",fg_color="#EDF1F5")
     Search_entry.place(relx=0.3, rely=0.2)
   
    
     
     return Report_frame


   def Appeared():
      Appeared_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5", corner_radius=20)
      Appeared_frame.place(relx=0.25, rely=0)
   
     
      return Appeared_frame
   
   
  
   
  
   
   def emergency():
   
      Emergency_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-250), height=(screen_height-100), fg_color="#EDF1F5")
      Emergency_frame.place(relx=0.25, rely=0)
   
   
    
   
      return Emergency_frame
   
   def setting():
      Setting_frame= Ctk.CTkFrame(master=Homepage, width=(screen_width-350), height=(screen_height-100), fg_color="#EDF1F5")
      Setting_frame.place(relx=0.25, rely=0)
   
    
   
  

    
   
   
 
   
      return Setting_frame
   
   menu()

   return dashboard_frame
   
   



dashboard()




Homepage.mainloop()
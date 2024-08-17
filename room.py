import customtkinter as Ctk
from tkinter import *
from PIL import Image
from datetime import datetime
from tkinter import messagebox

# from Login import username


Homepage= Ctk.CTk()

Ctk.set_appearance_mode('light')
Homepage.geometry("{0}x{1}+0+0".format(Homepage.winfo_screenwidth(), Homepage.winfo_screenheight()))
screen_width = Homepage.winfo_screenwidth()
screen_height = Homepage.winfo_screenheight()

current_frame = None


def room():

    

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

def change_room():
       
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
      messagebox.showinfo("Success","Your Request has been sent")
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
    tenant_label= Ctk.CTkLabel(master=tenant_frame, text="Tenant", text_color="black", font=("bold",15),
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
        messagebox.showinfo("Success", "Your request has been sent")
        room()
    
Homepage.mainloop()
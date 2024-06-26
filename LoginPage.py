import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

app= tk.Tk()

app.title("Griha Hostel")
# app.iconbitmap("abc.ico")
app.geometry("1366x768")
# app.maxsize(width=600 , height=400)
app.minsize(width=600, height=400)




def hygiene():
    print("")

def comfort():
    print("")

def security():
    print("")

def login():
    print(" Login button is clicked")

def register():
    print("Clicked")

# Set the background colour of the main window

app.configure(bg="#614BD4")

# top frame for the header

top_frame= tk.Frame(app, bg="#614BD4")
top_frame.pack(fill= tk.X)

#hostel name label

Hostel_label= tk.Label(top_frame, text="Griha Hostel", font=("helvetica", 25, "bold"), bg="#614BD4", fg="white")
Hostel_label.pack(side=tk.LEFT, padx=50, pady=20)

# login and register button
Login_btn= tk.Button(top_frame, text="Log In",command=login, bg="white", fg="#614BD4", padx=10, pady=5)
Login_btn.pack(side=tk.RIGHT, padx=5)

Register_btn= tk.Button(top_frame, text="Register",command= register, bg="white", fg="#614BD4", padx=10, pady=5)
Register_btn.pack(side=tk.RIGHT, padx=5)

# middle frame for the main content

middle_frame= tk.Frame(app, bg="#614BD4",width=600,height=100)
middle_frame.pack(fill=tk.BOTH, expand=True, pady=20)


#main headline label

Headline_label= tk.Label(middle_frame, text="YOUR HOME AWAY\nFROM HOME", font=("helvetica", 30, "bold"), bg="#614BD4", fg="white")
Headline_label.place(x=50,y=40)

#subheadline label

Subheadline_label= tk.Label(middle_frame, text="Experience Comfort In Every Corner", font=("helvetica", 14,"italic"), bg="#614BD4", fg="white")
Subheadline_label.place(x=50,y=150)

#frame for hygience, comfort and security

button_frame= tk.Frame(middle_frame, bg="pink",pady=8)
button_frame.pack(pady=200)

#hygience button

hygience_btn= tk.Button(button_frame, text="Hygience", command=hygiene, bg="white", fg="red", padx=150,pady=5)

hygience_btn.pack(side=tk.LEFT,padx=10)

#comfort button

comfort_btn= tk.Button(button_frame, text="Comfort",command=comfort, bg="white", fg="red", padx=150,pady=5)
comfort_btn.pack(side=tk.LEFT,padx=10)

#security button

security_btn= tk.Button(button_frame, text="Security", command=security, bg="white",fg="red", padx=150,pady=5)
security_btn.pack(side=tk.LEFT, padx=10)

#frame for the image

Image_frame= tk.Frame(app, bg="white", width=1366, height=800)
Image_frame.pack(fill=tk.BOTH, expand=True, pady=10)




#load and display an actual image

# image= Image.open("C:\\Users\\User\\OneDrive\\Desktop\\Project\\sunflower.png")
# resized_image= image.resize((1366,500))
# converted_image= ImageTk.PhotoImage(resized_image)
# image_label= tk.Label(Image_frame,image=resized_image, bg="white")
# image_label.pack(expand=True)

my_image= Image.open("C:\\Users\\User\\OneDrive\\Desktop\\Project\\Hostel.jpg")
resized_image= my_image.resize((1366,300))
converted_image= ImageTk.PhotoImage(resized_image)
my_label= tk.Label(Image_frame,image=converted_image)
my_label.pack()


mainloop()
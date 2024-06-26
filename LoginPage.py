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

canvas=tk.Canvas(app,bg="#614BD4",width=1366, height=300)
canvas.pack()

# top frame for the header

# top_frame= tk.Frame(app, bg="#614BD4")
# top_frame.pack(fill= tk.X)

#hostel name label

Hostel_label= tk.Label(app, text="Griha Hostel", font=("helvetica", 20, "bold"), bg="#614BD4", fg="white")
Hostel_label.place(x=50,y=20)

# login and register button
Login_btn= tk.Button(app, text="Log In",command=login, bg="white", fg="#614BD4", padx=10, pady=5)
Login_btn.place(x=1280,y=20)

Register_btn= tk.Button(app, text="Register",command= register, bg="white", fg="#614BD4", padx=10, pady=5)
Register_btn.place(x=1200,y=20)
# middle frame for the main content

# middle_frame= tk.Frame(app, bg="#614BD4",width=600,height=100)
# middle_frame.pack(fill=tk.BOTH, expand=True, pady=20)


#main headline label

Headline_label= tk.Label(app, text="YOUR HOME AWAY\nFROM HOME", font=("helvetica", 30, "bold"), bg="#614BD4", fg="white")
Headline_label.place(x=50,y=100)

#subheadline label

Subheadline_label= tk.Label(app, text="Experience Comfort In Every Corner", font=("helvetica", 14,"italic"), bg="#614BD4", fg="white")
Subheadline_label.place(x=50,y=200)

#frame for hygience, comfort and security


btn_canvas= tk.Canvas(app, bg="#E1DCDC",width=1050, height=50)
btn_canvas.place(x=150,y=280)

# hygiene button

hygiene_btn= tk.Button(app, text="Hygiene", command=hygiene, bg="white", fg="red", padx=80,pady=5)

hygiene_btn.place(x=200,y=290)

#comfort button

comfort_btn= tk.Button(app, text="Comfort",command=comfort, bg="white", fg="red", padx=80,pady=5)
comfort_btn.place(x=566,y=290)

# #security button

security_btn= tk.Button(app, text="Security", command=security, bg="white",fg="red", padx=80,pady=5)
security_btn.place(x=932,y=290)

#frame for the image

Image_frame= tk.Frame(app, bg="white", width=500, height=300)
Image_frame.pack(fill=tk.BOTH,expand=True)
Image_frame.destroy()


photo_canvas= tk.Canvas(app, bg="white", width=1366,height=400)
photo_canvas.place(x=0,y=400)


#load and display an actual image

# image= Image.open("C:\\Users\\User\\OneDrive\\Desktop\\Project\\sunflower.png")
# resized_image= image.resize((1366,500))
# converted_image= ImageTk.PhotoImage(resized_image)
# image_label= tk.Label(Image_frame,image=resized_image, bg="white")
# image_label.pack(expand=True)

# my_image=Image.open("C:\\Users\\User\\OneDrive\\Desktop\\Project\\Hostel.jpg")
# resized_image= my_image.resize((1366,400))
# converted_image= ImageTk.PhotoImage(resized_image)
# my_label= tk.Label(my_image,image=converted_image)
# my_label.place(x=0,y=300)


image_path = "C:\\Users\\User\\OneDrive\\Desktop\\Project\\Hostel.jpg"  # Replace with the path to your image
image = Image.open(image_path)
resized_image = image.resize((1366,350))
converted_image = ImageTk.PhotoImage(resized_image)
my_label= tk.Label(image=converted_image, bg="white")
my_label.place(x=0,y=380)




mainloop()
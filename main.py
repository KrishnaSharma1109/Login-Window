from tkinter import *
from PIL import ImageTk,Image
from customtkinter import *
import tkinter.messagebox as tmsg
import webbrowser

def button_function():
    if(savingInfo.get()==1):
        with open("Details.txt", "a") as f:
            f.write(f"Your Username is '{uservalue.get()}' and Password is '{PassValue.get()}'\n ")
    
    root.destroy()            # destroy current window and creating new one 
    w =CTk()  
    w.geometry("1280x720")
    w.title('Welcome to the Code Verse')
    l1=CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=CENTER)
    w.mainloop()

def forgetPass(event):
    tmsg.showinfo("Forgot Password","The email is sent to your account for changing password")
def callback(url):
   webbrowser.open_new_tab(url)
root=CTk()

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}")

root.minsize(width,height)
root.minsize(width,height)


root.title(" Login - Code Verse")
root.wm_iconbitmap("login_icon_176905.ico")

img=CTkImage(light_image=Image.open("file.png"),dark_image=Image.open("file.png"), size=(1299,750))


l1=CTkLabel(master=root,image=img)
l1.pack()

frame=CTkFrame(master=l1,height=390,width=300,corner_radius=20,bg_color="#3e1f6f",fg_color="#F9E400")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
 
wlcm=CTkLabel(master=frame, text='"Code Verse"',font=('Century Gothic',20,"bold"),text_color="#A020F0")
wlcm.place(x=91, y=12)

l2=CTkLabel(master=frame, text="  Log into your Account ",font=('Century Gothic',16,"bold"),text_color="black")
l2.place(x=53, y=49)

uservalue=StringVar()
l3=CTkLabel(master=frame, text="Username",font=('Century Gothic',13,"bold"),text_color="black")
l3.place(x=43, y=85)
entry1=CTkEntry(master=frame,textvariable=uservalue, width=220, placeholder_text='only alphanumeric,_,@',fg_color="white",corner_radius=30,text_color="black")
entry1.place(x=43, y=110)

PassValue=StringVar()
l4=CTkLabel(master=frame, text="Password",font=('Century Gothic',13,"bold"),text_color="black")
l4.place(x=43, y=138)
entry2=CTkEntry(master=frame,textvariable=PassValue, width=220, placeholder_text='Create a strong password', show="*",fg_color="white",corner_radius=30,text_color="black")
entry2.place(x=43, y=165)

l5=CTkButton(master=frame, text="Forget password?",font=('Century Gothic',12),fg_color="transparent",corner_radius=30,text_color="black",hover_color="#F9E400")
l5.place(x=147,y=195)
l5.bind('<Button-1>', forgetPass)
savingInfo=IntVar()
checkbox=CTkCheckBox(master=frame,text="Save Login info",font=('Century Gothic',13,"bold"),text_color="black",corner_radius=50,checkbox_height=17,checkbox_width=17,variable=savingInfo,fg_color="green",hover_color="yellow")
checkbox.place(x=43,y=215)

button1 = CTkButton(master=frame, width=220, text="Login", font=('Century Gothic',15,"bold"),command=button_function, corner_radius=6,fg_color="black",text_color="White",hover_color="#A020F0")
button1.place(x=50, y=250)

sep=CTkLabel(master=frame,text="----------------------------------------",font=('Century Gothic',12,"bold"),text_color="#A020F0",fg_color=None,bg_color="transparent")
sep.place(x=50,y=282)

msg=CTkLabel(master=frame,text="FOLLOW US ON",font=('Century Gothic',12,"bold"),text_color="#A020F0",fg_color=None,bg_color="transparent")
msg.place(x=115,y=310)

img2=CTkImage(Image.open("—Pngtree—instagram icon logo_3560507.png").resize((20,20)))
img3=CTkImage(Image.open("icons8-linkedin-48.png").resize((20,20)))
button2=CTkButton(master=frame, image=img2, text="Instagram", width=75, height=10, compound="left", fg_color="#F9E400", text_color='black', hover_color="#FD1D1D")
button2.place(x=50, y=340)
button2.bind('<Button-1>', lambda e: callback("https://www.instagram.com/_krishna0.5/") )

button3=CTkButton(master=frame, image=img3, text="Linkedin", width=75, height=10, compound="left", fg_color="#F9E400", text_color='black', hover_color="#0077B5")
button3.place(x=170, y=340)
button3.bind('<Button-1>', lambda e: callback("https://www.linkedin.com/in/krishna-sharma-649008219/"))


root.mainloop()

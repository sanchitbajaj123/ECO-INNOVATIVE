
from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import messagebox
import pyrebase
from tkinter import filedialog
import json
import subprocess
import pywhatkit as pwk


def adduser(root,db):
    window = tk.Toplevel(root)
    window.title("ADD USER")
    root.iconify()
    window.protocol("WM_DELETE_WINDOW", lambda: on_top_level_close(window,root))

    window.geometry("1041x588")
    window.configure(bg = "#FDFEF0")
    custom_font2 = ("Arial", 20)

    canvas = Canvas(
        window,
        bg = "#FDFEF0",
        height = 588,
        width = 1041,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=("assets3/frame0/image_1.png"))
    image_1 = canvas.create_image(
        177.0,
        262.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        362.0,
        25.0,
        1014.0,
        579.0,
        fill="#FDFEF0",
        outline="")

    entry_image_1 = PhotoImage(
        file=("assets3/frame0/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        792.0,
        266.5,
        image=entry_image_1
    )
    entry_1 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_1.place(
        x=611.0,
        y=223.0,
        width=362.0,
        height=85.0
    )

    entry_image_2 = PhotoImage(
        file=("assets3/frame0/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        792.0,
        133.5,
        image=entry_image_2
    )
    entry_2 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_2.place(
        x=611.0,
        y=94.0,
        width=362.0,
        height=77.0
    )

    button_image_1 = PhotoImage(
        file=("assets3/frame0/button_1.png"))
    button_1 = Button(window,
        bg="#FDFEF0",
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(entry_2,entry_1,db),
        relief="flat"
    )
    button_1.place(
        x=644.0,
        y=395.0,
        width=364.0,
        height=64.0
    )

    button_image_2 = PhotoImage(
        file=("assets3/frame0/button_2.png"))
    button_2 = Button(window,
        bg="#FDFEF0",
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete(entry_2,db),
        relief="flat"
    )
    button_2.place(
        x=362.0,
        y=348.0,
        width=259.0,
        height=151.0
    )

    button_image_3 = PhotoImage(
        file=("assets3/frame0/button_3.png"))
    button_3 = Button(window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show(db),
        relief="flat"
    )
    button_3.place(
        x=385.0,
        y=94.0,
        width=194.0,
        height=224.0
    )
    window.resizable(False, False)
    window.mainloop()
def add(e2,e1,db):
    name=e2.get()
    passw=e1.get()
    if(name.strip()==""):
        messagebox.showinfo("WARNING","FIELDS CAN NOT \n BE EMPTY.")   
    elif(passw.strip()==""):
        messagebox.showinfo("WARNING","FIELDS CAN NOT \n BE EMPTY.")   
    else:     
        collection_ref = db.collection('users')
        query = db.collection('users').where('user', '==', name)
        print(query)
        print(type(query))
        docs = query.get()
        print(docs)
        if(len(docs)>0):
            messagebox.showinfo("WARNING","ALREADY EXISTS.")
        else:
            data = {
                'user': name,
                'pass':passw
            }

            # Add data to Firestore
            document_ref = collection_ref.add(data)
            messagebox.showinfo("DATABASE",f"{name} is successfully added")
            e1.delete(0,"end")
            e2.delete(0,"end")    
            

            # Send the message instantly
            pwk.sendwhatmsg_instantly("+91"+name, f"HELLO ECO-INNOVATIVE THIS SIDE \n YOUR USERNAME AND PASSWORD IS \n USER:{name}\n PASS:{passw}" )   
def delete(name,db):
    field_value = name.get()
    query = db.collection('users').where('user', "==", field_value)
    result = query.get()
    if result:
        document_id = result[0].id
        print(document_id)
    # Delete the document using the retrieved document ID
        db.collection('users').document(document_id).delete()
        messagebox.showinfo("database",f"{field_value} sucessfully deleted.")
        name.delete(0,"end")
    else:
        messagebox.showinfo("database",f"{field_value} does not exists.")
def show(db):
    collection_ref = db.collection("users")
    docs = collection_ref.stream()

    data = {}
    for doc in docs:
        data[doc.id] = doc.to_dict()

    with open('firestore_data.txt', 'w') as file:
        json.dump(data, file, indent=2)
        file.write('\n')  
        
    print('Data saved to firestore_data.txt')
    try:
        subprocess.run(['notepad.exe',"firestore_data.txt" ], check=True)
    except Exception as e:
        print(f'Error opening the file: {e}')
        
def on_top_level_close(top_level,root):
    top_level.destroy()  # Destroy the top-level window
    root.deiconify()  
    

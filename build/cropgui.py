
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def cropadd(root):
    
    window1 = tk.Toplevel(root)
    root.iconify()
    window1.protocol("WM_DELETE_WINDOW", lambda: on_top_level_close(window1,root))
    cred = credentials.Certificate('build/eco-inno.json')
    firebase_admin.initialize_app(cred)    
    db=firestore.client()
    window1.geometry("1041x588")
    window1.configure(bg = "#FDFEF0")


    canvas = Canvas(
        window1,
        bg = "#FDFEF0",
        height = 588,
        width = 1041,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=("build/assets2/frame0/image_1.png"))
    image_1 = canvas.create_image(
        187.0,
        262.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        394.0,
        0.0,
        1061.0,
        588.0,
        fill="#FDFEF0",
        outline="")

    entry_image_1 = PhotoImage(
        file=("build/assets2/frame0/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        712.5,
        288.0,
        image=entry_image_1
    )
    entry_1 = Entry(window1,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=452.0,
        y=153.0,
        width=521.0,
        height=268.0
    )

    entry_image_2 = PhotoImage(
        file=("build/assets2/frame0/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        712.5,
        78.5,
        image=entry_image_2
    )
    entry_2 = Entry(window1,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        
    )
    entry_2.place(
        x=567.0,
        y=39.0,
        width=291.0,
        height=77.0
    )

    button_image_1 = PhotoImage(
        file=("build/assets2/frame0/button_1.png"))
    button_1 = Button(window1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(entry_1,entry_2,db),
        relief="flat"
    )
    button_1.place(
        x=531.0,
        y=459.0,
        width=364.0,
        height=64.0
    )
    window1.resizable(False, False)
    window1.mainloop()
def on_top_level_close(top_level,root):
    top_level.destroy()  # Destroy the top-level window
    root.deiconify()     # Deiconify (restore) the main window
def add(e1,e2,db):
    name= e1.get()
    det=e2.get()
    collection_ref = db.collection('crops')

    # Data to be added
    data = {
        'name': name,
        'details':det,
        # Add more fields as needed
    }

    # Add data to Firestore
    document_ref = collection_ref.add(data)
    #print(f'Document added with ID: {document_ref.id}')

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
import re


def disease(root,db):
    window = tk.Toplevel(root)
    window.title("ADD CROP DISEASE")
    root.iconify()
    window.protocol("WM_DELETE_WINDOW", lambda: on_top_level_close(window,root))


    window.geometry("1041x588")
    window.configure(bg = "#FDFEF0")


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
        file=("assets4/frame0/image_1.png"))
    image_1 = canvas.create_image(
        177.0,
        262.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        376.0,
        9.0,
        1028.0,
        563.0,
        fill="#FDFEF0",
        outline="")

    entry_image_1 = PhotoImage(
        file=("assets4/frame0/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        820.0,
        322.5,
        image=entry_image_1
    )
    entry_1 = Text(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=665.0,
        y=279.0,
        width=310.0,
        height=85.0
    )

    entry_image_2 = PhotoImage(
        file=("assets4/frame0/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        820.0,
        213.5,
        image=entry_image_2
    )
    entry_2 = Text(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=665.0,
        y=170.0,
        width=310.0,
        height=85.0
    )

    entry_image_3 = PhotoImage(
        file=("assets4/frame0/entry_3.png"))
    entry_bg_3 = canvas.create_image(
        820.0,
        54.0,
        image=entry_image_3
    )
    entry_3 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=665.0,
        y=32.0,
        width=310.0,
        height=42.0
    )

    entry_image_4 = PhotoImage(
        file=("assets4/frame0/entry_4.png"))
    entry_bg_4 = canvas.create_image(
        820.0,
        126.0,
        image=entry_image_4
    )
    entry_4 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=665.0,
        y=104.0,
        width=310.0,
        height=42.0
    )

    button_image_1 = PhotoImage(
        file=("assets4/frame0/button_1.png"))
    button_1 = Button(window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(db,entry_3,entry_4,entry_1,entry_2),
        relief="flat",
        bg="#fdfef0"
    )
    button_1.place(
        x=653.0,
        y=437.0,
        width=364.0,
        height=64.0
    )

    button_image_2 = PhotoImage(
        file=("assets4/frame0/button_2.png"))
    button_2 = Button(window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete(entry_3,db),
        relief="flat",
        bg="#fdfef0"
    )
    button_2.place(
        x=376.0,
        y=398.0,
        width=259.0,
        height=151.0
    )

    button_image_3 = PhotoImage(
        file=("assets4/frame0/button_3.png"))
    button_3 = Button(window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show(db),
        relief="flat",
        bg="#fdfef0"
    )
    button_3.place(
        x=391.0,
        y=31.0,
        width=236.0,
        height=335.0
    )
    custom_font2 = ("Arial", 20)
    entry_1.config(font=custom_font2)
    entry_2.config(font=custom_font2)
    entry_3.config(font=custom_font2)
    entry_4.config(font=custom_font2)
    window.resizable(False, False)
    window.mainloop()
def on_top_level_close(top_level,root):
    top_level.destroy()  # Destroy the top-level window
    root.deiconify()  
def add(db,e1,e2,e3,e4):
    name=e1.get()
    without_underscores = name.replace('_', '')

    # Convert to lowercase
    name = without_underscores.lower()
    name = re.sub(r'[^a-zA-Z0-9\-]', '', name)
    inf=e2.get()
    det= e3.get("1.0", "end-1c")
    cur=e4.get("1.0", "end-1c")
    if(det.strip()==""):
        messagebox.showinfo("WARNING","FIELDS CAN NOT \n BE EMPTY.")   
    elif(name.strip()==""):
        messagebox.showinfo("WARNING","FIELDS CAN NOT \n BE EMPTY.")   
    else:     
        collection_ref = db.collection('disease')
        query = db.collection('disease').where('name', '==', name)
        print(query)
        print(type(query))
        docs = query.get()
        print(docs)
        if(len(docs)>0):
            messagebox.showinfo("WARNING","ALREADY EXISTS.")
        else:
            messagebox.showinfo("IMAGE","NOW CHOOSE IMAGE.")
            config={
            "apiKey": "AIzaSyBZ0o3kFzCTPiuITe0jTZNkBPEmMjQeZPE",
            "authDomain": "eco--innovative.firebaseapp.com",
            "databaseURL":"https://eco--innovative.firebaseapp.com",
            "projectId": "eco--innovative",
            "storageBucket": "eco--innovative.appspot.com",
            "messagingSenderId": "82699048675",
            "appId": "1:82699048675:web:de8df09341d451419397d6",
            "measurementId": "G-778911CZPV"
            }
            firebase=pyrebase.initialize_app(config)
            storage=firebase.storage()
            path="images2/"+name+".jpg"
            file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.jpg;")])

            storage.child(path).put(file_path)
            url = storage.child(path).get_url(token=None)
            data = {
                'name': name,
                'details':cur,
                'infectious-noninfectios':inf,
                'cure':det,
                'img':url
            }

            # Add data to Firestore
            document_ref = collection_ref.add(data)
            messagebox.showinfo("DATABASE",f"{name} is successfully added")
            e3.delete("1.0", "end")
            e4.delete("1.0", "end")
            e1.delete(0,"end")
            e2.delete(0,"end")
def delete(name,db):
    field_value = name.get()
    without_underscores = field_value.replace('_', '')

    # Convert to lowercase
    field_value = without_underscores.lower()    
    query = db.collection('disease').where('name', "==", field_value)
    result = query.get()
    if result:
        document_id = result[0].id
        print(document_id)
    # Delete the document using the retrieved document ID
        db.collection('disease').document(document_id).delete()
        messagebox.showinfo("database",f"{field_value} sucessfully deleted.")
        name.delete(0,"end")
    else:
        messagebox.showinfo("database",f"{field_value} does not exists.")
def show(db):
    collection_ref = db.collection("disease")
    docs = collection_ref.stream()

    data = {}
    for doc in docs:
        data[doc.id] = doc.to_dict()

    with open('firestore_data_disease.txt', 'w') as file:
        json.dump(data, file, indent=2)
        file.write('\n')  
        
    print('Data saved to firestore_data.txt')
    try:
        subprocess.run(['notepad.exe',"firestore_data_disease.txt" ], check=True)
    except Exception as e:
        print(f'Error opening the file: {e}')
        




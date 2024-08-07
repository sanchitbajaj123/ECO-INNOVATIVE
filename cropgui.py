
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

def cropadd(root,db):
    window = tk.Toplevel(root)
    window.title("ADD CROPS")
    root.iconify()
    window.protocol("WM_DELETE_WINDOW", lambda: on_top_level_close(window,root))
  
    

    window.geometry("1041x588")
    window.configure(bg = "#FDFEF0")

    custom_font = ("Arial", 40)
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
        file=("assets2/frame0/image_1.png"))
    image_1 = canvas.create_image(
        187.0,
        262.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        391.0,
        12.0,
        1058.0,
        612.0,
        fill="#FDFEF0",
        outline="")

    entry_image_1 = PhotoImage(
        file=("assets2/frame0/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        810.5,
        441.0,
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
        x=709.0,
        y=426.0,
        width=203.0,
        height=28.0
    )

    entry_image_2 = PhotoImage(
        file=("assets2/frame0/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        810.5,
        479.0,
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
        x=709.0,
        y=464.0,
        width=203.0,
        height=28.0
    )

    entry_image_3 = PhotoImage(
        file=("assets2/frame0/entry_3.png"))
    entry_bg_3 = canvas.create_image(
        810.5,
        397.0,
        image=entry_image_3
    )
    entry_3 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_3.place(
        x=709.0,
        y=382.0,
        width=203.0,
        height=28.0
    )

    entry_image_4 = PhotoImage(
        file=("assets2/frame0/entry_4.png"))
    entry_bg_4 = canvas.create_image(
        712.5,
        172.5,
        image=entry_image_4
    )
    entry_4 = Text(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_4.place(
        x=452.0,
        y=122.0,
        width=521.0,
        height=99.0
    )

    entry_image_5 = PhotoImage(
        file=("assets2/frame0/entry_5.png"))
    entry_bg_5 = canvas.create_image(
        710.5,
        60.5,
        image=entry_image_5
    )
    entry_5 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font
    )
    entry_5.place(
        x=565.0,
        y=21.0,
        width=291.0,
        height=77.0
    )

    button_image_1 = PhotoImage(
        file=("assets2/frame0/button_1.png"))
    button_1 = Button(window,
        bg="#FDFEF0",
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(entry_4,entry_5,db,entry_1,entry_2,entry_3,entry_6,entry_7,entry_8),
        relief="flat"
    )
    button_1.place(
        x=531.0,
        y=514.0,
        width=364.0,
        height=64.0
    )

    button_image_2 = PhotoImage(
        file=("assets2/frame0/button_2.png"))
    button_2 = Button(window,
        bg="#FDFEF0",
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete(entry_5,db),
        relief="flat"
    )
    button_2.place(
        x=58.0,
        y=431.0,
        width=259.0,
        height=151.0
    )

    entry_image_6 = PhotoImage(
        file=("assets2/frame0/entry_6.png"))
    entry_bg_6 = canvas.create_image(
        811.5,
        256.5,
        image=entry_image_6
    )
    entry_6 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_6.place(
        x=711.0,
        y=240.0,
        width=201.0,
        height=31.0
    )

    entry_image_7 = PhotoImage(
        file=("assets2/frame0/entry_7.png"))
    entry_bg_7 = canvas.create_image(
        812.0,
        309.0,
        image=entry_image_7
    )
    entry_7 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_7.place(
        x=711.0,
        y=294.0,
        width=202.0,
        height=28.0
    )

    entry_image_8 = PhotoImage(
        file=("assets2/frame0/entry_8.png"))
    entry_bg_8 = canvas.create_image(
        810.5,
        351.0,
        image=entry_image_8
    )
    entry_8 = Entry(window,
        bd=0,
        bg="#90EE90",
        fg="#000716",
        highlightthickness=0,
        font=custom_font2
    )
    entry_8.place(
        x=709.0,
        y=336.0,
        width=203.0,
        height=28.0
    )

    button_image_3 = PhotoImage(
        file=("assets2/frame0/button_3.png"))
    button_3 = Button(window,
        bg="#0B2A3E",
        fg="#90EE90",
        text="Family Name\nScientific Name\nSunlight\n Temperature\n Soil Moisture\nTime",
        borderwidth=0,
        font=("Arial", 20, "italic"),
        highlightthickness=0,
        command=lambda: show(db),
        relief="flat",
    
    )
    button_3.place(
        x=434.0,
        y=240.0,
        width=259.0,
        height=254.0
    )
    window.resizable(False, False)
    window.mainloop()
def on_top_level_close(top_level,root):
    top_level.destroy()  # Destroy the top-level window
    root.deiconify()     # Deiconify (restore) the main window
    
def add(e1,e2,db,hum,tip,airm,sunli,airq,temp):
    det= e1.get("1.0", "end-1c")
    name=e2.get()
    hu=hum.get()
    ti=tip.get()
    air=airm.get()
    sunl=sunli.get()
    aiq=airq.get()
    tem=temp.get()

    if(det.strip()==""):
        messagebox.showinfo("WARNING","FIELDS CAN NOT \n BE EMPTY.")   
    elif(name.strip()==""):
        messagebox.showinfo("WARNING","FIELDS CAN NOT \n BE EMPTY.")   
    else:     
        collection_ref = db.collection('crops')
        query = db.collection('crops').where('name', '==', name)
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
            path="images/"+name+".png"
            file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.png;")])

            storage.child(path).put(file_path)
            url = storage.child(path).get_url(token=None)
            data = {
                'name': name,
                'details':det,
                'image':url,
                'soil moisture':hu,
                'time period':ti,
                'temperature':air,
                'family name':sunl,
                'scientific name':aiq,
                'sunlight requirment':tem
            }

            # Add data to Firestore
            document_ref = collection_ref.add(data)
            messagebox.showinfo("DATABASE",f"{name} is successfully added")
            e1.delete("1.0", "end")
            e2.delete(0,"end")
            hum.delete(0,"end")
            temp.delete(0,"end")
            airm.delete(0,"end")
            airq.delete(0,"end")
            sunli.delete(0,"end")
            tip.delete(0,"end")
        #print(f'Document added with ID: {document_ref.id}')
def delete(name,db):
    field_value = name.get()
    query = db.collection('crops').where('name', "==", field_value)
    result = query.get()
    if result:
        document_id = result[0].id
        print(document_id)
    # Delete the document using the retrieved document ID
        db.collection('crops').document(document_id).delete()
        messagebox.showinfo("database",f"{field_value} sucessfully deleted.")
        name.delete(0,"end")
    else:
        messagebox.showinfo("database",f"{field_value} does not exists.")
def show(db):
    collection_ref = db.collection("crops")
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
        

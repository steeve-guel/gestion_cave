import sqlite3
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox



def add_boisson(frame):
    # Label(frame, text="Ajouter une nouvelle boisson",font=("Arial",14)).grid(
    #     row=0, column=0
    # )

    def valider():

        _boisson_name = boisson_name_entry.get()
        _boisson_type = boisson_type_entry.get()
        _boisson_volume = boisson_volume_spinbox.get()
        _boisson_prix = boisson_price_spingbox.get()

        if _boisson_name and _boisson_type and _boisson_volume and _boisson_prix:

            conn = sqlite3.connect('data.db')

            data_insert_query = '''INSERT INTO boisson (boisson_name, type, volume, 
                prix) VALUES 
                (?, ?, ?, ?)'''
            
            data_insert_tuple = (_boisson_name,_boisson_type,_boisson_volume,_boisson_prix)

            cursor = conn.cursor()

            cursor.execute(data_insert_query,data_insert_tuple)

            conn.commit()
            conn.close()

            messagebox.showinfo("Succès", "Enregistrer avec succès !")

            boisson_name_entry.delete(0,END)
            boisson_type_entry.delete(0,END)
            boisson_volume_spinbox.delete(0,END)
            boisson_price_spingbox.delete(0,END)

            
        else: 
            messagebox.showwarning(title="Error", message="Remplissez les champs vides.")

    boisson_info_frame = LabelFrame(frame,text="Information sur la boisson")
    boisson_info_frame.grid(row=0,column=0,padx=20,pady=10)
    #####
    boisson_name_label = Label(boisson_info_frame,text="Nom de la boisson")
    boisson_name_label.grid(row=0,column=0)

    boisson_name_entry = Entry(boisson_info_frame)
    boisson_name_entry.grid(row=1,column=0)
    #######
    boisson_type_label = Label(boisson_info_frame,text="Type de la boisson")
    boisson_type_label.grid(row=0,column=1)

    boisson_type_entry = ttk.Combobox(boisson_info_frame,values=["Bière","Sucrérie"])
    boisson_type_entry.grid(row=1,column=1)

    ############
    boisson_volume_label = Label(boisson_info_frame,text="Volume (cl)")
    boisson_volume_label.grid(row=0,column=3)

    boisson_volume_spinbox = ttk.Spinbox(boisson_info_frame,from_=0,)
    boisson_volume_spinbox.grid(row=1,column=3)

    ############
    boisson_price_label = Label(boisson_info_frame,text="Prix")
    boisson_price_label.grid(row=0,column=4)

    boisson_price_spingbox = ttk.Spinbox(boisson_info_frame,from_=0)
    boisson_price_spingbox.grid(row=1,column=4)


    ######
    for widget in boisson_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    # Button
    button = tkinter.Button(frame, text="Enregistrer",command=valider)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
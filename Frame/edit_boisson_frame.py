import sqlite3
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox

def modifier_boisson_frame(frame):

    def rechercher():

        id_boisson = edit_boisson_entry.get()

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        data_select_query = '''SELECT * FROM boisson WHERE id = ?'''

        data_select_indice = (id_boisson)
        cursor.execute(data_select_query, data_select_indice)

        boisson = cursor.fetchone()

        if boisson:
            messagebox.showinfo("Succes",str(boisson[1]))
            afficher(boisson=boisson)
        else:
            messagebox.showerror("Error","Aucune boisson trouve. Entrez un identifiant valide")

    def afficher(boisson):

        #############
        boisson_info_frame = LabelFrame(frame,text="Modifier la boisson")
        boisson_info_frame.grid(row=1,column=0,padx=20,pady=10)
        #####
        boisson_name_label = Label(boisson_info_frame,text="Nom de la boisson")
        boisson_name_label.grid(row=2,column=0)

        boisson_name_entry = Entry(boisson_info_frame)
        boisson_name_entry.grid(row=3,column=0)
        boisson_name_entry.insert(0,boisson[1])
        #######
        boisson_type_label = Label(boisson_info_frame,text="Type de la boisson")
        boisson_type_label.grid(row=2,column=1)

        boisson_type_entry = ttk.Combobox(boisson_info_frame,values=["Bière","Sucrérie"])
        boisson_type_entry.grid(row=3,column=1)
        boisson_type_entry.insert(0,boisson[2])

        ############
        boisson_volume_label = Label(boisson_info_frame,text="Volume (cl)")
        boisson_volume_label.grid(row=2,column=3)

        boisson_volume_spinbox = ttk.Spinbox(boisson_info_frame,from_=0,)
        boisson_volume_spinbox.grid(row=3,column=3)
        boisson_volume_spinbox.insert(0,boisson[3])

        ############
        boisson_price_label = Label(boisson_info_frame,text="Prix")
        boisson_price_label.grid(row=2,column=4)

        boisson_price_spingbox = ttk.Spinbox(boisson_info_frame,from_=0)
        boisson_price_spingbox.grid(row=3,column=4)
        boisson_price_spingbox.insert(0,boisson[4])

        ######
        for widget in boisson_info_frame.winfo_children():
            widget.grid_configure(padx=10,pady=5)

        
        

        def valider():

            item_id = boisson[0]

            _boisson_name = boisson_name_entry.get()
            _boisson_type = boisson_type_entry.get()
            _boisson_volume = boisson_volume_spinbox.get()
            _boisson_prix = boisson_price_spingbox.get()

            if _boisson_name and _boisson_type and _boisson_volume and _boisson_prix:

                try:
                    conn = sqlite3.connect('data.db')

                    data_insert_query = '''UPDATE boisson
                                        SET boisson_name = ?, type = ?,volume = ? , prix = ?
                                        WHERE id = ?'''
                    
                    data_insert_tuple = (_boisson_name,_boisson_type,_boisson_volume,_boisson_prix,item_id)

                    cursor = conn.cursor()

                    cursor.execute(data_insert_query,data_insert_tuple)

                    conn.commit()
                
                    messagebox.showinfo("Succès", "Modifier avec succès !")

                    boisson_name_entry.delete(0,END)
                    boisson_type_entry.delete(0,END)
                    boisson_volume_spinbox.delete(0,END)
                    boisson_price_spingbox.delete(0,END)
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))
                finally:
                    # Fermer la connexion
                    conn.close()

                
            else: 
                messagebox.showwarning(title="Error", message="Remplissez les champs vides.")

            # Button
        button = tkinter.Button(frame, text="Modifier",command = valider)
        button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    ##############33

    #############

    edit_info_frame = LabelFrame(frame,text="Recherche")
    edit_info_frame.grid(row=0,column=0,padx=20,pady=10)

    edit_boisson_label = Label(edit_info_frame, text="ID de la boisson")
    edit_boisson_label.grid(row=0,column=0)

    edit_boisson_entry = ttk.Spinbox(edit_info_frame,from_=0)
    edit_boisson_entry.grid(row=0,column=1)
    Button(edit_info_frame,text="Rechercher",command=rechercher).grid(row=0,column=2,sticky='news')

    

    for widget in edit_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    

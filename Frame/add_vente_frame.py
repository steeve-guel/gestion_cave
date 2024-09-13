import sqlite3
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from hashlib import sha256



def add_vente_frame(frame):
    # Label(frame, text="Ajouter une nouvelle boisson",font=("Arial",14)).grid(
    #     row=0, column=0
    # )

    def valider():

        _user_nom = user_nom_entry.get()
        _user_prenom = user_prenom_entry.get()
        _user_ville = user_ville_entry.get()
        _user_phone = user_phone_spingbox.get()
        
        _boisson_name = boisson_name_entry.get()
        _boisson_type = boisson_type_entry.get()
        _boisson_volume = boisson_volume_spinbox.get()
        _boisson_price = boisson_price_spingbox.get()

        _quantite_commandee = quantite_name_entry.get()
        _mode_paiement = mode_paiement_combobox.get()
        _motant = montant_spinbox.get()

        if _user_nom and _user_prenom and _user_phone and _user_ville and _boisson_name and _boisson_type and _boisson_price and _boisson_volume and _quantite_commandee and _mode_paiement and _motant:
            # hashed_password = sha256(_user_password.encode()).hexdigest()
            try:
                conn = sqlite3.connect('data.db')

                data_insert_query = '''INSERT INTO ventes (nom_client, prenom_client, ville, telephone,
                                        boisson_name, boisson_type, boisson_volume,
                                        boisson_prix_unitaire, quantite_commandee, mode_paiement,
                                        montant) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                
                data_insert_tuple = (_user_nom,_user_prenom,
                                     _user_ville,_user_phone,_boisson_name,
                                     _boisson_type,_boisson_volume,_boisson_price,
                                     _quantite_commandee,_mode_paiement,_motant)

                cursor = conn.cursor()

                cursor.execute(data_insert_query,data_insert_tuple)

                conn.commit()
                conn.close()

                messagebox.showinfo("Succès", "Enregistrer avec succès !")

                user_nom_entry.delete(0,END)
                user_nom_entry.delete(0,END)
                user_prenom_entry.delete(0,END)
                user_ville_entry.delete(0,END)
                user_phone_spingbox.delete(0,END)
                # user_password_entry.delete(0,END)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {e}")
                messagebox.showinfo(title="Inscription Success", message="Inscription reussie.")
        else: 
            messagebox.showwarning(title="Error", message="Remplissez les champs vides.")

    user_info_frame = LabelFrame(frame,text="Information sur le client")
    user_info_frame.grid(row=0,column=0,padx=20,pady=10)
    #####
    user_nom_label = Label(user_info_frame,text="Nom")
    user_nom_label.grid(row=0,column=0)

    user_nom_entry = Entry(user_info_frame)
    user_nom_entry.grid(row=1,column=0)

    #######
    user_prenom_label = Label(user_info_frame,text="Prenom")
    user_prenom_label.grid(row=0,column=1)

    user_prenom_entry = Entry(user_info_frame)
    user_prenom_entry.grid(row=1,column=1)

    ############
    user_ville_label = Label(user_info_frame,text="Ville")
    user_ville_label.grid(row=0,column=3)

    user_ville_entry = Entry(user_info_frame)
    user_ville_entry.grid(row=1,column=3)

    ############
    user_phone_label = Label(user_info_frame,text="Telephone")
    user_phone_label.grid(row=0,column=4)

    user_phone_spingbox = ttk.Spinbox(user_info_frame,from_=0)
    user_phone_spingbox.grid(row=1,column=4)
    
    ######
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    ######Produit
    boisson_info_frame = LabelFrame(frame,text="Information sur la boisson")
    boisson_info_frame.grid(row=4,column=0,padx=20,pady=10)
    #####
    boisson_name_label = Label(boisson_info_frame,text="Nom de la boisson")
    boisson_name_label.grid(row=5,column=0)

    boisson_name_entry = Entry(boisson_info_frame)
    boisson_name_entry.grid(row=6,column=0)
    #######
    boisson_type_label = Label(boisson_info_frame,text="Type de la boisson")
    boisson_type_label.grid(row=5,column=1)

    boisson_type_entry = ttk.Combobox(boisson_info_frame,values=["Bière","Sucrérie"])
    boisson_type_entry.grid(row=6,column=1)

    ############
    boisson_volume_label = Label(boisson_info_frame,text="Volume (cl)")
    boisson_volume_label.grid(row=5,column=3)

    boisson_volume_spinbox = ttk.Spinbox(boisson_info_frame,from_=0,)
    boisson_volume_spinbox.grid(row=6,column=3)

    ############
    boisson_price_label = Label(boisson_info_frame,text="Prix Unitaire")
    boisson_price_label.grid(row=5,column=4)

    boisson_price_spingbox = ttk.Spinbox(boisson_info_frame,from_=0)
    boisson_price_spingbox.grid(row=6,column=4)


    ######
    for widget in boisson_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    ######Quantite
    quantite_info_frame = LabelFrame(frame,text="Information sur la quantite")
    quantite_info_frame.grid(row=7,column=0,padx=20,pady=10)
    #####
    quantite_name_label = Label(quantite_info_frame,text="Quantite commandée")
    quantite_name_label.grid(row=8,column=0)

    quantite_name_entry = Entry(quantite_info_frame)
    quantite_name_entry.grid(row=9,column=0)

    #######
    mode_paiement_label = Label(quantite_info_frame,text="Mode de paiement")
    mode_paiement_label.grid(row=8,column=1)

    mode_paiement_combobox = ttk.Combobox(quantite_info_frame,values=["Carte","Espèce","Mobile money"])
    mode_paiement_combobox.grid(row=9,column=1)

    ############
    montant_label = Label(quantite_info_frame,text="Montant")
    montant_label.grid(row=8,column=3)

    montant_spinbox = ttk.Spinbox(quantite_info_frame,from_=0,)
    montant_spinbox.grid(row=9,column=3)

    ######
    for widget in quantite_info_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    # Button
    button = tkinter.Button(frame, text="Enregistrer",command=valider)
    button.grid(row=10, column=0, sticky="news", padx=20, pady=10)
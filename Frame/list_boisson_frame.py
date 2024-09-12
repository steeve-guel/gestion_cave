import sqlite3
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox

def list_boisson_frame(frame):

    def afficher_boissons():

        for row in tree.get_children():
            tree.delete(row)

        # Connexion à la base de données SQLite
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        # Requête pour récupérer les utilisateurs
        cursor.execute("SELECT * FROM boisson")
        boissons = cursor.fetchall()

        
        
        # Insertion des données dans le Treeview
        for boisson in boissons:
            tree.insert("", END, values=boisson)
        
        # Fermer la connexion
        conn.close()

    def supprimer_utilisateur():

        id_utilisateur = delete_boisson_entry.get()

        if id_utilisateur:

            # Connexion à la base de données SQLite
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            
            # Suppression d'une boisson
            cursor.execute("DELETE FROM boisson WHERE id = ?", (id_utilisateur,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succes","Boisson supprimer avec succes")
            afficher_boissons()
        else:
            messagebox.showerror("Error","Entrer un identifiant")

    


   
    # afficher_utilisateurs()

    Label(frame, text="Appuyer sur le bouton Afficher la liste pour afficher la liste ou l'actualiser après modification.").pack(padx=20, pady=20)

    #############

    delete_info_frame = LabelFrame(frame,text="Supprimer une boisson")
    delete_info_frame.pack(padx=55,pady=5)

    delete_boisson_label = Label(delete_info_frame, text="ID de la boisson")
    delete_boisson_label.pack()

    delete_boisson_entry = ttk.Spinbox(delete_info_frame,from_=0)
    delete_boisson_entry.pack()
    Button(delete_info_frame,text="Supprimer",command=supprimer_utilisateur).pack(padx=10,pady=5)
    

    ############

    tree = ttk.Treeview(frame, columns=("ID", "Boisson", "Type","Volume","Prix",), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Boisson", text="Boisson")
    tree.heading("Type", text="Type")
    tree.heading("Volume", text="Volume")
    tree.heading("Prix", text="Prix")
    
    tree.pack(fill=BOTH, expand=True,padx=20,pady=10)

    tree.column("ID", width=50)
    tree.column("Volume", width=30)
    tree.column("Boisson",width=80)
    tree.column("Type",width=80)
    tree.column("Prix", width=60)

    btn_modifier = Button(frame, text="Afficher la liste",command=afficher_boissons)
    btn_modifier.pack(side=LEFT, padx=10, pady=10)
    btn_modifier.place(x=20,y=20)


    # label_info = Button(frame,text="Appuyer sur ce bouton pour afficher et aussi actualiser la liste")

    # label_info.place(x = 30, y=20)
    # Création du Treeview
    

    
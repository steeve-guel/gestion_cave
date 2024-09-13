import sqlite3
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox

def list_user_frame(frame):

    def afficher_boissons():

        for row in tree.get_children():
            tree.delete(row)

        # Connexion à la base de données SQLite
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        # Requête pour récupérer les utilisateurs
        cursor.execute("SELECT id,username,role,nom,phone,ville FROM utilisateurs")
        users = cursor.fetchall()

        
        
        # Insertion des données dans le Treeview
        for user in users:
            tree.insert("", END, values=user)
        
        # Fermer la connexion
        conn.close()

    def supprimer_utilisateur():

        id_utilisateur = delete_user_entry.get()

        if id_utilisateur:

            try:
                # Connexion à la base de données SQLite
                conn = sqlite3.connect('data.db')
                cursor = conn.cursor()
                
                # Suppression d'une boisson
                cursor.execute("DELETE FROM utilisateurs WHERE id = ?", (id_utilisateur,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Succes","Boisson supprimer avec succes")
                afficher_boissons()
                delete_user_entry.delete(0,END)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {e}")
                messagebox.showinfo(title="Inscription Success", message="Inscription reussie.")    
        else:
            messagebox.showerror("Error","Entrer un identifiant")
   
    # afficher_utilisateurs()

    Label(frame, text="Appuyer sur le bouton Afficher la liste pour afficher la liste ou l'actualiser après modification.").pack(padx=20, pady=20)

    #############

    delete_info_frame = LabelFrame(frame,text="Supprimer un utilisateur")
    delete_info_frame.pack(padx=55,pady=5)

    delete_user_label = Label(delete_info_frame, text="ID de l'utilisateur")
    delete_user_label.pack()

    delete_user_entry = ttk.Spinbox(delete_info_frame,from_=0)
    delete_user_entry.pack()
    Button(delete_info_frame,text="Supprimer",command=supprimer_utilisateur).pack(padx=10,pady=5)
    

    ############

    tree = ttk.Treeview(frame, columns=("ID", "Username", "Role","Nom","Phone","Ville"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Username", text="Username")
    tree.heading("Role", text="Role")
    tree.heading("Nom", text="Nom")
    tree.heading("Phone", text="Phone")
    tree.heading("Ville", text="Ville")
    
    tree.pack(fill=BOTH, expand=True,padx=20,pady=10)

    tree.column("ID", width=50)
    tree.column("Username", width=65)
    tree.column("Phone",width=80)
    tree.column("Ville",width=80)
    tree.column("Role", width=60)

    btn_modifier = Button(frame, text="Afficher la liste",command=afficher_boissons)
    btn_modifier.pack(side=LEFT, padx=10, pady=10)
    btn_modifier.place(x=20,y=20)


    # label_info = Button(frame,text="Appuyer sur ce bouton pour afficher et aussi actualiser la liste")

    # label_info.place(x = 30, y=20)
    # Création du Treeview
    

    
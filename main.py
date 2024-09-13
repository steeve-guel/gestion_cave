from hashlib import sha256
import os
import tkinter as tk
from tkinter import messagebox

import sqlite3

from Frame.add_boisson_frame import add_boisson
from Frame.add_user_frame import add_user_frame
from Frame.add_vente_frame import add_vente_frame
from Frame.edit_boisson_frame import modifier_boisson_frame
from Frame.fenetre1 import create_frame1
from Frame.fenetre2 import create_frame2
from Frame.list_boisson_frame import list_boisson_frame
from Frame.list_user_frame import list_user_frame
from Frame.list_ventes_frame import list_ventes_frame

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Cave")
        self.geometry("800x500")

        # Créer le menu
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_command(label="admin")
        file_menu.add_separator()
        file_menu.add_command(label="Profil", command=self.show_frame1)
        file_menu.add_command(label="Fenêtre 2", command=self.show_frame2)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)

        #boisson

        boisson = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='Boisson',menu= boisson)

       
        #root.config(menu=menuBar)
        boisson.add_command(label='Ajouter une boisson',command=self.show_add_boisson)
        boisson.add_command(label='Liste des boissons',command=self.show_list_boisson)
        boisson.add_separator()
        boisson.add_command(label="Modifier une boisson",command=self.show_edit_boisson)

        #Utilisateur
        user = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='Utilisateurs',menu=user)
        user.add_command(label='Ajouter un utilisateur',command=self.show_add_user)
        user.add_separator()
        user.add_command(label='Liste des utilisateurs',command=self.show_list_user)
        # utilisateur.add_command(label='Paste')
        # utilisateur.add_command(label='Select all')
        # user.add_separator()
        # user.add_command(label='Ajouter un client')
        # user.add_command(label='Liste des clients')

        #Ventes
        vente = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="Vente",menu=vente)
        vente.add_command(label="Ajouter une vente",command=self.show_add_vente)
        vente.add_command(label="Liste des ventes",command=self.show_list_vente)

        # #Profil
        # profil = tk.Menu(menu_bar,tearoff=0)
        # menu_bar.add_cascade(label='Profil',menu=profil)

        # profil.add_command(label='admin')
        # profil.add_separator()
        # profil.add_command(label='Paramètre du profile')

        #Aide
        help = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='Aide',menu=help)
        help.add_command(label='Aide Cave')
        # help.add_command(label='Demo')
        help.add_separator()
        help.add_command(label='exit')

        # Créer les Frames
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)

        self.frame3_add_b = tk.Frame(self)
        self.frame3_list_b = tk.Frame(self)
        self.frame3_edit_b = tk.Frame(self)

        self.frame4_add_u = tk.Frame(self)
        self.frame4_list_u = tk.Frame(self)

        self.frame5_add_v = tk.Frame(self)
        self.frame5_list_v = tk.Frame(self)

        create_frame1(self.frame1)
        create_frame2(self.frame2)
        ###boisson
        add_boisson(self.frame3_add_b)
        list_boisson_frame(self.frame3_list_b)
        modifier_boisson_frame(self.frame3_edit_b)

        ###User
        add_user_frame(self.frame4_add_u)
        list_user_frame(self.frame4_list_u)

        ###Vente
        add_vente_frame(self.frame5_add_v)
        list_ventes_frame(self.frame5_list_v)
        
        ################
        self.current_frame = None
        self.show_frame1()

    #####Show frame
    def show_frame1(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.frame1.pack(fill='both', expand=True)
        self.current_frame = self.frame1

    def show_frame2(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.frame2.pack(fill='both', expand=True)
        self.current_frame = self.frame2

    def show_add_boisson(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.frame3_add_b.pack(fill='both',expand=True)
        self.current_frame = self.frame3_add_b

    def show_list_boisson(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.frame3_list_b.pack(fill='both',expand=True)
        self.current_frame = self.frame3_list_b

    def show_edit_boisson(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.frame3_edit_b.pack(fill='both',expand=True)
        self.current_frame = self.frame3_edit_b    

    def show_add_user(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            self.frame4_add_u.pack(fill='both',expand=True)
            self.current_frame = self.frame4_add_u

    def show_list_user(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            self.frame4_list_u.pack(fill='both',expand=True)
            self.current_frame = self.frame4_list_u

    def show_add_vente(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            self.frame5_add_v.pack(fill='both',expand=True)
            self.current_frame = self.frame5_add_v

    def show_list_vente(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            self.frame5_list_v.pack(fill='both',expand=True)
            self.current_frame = self.frame5_list_v

indicateur_fichier = "premier_lancement.txt"

def premier_lancement():
    # Vérifie si le fichier existe déjà
    if not os.path.exists(indicateur_fichier):
        # Action à exécuter une seule fois
        print("Ceci s'exécute uniquement au premier lancement.")
        _user_username="admin"
        _user_nom="admin"
        _user_type="Administrateur"
        _user_ville="Bobo-Dioulasso"
        _user_phone="67676767"
        _user_password="admin"
        hashed_password = sha256(_user_password.encode()).hexdigest()

        data_insert_query = '''INSERT INTO utilisateurs (username, nom, role,
              password,ville,phone) VALUES (?, ?, ?, ?, ?, ?)'''
            
        data_insert_tuple = (_user_username,_user_nom,_user_type,hashed_password,_user_ville,_user_phone)

        conn = sqlite3.connect('data.db')

        cursor = conn.cursor()

        cursor.execute(data_insert_query,data_insert_tuple)

        conn.commit()
        conn.close()
        
        # Crée le fichier pour indiquer que l'action a été exécutée
        with open(indicateur_fichier, 'w') as f:
            f.write("Cette action a été exécutée.")

#########Login Fonction
def check_login():
    username = entry_username.get()
    password = entry_password.get()

    hashed_password = sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utilisateurs WHERE username = ? AND password = ?', (username, hashed_password))

    user = cursor.fetchone()

    if user:
        # messagebox.showinfo(title="Login Success", message="Connexion reussie.")
        root_login.destroy()  # Fermer la fenêtre de connexion
        app = Application()  # Afficher la fenêtre d'accueil
        app.mainloop()
        return True
    else:
        messagebox.showerror(title="Error", message="Nom d'utilisateur ou mot de passe invalid.")
        return False
    
    # if username == "admin" and password == "admin":
    #     root_login.destroy()  # Fermer la fenêtre de connexion
    #     app = Application()  # Afficher la fenêtre d'accueil
    #     app.mainloop()
    # else:
    #     messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")

def on_closing(self):
        # Fermer la connexion à la base de données
        self.cursor.close()
        self.conn.close()
        self.destroy()   

# Création de la fenêtre de connexion
root_login = tk.Tk()
root_login.title("Connexion")
root_login.geometry("300x300")

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
        
conn.execute('''
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                nom TEXT,
                role TEXT NOT NULL,
                password TEXT NOT NULL,
                ville TEXT,
                phone NUMBER
            )
        ''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS boisson (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                boisson_name TEXT NOT NULL,
                type TEXT NOT NULL,
                volume NUMBER NOT NULL,
                prix NUMBER NOT NULL
            )
        ''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_client TEXT NOT NULL,
                prenom_client TEXT NOT NULL,
                ville TEXT NOT NULL,
                telephone TEXT NOT NULL,
                boisson_name TEXT NOT NULL,
                boisson_type TEXT NOT NULL,
                boisson_volume NUMBER NOT NULL,
                boisson_prix_unitaire NUMBER NOT NULL,
                quantite_commandee NUMBER NOT NULL,
                mode_paiement TEXT NOT NULL,
                montant NUMBER TEXT NOT NULL,
                date Date NOT NULL
            )
        ''')

conn.commit()

conn.close()

premier_lancement()

tk.Label(root_login,text="Connexion",font=("Arial",20)).pack(padx=20,pady=10)

tk.Label(root_login, text="Nom d'utilisateur").pack(padx=20, pady=5)
entry_username = tk.Entry(root_login)
entry_username.pack(padx=20, pady=5)

tk.Label(root_login, text="Mot de passe").pack(padx=20, pady=5)
entry_password = tk.Entry(root_login, show="*")
entry_password.pack(padx=20, pady=5)

tk.Button(root_login, text="Se connecter", command=check_login).pack(padx=20, pady=20)

root_login.mainloop()
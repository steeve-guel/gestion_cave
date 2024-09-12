import tkinter as tk
from tkinter import messagebox

import sqlite3

from Frame.add_boisson_frame import add_boisson
from Frame.fenetre1 import create_frame1
from Frame.fenetre2 import create_frame2

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
        file_menu.add_command(label="Fenêtre 1", command=self.show_frame1)
        file_menu.add_command(label="Fenêtre 2", command=self.show_frame2)
        file_menu.add_command(label="Quitter", command=self.quit)

        #boisson

        boisson = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='Boisson',menu= boisson)

       
        #root.config(menu=menuBar)
        boisson.add_command(label='Ajouter une boisson',command=self.show_add_boisson)
        boisson.add_command(label='Liste des boissons')

        #Utilisateur
        user = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='Utilisateurs',menu=user)
        user.add_command(label='Ajouter un administrateur')
        user.add_command(label='Liste des administrateur')
        # utilisateur.add_command(label='Paste')
        # utilisateur.add_command(label='Select all')
        user.add_separator()
        user.add_command(label='Ajouter un client')
        user.add_command(label='Liste des clients')

        #Profil
        profil = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='Profil',menu=profil)

        profil.add_command(label='admin')
        profil.add_separator()
        profil.add_command(label='Paramètre du profile')

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
        
        create_frame1(self.frame1)
        create_frame2(self.frame2)
        add_boisson(self.frame3_add_b)
        
        self.current_frame = None
        self.show_frame1()

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

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Remplace ces conditions par la vérification réelle de tes identifiants
    if username == "admin" and password == "admin":
        root_login.destroy()  # Fermer la fenêtre de connexion
        app = Application()  # Afficher la fenêtre d'accueil
        app.mainloop()
    else:
        messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")

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
                role TEXT NOT NULL,
                password TEXT NOT NULL
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

conn.commit()

conn.close()

tk.Label(root_login,text="Connexion",font=("Arial",20)).pack(padx=20,pady=10)

tk.Label(root_login, text="Nom d'utilisateur").pack(padx=20, pady=5)
entry_username = tk.Entry(root_login)
entry_username.pack(padx=20, pady=5)

tk.Label(root_login, text="Mot de passe").pack(padx=20, pady=5)
entry_password = tk.Entry(root_login, show="*")
entry_password.pack(padx=20, pady=5)

tk.Button(root_login, text="Se connecter", command=check_login).pack(padx=20, pady=20)

root_login.mainloop()

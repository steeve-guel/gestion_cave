import tkinter as tk
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter

class ProfilFrame(tk.Frame):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username

        self.create_widgets()

    def create_widgets(self):
        
        self.label = tk.Label(self, text="Gestion du Profil")
        self.label.pack(pady=10)

        self.username_label = tk.Label(self, text="Nom d'utilisateur")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.insert(0, self.username)  # Remplir avec le nom d'utilisateur actuel
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Nouveau mot de passe")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.save_button = tk.Button(self, text="Sauvegarder", command=self.save_profile)
        self.save_button.pack(pady=20)

    def save_profile(self):
        new_username = self.username_entry.get()
        new_password = self.password_entry.get()
        # Ajoutez ici la logique pour mettre à jour le profil dans la base de données
        print(f"Profil mis à jour : {new_username}, {new_password}")
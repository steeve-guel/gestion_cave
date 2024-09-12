from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import sqlite3
from hashlib import sha256

from frames.boisson.ajouterBoisson import AjouterBoissonFrame
from frames.connexionFrame import ConnexionFrame
from frames.gestionCave import GestionFrame
from frames.inscriptionFrame import InscriptionFrame
from frames.profilFrame import ProfilFrame

class Application(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Gestion de Cave")
        self.geometry("800x500")
        self.configure(bg='#f8f8f8')

        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        # Créer des frames pour les pages
        self.frame1 = ConnexionFrame(self,self.show_gestion)
        self.frame2 = InscriptionFrame(self)
        #self.frame3 = GestionFrame(self,username=None,self.add_boisson)

        # Afficher la page de connexion
        self.frame1.pack(fill='both', expand=True)

       

    # def show_connexion_frame(self):
    #     self.connexion_frame = ConnexionFrame(self,self.show_profil_frame)
    #     self.connexion_frame.pack(fill="both", expand=True)

    #Fenetre du dashboard
    def show_gestion(self,username):
        self.frame1.pack_forget()
        self.gestion_frame = GestionFrame(self,username)
        self.gestion_frame.pack(fill='both',expand=True)

    #Fenetre ajouter boisson
    def show_add_boisson(self,username):
        #self.frame3.pack_forget()
        self.add_boisson = AjouterBoissonFrame(self)
        self.add_boisson.pack(fill='both',expand=True)

    def show_profil_frame(self, username):
        self.frame1.pack_forget()  # Masquer le frame de connexion
        self.profil_frame = ProfilFrame(self, username)
       
        self.profil_frame.pack(fill="both", expand=True)
        
        
    # def show_inscription_frame(self):
    #     self.inscription_frame = InscriptionFrame(self)
    #     self.inscription_frame.pack(fill="both", expand=True)
    #     self.show_connexion_frame.pack_forget()
    #     self.show_inscription_frame.pack_forget()

    def show_frame(self, frame):
        frame.pack(fill='both', expand=True)
        if frame == self.frame1:
            self.frame2.pack_forget()
        else:
            self.frame1.pack_forget()  

    def create_table(self):
    # Créer une table si elle n'existe pas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                phone TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def on_closing(self):
        # Fermer la connexion à la base de données
        self.cursor.close()
        self.conn.close()
        self.destroy()   

   

class Frame3(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = Label(self, text="Page 2")
        label.pack(pady=10)

        button = Button(self, text="Retour à la Page 1", command=lambda: parent.show_frame(parent.frame1))
        button.pack(pady=10)

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
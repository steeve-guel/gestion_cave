from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import sqlite3
from hashlib import sha256



#############################################################################        
#Frame Inscription
class InscriptionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

        def inscription():
            username = username_entry.get()
            phone = phone_entry.get()
            password = password_entry.get()
            if not username or not phone or not password:
                messagebox.showerror(title="Error", message="Remplir les champs vides.")
                
                # parent.show_frame(parent.frame2)
            else:
                try:
                    hashed_password = sha256(password.encode()).hexdigest()
                    self.cursor.execute("INSERT INTO utilisateurs (user, phone, password) VALUES (?, ?, ?)",
                                (username, phone, hashed_password))
                    self.conn.commit()
                    messagebox.showinfo("Succès", "Utilisateur enregistré avec succès !")
                    username_entry.delete(0, END)
                    phone_entry.delete(0, END)
                    password_entry.delete(0, END)
                except Exception as e:
                    messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {e}")
                    messagebox.showinfo(title="Inscription Success", message="Inscription reussie.")

        label = Label(self, text="Inscription",font=('Arial',25))
        label.pack(pady=10)

        username_label = Label(self, text="Nom d'utilisateur", font=("Arial", 16))
        username_entry = Entry(self, font=("Arial", 16))

        phone_label = Label(self,text="Téléphone",font=("Arial",16))
        phone_entry = Entry(self,font=("Arial",16))

        password_entry = Entry(self, show="*", font=("Arial", 16))
        password_label = Label(self, text="Mot de passe", font=("Arial", 16))

        login_button = Button(self, text="Connexion",
                               bg="#007FFF", fg="#FFFFFF", font=("Arial", 16),
                                 command=lambda: parent.show_frame(parent.frame1))

        inscription_button = Button(self,text="Enregistrer",
                                    bg="#80FF00", font=("Arial",16),
                                        command=inscription)


        # Placing widgets on the screen
        label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=20,padx=4)

        phone_label.grid(row=2, column=0)
        phone_entry.grid(row=2, column=1, pady=20,padx=4)

        password_label.grid(row=3, column=0)
        password_entry.grid(row=3, column=1, pady=20,padx=4)

        inscription_button.grid(row=4,column=1,columnspan=2, pady=20)
        login_button.grid(row=5, column=1, columnspan=2, pady=20)

        # button = Button(self, text="Aller à la Page 2", command=lambda: parent.show_frame(parent.frame2))
        # button.pack(pady=10)
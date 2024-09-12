from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import sqlite3
from hashlib import sha256

##############################################################################################
#Frame Connexion
class ConnexionFrame(Frame):
    def __init__(self, parent,show_profile_frame_callback):
        super().__init__(parent)
        
        self.show_profile_frame_callback = show_profile_frame_callback

        def login():
            username = username_entry.get()
            password = password_entry.get()
            hashed_password = sha256(password.encode()).hexdigest()
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM utilisateurs WHERE user = ? AND password = ?', (username, hashed_password))

            user = cursor.fetchone()

            if user:
                messagebox.showinfo(title="Login Success", message="Connexion reussie.")
                self.show_profile_frame_callback(username)
                return True
            else:
                messagebox.showerror(title="Error", message="Nom d'utilisateur ou mot de passe invalid.")
                return False

            # if username_entry.get()==username and password_entry.get()==password:
            #     messagebox.showinfo(title="Login Success", message="Connexion reussie.")
            #     # parent.show_frame(parent.frame2)
            # else:
            #     messagebox.showerror(title="Error", message="Nom d'utilisateur ou mot de passe invalid.")

        label = Label(self, text="Connexion",font=('Arial',25))
        label.pack(pady=10)

        username_label = Label(self, text="Nom d'utilisateur", font=("Arial", 16))
        username_entry = Entry(self, font=("Arial", 16))

        password_entry = Entry(self, show="*", font=("Arial", 16))

        password_label = Label(self, text="Mot de passe", font=("Arial", 16))

        login_button = Button(self, text="Connexion", bg="#007FFF", fg="#FFFFFF", font=("Arial", 16), command=login)

        inscription_button = Button(self,text="Inscription",bg="#80FF00", font=("Arial",16), command=lambda: parent.show_frame(parent.frame2))


        # Placing widgets on the screen
        label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=20,padx=4)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=20,padx=4)
        login_button.grid(row=3, column=1, columnspan=2, pady=30)
        inscription_button.grid(row=4,column=1,columnspan=2, pady=30)

        # button = Button(self, text="Aller à la Page 2", command=lambda: parent.show_frame(parent.frame2))
        # button.pack(pady=10)
# import tkinter as tk
# from tkinter import messagebox

# # Fonction pour vérifier les identifiants
# def check_login():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     # Remplace ces conditions par la vérification réelle de tes identifiants
#     if username == "admin" and password == "admin":
#         root_login.destroy()  # Fermer la fenêtre de connexion
#         show_home_window()    # Afficher la fenêtre d'accueil
#     else:
#         messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")

# # Fonction pour afficher la fenêtre d'accueil
# def show_home_window():
#     global root_home
#     root_home = tk.Tk()
#     root_home.title("Page d'accueil")

#     # Créer le menu
#     menu_bar = tk.Menu(root_home)
#     root_home.config(menu=menu_bar)
    
#     file_menu = tk.Menu(menu_bar, tearoff=0)
#     menu_bar.add_cascade(label="Menu", menu=file_menu)
#     file_menu.add_command(label="Fenêtre 1", command=open_window1)
#     file_menu.add_command(label="Fenêtre 2", command=open_window2)
#     file_menu.add_command(label="Quitter", command=root_home.quit)
    
#     root_home.mainloop()

# # Fonctions pour ouvrir différentes fenêtres
# def open_window1():
#     window1 = tk.Toplevel(root_home)
#     window1.title("Fenêtre 1")
#     tk.Label(window1, text="Ceci est la fenêtre 1").pack(padx=20, pady=20)

# def open_window2():
#     window2 = tk.Toplevel(root_home)
#     window2.title("Fenêtre 2")
#     tk.Label(window2, text="Ceci est la fenêtre 2").pack(padx=20, pady=20)

# # Création de la fenêtre de connexion
# root_login = tk.Tk()
# root_login.title("Connexion")

# tk.Label(root_login, text="Nom d'utilisateur").pack(padx=20, pady=5)
# entry_username = tk.Entry(root_login)
# entry_username.pack(padx=20, pady=5)

# tk.Label(root_login, text="Mot de passe").pack(padx=20, pady=5)
# entry_password = tk.Entry(root_login, show="*")
# entry_password.pack(padx=20, pady=5)

# tk.Button(root_login, text="Se connecter", command=check_login).pack(padx=20, pady=20)

# root_login.mainloop()


import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Page d'accueil")

        # Créer le menu
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_command(label="Fenêtre 1", command=self.show_frame1)
        file_menu.add_command(label="Fenêtre 2", command=self.show_frame2)
        file_menu.add_command(label="Quitter", command=self.quit)

        # Créer les Frames
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        
        self.create_frame1()
        self.create_frame2()
        
        self.current_frame = None
        self.show_frame1()

    def create_frame1(self):
        tk.Label(self.frame1, text="Ceci est la fenêtre 1").pack(padx=20, pady=20)

    def create_frame2(self):
        tk.Label(self.frame2, text="Ceci est la fenêtre 2").pack(padx=20, pady=20)

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

# Création de la fenêtre de connexion
root_login = tk.Tk()
root_login.title("Connexion")

tk.Label(root_login, text="Nom d'utilisateur").pack(padx=20, pady=5)
entry_username = tk.Entry(root_login)
entry_username.pack(padx=20, pady=5)

tk.Label(root_login, text="Mot de passe").pack(padx=20, pady=5)
entry_password = tk.Entry(root_login, show="*")
entry_password.pack(padx=20, pady=5)

tk.Button(root_login, text="Se connecter", command=check_login).pack(padx=20, pady=20)

root_login.mainloop()

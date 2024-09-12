# import tkinter as tk

# def on_button_click():
#     label.config(text="Bonjour, monde!")

# # Créer la fenêtre principale
# root = tk.Tk()
# root.title("Mon Application")

# # Ajouter un label
# label = tk.Label(root, text="Cliquez sur le bouton")
# label.pack(pady=10)

# # Ajouter un bouton
# button = tk.Button(root, text="Cliquez-moi", command=on_button_click)
# button.pack(pady=10)

# # Lancer la boucle principale
# root.mainloop()

# import tkinter as tk

# def on_button_click():
#     entered_text = entry.get()
#     label.config(text=f"Vous avez saisi : {entered_text}")

# # Créer la fenêtre principale
# root = tk.Tk()
# root.title("Mon Application avec Widgets")

# # Ajouter un label
# label = tk.Label(root, text="Saisissez quelque chose :")
# label.pack(pady=10)

# # Ajouter un champ de saisie
# entry = tk.Entry(root)
# entry.pack(pady=10)

# # Ajouter un bouton
# button = tk.Button(root, text="Valider", command=on_button_click)
# button.pack(pady=10)

# # Ajouter une case à cocher
# check_var = tk.BooleanVar()
# checkbutton = tk.Checkbutton(root, text="Activer une option", variable=check_var)
# checkbutton.pack(pady=10)

# # Ajouter des boutons radio
# radio_var = tk.StringVar(value="Option 1")
# radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
# radiobutton1.pack(pady=5)
# radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
# radiobutton2.pack(pady=5)

# # Ajouter une liste
# listbox = tk.Listbox(root)
# listbox.insert(1, "Élément 1")
# listbox.insert(2, "Élément 2")
# listbox.insert(3, "Élément 3")
# listbox.pack(pady=10)

# # Lancer la boucle principale
# root.mainloop()

import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Gestion de la Cave")
        self.geometry("400x300")

        # Créer des frames pour les pages
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)

        # Afficher la première page
        self.frame1.pack(fill='both', expand=True)

    def show_frame(self, frame):
        frame.pack(fill='both', expand=True)
        if frame == self.frame1:
            self.frame2.pack_forget()
        else:
            self.frame1.pack_forget()

class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = tk.Label(self, text="Page 1")
        label.pack(pady=10)

        button = tk.Button(self, text="Aller à la Page 2", command=lambda: parent.show_frame(parent.frame2))
        button.pack(pady=10)

class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = tk.Label(self, text="Page 2")
        label.pack(pady=10)

        button = tk.Button(self, text="Retour à la Page 1", command=lambda: parent.show_frame(parent.frame1))
        button.pack(pady=10)

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
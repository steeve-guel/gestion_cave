from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter

from frames.boisson.ajouterBoisson import AjouterBoissonFrame

class GestionFrame(Frame):
    def __init__(self,parent,username):
        super().__init__(parent)
        #self.show_add_boisson_frame_callback = show_add_boisson_frame_callback

        self.create_menu(username=username,parent=parent)
        self.create_widget()

    def create_menu(self,username,parent):

        menuBar = Menu(self)

        boisson = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Boisson',menu= boisson)

       
        #root.config(menu=menuBar)
        boisson.add_command(label='Ajouter une boisson',command= lambda: AjouterBoissonFrame)
        boisson.add_command(label='Liste des boissons')
        # boisson.add_separator()
        # boisson.add_command(label='Exit',command=self.destroy)

        #Utilisateur
        user = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Utilisateurs',menu=user)
        user.add_command(label='Ajouter un administrateur')
        user.add_command(label='Liste des administrateur')
        # utilisateur.add_command(label='Paste')
        # utilisateur.add_command(label='Select all')
        user.add_separator()
        user.add_command(label='Ajouter un client')
        user.add_command(label='Liste des clients')

        #Profil
        profil = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Profil',menu=profil)

        profil.add_command(label=username)
        profil.add_separator()
        profil.add_command(label='Paramètre du profile')

        #Aide
        help = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Aide',menu=help)
        help.add_command(label='Aide Cave')
        # help.add_command(label='Demo')
        help.add_separator()
        help.add_command(label='exit')

        self.master.config(menu=menuBar) # type: ignore

    def create_widget(self):
        self.label = Label(self, text="Dashboard",font=("Arial",20))
        self.label.pack(pady=10)

    
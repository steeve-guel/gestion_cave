from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter

class AjouterBoissonFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.create_widget()

    def create_widget(self):
        self.label = Label(text='Ajouter une boisson')
        self.label.pack(pady=30)
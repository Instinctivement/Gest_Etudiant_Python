from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter
import tkinter as ttk
from ttkbootstrap.constants import *

class AddStudent_UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ajout Etudiant')
        self.geometry('600x480')
        
        self.firstName = StringVar(value="")
        self.secondName = StringVar(value="")
        self.birthday = StringVar(value="")
        self.academicYear = StringVar(value="")
        self.level = StringVar(value="")
        self.comment = StringVar(value="")
        self.sem_one = StringVar(value="")
        self.sem_two = StringVar(value="")
        self.general = StringVar(value="")
        
        tk.Label(self, text = 'A label').pack()
        
        self.main_container = tk.Frame(self)
        self.main_container.pack(fill=X, expand=YES, pady=5)
        
        self.create_form_entry("Prenom", self.firstName)
        self.create_form_entry("Nom", self.secondName)
        self.create_form_entry("Date de naissance", self.birthday)
        self.create_form_entry("Année académique", self.academicYear)
        self.create_form_entry("Niveau", self.level)
        self.create_form_entry("Commentaire", self.comment)
        self.create_buttonbox()
        
    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = tk.Frame(self.main_container)
        container.pack(fill=X, expand=YES, pady=6)

        lbl = tk.Label(master=container, text=label.title(), width=16)
        lbl.pack(side=LEFT, padx=5)

        ent = tk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)


    
        
        
if __name__ == '__main__':
    app = AddStudent_UI()
    app.mainloop()
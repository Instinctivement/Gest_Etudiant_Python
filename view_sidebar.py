from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter
import customtkinter as ctk


class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.show_sidebar()
    
        self.grid_rowconfigure(4, weight=1)
      
    def show_sidebar(self):
        # create sidebar frame with widgets
        
        self.logo_label = customtkinter.CTkLabel(self, text="OMG | ISTY", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Top Sidebar
        self.sidebar_button_1 = customtkinter.CTkButton(self, text="Inscription", command=self.show_addStudent_UI)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self, text="Niveau", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Années", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        # Bottom Sidebar
        self.sidebar_button_4 = customtkinter.CTkButton(self, text="Exporter PDF", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_5 = customtkinter.CTkButton(self, text="Exporter CSV", command=self.sidebar_button_event)
        self.sidebar_button_5.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_6 = customtkinter.CTkButton(self, text="A Propos", command=self.sidebar_button_event)
        self.sidebar_button_6.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Clair", "Sombre", "Système"],
                                                                       command=self.sidebar_button_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(4, 10))
    
    def show_addStudent_UI(self):
        add_student = AddStudent_UI()
        
    def sidebar_button_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")


class AddStudent_UI():
    def __init__(self):
        super().__init__()
        self.title('Ajout Etudiant')
        self.geometry('400x400')
        #self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        
        self.firstName = StringVar(value="")
        self.secondName = StringVar(value="")
        self.birthday = StringVar(value="")
        self.academicYear = StringVar(value="")
        self.level = StringVar(value="")
        self.comment = StringVar(value="")
        
        # Ajouter un champ de saisie pour le nom de l'étudiant
        self.name_label = ctk.CTkLabel(self, text="Nom:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.grid(row=0, column=1)

        # Ajouter un bouton pour ajouter l'étudiant
        self.add_button = ctk.CTkButton(self, text="Ajouter")
        self.add_button.grid(row=1, column=0)

        # Ajouter un bouton pour fermer la fenêtre de dialogue
        self.cancel_button = ctk.CTkButton(self, text="Annuler", command=self.destroy)
        self.cancel_button.grid(row=1, column=1)

        
    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = tk.Frame(self.main_container)
        container.pack(fill=X, expand=YES, pady=6)

        lbl = tk.Label(master=container, text=label.title(), width=16)
        lbl.pack(side=LEFT, padx=5)

        ent = tk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
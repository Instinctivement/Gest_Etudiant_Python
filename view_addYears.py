from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class AddYears_UI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Ajouter un niveau')
        self.geometry('400x300')
        
        # form variables
        self.academicYear = ttk.StringVar()
        
        # register the validation callback
        self.digit_func = self.register(self.validate_number)
        self.alpha_func = self.register(self.validate_alpha)

        # form header
        hdr_txt = "Ajouter un nouveau niveau" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        list_level = ["CPI-1","CPI-2","IATIC-3", "IATIC-4", "IATIC-5"]
        self.create_form_entry_select("Niveau", list_level)
        self.create_form_entry("Année", self.academicYear, self.alpha_func)
        self.create_buttonbox()

    def validate_number(self, x) -> bool:
        """Validates that the input is a number"""
        if x.isdigit():
            return True
        elif x == "":
            return True
        else:
            return False

    def validate_alpha(self, x) -> bool:
        """Validates that the input is alpha"""
        if x.isdigit():
            return False
        elif x == "":
            return True
        else:
            return True
    
    def create_form_entry(self, label, variable, valid_function):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=10)

        ent = ttk.Entry(master=container, textvariable=variable, validate="focus", validatecommand=(valid_function, '%P'))
        ent.pack(side=LEFT, padx=10, fill=X, expand=YES)
        
    def create_form_entry_date(self, label):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=10)

        ent = ttk.DateEntry(master=container)
        ent.pack(side=LEFT, padx=10, fill=X, expand=YES)
        return ent
    
    # Template of select data
    def create_form_entry_select(self, label, val):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=10)

        ent = ttk.Combobox(master=container, values=val)
        ent.pack(side=LEFT, padx=10, fill=X, expand=YES)
        return ent

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 20), padx=10)

        sub_btn = ttk.Button(
            master=container,
            text="Envoyer",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=12,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Annuler",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=12,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        """Print the contents to console and return the values."""
        infos = {}
        infos["academicYear"] = self.academicYear.get()
        print(json.dumps(infos, indent=4))
        self.on_cancel()
       
    def on_cancel(self):
        """Cancel all input."""
        self.academicYear.set("")
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import schooling

class AddStudent_UI(ttk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title('Ajout')
        self.geometry('400x500')
        self.schooling = schooling.Schooling()
        
        # set the controller 
        self.controller = controller
        
        # form variables
        self.firstName = ttk.StringVar()
        self.secondName = ttk.StringVar()
        self.birthday = ttk.StringVar()
        self.academicYear = ttk.StringVar()
        self.level = ttk.StringVar()
        self.comment = ttk.StringVar()
        
        # register the validation callback
        self.digit_func = self.register(self.validate_number)
        self.alpha_func = self.register(self.validate_alpha)

        # form header
        hdr_txt = "Ajout d'un nouvel étudiant" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Prenom", self.firstName, self.alpha_func)
        self.create_form_entry("Nom", self.secondName, self.alpha_func)
        self.birthday = self.create_form_entry_date("Date de naissance")
        self.create_form_entry_select("Année académique", self.schooling.academic_year, self.academicYear)
        self.create_form_entry_select("Niveau", self.schooling.level, self.level)
        self.create_form_entry("Commentaire", self.comment, self.alpha_func)
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
    def create_form_entry_select(self, label, val, var):
        container = ttk.Frame(self) 
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=10)

        ent = ttk.Combobox(master=container, values=val, textvariable=var)
        ent.pack(side=LEFT, padx=10, fill=X, expand=YES)
        return ent

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 20), padx=10)

        sub_btn = ttk.Button(
            master=container,
            text="Envoyer",
            command=self.add_student,
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

    def add_student(self):
        """Appelée lorsque le bouton d'ajout est cliqué"""
        student_data = {
            "firstName": self.firstName.get(),
            "secondName": self.secondName.get(),
            "birthday": self.birthday.entry.get(),
            "academicYear": self.academicYear.get(),
            "level": self.level.get(),
            "comment": self.comment.get()
        }
        if self.controller:
            self.controller.add_student(student_data)
            
    def on_cancel(self):
        """Cancel all input."""
        self.firstName.set("")
        self.secondName.set("")
        self.comment.set("")
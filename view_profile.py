from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json


class Profile(ttk.Frame):
    def __init__(self, master, table, **kwargs):
        super().__init__(master, **kwargs)
        
        # access App attributes
        self.table_instance = table
        self.controller = None
        
        #creating custom frame
        self.frame=ttk.Frame(master=self, width=320, height=360)
        self.frame.pack(pady=20, padx=16, fill="both", expand=True)
        
        # configure grid layout (4x4)
        self.frame.grid_rowconfigure(10, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.show_userDataEntry()
        self.show_modify_zone()
        
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        #User data Section 
    
    def show_userDataEntry(self):
        info_frame = ttk.Labelframe(
            master=self.frame,
            text="Zone d'Informations statiques",
            padding=(20, 5)
        )
        info_frame.pack(fill=BOTH, expand=YES, pady=10)
        
       
        # First row
        self.create_form_entry(info_frame,"Prenom", self.table_instance.firstName)
        self.create_form_entry(info_frame,"Nom", self.table_instance.secondName)
        self.create_form_entry(info_frame,"Date de naissance", self.table_instance.birthday)
        self.create_form_entry(info_frame,"Année académique", self.table_instance.academicYear)
        self.create_form_entry(info_frame,"Niveau", self.table_instance.level)
        
    def show_modify_zone(self):
        modify_frame = ttk.Labelframe(
            master=self.frame,
            text='Zone de modification',
            padding=(20, 5)
        )
        modify_frame.pack(fill=BOTH, expand=YES, pady=10)
                
        self.create_form_entry(modify_frame,"Semestre-1", self.table_instance.sem_one)
        self.create_form_entry(modify_frame,"Semestre-2", self.table_instance.sem_two)
        self.create_form_entry(modify_frame,"Générale", self.table_instance.general)        
        self.create_form_entry(modify_frame,"Commentaire", self.table_instance.comment)        
        self.create_buttonbox(modify_frame)
        
    def create_form_entry(self, parent, label, variable):
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=(5,10))

        ent = ttk.Entry(container, width=20, textvariable=variable)
        ent.pack(side=LEFT, fill=X, expand=YES, padx=(0,5))
        
        return ent
    
    def create_buttonbox(self, parent):
        """Create the application buttonbox"""
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=(10, 20), padx=16)

        sub_btn = ttk.Button(
            master=container,
            text="Modifier",
            command=self.modify,
            bootstyle=PRIMARY,
            width=12,
        )
        sub_btn.pack(side=LEFT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Supprimer",
            command=self.delete,
            bootstyle=DANGER,
            width=12,
        )
        cnl_btn.pack(side=RIGHT, padx=5)
    
    def modify(self):
        student_data = (
            self.table_instance.sem_one.get(),
            self.table_instance.sem_two.get(),
            self.table_instance.general.get(),
            self.table_instance.comment.get())
        if self.controller:
            print(student_data)
            self.controller.update_student(self.table_instance.id.get(), student_data)
       
       
    def delete(self):
        if self.controller:
            self.controller.delete_student(self.table_instance.id.get())
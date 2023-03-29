from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter


class Profile(customtkinter.CTkFrame):
    def __init__(self, master, table, **kwargs):
        super().__init__(master, **kwargs)
        
        # access App attributes
        self.table_instance = table
        
        #creating custom frame
        self.frame=customtkinter.CTkFrame(master=self, width=320, height=360, corner_radius=15)
        self.frame.pack(pady=20, padx=16, fill="both", expand=True)
        
        # configure grid layout (4x4)
        self.frame.grid_rowconfigure(10, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.show_userDataEntry()
        

        #User data Section 
    
    def show_userDataEntry(self):
        title=customtkinter.CTkLabel(self.frame, text="Détailles",font=customtkinter.CTkFont('Century Gothic',size=20, weight="bold"))
        title.grid(row=0, column=0, padx=16, pady=(40, 30), sticky="nsw")
        
        # First row
        self.create_form_entry("Prenom", "Entrer prenom", 1, self.table_instance.firstName)
        self.create_form_entry("Nom", "Entrer nom", 2, self.table_instance.secondName)
        self.create_form_entry("Date de naissance", "Date de naissance", 3, self.table_instance.birthday)
        self.create_form_entry("Année académique", "Année académique", 4, self.table_instance.academicYear)
        self.create_form_entry("Niveau", "Niveau", 5, self.table_instance.level)
        self.create_form_entry("Semestre-1", "Semestre-1", 6, self.table_instance.sem_one)
        self.create_form_entry("Semestre-2", "Semestre-2", 7, self.table_instance.sem_two)
        self.create_form_entry("Générale", "Générale", 8, self.table_instance.general)        
        
        lbl = customtkinter.CTkLabel(self.frame, text="Commentaire", font=customtkinter.CTkFont('Century Gothic',16))
        lbl.grid(row=9, column=0, padx=(16, 16), pady=(0, 20), sticky="snw")
        text_1 = customtkinter.CTkTextbox(self.frame, width=200, height=70)
        text_1.grid(row=9, column=1, padx=(0, 16), pady=(0, 10), sticky="sne")
        #update_btn = Button(text="Update", command=self.update_student)
        #add_btn = Button(text="Add", command=self.add_student)
        #delete_btn = Button(text="Delete", command=self.delete_student)

        #update_btn.grid(row=4, column=0, padx=5, pady=3)
        #add_btn.grid(row=4, column=1, padx=5, pady=3)
        #delete_btn.grid(row=4, column=2, padx=5, pady=3)
        
    def create_form_entry(self, label, myplaceholder, row, variable):

        lbl = customtkinter.CTkLabel(self.frame, text=label.title(), font=customtkinter.CTkFont('Century Gothic',16))
        lbl.grid(row=row, column=0, padx=(16, 16), pady=(0, 20), sticky="snw")

        ent = customtkinter.CTkEntry(self.frame, width=200, textvariable=variable, placeholder_text=myplaceholder)
        ent.grid(row=row, column=1, padx=(0, 16), pady=(0, 10), sticky="sne")
        
        return ent
    
    # Template of select data
    def create_form_entry_select(self,  parent, label, row, col, val, variable):
        lbl = ttk.Label(master=parent, text=label.title(), width=42)
        lbl.grid(row=row, column=col)

        ent = ttk.Combobox(master=parent, values=val, width=42)
        ent.grid(row=row+1, column=col)
        return ent
    
    # Template of input date
    def create_form_entry_date(self,  parent, label, row, col, variable):
        lbl = ttk.Label(master=parent, text=label.title(), width=42)
        lbl.grid(row=row, column=col)

        ent = ttk.DateEntry(master=parent, width=42)
        ent.grid(row=row+1, column=col)
        return ent
    
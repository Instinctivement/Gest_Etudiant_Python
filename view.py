import error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

# Local class
import view_profile
import view_table
import view_sidebar

class View(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # configure grid layout (4x4)
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
                
        # set the controller 
        self.controller = None
        
        self.trv = None
        
        # create scrollable label and button frame
        self.Sidebar_frame = view_sidebar.SideBar(master=self, width=140, corner_radius=0)
        self.Sidebar_frame.grid(row=0, column=0, sticky="nswe")
        
        
        # create scrollable label and button frame
        self.table_frame = view_table.Table_section(master=self, width=700, corner_radius=0)
        self.table_frame.grid(row=0, column=1, padx=10, pady=0, sticky="nswe")
        
       
        # create scrollable radiobutton frame
        self.profile_frame = view_profile.Profile(master=self, table=self.table_frame, width=200)
        self.profile_frame.grid(row=0, column=2, padx=10, pady=15, sticky="nswe")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    #*********************************************************************************
    
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        self.table_frame.set_controller(self.controller)
            
    def add_student(self):
        """
        Handle button click event
        :return:
        """
        tuple_data = (self.firstName.get(),self.secondName.get(),self.birthday.get(),self.academicYear.get(),self.level.get(),self.comment.get())
        if messagebox.askyesno("Ajout étudiant", "Confirmez pour ajouter cet étudiant"):
            if self.controller:
                query = self.controller.add_student(tuple_data)
                if query:
                    print("Success")
                    self.clear_data()
                else:
                    print("Failed")
        else:
            pass
            
    def update_student(self):
        """
        Handle button click event
        :return:
        """
        tuple_data = (self.firstName.get(),self.secondName.get(),self.birthday.get(),self.academicYear.get(),self.level.get(),self.comment.get(),self.id.get())
        if messagebox.askyesno("Confirmation", f"Vous allez mettre à jour les information de l'étudiant: {self.firstName.get()}"):
            if self.controller:
                query = self.controller.update_student(tuple_data)
                if query:
                    print("Success")
                    self.clear_data()
                else:
                    print("Failed")
        else:
            pass
            
    def delete_student(self):
        """
        Handle button click event
        :return:
        """
        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cet étudiant ?"):
            if self.controller:
                query = self.controller.delete_student(self.id.get())
                if query:
                    print("Success")
                    self.clear_data()
                else:
                    print("Failed")
        else:
            pass
                
    def enter_data(self):
        
        # User info
        infos = {}
        if error.char_lenght_error(self.firstName.get(), 16):
            infos["firstName"] = self.firstName.get()
            if error.char_lenght_error(self.secondName.get(), 16):
                infos["secondName"] = self.secondName.get()
                if error.birthday_format_error(self.birthday.get()) and error.birthday_limit_error(self.birthday.get()):
                    infos["birthday"] = self.birthday.get()
                
                else:
                    ttk.messagebox.showwarning(title= "ERREUR", message="ERREUR: Le champ nom ne peut pas dépasser 16 caractères")
            else:
                ttk.messagebox.showwarning(title= "ERREUR", message="ERREUR: Le champ nom ne peut pas dépasser 16 caractères")
        else:
            ttk.messagebox.showwarning(title= "ERREUR", message="ERREUR: Le champ nom ne peut pas dépasser 16 caractères")



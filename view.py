import error
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

class View(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # configure grid layout (4x4)
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
                
        # set the controller 
        self.controller = None
        
        self.trv = None
    
        # form variables
        self.id = StringVar()
        self.firstName = StringVar(value="")
        self.secondName = StringVar(value="")
        self.birthday = StringVar(value="")
        self.academicYear = StringVar(value="")
        self.level = StringVar(value="")
        self.comment = StringVar(value="")
        self.search_var = StringVar(value="")
        
        self.show_sidebar()
        #self.show_mainSection()
        
        # Sections
        self.wrapper1 = LabelFrame(self, text="Customer List")
        self.wrapper2 = LabelFrame(self, text="Search")
        self.wrapper3 = LabelFrame(self, text="Customer Data")
        
        #self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        #self.wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
        #self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
        
        #self.show_search()
        #self.show_userDataEntry()
        
    def show_sidebar(self):
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="OMG | ISTY", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Top Sidebar
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Inscription", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Niveau", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Années", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        # Bottom Sidebar
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Exporter PDF", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Exporter CSV", command=self.sidebar_button_event)
        self.sidebar_button_5.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="A Propos", command=self.sidebar_button_event)
        self.sidebar_button_6.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Clair", "Sombre", "Système"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(4, 10))
    
       

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        
    #Table Section
    def show_table(self):
        
        self.trv = ttk.Treeview(self.wrapper1, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="10")
        self.trv.pack()

        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="Prenom")
        self.trv.heading(3, text="Nom")
        self.trv.heading(4, text="Date de Naiss")
        self.trv.heading(5, text="Année Acad")
        self.trv.heading(6, text="Niveau")
        self.trv.heading(7, text="Commentaire")
        self.trv.heading(8, text="Semestre-1")
        self.trv.heading(9, text="Semestre-2")
        self.trv.heading(10, text="Général")

        self.trv.bind('<Double 1>', self.getrow_table)

        rows = self.show_all_data_table()
        self.update_data_table(rows)
    
    #Search Section 
    def show_search(self):
        lbl = Label(self.wrapper2, text="Search")
        lbl.pack(side=tk.LEFT, padx=10)
        ent = Entry(self.wrapper2, textvariable=self.search_var)
        ent.pack(side=tk.LEFT, padx=6)
        btn = Button(self.wrapper2, text="Search", command=self.search_data)
        btn.pack(side=tk.LEFT, padx=6)
        cbtn = Button(self.wrapper2, text="Clear", command=self.clear_data)
        cbtn.pack(side=tk.LEFT, padx=6)
    
    #User data Section 
    def show_userDataEntry(self):
        # First row
        self.create_form_entry(self.wrapper3, "Prenom", 0, 0, self.firstName)
        self.create_form_entry(self.wrapper3, "Nom", 0, 1, self.secondName)
        self.create_form_entry(self.wrapper3, "Date de naissance", 0, 2, self.birthday)
        
        
        # Second row
        self.create_form_entry(self.wrapper3, "Année académique",  2, 0, self.academicYear)
        self.create_form_entry(self.wrapper3, "Niveau", 2, 1, self.level)
        self.create_form_entry(self.wrapper3, "Commentaire", 2, 2, self.comment)
        
        update_btn = Button(self.wrapper3, text="Update", command=self.update_student)
        add_btn = Button(self.wrapper3, text="Add", command=self.add_student)
        delete_btn = Button(self.wrapper3, text="Delete", command=self.delete_student)

        update_btn.grid(row=4, column=0, padx=5, pady=3)
        add_btn.grid(row=4, column=1, padx=5, pady=3)
        delete_btn.grid(row=4, column=2, padx=5, pady=3)
        
        
        for widget in self.wrapper3.winfo_children():
            widget.grid_configure(padx=10, pady=5)
 
    # Create text/numerical inputs
    def create_form_entry(self, parent, label, row, col, variable):

        lbl = ttk.Label(master=parent, width=46, text=label.title())
        lbl.grid(row=row, column=col)

        ent = ttk.Entry(master=parent, textvariable=variable, width=46)
        ent.grid(row=row+1, column=col)
        
        return ent
    
    # Template of input date
    def create_form_entry_date(self,  parent, label, row, col, variable):
        lbl = ttk.Label(master=parent, text=label.title(), width=42)
        lbl.grid(row=row, column=col)

        ent = ttk.DateEntry(master=parent, width=42)
        ent.grid(row=row+1, column=col)
        return ent
    
    # Template of select data
    def create_form_entry_select(self,  parent, label, row, col, val, variable):
        lbl = ttk.Label(master=parent, text=label.title(), width=42)
        lbl.grid(row=row, column=col)

        ent = ttk.Combobox(master=parent, values=val, width=42)
        ent.grid(row=row+1, column=col)
        return ent
    
    #Action section
    def getrow_table(self, event):
        rowid = self.trv.identify_row(event.y)
        item = self.trv.item(self.trv.focus())
        self.id.set(item['values'][0])
        self.firstName.set(item['values'][1])
        self.secondName.set(item['values'][2])
        self.birthday.set(item['values'][3])
        self.academicYear.set(item['values'][4])
        self.level.set(item['values'][5])
        self.comment.set(item['values'][6])
            
    def show_all_data_table(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            rows = self.controller.show_all_data_table()
            return rows
            
    def update_data_table(self, rows):
        """
        Handle button click event
        :return:
        """
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i)
            
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
            
    def search_data(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            rows = self.controller.search_data_table(self.search_var.get())
            self.update_data_table(rows)
             
    def clear_data(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.search_var.set("")
            self.id.set(None)
            self.firstName.set("")
            self.secondName.set("")
            self.birthday.set("")
            self.academicYear.set("")
            self.level.set("")
            self.comment.set("")
            rows = self.controller.show_all_data_table()
            self.update_data_table(rows)
    
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

            
class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Command", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
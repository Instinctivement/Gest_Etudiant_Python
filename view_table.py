from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter


class Table_section(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
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
        self.sem_one = StringVar(value="")
        self.sem_two = StringVar(value="")
        self.general = StringVar(value="")
        self.search_var = StringVar(value="")

        # create main entry and button
        self.search_section = customtkinter.CTkFrame(master=self)
        self.search_section.pack(fill="both", expand="yes", padx=6, pady=6)
        
        self.entry = customtkinter.CTkEntry(self.search_section, textvariable=self.search_var, placeholder_text="Rechercher")
        self.entry.pack(side=LEFT, padx=(10, 20), pady=6, fill=X, expand=YES)

        self.search_button = customtkinter.CTkButton(master=self.search_section, text="Rechercher", command=self.search_data, border_width=1)
        self.search_button.pack(side=LEFT, padx=(0, 10), pady=6)
        self.reset_button = customtkinter.CTkButton(master=self.search_section, text="Reinitialiser", command=self.clear_data, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.reset_button.pack(side=LEFT, padx=(0, 10), pady=6)
        
        self.frame=customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=6, padx=6, fill="both", expand=True)
        
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        
    #Table Section
    def show_table(self):
        
        self.trv = ttk.Treeview(self.frame, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="30")
        self.trv.pack(fill = 'both', expand = True)

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
        
    def update_data_table(self, rows):
        """
        Handle button click event
        :return:
        """
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', END, values=i)
            
    def show_all_data_table(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            rows = self.controller.show_all_data_table()
            return rows
            
    def search_data(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            rows = self.controller.search_data_table(self.search_var.get())
            self.update_data_table(rows)
            
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
        self.sem_one.set(item['values'][7])
        self.sem_two.set(item['values'][8])
        self.general.set(item['values'][9])
        
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
            self.sem_one.set("")
            self.sem_two.set("")
            self.general.set("")
            rows = self.controller.show_all_data_table()
            self.update_data_table(rows)
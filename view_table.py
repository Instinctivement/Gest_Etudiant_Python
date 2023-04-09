from tkinter import *
import ttkbootstrap as ttk
import schooling

class Table_section(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # set the controller 
        self.controller = None
        self.trv = None
        self.schooling = schooling.Schooling()
        
        # form variables
        self.id = StringVar()
        self.firstName = StringVar()
        self.secondName = StringVar()
        self.birthday = StringVar()
        self.academicYear = StringVar()
        self.level = StringVar()
        self.comment = StringVar()
        self.sem_one = StringVar()
        self.sem_two = StringVar()
        self.general = StringVar()
        self.search_var = StringVar()
        self.search_var1 = StringVar()
        self.search_var2 = StringVar()

        # create main entry and button
        self.search_section = ttk.Labelframe(
            master=self,
            text='Recherche générale',
            padding=(20, 5))
        self.search_section.pack(fill="x", expand="yes", padx=6, pady=6)
        
        self.entry = ttk.Entry(self.search_section, textvariable=self.search_var)
        self.entry.pack(side=LEFT, padx=(10, 20), pady=6, fill=X, expand=YES)

        self.search_button = ttk.Button(master=self.search_section, text="Rechercher", command=self.search_data)
        self.search_button.pack(side=LEFT, padx=(0, 10), pady=6)
        self.reset_button = ttk.Button(master=self.search_section, text="Reinitialiser", command=self.clear_data)
        self.reset_button.pack(side=LEFT, padx=(0, 10), pady=6)
        
        self.search_data_advanced()
        # form header
        hdr_txt = "**Faites un double clic sur une ligne du tableau pour modifier les informations d'un étudiant" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=150)
        hdr.pack(fill=X, padx=10, pady=10)
        
        self.frame=ttk.Frame(master=self)
        self.frame.pack(pady=6, padx=6, fill="both", expand=YES)
        
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
        self.trv.pack(side=LEFT, expand="yes",  fill="both")
        #self.trv.place(x=0, y=0)

        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="Prenom")
        self.trv.heading(3, text="Nom")
        self.trv.heading(4, text="Date de Naiss")
        self.trv.heading(5, text="Année Acad")
        self.trv.heading(6, text="Niveau")
        self.trv.heading(7, text="Comment")
        self.trv.heading(8, text="Sem-1")
        self.trv.heading(9, text="Sem-2")
        self.trv.heading(10, text="Général")
        
        self.trv.column(1, width=50, minwidth=60)
        self.trv.column(2, width=100, minwidth=120)
        self.trv.column(3, width=100, minwidth=120)
        self.trv.column(4, width=100, minwidth=120)
        self.trv.column(5, width=100, minwidth=120)
        self.trv.column(6, width=100, minwidth=120)
        self.trv.column(7, width=100, minwidth=120)
        self.trv.column(8, width=100, minwidth=120)
        self.trv.column(9, width=100, minwidth=120)
        self.trv.column(10, width=100, minwidth=120)

        self.trv.bind('<Double 1>', self.getrow_table)

        rows = self.show_all_data_table()
        self.update_data_table(rows)
        
        
        #horizontal scrollbar
        xscrollbar = Scrollbar(self.frame, orient="horizontal", command=self.trv.xview)
        xscrollbar.pack(side=BOTTOM, fill="x")
        
        self.trv.configure(xscrollcommand=xscrollbar.set)
        
        
        
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
            
    def search_data_advanced_func(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            student_data = (self.search_var1.get(),self.search_var2.get())
            rows = self.controller.search_data_table_advanced(student_data)
            self.update_data_table(rows)
            
    def search_data_advanced(self):
        modify_frame = ttk.Labelframe(
            master=self,
            text='Recherche spécifique',
            padding=(20, 5)
        )
        modify_frame.pack(fill="x", expand="yes", padx=6, pady=6)
                
        self.create_form_entry_select(modify_frame, "Année académique", self.schooling.academic_year, self.search_var1)
        self.create_form_entry_select(modify_frame, "Niveau", self.schooling.level, self.search_var2)        
        search_button = ttk.Button(master=modify_frame, text="Rechercher", command=self.search_data_advanced_func)
        search_button.pack(side=LEFT, padx=(0, 10), pady=6)
            
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
            
    def create_form_entry_select(self, parent, label, val, var):
        container = ttk.Frame(parent) 
        container.pack(side=LEFT, padx=10)

        lbl = ttk.Label(master=container, text=label.title())
        lbl.pack(side=LEFT, padx=10)

        ent = ttk.Combobox(master=container, values=val, textvariable=var)
        ent.pack(side=LEFT, padx=10, fill=X, expand=YES)
        return ent
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import view_addStudent as AddStud
import view_addLevel as AddLev
import view_addYears as AddYears


class SideBar(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # set the controller 
        self.controller = None
        self.add_Student_Win = None
        
        self.show_sidebar()
        self.grid_rowconfigure(4, weight=1)
        
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
      
    def show_sidebar(self):
        # create sidebar frame with widgets
        
        self.logo_label = ttk.Label(self, text="OMG | ISTY")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Top Sidebar
        self.sidebar_button_1 = ttk.Button(self, text="Inscription", width=16, command=self.show_addStudent_UI)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ttk.Button(self, text="Niveau", width=16, command=self.show_addLevel_UI)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ttk.Button(self, text="Années", width=16, command=self.show_addYears_UI)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        # Bottom Sidebar
        self.sidebar_button_4 = ttk.Button(self, text="Exporter PDF", width=16, command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_5 = ttk.Button(self, text="Exporter CSV", width=16, command=self.sidebar_button_event)
        self.sidebar_button_5.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_6 = ttk.Button(self, text="A Propos", width=16, command=self.sidebar_button_event)
        self.sidebar_button_6.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label = ttk.Label(self, text="Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ttk.Combobox(self, width=16, values=["Clair", "Sombre", "Système"])
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(4, 10))
    
    def show_addStudent_UI(self):
        AddStud.AddStudent_UI(self.controller)
        
    def show_addLevel_UI(self):
        AddLev.AddLevel_UI()
        
    def show_addYears_UI(self):
        AddYears.AddYears_UI()
                
    def sidebar_button_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

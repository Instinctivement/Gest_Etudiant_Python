from tkinter import *
import customtkinter
from ttkbootstrap.toast import ToastNotification

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
        self.Sidebar_frame = view_sidebar.SideBar(master=self, width=140)
        self.Sidebar_frame.grid(row=0, column=0, sticky="nswe")
        
        
        # create scrollable label and button frame
        self.table_frame = view_table.Table_section(master=self, width=200)
        self.table_frame.grid(row=0, column=2, sticky="nswe")
        
       
        # create scrollable radiobutton frame
        self.profile_frame = view_profile.Profile(master=self, table=self.table_frame, width=200)
        self.profile_frame.grid(row=0, column=1, sticky="nse")

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
        self.Sidebar_frame.set_controller(self.controller)
        self.profile_frame.set_controller(self.controller)
    
    def show_error(self, msg):
        toast = ToastNotification(
            title = 'ERREUR', 
            message = msg,
            duration = 4000,
            bootstyle = 'danger',
            position = (50, 50, 'sw'))
        return toast.show_toast()
    
    def show_success(self, msg):
        toast = ToastNotification(
            title = 'SUCCESS', 
            message = msg,
            duration = 4000,
            bootstyle = 'success',
            position = (50, 50, 'ne'))
        return toast.show_toast()


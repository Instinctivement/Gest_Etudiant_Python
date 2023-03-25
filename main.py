from tkinter import *
import customtkinter

from view import * 
from model import * 
from controller import * 

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.title("OMG | Etudiant")
        self.geometry(f"{1100}x{580}")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        # create a model
        model = DB() 

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, sticky="nsew")

        # create a controller
        self.controller = Controller(model, view)

        # set the controller to view
        #view.set_controller(controller)
        #view.table_frame.show_table()
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
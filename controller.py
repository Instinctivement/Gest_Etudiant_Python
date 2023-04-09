from student import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # set the controller to view
        self.view.set_controller(self)
        self.view.table_frame.show_table()
    
    def show_all_data_table(self):
        rows = self.model.select_all_in_db()
        return rows
            
    def search_data_table(self, elem):
        rows = self.model.search_in_db(elem)
        return rows
            
    def search_data_table_advanced(self, elem):
        rows = self.model.search_in_db_advanced(elem)
        return rows
    
    def add_student(self, student_data):
        """Ajouter un nouvel étudiant"""
        try:
            student = Student(student_data)
            student.verify_integrity()  # Vérifier l'intégrité des données de l'étudiant
            if Messagebox.okcancel("Confirmez pour ajouter cet étudiant", "Ajout étudiant") == "OK":
                datas = student.parse_attribut_to_array()
                self.model.add_student(datas)
                self.view.table_frame.clear_data()
                self.view.show_success("L'étudiant a été ajouté avec succès.")
            else:
                pass
        except Exception as e:
            self.view.show_error(str(e))
    
    def update_student(self, id, student_data):
        try:
            datas_with_id = list(student_data)
            datas_with_id.append(id)
            if Messagebox.okcancel(f"Vous allez mettre à jour les information de cet étudiant ?", "Confirmation") == "OK":
                self.model.update_row_in_db(tuple(datas_with_id))
                self.view.table_frame.clear_data()
                self.view.show_success("Les informations de cet étudiant ont été modifié avec succès.")
            else:
                pass
        except Exception as e:
            Messagebox.ok(str(e), "ERREUR")
            
    def delete_student(self, id):
        try:
            if Messagebox.okcancel("Voulez-vous vraiment supprimer cet étudiant ?", "Confirmation") == "OK":
                self.model.delete_row_in_db(id)
                self.view.table_frame.clear_data()
                self.view.show_success("Cet étudiant a bien supprmé.")
            else:
                pass
        except Exception as e:
            Messagebox.ok(str(e), "ERREUR")

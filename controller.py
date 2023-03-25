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
        
    def add_student(self, tuple_data):
        query = self.model.insert_row_in_db(tuple_data)
        if query:
            return True
        else:
            return False
        
    def update_student(self, tuple_data):
        query = self.model.update_row_in_db(tuple_data)
        if query:
            return True
        else:
            return False
        
    def delete_student(self, id):
        query = self.model.delete_row_in_db(id)
        if query:
            return True
        else:
            return False

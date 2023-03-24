from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import model

def show_all_data():
    rows = mydb.select_all_in_db()
    return rows

def update_table(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)
        
def search():
    q2 = q.get()
    query = mydb.search_in_db(q2)
    update_table(query)

def clear():
    q.set("")
    query = show_all_data()
    update_table(query)
    
def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t0.set(item['values'][0])
    t1.set(item['values'][1])
    t2.set(item['values'][2])
    t3.set(item['values'][3])
    t4.set(item['values'][4])
    t5.set(item['values'][5])
    t6.set(item['values'][6])
    t7.set(item['values'][7])
    t8.set(item['values'][8])
    t9.set(item['values'][9])
    
def update_student():
    tuple_data = (t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t0.get())
    if messagebox.askyesno("Confirmation", f"Vous allez mettre à jour les information de l'étudiant: {t1.get()}"):
        query = mydb.update_row_in_db(tuple_data)
        if query:
            print("Success")
            clear()
        else:
            print("Failed")
    else:
        pass
    
def add_student():
    tuple_data = (t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get())
    
    if messagebox.askokcancel("Ajout étudiant", "Confirmez pour ajouter cet étudiant"):
        query = mydb.insert_row_in_db(tuple_data)
        if query:
            print("Success")
            clear()
        else:
            print("Failed")
    else:
        pass
    
def delete_student():
    if messagebox.askyesno("Confirmation de suppression", "Voulez-vous vraiment supprimer cet étudiant ?"):
        query = mydb.delete_row_in_db(t0.get())
        if query:
            print("Success")
            clear()
        else:
            print("Failed")
    else:
        pass
        
        
mydb = model.DB()
root = Tk()

q = StringVar()
t0 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()

wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="10")
trv.pack()

trv.heading(1, text="ID")
trv.heading(2, text="Prenom")
trv.heading(3, text="Nom")
trv.heading(4, text="Date de Naiss")
trv.heading(5, text="Année Acad")
trv.heading(6, text="Niveau")
trv.heading(7, text="Commentaire")
trv.heading(8, text="Semestre-1")
trv.heading(9, text="Semestre-2")
trv.heading(10, text="Général")

trv.bind('<Double 1>', getrow)

rows = show_all_data()
update_table(rows)

#Search Section 
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)

#User data Section 
lbl1 = Label(wrapper3, text="Prenom")
lbl1.grid(row=0, column=0, padx=5,pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Nom")
lbl2.grid(row=0, column=2, padx=5,pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=0, column=3, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Birthday")
lbl3.grid(row=0, column=4, padx=5,pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=0, column=5, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Annee")
lbl4.grid(row=1, column=0, padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=1, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Niveau")
lbl4.grid(row=1, column=2, padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t5)
ent4.grid(row=1, column=3, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Comment")
lbl4.grid(row=1, column=4, padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t6)
ent4.grid(row=1, column=5, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Sem - 1")
lbl4.grid(row=2, column=0, padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t7)
ent4.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Sem - 2")
lbl4.grid(row=2, column=2, padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t8)
ent4.grid(row=2, column=3, padx=5, pady=3)

lbl4 = Label(wrapper3, text="General")
lbl4.grid(row=2, column=4, padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t9)
ent4.grid(row=2, column=5, padx=5, pady=3)

update_btn = Button(wrapper3, text="Update", command=update_student)
add_btn = Button(wrapper3, text="Add", command=add_student)
delete_btn = Button(wrapper3, text="Delete", command=delete_student)

update_btn.grid(row=3, column=1, padx=5, pady=3)
add_btn.grid(row=3, column=3, padx=5, pady=3)
delete_btn.grid(row=3, column=5, padx=5, pady=3)


root.title("Student")
root.geometry("1080x700")
root.mainloop()
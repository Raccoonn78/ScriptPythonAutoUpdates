from tkinter import *
import tkinter as tk
from tkinter import LEFT, ttk
import sqlite3
from turtle import bgcolor
import tkinter.font as tkFont
import scriptStart 
from PIL import ImageTk,Image 


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()




    def init_main(self):
        
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.mass=[]

        self.add_img = tk.PhotoImage('output\\DataBase_GUI\\add2.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить путь', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage('output\\DataBase_GUI\\edit.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage('output\\DataBase_GUI\\delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить путь', bg='#d7d8e0', bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage('output\\DataBase_GUI\\search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage('output\\DataBase_GUI\\update.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                               compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'name',  'path', 'login', 'password'), height=15, show='headings')


        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=365, anchor=tk.CENTER)
        self.tree.column('path', width=365, anchor=tk.CENTER)
        self.tree.column('login', width=365, anchor=tk.CENTER)
        self.tree.column('password', width=365, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('name', text='Название')
        self.tree.heading('path', text='Путь')
        self.tree.heading('login', text='Login')
        self.tree.heading('password', text='Password')

        self.tree.pack()


        style_button=tkFont.Font(family="Verdana", size=18, weight="bold")
        self.start_button= tk.Button(text="Запустить", bd=1, compound=LEFT, width=50, height=3, bg='#256D7B', font=style_button, borderwidth=3,
                                                                                                 relief="ridge",command=self.start_programm)
        self.start_button.pack(side=tk.BOTTOM)


    def records(self, name,  path , login, password):
        self.db.insert_data(name,  path, login, password)
        self.view_records()

    def update_record(self, name,  path, login, password):
        self.db.c.execute('''UPDATE updates SET name=?, path=?,login=?,password=? WHERE ID=?''',
                          (name,path,login,password, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM updates''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM updates WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, name):
        name = ('%' + name + '%',)
        self.db.c.execute('''SELECT * FROM updates WHERE name LIKE ?''', name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
#########################################
#########################################
#########################################

    def start_programm(self):
        battle= 'battlenet'
        print(self.mass)
        x=0
        name = ('%' + battle + '%',)
        self.db.c.execute('''SELECT * FROM updates ''')

        for rew in self.db.c.fetchall():
            self.mass.insert(x,rew)
            x=x+1
            print(self.mass[0][1])
        print(self.mass)
        print("ХУЙ")
        scriptStart.q(self.mass)
#########################################
# #########################################
# #########################################        
   

# #########################################  



    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить путь')
        self.geometry('400x420+400+300')
        self.resizable(False, False)

        label_name = tk.Label(self, text='Название:')
        label_name.place(x=50, y=50)
        
        label_path = tk.Label(self, text='Путь:')
        label_path.place(x=50, y=110)

        label_login = tk.Label(self, text='логин:')
        label_login.place(x=50, y=170)

        label_password = tk.Label(self, text='пароль:')
        label_password.place(x=50, y=230)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)

        self.entry_path = ttk.Entry(self)
        self.entry_path.place(x=200, y=110)

        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x=200, y=170)

        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x=200, y=230)


        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=290)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=290)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(),
                                                                       self.entry_path.get(), self.entry_login.get(), self.entry_password.get()    ))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать путь')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=290)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_name.get(),
                                                                          self.entry_path.get(),
                                                                          self.entry_login.get(), self.entry_password.get()))

        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM updates WHERE id=?''', (self.view.tree.set(self.view.tree.selection()[0], '#1' ),))
        row = self.db.c.fetchone()
        self.entry_name.insert(0, row[1])
        if row[2] != 'Доход':
            self.combobox.current(1)
        self.entry_path.insert(0, row[3])
        

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('updates.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS updates(id integer primary key, name text, path text,login text, password text)''')
        self.conn.commit()

    def insert_data(self, name,  path, login, password):
        self.c.execute('''INSERT INTO updates(name,  path, login, password) VALUES (?, ?, ?, ?)''',
                       (name,  path, login, password))
        self.conn.commit()
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

if __name__ == "__main__":
    root=tk.Tk()## создает корневое окно программы
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Update")
    root.geometry("1450x750+100+50")
    root.resizable(False,False)
    root.mainloop()

##############################################################################################








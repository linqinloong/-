import tkinter as tk
from tkinter import messagebox
class verification_window(tk.Frame):
    def __init__(self):
        global root
        root = tk.Tk()
        root.geometry('150x150+885+465')
        root.resizable(0,0)
        super().__init__()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.pack()
        self.main_window()
        root.mainloop()
    def main_window(self):
        global root
        username_label = tk.Label(root,text='Username',font=('Aral',12)).place(x=32,y=10)
        username_input = tk.StringVar
        username_entry = tk.Entry(root,textvariable=self.username).place(x=2,y=35)
        password_input = tk.StringVar
        password_entry = tk.Entry(root,textvariable=self.password,show='*').place(x=2,y=85)
        conformation_button = tk.Button(root,text='CONFIRH',command=self.verification,fg='white',bg='black',activeforeground='white',activebackground='navy',width=8,height=1)
        conformation_button.place(x=6,y=112)
        quit_button = tk.Button(root,text='QUIT',command=root.quit,fg='white',bg='black',activeforeground='white',activebackground='red',width=8,height=1)
        quit_button.place(x=78,y=112)
    def verification(self):
        global root
        user_dict = {'admin':'123456','123456':'admin'}
        if user_dict.get(self.username.get()) == self.password.get():
            messagebox.showinfo(title='Correct',message=f'{self.username.get()},welcame')
            root.withdarm();
        else:
            messagebox.showerror(title='wrong inputs',message='Please enter correct username or password.')
if __name__ == "__main__":
    verification_window()
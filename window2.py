from tkinter import *

prog = Tk()
prog.title('My first window')
prog.geometry('900x600+500+100')  # 900x600 розмір вікна +500+100 + 500 по координаті х і +100 по координаті у
prog.minsize(500, 400)  # встановлення мінімуму для звуження вікна
prog.maxsize(1000, 800)
prog.config(bg='greenYellow')  # Колір
prog.wm_attributes("-alpha", 0.8)  # прозорість
prog.iconbitmap('C:/Users/Admin/Desktop/MY_PROGS/requestPrivat/dog.ico')  # шлях до іконки формат ico



def work():
    name = login.get()
    password1 = int(password.get())
    if name =='abc' and password1 == 123:
       server.config(text="Hello",bg='yellow')
    else:
        server.config(text="Retry please",bg='red')
    login.delete(0, END)  # очистить поле вводу
    login.focus()  # поверне кур
    password.delete(0, END)  # очистить поле вводу
    password.focus()  # поверне кур


def work2():
    log = login.get()
    pas = password.get()
    if log == '' or pas == '':
        server.config(text="Retry please", bg='red')
    else:
        server.config(text='You login is ' + log + '\nyou password is ' + pas, bg='greenYellow')


user_name = Label(prog, bg='sky blue', fg='white', font=('Comic Sanc MS', 15, 'bold'), text='Логін Користувача:', padx=20, anchor=E, )

user_login = Label(prog, bg='sky blue', fg='white', font=('Comic Sanc MS', 15, 'bold'), text='Пароль:', padx=20,anchor=E )


login = Entry(prog, font=('Comic Sanc MS', 15, 'bold'))
password = Entry(prog, font=('Comic Sanc MS', 15, 'bold'), show='*') # show='-' скриває пароль


ent_exit = Button(prog, text='Вхід', fg="black", font=('Comic Sanc MS', 15, 'bold'),command=work2 )

server = Label(prog, bg='green', fg='white', font=('Comic Sanc MS', 22, 'bold'),
                  text='SERVER\n - вкажіть персональні данні\n для аутендифікації:', padx=20, relief=GROOVE,
               bd=10 )

user_name.place(x=200,y=100,width=220,height=30)
user_login.place(x=200,y=140,width=220,height=30)
login.place(x=430,y=100,width=220,height=30)
password.place(x=430,y=140,width=220,height=30)
ent_exit.place(x=320,y=180,width=220,height=30)
server.place(x=200,y=350, width=450,height=150)










prog.mainloop()
from tkinter import *

prog = Tk()
prog.title('My first window')
prog.geometry('900x600+500+100')  # 900x600 розмір вікна +500+100 + 500 по координаті х і +100 по координаті у
prog.minsize(500, 400)  # встановлення мінімуму для звуження вікна
prog.maxsize(1000, 800)
# prog.resizable(width=False, height=False) # заборона зміни вікна
# print('Hello')
prog.config(bg='greenYellow')  # Колір
prog.wm_attributes("-alpha", 0.8)  # прозорість
prog.iconbitmap('C:/Users/Admin/Desktop/MY_PROGS/requestPrivat/dog.ico')  # шлях до іконки формат ico
# photo=PhotoImage('C:/Users/Admin/Desktop/MY_PROGS/requestPrivat/south.png') # для формату png
# prog.iconphoto(False,photo)

user_name = Label(prog, bg='sky blue', fg='white', font=('Comic Sanc MS', 15, 'bold'), text='Логін Користувача:', padx=20, anchor=E, )
user_name.place(x=150,y=100,width=220,height=30)
user_login = Label(prog, bg='sky blue', fg='white', font=('Comic Sanc MS', 15, 'bold'), text='Пароль:', padx=20,anchor=E )
user_login.place(x=150,y=140,width=220,height=30)



login = Entry(prog, font=('Comic Sanc MS', 15, 'bold'))
password = Entry(prog, font=('Comic Sanc MS', 15, 'bold'))
login.place(x=380,y=100,width=220,height=30)
password.place(x=380,y=140,width=220,height=30)

ent_exit = Button(prog, text='Вхід', fg="black", font=('Comic Sanc MS', 15, 'bold') )
ent_exit.place(x=270,y=180,width=220,height=30)





def word():
    return "YO!!!!"


gl_text = Label(prog,
                text="Hello from Bandera",  # текст у вікні
                bg='greenYellow',  # залівка
                fg="black",  # колір самого тексту
                font=('Comic Sanc MS', 20, 'bold', 'italic', 'underline'),  # сам текст шрифт, величина, жирність...
                relief=RAISED,  # рамка
                bd=10,  # пікселі рамки
                # width = 20,
                # height= 2,
                justify=CENTER,  # теуст по центру
                # anchor=W,
                padx=50,
                pady=20

                )

gl_text.place(x=280, y=300, width=300, height=100)  # задаемо розташування тексту

but_1 = Button(prog,
               text="Kill ork",  # текст у вікні
               bg='red',  # залівка
               fg="black",  # колір самого тексту
               font=('Comic Sanc MS', 10),  # сам текст шрифт, величина, жирність...
               relief=RAISED,  # рамка
               bd=10,  # пікселі рамки
               # прописуємо команди для кнопки(змінить текст напису і колір і шрифт)
               command=lambda: gl_text.config(
                   text="orks must die", bg="sky blue", fg="dark blue", font=('Comic Sanc MS', 30) )
               )

but_1.place(x=180, y=450, width=200, height=50)

but_2 = Button(prog,
               text="Dectrow orks",  # текст у вікні
               bg='red',  # залівка
               fg="black",  # колір самого тексту
               font=('Comic Sanc MS', 10),  # сам текст шрифт, величина, жирність...
               relief=RAISED,  # рамка
               bd=10,  # пікселі рамки
               command=lambda: gl_text.config(
                   text=word(), bg="yellow", fg="blue", font=('Comic Sanc MS', 30) )
               )

but_2.place(x=480, y=450, width=200, height=50)



prog.mainloop()

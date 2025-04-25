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

gl_text.place(x=280, y=250, width=300, height=100)  # задаемо розташування тексту

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

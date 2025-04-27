from tkinter import *

from test_buttons import button

prog = Tk()
prog.title('Calculator window')
prog.geometry('400x300+1100+400')  # 900x600 розмір вікна +500+100 + 500 по координаті х і +100 по координаті у
#prog.minsize(500, 400)  # встановлення мінімуму для звуження вікна
#prog.maxsize(1000, 800)
prog.config(bg='greenYellow', padx=40, pady=20)  # Колір
prog.wm_attributes("-alpha", 0.8)  # прозорість


def kalc():
    return '5'


for i in range(8):
    prog.grid_columnconfigure(i, minsize=80) # для всіх кнопок завдали size

pole = Entry(prog, font=("Arial",16) )

button_1 = Button(prog, font=("Arial",20),text="+",command=lambda:kalc('+')).grid(column=0,row=1,stick = "we")
button_2 = Button(prog, font=("Arial",20),text="-",command=lambda:kalc('-')).grid(column=1,row=1,stick = "we")
button_3 = Button(prog, font=("Arial",20),text="*",command=lambda:kalc('*')).grid(column=2,row=1,stick = "we")
button_4 = Button(prog, font=("Arial",20),text="/",command=lambda:kalc('/')).grid(column=3,row=1,stick = "we")

button_5 = Button(prog, font=("Arial",20),text="1",command=lambda :kalc('1')).grid(column=0,row=2,stick = "we")
button_6 = Button(prog, font=("Arial",20),text="2",command=lambda :kalc('2')).grid(column=1,row=2,stick = "we")
button_7 = Button(prog, font=("Arial",20),text="3",command=lambda :kalc('3')).grid(column=2,row=2,stick = "we")
button_8 = Button(prog, font=("Arial",20),text="CE",command=lambda :kalc('CE')).grid(column=3,row=2,stick = "we")

button_5 = Button(prog, font=("Arial",20),text="4",command=lambda :kalc('4')).grid(column=0,row=3,stick = "we")
button_6 = Button(prog, font=("Arial",20),text="5",command=lambda :kalc('5')).grid(column=1,row=3,stick = "we")
button_7 = Button(prog, font=("Arial",20),text="6",command=lambda :kalc('6')).grid(column=2,row=3,stick = "we")
button_8 = Button(prog, font=("Arial",20),text="<-",command=lambda :kalc('<-')).grid(column=3,row=3,stick = "we")

button_5 = Button(prog, font=("Arial",20),text="7",command=lambda :kalc('7')).grid(column=0,row=4,stick = "we")
button_6 = Button(prog, font=("Arial",20),text="8",command=lambda :kalc('8')).grid(column=1,row=4,stick = "we")
button_7 = Button(prog, font=("Arial",20),text="9",command=lambda :kalc('9')).grid(column=2,row=4,stick = "we")
button_8 = Button(prog, font=("Arial",20),text="=",command=lambda :kalc('=')).grid(column=3,row=4,stick = "we")

pole.grid(column=0, row=0,columnspan=4,stick = "we")








#name = Label(prog, text='Name', font=("Arial",16))
#text_name = Entry(prog, font=("Arial",16))
#send = Button(prog, text='Send mail', font=("Arial",16))

#prog.grid_columnconfigure(0,minsize=100) #  конфігурація колонки

# сітка задаємо стовпи
#name.grid(column=0, row=0,stick = "we") # сітка задаємо стовпи, stick = "we" ніби розширення кнопки на весь стовпець
#text_name.grid(column=1, row=0)
#send.grid(column=0, row=2, stick = "we", columnspan=2) # columnspan=2 розтягуваня на два стовпчика вправо



prog.mainloop()
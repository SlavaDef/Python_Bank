from tkinter import *



prog = Tk()
prog.title('Calculator window')
prog.geometry('400x400+1100+400')  # 900x600 розмір вікна +500+100 + 500 по координаті х і +100 по координаті у
#prog.minsize(500, 400)  # встановлення мінімуму для звуження вікна
#prog.maxsize(1000, 800)
prog.config(bg='greenYellow', padx=40, pady=45)  # Колір
prog.wm_attributes("-alpha", 0.8)  # прозорість


def do_operation(sym):
    b = pole.get() # у змінну записуємо що в полі
    pole.delete(0,END) # видаляємо все
    if sym == '/' and b[-1] == '0' and len(b)==1:
        pole.insert(0,'на нуль ділити не можна')
    elif sym == "=":
        if '/' in b and b[-1] == '0' and len(b)==1:
            pole.insert(0,'на нуль ділити не можна')
        else:
            pole.insert(0, str(eval(b))) # просто повертаємо результат бо не на 0 ділимо
    else: # eval функція аналізує чи є у виразі +-*/ виконує дію і повертає результат
        pole.insert(0, str(eval(b))+sym)




def kalc(symbol):
   if symbol=='CE':
       pole.delete(0,END) # видаляємо все від початку до кінця
       pole.insert(0, '0') # вставка нуля на початку, при запуску

   elif symbol == '<=':
       pole.delete(len(pole.get())-1) # видаляємо останній символ
       if pole.get()=='' :
           pole.insert(0, '0')

   elif symbol == '.':    # and pole.get().count('.')==0:
       pole.insert(END, '.')


   elif symbol in '+-*/': # якщо символ в переліку
       s = pole.get()
       if s[-1 ] in '+-*/': # якщо останній символ в переліку
           s = s[0:-1]+symbol # зріз від початку до кінця не включно + цей символ
           pole.delete(0, END)
           pole.insert(0, s)

       elif ('+' in s) or ('-' in s) or ('*' in s) or ('/' in s):
           do_operation(symbol)

       else:
           s= s+symbol
           pole.delete(0, END)
           pole.insert(0, s)

   elif symbol == "=":
       k = pole.get()
       if k[-1 ] in '+-*/':
           ch = k[0:-1] # окремо записали все крім останнього знаку
           k = k+ch # формуємо новечисло без знаку
           pole.delete(0, END) # чистимо поле
           pole.insert(0, str(eval(k)))
       else:
           do_operation(symbol)

   else:
        if pole.get() == '0':pole.delete(0,END) # видалення 0 на початку

        if symbol in '0123456789': # якщо символ є в переліку то відображаємо його
              pole.insert(END,symbol) # insert вставить щось у поле, відображае вводимі значення


for i in range(15):
    prog.grid_columnconfigure(i, minsize=80) # для всіх кнопок завдали size

pole = Entry(prog, font=("Arial",16), justify=RIGHT )
pole.insert(0,'0')

button_1 = Button(prog, font=("Arial",20),text='+',command=lambda:kalc('+')).grid(column=0,row=1,stick = 'we')
button_2 = Button(prog, font=("Arial",20),text='-',command=lambda:kalc('-')).grid(column=1,row=1,stick = 'we')
button_3 = Button(prog, font=("Arial",20),text='*',command=lambda:kalc('*')).grid(column=2,row=1,stick = 'we')
button_4 = Button(prog, font=("Arial",20),text='/',command=lambda:kalc('/')).grid(column=3,row=1,stick = 'we')

button_5 = Button(prog, font=("Arial",20),text='1',command=lambda :kalc('1')).grid(column=0,row=2,stick = 'we')
button_6 = Button(prog, font=("Arial",20),text='2',command=lambda :kalc('2')).grid(column=1,row=2,stick = 'we')
button_7 = Button(prog, font=("Arial",20),text='3',command=lambda :kalc('3')).grid(column=2,row=2,stick = 'we')
button_8 = Button(prog, font=("Arial",20),text='CE',command=lambda :kalc('CE')).grid(column=3,row=2,stick = 'we')

button_6 = Button(prog, font=("Arial",20),text='4',command=lambda :kalc('4')).grid(column=0,row=3,stick = 'we')
button_7 = Button(prog, font=("Arial",20),text='5',command=lambda :kalc('5')).grid(column=1,row=3,stick = 'we')
button_8 = Button(prog, font=("Arial",20),text='6',command=lambda :kalc('6')).grid(column=2,row=3,stick = 'we')
button_9 = Button(prog, font=("Arial",20),text='<=',command=lambda :kalc('<=')).grid(column=3,row=3,stick = 'we')

button_10 = Button(prog, font=("Arial",20),text='7',command=lambda :kalc('7')).grid(column=0,row=4,stick = 'we')
button_11 = Button(prog, font=("Arial",20),text='8',command=lambda :kalc('8')).grid(column=1,row=4,stick = 'we')
button_12 = Button(prog, font=("Arial",20),text='9',command=lambda :kalc('9')).grid(column=2,row=4,stick = 'we')
button_13 = Button(prog, font=("Arial",20),text=',',command=lambda :kalc('.')).grid(column=3,row=4,stick = 'we')

button_14 = Button(prog, font=("Arial",20),text='0',command=lambda :kalc('0')).grid(column=0,row=5,stick = 'we')
button_15 = Button(prog, font=("Arial",20),text='=',command=lambda :kalc('=')).grid(column=1,row=5,stick = 'we',columnspan=3)

pole.grid(column=0, row=0,columnspan=4,stick = 'we')








#name = Label(prog, text='Name', font=("Arial",16))
#text_name = Entry(prog, font=("Arial",16))
#send = Button(prog, text='Send mail', font=("Arial",16))

#prog.grid_columnconfigure(0,minsize=100) #  конфігурація колонки

# сітка задаємо стовпи
#name.grid(column=0, row=0,stick = "we") # сітка задаємо стовпи, stick = "we" ніби розширення кнопки на весь стовпець
#text_name.grid(column=1, row=0)
#send.grid(column=0, row=2, stick = "we", columnspan=2) # columnspan=2 розтягуваня на два стовпчика вправо



prog.mainloop()
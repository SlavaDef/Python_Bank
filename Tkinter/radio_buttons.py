from tkinter import *
from tkinter.messagebox import showinfo

window = Tk()
window.title('Radio_button_window')
window.geometry('500x700+1000+300')  # 900x600 розмір вікна +500+100 + 500 по координаті х і +100 по координаті у
window.config(bg='aqua', padx=40, pady=45)  # Колір   bg='aqua'
window.wm_attributes("-alpha", 0.8)  # прозорість
img_1 = PhotoImage(file='photo/red_30.png')
img_2 = PhotoImage(file='photo/green_30.png')
img_3 = PhotoImage(file='photo/yellow_30.png')


def test():
    ball = 0
    if answer_1.get()==1 : ball+=2
    if answer_2.get() == 1: ball += 2
    if answer_1.get() == 2: ball += 4
    if answer_2.get() == 2: ball += 4
    if answer_1.get()==3 : ball+=6
    if answer_2.get()==3 : ball+=6
    showinfo('Difficulty is ',  str(ball))
    difficulty.config(state=DISABLED) # ніби вимкнення кнопки після спрацювання



items_1 = Label(window, text="Сhoose your level", font=('Arial', 18), bg='yellow')
items_1.place(x=10,y=20, width=440)

answer_1 = IntVar() # змінна для відповідей радіо кнопок
answer_2 = IntVar()

# у кожної кнопки свій value
# indicatoron=0 - вимкнення кружечку у кнопці (тепер вибраний варіант просто виділяється)
# image підгрузка зображення
# compound='right' вирівнювання зображення по якомусь із країв
# padx=10 відступ від границь, що картинки, що тексту
# selectcolor='yellow' вибір кольора вибору у кружечку

res_1 = Radiobutton(window, text='Easy', font=('Arial', 14), anchor='w',
                    value=1, variable=answer_1, indicatoron=0, image=img_3,compound='left', padx=10)
res_1.place(x=40,y=70, width=250)

res_2 = Radiobutton(window, text=' Middle', font=('Arial', 14), anchor='w',
                    value=2, variable=answer_1, indicatoron=0, image=img_2, compound='left', padx=10)
res_2.place(x=40,y=120, width=250)

res_3 = Radiobutton(window, text=' Hard', font=('Arial', 14), anchor='w',
                    value=3, variable=answer_1, indicatoron=0, image=img_1, compound='left', padx=10)
res_3.place(x=40,y=170, width=250)


items_2 = Label(window, text="Are your sure", font=('Arial', 18), bg='yellow')
items_2.place(x=10,y=250, width=440)


res_4 = Radiobutton(window, text='Easy', font=('Arial', 14), anchor='w', value=1, variable=answer_2, selectcolor='yellow')
res_4.place(x=40,y=300, width=250)

res_5 = Radiobutton(window, text='Middle', font=('Arial', 14), anchor='w', value=2, variable=answer_2, selectcolor='green')
res_5.place(x=40,y=350, width=250)

res_6 = Radiobutton(window, text='Hard', font=('Arial', 14), anchor='w', value=3, variable=answer_2, selectcolor='red')
res_6.place(x=40,y=400, width=250)

difficulty = Button(window, text='Difficulty', font=('Arial', 14), bg='greenYellow', command=test, state=NORMAL )
difficulty.place(x=10,y=500, width=410)


window.mainloop()
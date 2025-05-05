from tkinter import *
import json
from Constants.constants import FILENAME
#from tkinter import PhotoImage
from PIL import Image, ImageTk  # 👈 імпортуємо через Pillow


def load_file():
    try:
        with open(FILENAME, "r") as f:
            bankin = json.load(f)
    except (FileNotFoundError,
            json.JSONDecodeError):  # якщо файлу немає чи помилка читання загрузиться дефолтний словник
        bankin = {'USD': 500, 'EUR': 500, 'GBP': 500, 'UAN': 500}

    return bankin


bank = load_file()


def save_file():
    with open(FILENAME, "w") as f:
        json.dump(bank, f)  # Збереження


def add_currency(currency2, summa):
    bank[currency2] = summa
    return summa


def on_button_click(currency2):
    summa = entry.get()  # беремо значення з поля вводу
    if summa.strip():  # перевіряємо, що щось введено
        try:
            result = add_currency(currency2, float(summa))  # конвертуємо в число
            gl_text2.config(text=result, bg="yellow", fg="black", font=('Comic Sanc MS', 10))
        except ValueError:
            gl_text2.config(text="Введіть число!", bg="orange", fg="black")
    else:
        gl_text2.config(text="Поле пусте", bg="red", fg="white")
    entry.delete(0, END)  # очистить поле вводу
    entry.focus()  # поверне курсор для вводу
    return bank


prog = Tk()
prog.title('My_banking_window')
prog.geometry('900x600+500+100')  # 900x600 розмір вікна +500+100 + 500 по координаті х і +100 по координаті у
prog.config(bg='greenYellow')  # Колір
prog.wm_attributes("-alpha", 0.8)  # прозорість

entry = Entry(prog, font=('Comic Sanc MS', 12), bg='yellow')
entry.place(x=330, y=350, width=200, height=30)


# Список валют
currencies = ["USD", "EUR", "GBP", "UAN"]

# Автоматичне створення кнопок
start_x = 50  # початкова координата по y


# Завантажуємо картинку через Pillow
image = Image.open("../egs.png")
img = ImageTk.PhotoImage(image)

gl_text = Label(prog,
                text='Ваш початковий баланс',  # текст у вікні
                bg='yellow',  # залівка
                fg="black",  # колір самого тексту
                font=('Comic Sanc MS', 10, 'bold'),
                relief=RAISED,  # рамка
                bd=10,  # пікселі рамки
                width=20,
                height=4
                )



gl_text2 = Label(prog,
                 text=bank,  # текст у вікні
                 bg='yellow',  # залівка
                 fg="black",  # колір самого тексту
                 font=('Comic Sanc MS', 10, 'bold'),
                 relief=RAISED,  # рамка
                 bd=10,  # пікселі рамки
                 width=50,
                 height=4
                 )




#for currency in currencies:
button = Button(prog,
                     text=f"Add {'USD'}",  # текст у вікні
                     #bg=img,  #залівка
                     image=img,
                     fg="black",  # колір самого тексту
                     font=('Comic Sanc MS', 10),  # сам текст шрифт, величина, жирність...
                     #relief=RAISED,
                     bd=10,
                     command=lambda: (gl_text2.config(
                         text=on_button_click('USD'), bg="yellow", fg="black", font=('Comic Sanc MS', 10, 'bold')),
                                      gl_text.config(
                                          text="New balance", bg="yellow", fg="black", font=('Comic Sanc MS', 10, 'bold'))
                     )
                     )

button.place(x=start_x, y=150, width=200, height=80)
start_x += 200  # наступна кнопка буде лівіше на 200 пікселів

but_save = Button(prog,
                  text="Save_balanсe",  # текст у вікні
                  bg='sky blue',  # залівка
                  fg="black",  # колір самого тексту
                  font=('Comic Sanc MS', 10),  # сам текст шрифт, величина, жирність...
                  relief=RAISED,
                  bd=5,
                  command=save_file)


gl_text.place(x=10, y=10)  # задаемо розташування тексту
gl_text2.place(x=350, y=10)


but_save.place(x=550, y=550, width=100, height=30)

prog.mainloop()

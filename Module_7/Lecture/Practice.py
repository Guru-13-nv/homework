import tkinter
import os
from tkinter import filedialog #импортируем функцию filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(("Текстовые файлы", ".txt"),
                                                     ("Все файлы", "*")))
    text['text'] = text['text'] + "" + filename #
    os.startfile(filename) #Вызов функции для открытия файла из модуля os

window = tkinter.Tk()
window.title("Проводник")
window.geometry("350x150")
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', width=65, height=5, background='silver',
                     foreground='blue')
text.grid(row=1, column=1) #Расположение кнопки в 1 столбце и 1 строке
button_select = tkinter.Button(window, text='Выберете файл', width=20, height=3,
                               background='silver', foreground='blue',
                               command=file_select)
button_select.grid(row=2, column=1, pady=10) #Расположение кнопки в 1 столбце и 2 строке
window.mainloop()  # Обновление окна. Ставится в конец

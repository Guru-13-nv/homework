# Лекция 5
import os

print('Текущая директория: ', os.getcwd()) # получение текущей директории
if os.path.exists('second_dir'): # проверка на существование директории
    os.chdir('second_dir') # изменение текущей директории
else:
    os.mkdir('second_dir') # создание директории
    os.chdir('second_dir') # изменение текущей директории
print('Текущая директория: ', os.getcwd()) # Вывод текущей директории
print(os.listdir()) # список файлов и папок в текущей директории
for i in os.walk('.'):  # перебор всех папок и файлов в текущей директории
    print(i) # вывод всех папок и файлов в текущей директории
#Сортировка содержимого
os.chdir(r'D:\Maxim\Документы\Urban University\Project Python\homework\Module_7') # изменение текущей директории
print(os.listdir()) # список файлов и папок в текущей директории
print('Текущая директория: ', os.getcwd()) # Вывод текущей директории
file = [f for f in os.listdir() if os.path.isfile(f)] # список файлов в текущей директории
dirs = [d for d in os.listdir() if os.path.isdir(d)] # список папок в текущей директории
print(dirs)
print(file)
print(os.stat(file[3]).st_size) # вывод информации о файле st.size - размер файла
os.system('pip install random2') # установка пакета pip и random2
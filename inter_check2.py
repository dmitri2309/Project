import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
from PIL import Image
import numpy as np

window = tk.Tk()
window.title('Подбор анилокса')

window.geometry("500x250")

frame = Frame(window, padx=10, pady=10)
frame.pack(fill=BOTH, expand=True)

# Создание выпадающего списка для выбора директории
directory_lbl = Label(frame, text="Выберите линиатуру анилокса:")
directory_lbl.grid(row=2, column=1)


#current_directory = os.getcwd() # Получаем текущую директорию
current_directory =  'C:\\Users\\kerzhid\\PycharmProjects\\Anilox_check\\Anilox_checkout\\Aniloxes' # Получаем текущую директорию
directory_options = []
for dirname in os.listdir(current_directory):
    fullpath = os.path.join(current_directory, dirname)
    if os.path.isdir(fullpath):
        directory_options.append(fullpath)
        #directory_options.append(dirname)


directory_var = StringVar()
directory_combobox = Combobox(frame, textvariable=directory_var, state="readonly")
directory_combobox["values"] = directory_options
#directory_combobox.current(0)
directory_combobox.grid(row=2, column=2, padx=5, pady=5)

# Создание выпадающего списка для выбора файла
file_lbl = Label(frame, text="Выберите номер анилокса:")
file_lbl.grid(row=3, column=1)

file_options = []

# Глобальная переменная для выпадающего списка файлов
file_combobox = None

# Определение функции update_file_options
def update_file_options(directory):
    global file_combobox  # Объявление file_combobox как глобальной переменной
    file_options.clear()
    dsg_file_options.clear()
    for file in os.listdir(directory):
        if file.endswith(".png") or file.endswith(".xls"):
            # if 'anilox' in file:
            file_options.append(file)
            file_combobox["values"] = file_options
            file_combobox.current(0)
            # else:
            #     dsg_file_options.append(file)
            #     dsg_file_combobox["values"] = dsg_file_options
            #     dsg_file_combobox.current(0)

# Обновление элементов выпадающего списка файлов при изменении выбранной директории
def directory_combobox_changed(event):
    #update_file_options('C:\\Users\\kerzhid\\PycharmProjects\\Anilox_check\\Anilox_checkout')
    selected_directory = directory_var.get()
    #selection = combobox.get()
    update_file_options(selected_directory)

directory_combobox.bind('<<ComboboxSelected>>', directory_combobox_changed)

# Заполнение списка элементов выпадающего списка файлов
if len(file_options) > 0:
    file_combobox.current(0)

# Инициализация выпадающего списка файлов
file_var = StringVar()
file_combobox = Combobox(frame, textvariable=file_var, state="readonly")
file_combobox["values"] = file_options
#file_combobox.current(0)
file_combobox.grid(row=3, column=2, padx=5, pady=5)

#Выбор способа оценки пересечения дефектоа анилокса и печати
method_lbl = Label(frame, text="Выберите способ подбора анилокса")
method_lbl.grid(row=1, column=1)

method_options = ['Ручной подбор', 'Автоматический подбор']

method_var = StringVar()
method_combobox = Combobox(frame, textvariable=method_var, state="readonly")
method_combobox["values"] = method_options
#directory_combobox.current(0)
method_combobox.grid(row=1, column=2, padx=5, pady=5)

#Создание выпадающего списка для выбора директории номера дизайна
dsg_directory_lbl = Label(frame, text="Выберите номер дизайна:")
dsg_directory_lbl.grid(row=4, column=1)


#current_directory = os.getcwd() # Получаем текущую директорию
dsg_current_directory =  'C:\\Users\\kerzhid\\PycharmProjects\\Anilox_check\\Anilox_checkout\\Designs' # Получаем текущую директорию
dsg_directory_options = []
for dirname in os.listdir(dsg_current_directory):
    fullpath = os.path.join(dsg_current_directory, dirname)
    if os.path.isdir(fullpath):
        dsg_directory_options.append(fullpath)
        #directory_options.append(dirname)


dsg_directory_var = StringVar()
dsg_directory_combobox = Combobox(frame, textvariable=dsg_directory_var, state="readonly")
dsg_directory_combobox["values"] = dsg_directory_options
#directory_combobox.current(0)
dsg_directory_combobox.grid(row=4, column=2, padx=5, pady=5)



# Создание выпадающего списка для выбора файла
dsg_file_lbl = Label(frame, text="Выберите цвет:")
dsg_file_lbl.grid(row=5, column=1)

dsg_file_options = []

# Глобальная переменная для выпадающего списка файлов
dsg_file_combobox = None

#Определение функции update_file_options
def dsg_update_file_options(directory):
    global dsg_file_combobox  # Объявление file_combobox как глобальной переменной
    dsg_file_options.clear()
    for file in os.listdir(directory):
        if file.endswith(".png") or file.endswith(".jpg"):
            dsg_file_options.append(file)
    dsg_file_combobox["values"] = dsg_file_options
    dsg_file_combobox.current(0)

# Обновление элементов выпадающего списка файлов при изменении выбранной директории
def dsg_directory_combobox_changed(event):
    #update_file_options('C:\\Users\\kerzhid\\PycharmProjects\\Anilox_check\\Anilox_checkout')
    selected_directory = dsg_directory_var.get()
    #selection = combobox.get()
    dsg_update_file_options(selected_directory)

dsg_directory_combobox.bind('<<ComboboxSelected>>', dsg_directory_combobox_changed)

# Заполнение списка элементов выпадающего списка файлов
if len(dsg_file_options) > 0:
    dsg_file_combobox.current(0)

# Инициализация выпадающего списка файлов
dsg_file_var = StringVar()
dsg_file_combobox = Combobox(frame, textvariable=dsg_file_var, state="readonly")
dsg_file_combobox["values"] = dsg_file_options
#file_combobox.current(0)
dsg_file_combobox.grid(row=5, column=2, padx=5, pady=5)

print(directory_options)
print(dsg_directory_options)

# Часть программы сравнения анилокса и дизайна
def anlx_dsg(anlx_dir, repl_dsg_nr):
    anilox_list = []
    with Image.open(repl_dsg_nr) as img1:
        img1.load()
    for root, dirs, files in os.walk(anlx_dir):
        for file in files:
            path = os.path.join(root, file)
            #print("Opening image: {}".format(path))
            try:
                with Image.open(path) as img2:
                    img2.load()
                # with Image.open(repl_dsg_nr) as design:
                #     design.load()
                new_width = img2.size[0]
                new_height = img1.size[1]
                new_size = (new_width, new_height)
                img_new = Image.new('L', new_size)
                img_new.paste(img1, (870, 0))
                img2_new = img2.resize(img_new.size)

                img_new.convert('L')
                img2_new.convert('L')

                dsg_array = np.array(img_new, dtype=np.uint8)
                # dsg_array[dsg_array != 0] = 255
                anlx_array = np.array(img2_new, dtype=np.uint8)
                # anlx_array[anlx_array != 0] = 255

                diff_array = anlx_array + dsg_array
                diff_array[diff_array != 0] = 255
                diff_array_sum = diff_array.sum()
                print(diff_array_sum)

                x, y = diff_array.shape
                sum_white = x * y * 255
                sum_white_fill = np.full((x, y), 255)
                print(sum_white_fill.sum())
                print(sum_white)
                print(diff_array.sum())

                if sum_white == diff_array_sum:
                    # if np.array_equal(sum_white_fill, diff_array_sum):
                    print('Нет пересечения')
                    anilox_list.append(file)
                else:
                    print('Есть пересечение')


                diff = Image.fromarray(diff_array)
                diff.show()

                diff2_array = dsg_array - anlx_array
                diff2_array[diff2_array != 0] = 255  # для получения визульного контроля пересечения
                diff2 = Image.fromarray(diff2_array)
                diff2.show()
            except OSError:
                print('Файл не является изображением') # Handle exception if needed
    return anilox_list

#создание кнопки для выполнения программы сравнения анилокса
anlx_check_btn = Button(frame, text='Проверить анилоксы',
                        command= lambda:anlx_dsg(directory_var, dsg_file_var))
anlx_check_btn.grid(row=6, column=2, padx=5, pady=5)

window.mainloop()
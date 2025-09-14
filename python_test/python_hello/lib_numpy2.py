import numpy as np

rand_num_int= np.random.randint(0, 100, size=(20), dtype=np.int32)  # Генерация случайных целых чисел от 0 до 100
print("Случайные целые числа:\n", rand_num_int)  # Вывод случайных целых чисел
lines = rand_num_int.reshape(-1, 10)  # Преобразование в двумерный массив с 10 столбцами
print("Преобразованный массив:\n", lines)  # Вывод преобразованного
np.savetxt('data.txt', lines, fmt='%d', delimiter=' ')  # Сохранение массива в файл data.txt
print("Данные сохранены в файл data.txt")  # Подтверждение сохранения данных   

#miscellaneous numpy functions
#Load data from file
filedata = np.genfromtxt('data.txt', delimiter=',')  # Загрузка данных из файла data.txt с разделителем запятой
print("Данные из файла:\n", filedata)  # Вывод загруженных данных
print("Размерность данных из файла:", filedata.shape)  # Вывод размерности загруженных данных
print("Тип данных из файла:", filedata.dtype)  # Вывод типа данных загруженных данных
print("Общая память данных из файла:", filedata.nbytes)  # Вывод общей памяти загруженных данных
filedata[filedata > 50]
# Вывод логического массива, где True для элементов больше 50
print("Элементы больше 50:\n", filedata[filedata > 50])

import numpy
print(numpy.__version__)

import numpy as np

a = np.array([1, 2, 3])
print("Массив:", a) # [1 2 3]






"""
print("Тип массива:", type(a))  # <class 'numpy.ndarray'>
print("Размерность массива:", a.ndim)  # 1D array  array.number of dimensions
print("Форма массива:", a.shape)  # (3,)

print("Тип данных массива:", a.dtype)  # int64 by default  a.data type 
print("Размер массива:", a.size)  # 3   # Number of elements
print("Байты на элемент:", a.itemsize)  # 8 bytes for int   # 64-bit integer # I can also use a.nbytes to get total bytes 
                                        # Total bytes = size * itemsize 
                                        # a=np.array([1, 2, 3], dtype='int16') # 2 bytes for int16. Item показывает сколько байтов занимает каждый элемент
print("Общая память массива:", a.nbytes)  # 24 bytes (3 elements * 8 bytes each)
print("Максимальное значение:", a.max())  # 3
print("Минимальное значение:", a.min())  # 1  # Сумма элементов
print("Сумма элементов:", a.sum())  # 6 # Среднее значение
print("Среднее значение:", a.mean())  # 2.0
print("Стандартное отклонение:", a.std())  # 0.816496580927726
print("Квадратный корень каждого элемента:", np.sqrt(a))  # [1. 1.41421356 1.73205081]  
print("Квадрат каждого элемента:", np.square(a))  # [1 4 9]
print("Сумма по осям:", a.sum(axis=0))  # Сумма по всем элементам, т.к. 1D
print("Сумма по осям (2D):", np.array([[1, 2], [3, 4]]).sum(axis=0))  # [4 6] - Сумма по столбцам
print("Сумма по осям (2D):", np.array([[1, 2], [3, 4]]).sum(axis=1))  # [3 7] - Сумма по строкам
print("Квадратный корень от 16:", np.sqrt(16))  # 4.0
print("Квадратный корень от 25:", np.sqrt(25))  # 5.0  
print("Квадратный корень от 0:", np.sqrt(0))  # 0.0
print("Квадратный корень от -1:", np.sqrt(-1))  # RuntimeWarning: invalid value encountered in sqrt
[[1,2,3,4,5,6],[7,8,9,10,11,12]] # 2D array 
[[1  2  3   4   5   6] 
 [7  8  9  10  11  12]] 
 a[0, 1:6:2] = 2, 4, 6 # a[0, 1:6:2] = [2, 4, 6] - Срез по строке 0, столбцы с 1 по 6 с шагом 2
2 row 6 colomns - a[0, :0] = 1, a[0, 1] = 2, a[0, 2] = 3, a[1, 0] = 4, a[1, 1] = 5, a[1, 2] = 6 Выведется 1, 2, 3, 4, 5, 6 вся row. 
# all zeros array
zeros_array = np.zeros((2, 3))  # Создает массив 2x3, заполненный нулями    
# fulls array
fulls_array = np.full((2, 3), 7)  # Создает массив 2x3, заполненный 7ками.
# random array
random_array = np.random.rand(2, 3)  # Создает массив 2x3 с случайными числами от 0 до 1
#random integers array
random_integers_array = np.random.randint(0, 10, (2, 3))  # Создает массив 2x3 с случайными целыми числами от 0 до 10
# identity matrix
identity_matrix = np.eye(3)  # Создает единичную матрицу
"""

"""
random_integers_array = np.random.randint(0, 10, (2, 3))  # Создает массив 2x3 с случайными целыми числами от 0 до 10
print("Случайный массив целых чисел:\n", random_integers_array)  # Вывод случайного массива целых чисел
print("Размерность случайного массива:", random_integers_array.shape)  # Вывод размерности случайного массива
print("Тип данных случайного массива:", random_integers_array.dtype)  # Вывод типа данных случайного массива
print("Общая память случайного массива:", random_integers_array.nbytes)  # Вывод общей памяти случайного массива
print("Максимальное значение случайного массива:", random_integers_array.max())  # Вывод максимального значения случайного массива
print("Минимальное значение случайного массива:", random_integers_array.min())  #   Вывод минимального значения случайного массива
print("Сумма элементов случайного массива:", random_integers_array.sum())  # Вывод суммы элементов случайного массива
print("Среднее значение случайного массива:", random_integers_array.mean())  # Вывод среднего значения случайного массива
print("Стандартное отклонение случайного массива:", random_integers_array.std())  # Вывод стандартного отклонения случайного массива
print("Квадратный корень каждого элемента случайного массива:\n", np.sqrt(random_integers_array))  # Вывод квадратного корня каждого элемента случайного массива
print("Квадрат каждого элемента случайного массива:\n", np.square(random_integers_array))  # Вывод квадрата каждого элемента случайного массива
print("Случайный массив целых чисел:\n", random_integers_array)  # Вывод случайного массива целых чисел
print("Сумма по осям случайного массива (по столбцам):", random_integers_array.sum(axis=0))  # Сумма по столбцам
print("Сумма по осям случайного массива (по строкам):", random_integers_array.sum(axis=1))  # Сумма по строкам
print("Квадратный корень от 16:", np.sqrt(16))  # 4.0
print("Квадратный корень от 25:", np.sqrt(25))  # 5.0
print("Квадратный корень от 0:", np.sqrt(0))  # 0.
"""


output = np.ones((5,5)) # Создает массив 5x5, заполненный единицами
print("Массив единиц 5x5:\n", output)  # Вывод массива единиц 5x5

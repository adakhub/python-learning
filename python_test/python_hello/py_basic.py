x = 10
name = "Alice"
is_ready = True #   Name =! name

text = "Hello, person"
print(text[0])      #'H'
print(text.lower()) # 'hello, person'
print(text.upper()) # 'HELLO, PERSON'

# list
fruits = ["apple", "banana", "cherry"]
fruits.append("kiwi")
print(fruits[1])      # 'banana'
print(fruits[-1])     # 'kiwi'
print(fruits[0:2])   # ['apple', 'banana']
print(fruits[-2:])   # ['banana', 'cherry', 'kiwi']
print(fruits[1:3])   # ['banana', 'cherry']

# dictionary 
user = {"name": "Olga", "age": 30, "city": "New York"}
print(user["name"])  # 'Olga'
print(user.get("age")) # 30
print(user.get("country", "USA")) # 'USA' (default value if key not found)
print(user.keys())   # dict_keys(['name', 'age', 'city'])

"""
# Перебор ключей в цикле:

for key in user:
    print(key, "->", user[key])
"""

# множество SET
nums = {1, 2, 2, 3}
print(nums) # {1, 2, 3} - уникальные значения
print(2 in nums) # True

#if, esle, elif
x = 10
if x > 0 :
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
# while loop
i = 0
while i < 3:
    print(i)  # 0, 1, 2
    i += 1

# function
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))  # 'Hello, Alice!' 

"""name = "Olga"
age = 25
print(f"Меня зовут {name}, мне {age} лет.")
print("Меня зовут " + name + ", мне " + str(age) + " лет.")         #Без f
"""

# работа с файлами
with open("hello.py", "r") as file:
    content = file.read()
    print(content)  # 'Hello, World!'
# writing to a file
with open("hello.py", "w") as file:
    file.write("print('Hello, World!')\n")
#    with автоматически закрывает файл. "r" — чтение, "w" — запись, "a" — дозапись.

# importing libraries
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793

import numpy as np
print(np.array([1, 2, 3]))  # array([1, 2, 3])
print(np.arange(5))  # array([0, 1, 2, 3, 4])

import pandas as pd
data = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(data)  #    A  B  # 0  1  3  # 1  2  4

import requests
print(requests.__version__)

url = "https://jsonplaceholder.typicode.com/todos/1"
  
#response = requests.get(url)
response = requests.get(url, timeout=5) # timeout = 5 секунд ждём ответ

print("Ответ получен!")
print("Код ответа:", response.status_code)   # 200 = всё прошло успешно
print("Текст ответа:", response.text)       # выводим сырой ответ (обычно текст или JSON)
print(response.json())                       # преобразуем в словарь Python (удобно работать)
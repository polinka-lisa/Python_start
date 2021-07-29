engl = {"dog": "собака", "cat": "кошка", "monkey": "обезьяна", "mouse": "мышь"}

# print(engl["dog"])

# Методы
# print(engl.items()) #получить список пар ключ-значение
print(list(engl.items())[1])  # превращение словаря в список и обращение к определенному элементу по индексу
print(engl.values())  # получить список значений
print(engl.keys())  # получить список ключей

for key, value in engl.items():  # для всех ключей и значений в словаре
    print(key, "-", value)  # вывести все ключи и значения через тире

if "Собака" in engl.values():  # ищет слово собака в значениях словаря. Регистрозависимо.
    print("Нашлось")
else:
    print("Нет такого слова")
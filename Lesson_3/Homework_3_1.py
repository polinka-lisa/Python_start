string1 = 'Съешь ещё этих мягких французских булок ДА выпей же чаю'
print(string1.split()) #вывод строки с разбивкой на отдельные слова

string1 = string1.upper() #все буквы в строке переводятся в верхний регистр
print(string1.split()[3]) #вывод четвёртого слова в строке

string1 = string1.lower() #все буквы в строке переводятся в нижний регистр
print(string1.split()[6]) #вывод седьмого слова в строке

print(string1.split()[7][2]) #вывод 3 буквы 8 слова

for i in string1.split(): #для всех элементов строки (разбтитой по словам)
    print(i) #вывести элементы










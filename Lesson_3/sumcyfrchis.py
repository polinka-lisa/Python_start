user_num = input("Введите число: ")
summa = 0
for i in user_num: #цикл обращается к каждому символу строки user_num
    summa = summa + int(i) #к каждому предыдущему значению суммы цикл прибавляет следующий символ по счету, превращая его в целое число
print(summa) #выводит итоговое значение сумы, после того как цикл перебрал все символы в user_num
stroka = "тили-тили трали-вали"
print(stroka.index("вали")) #поиск индекса символа, указанного в скобках в заданной строке
print(stroka.replace("тили", "гали")) #а-ля "найти и заменить"
print(stroka.isalpha())
print(len(stroka))
#удобно применять длину строки для цикла
for i in range(0, len(stroka)):
    print("Символ под номером", i, "-", stroka[i])




speech_1 = ['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,', 'Вместе с тем,', 'С другой стороны,']
speech_2 = ['парадигма цифровой экономики', 'контекст геймификации', 'дижитализация бизнес-процессов', 'прагматичный подход к облачным платформам', 'совокупность сквозных технологий', 'программа прорывных исследований', 'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data']
speech_3 = ['открывает новые возможности для', 'выдвигает новые требования', 'несет в себе риски', 'расширяет горизонты', 'заставляет искать варианты', 'не оставляет шанса для', 'повышает вероятность', 'обостряет проблему']
speech_4 = ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта', 'компроментации конфиденциальных', 'несанкционированной кастомизации', 'нормативного регулирования', 'практического применения', 'практического применения']
speech_5 = ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных экспериментов.', 'государственно-частных партнеров.', 'цифровых следов граждан.', 'нежелательных последствий.', 'случайных открытий.']

from random import randint
count = 0
text = []

while count != 10:
    x = [randint(0, 7)]
    for i in x:
        a = speech_1[i]
        text.append(a)
    x = [randint(0, 7)]
    for i in x:
        b = speech_2[i]
        text.append(b)
    x = [randint(0, 7)]
    for i in x:
        c = speech_3[i]
        text.append(c)
    x = [randint(0, 6)]
    for i in x:
        d = speech_4[i]
        text.append(d)
    x = [randint(0, 7)]
    for i in x:
        e = speech_5[i]
        text.append(e)
    count = count + 1
print("Текст:")
for elem in range(0, 50):
        print(text[elem], end=' ')


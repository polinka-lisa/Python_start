depozit = 10000 # присваиваем значение переменной депозита

print("Приветствуем тебя в нашем виртуальном казино! " #приветствие пользователя
      "Тебе обязательно повезёт!"
      "Сумма твоего депозита: ", depozit)

while depozit != 0: #устанавливаем значение переменной депозита, при котором цикл перестанет работать
    a = int(input("Введи число от 2 до 12: ")) #призыв пользователя ввести число в диапазоне 2-12 + присваиваем тип данных - целое число этой цифре

    from random import randint #генератор случайных целых чисел

    b = randint(2, 12) #присвоение переменнной b значения, которое выпадет в генераторе. Диапазон генератора 2-12.
    print("На кубиках выпало: ", b) #выводим результат, выпавший на генераторе
    c = a - b #присваиваем переменной с значение разницы чисел введённого пользователем и выпавшего на генераторе
    if c == 0: #вводим условие для выполнения дальнейших действий, сравниваем переменную с с нулём. Если разница равна нулю, значит число пользователя совпадает с числом на генераторе.
        print("Вы угадали! Ваш депозит вырос на 1000 единиц!") #сообщение для пользователя о выигрыше
        depozit = depozit + 1000 #увеличение значения депозита на 1000 единиц
        print("Сумма депозита: ", depozit) #сообщение для пользователя о новом значении суммы депозита
    else: #вторая часть условия - когда значение переменной  с не равно нулю (это подразумевается по умолчанию в слове "иначе"
        print("К сожалению, Вы не угадали. Попробуйте еще раз!") #сообщение для пользователя о проигрыше
        depozit = depozit - 1000 #уменьшение значения депозита на 1000 единиц
        print("Сумма депозита: ", depozit) #сообщение для пользователя о новом значении суммы депозита

print("К сожалению, у Вас больше нет средств для игры. Пополните баланс.") #сообщение для пользователя после завершения работы цикла, когда депозит стал равен нулю.



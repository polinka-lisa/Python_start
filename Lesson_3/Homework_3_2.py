table = [] #создаём пустой список для будущей таблицы
for i in range(1, 10): #для всех значений в диапазоне от 1 до 10 применить следующие условия
    for n in range(1, 10): #для всех значений другого диапазона от 1 до 10 вычислить переменную temp
        temp = i * n #переменная temp, равная произведению значения из первого диапазона со значением из второго диапазона.
        table.append([i, n, temp]) #добавляем до конца цикла полученные значения: значение диапазона 1, значение диапазона 2, произведение значений

for i in table: #цикл для вывода значений в заданном виде. Для всех значений списка table.
    print(i[0], "*", i[1], "=", i[2]) #выводятся все значения, сохранённые ранее, в заданном виде


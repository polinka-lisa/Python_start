table = []
for i in range(1, 10):
    for n in range(1, 10):
        temp = i * n
        table.append([i, n, temp])

for i in table:
    print(i[0], "*", i[1], "=", i[2])


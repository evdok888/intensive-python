num = int(input("Для какого числа построить таблицу?  "))

for i in range(1, 11):
    result = num * i
    print(f"{num}*{i} = {result}")

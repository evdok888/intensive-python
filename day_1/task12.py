amount = int(input("Введите сумму: "))
den = [5000, 1000, 500, 100]
result = {}

for x in den:
    count = amount // x
    result[x] = count
    amount %= x

print(result)

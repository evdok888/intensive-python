num_str = input("Введите число: ")
if '.' in num_str:
    num = float(num_str)
else:
    num = int(num_str)
print(type(num))

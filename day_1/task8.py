total = int(input("Введите общ. кол-во секунд: "))

hours = total // 3600
minutes =  (total%3600) // 60
seconds = total % 60

print(f"{total} sec., = {hours} h., {minutes} min., {seconds} sec.")

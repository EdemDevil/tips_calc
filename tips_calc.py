bill = float(input("Добро пожаловать в калькулятор чаевых\nКакой был общий счёт? "))
percent = int(input("Какой процент вы бы оставили? 10, 12 или 15? "))
total_person = int(input("Как много людей разделят счёт? "))
tips = bill * (percent / 100) + 1 / total_person

print(f"Каждый человек должен заплатить {round(tips, 2)} рублей")
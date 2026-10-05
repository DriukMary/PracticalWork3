#Ask in user his sum

n = int(input("Введіть суму: "))

for banknote in [64, 32, 16, 8, 4, 2, 1]:
    quantity = n // banknote

    if quantity > 0:
        print(quantity, f"({banknote})")

    n = n % banknote

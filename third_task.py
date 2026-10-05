# Create stairs with symbols #

quantity = int(input(f"Please write quantity of stairs: "))

#Calculating and print symbols
for i in range(1, quantity + 1):
    stairs = ' ' * (quantity - i) + '#' * i
    print(stairs)

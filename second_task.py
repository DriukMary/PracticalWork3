#Calculating mistakes maken for a certain period of times


quantity = int(input(f"Please write quantity of days: "))

total_mistakes = 0

for i in range(quantity):
    numbers = int(input(f"Please write a number: "))
    total_mistakes += numbers

print(total_mistakes)


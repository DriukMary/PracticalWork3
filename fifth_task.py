n = int(input())

for num in range(10, n + 1):
    is_valid = True

    # Convert the number to a string to check if it is divisible by each of its digits
    for digit_str in str(num):
        digit = int(digit_str)

        if digit == 0 or num % digit != 0:
            is_valid = False
            break

    # Print the valid numbers in a single line separated by spaces
    if is_valid:
        print(num, end=" ")

# Initialize the variable to store the maximum value
max_number = 0

while True:
    # Read an integer from the user input
    num = int(input(f"Input numbers: "))

    # If the number is 0, terminate the loop (end of sequence)
    if num == 0:
        break

    # If the current number is greater than the known maximum, update it
    if num > max_number:
        max_number = num

print(max_number)

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1


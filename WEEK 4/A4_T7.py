print("Starting program.\n")
print("Check multiplicative persistence.")
input = int(input("Insert an integer: "))
final = 0

while input >= 10:
    product = 1
    temp = input
    digits = []

    while temp > 0:
        digit = temp % 10
        digits = [digit] + digits
        product *= digit
        temp //= 10

    for i in range(len(digits)):
        if i > 0:
            print(" * ", end="")
        print(digits[i], end="")
    print(" =", product)

    input = product
    final += 1
print("No more steps.")
print("\nThis program took", final,"step(s)\n\nProgram ending.")
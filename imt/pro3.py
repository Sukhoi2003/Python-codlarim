number1 = 0
while (1):
    number2 = input("Enter number: ")
    """Raqam kiritishni to'xtatish uchun (c) harfini kiriting"""
    if number2 == 'c':
        break
    else:
        number1 += int(number2)

print(number1)  
n = int(input())
for i in range(0,n):
    number = int(input())
    dividing_digits = 0
    for j in range(0, len(str(number))):
        digit = str(number)[j]
        if int(digit) != 0:
            if number % int(digit) == 0:
                dividing_digits = dividing_digits + 1
    print(dividing_digits)

n = int(input())

for i in range(0,n):
    stones = int(input())
    step1 = int(input())
    step2 = int(input())
    first_step = min(step1, step2)
    second_step = max(step1, step2)
    current = first_step * (stones - 1)
    last_possible = second_step * (stones-1)
    difference = second_step - first_step
    possibles = str(current)
    if difference == 0:
        possibles = str(current)
    else:
        while current < last_possible:
            current = current + difference
            possibles = possibles + " " + str(current)

    print(possibles)

import math

n = int(input())

for i in range(0,n):
    args = input().split(' ')
    a = int(args[0])
    b = int(args[1])

    root_a = math.sqrt(a)
    root_b = math.sqrt(b)

    square_numbers = int(math.floor(root_b)) - int(math.ceil(root_a)) + 1

    print(square_numbers)

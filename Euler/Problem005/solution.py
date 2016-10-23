'''2520 is the smallest number that can be divided by each of the numbers from 1
 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?'''



check = False
num = 0
divisible_by = 20

while check == False:
    if num % 1000 == 0:
        print(num)
    num += 1
    for i in range(1,divisible_by+1):
        if num % i != 0:
            break
        if i == divisible_by:
            check = True

print(num)

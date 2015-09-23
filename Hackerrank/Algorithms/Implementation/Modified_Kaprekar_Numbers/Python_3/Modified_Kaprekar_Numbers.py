def is_kaprekar(n):
    if n == 1:
        return True
    square_of_n = n * n
    string_square = str(square_of_n)
    if square_of_n >= 10:
        if len(str(square_of_n)) % 2 == 0:
            divide_in = int(len(string_square)/2)            
            part_1 = string_square[:divide_in]
            part_2 = string_square[-divide_in:]
            part_3 = string_square[:divide_in]
            part_4 = string_square[-divide_in:]
        else:
            divide_in = int(len(str(n)))            
            part_1 = string_square[:divide_in]
            part_2 = string_square[-(len(string_square)-divide_in):]
            part_3 = string_square[:(divide_in-1)]
            part_4 = string_square[-(len(string_square)-divide_in+1):]            
        if ((int(part_1) + int(part_2) == n) or (int(part_3) + int(part_4) == n)) and (int(part_1) > 0) and (int(part_2) > 0):
            return True
        else:
            return False
    else:
        return False
        
lower_number = int(input())
upper_number = int(input())
kaprekars_in_range = ""
for i in range(lower_number, upper_number+1):
    if is_kaprekar(i):
        kaprekars_in_range = kaprekars_in_range + " " + str(i)

if kaprekars_in_range.strip() == "":
    print("INVALID RANGE")
else:
    print(kaprekars_in_range.strip())
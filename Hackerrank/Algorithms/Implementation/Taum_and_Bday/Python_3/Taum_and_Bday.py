n = int(input())
for i in range(0,n):
    a = input().split(' ')
    black_presents = int(a[0])
    white_presents = int(a[1])
    b = input().split(' ')
    cost_black = int(b[0])
    cost_white = int(b[1])
    conversion_cost = int(b[2])
    cost = 0
    if (conversion_cost + cost_white >= cost_black) and (conversion_cost + cost_black >= cost_white):
        cost = black_presents * cost_black + white_presents * cost_white
    elif (conversion_cost + cost_white < cost_black):
        cost = (cost_white * white_presents) + ((cost_white + conversion_cost)*black_presents)
    elif (conversion_cost + cost_black < cost_white):
        cost = (cost_black * black_presents) + ((cost_black + conversion_cost)*white_presents)
        
    print(cost)
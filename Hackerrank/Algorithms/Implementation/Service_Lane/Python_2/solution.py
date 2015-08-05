# Enter your code here. Read input from STDIN. Print output to STDOUT
n, t = raw_input().split()
n = int(n)
t = int(t)

width = raw_input().split(' ')

for i in range(0,n):
    entry, exit = raw_input().split()
    entry, exit = int(entry), int(exit)
    max_width = 0
    for j in range(entry,exit+1):
        current_width = width[j]
        if max_width == 0:
            max_width = current_width
        else:
            if current_width < max_width:
                max_width = current_width
    print max_width

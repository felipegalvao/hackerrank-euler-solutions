T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    answer = 0
    wrappers = 0
    answer = int(N) // int(C)
    proceed = False
    wrappers = answer
    while proceed == False:
        if wrappers < int(M):
            proceed = True
        else:
            chocs = (wrappers//int(M))
            answer = answer + chocs
            wrappers = wrappers - (int(M)*chocs)+chocs

    print(answer)

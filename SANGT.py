n = int(input())
def SangNT(n):
    check = [True]*(n+1)
    check[0] = False
    check[1] = False
    for i in range(2, int(n**0.5)+1):
        if check[i] == True:
            for j in range(i*i, n+1, i):
                check[j] = False
    return check
def NT(n):
    check = SangNT(n)
    for i in range(2, n+1):
        if check[i] == True:
            print(i, end = ' ')
NT(n)
            
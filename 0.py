test = int(input())
while test > 0:
    n = int(input())
    ans = 0
    pow = 5
    while pow < n:
        ans = ans + int(n/pow)
        pow = pow*5
    print(ans, end="\n")

import math
def NT(n):
    if n<2:
        return False
    else:
        x= int(math.sqrt(n))
        for i in range(2,x+1):
            if n % i == 0:
                return False
        return True
n = int(input())
if NT(n):
    print("YES")
else:
    print("NO")
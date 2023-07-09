import math

# Tìm giá trị L
def find_L(N):
    x = 1
    while True:
        if math.floor(math.log10(math.factorial(x))) + 1 >= N:
            return x
        x *= 2

# Tìm giá trị R
def find_R(N):
    x = 1
    while True:
        if math.floor(math.log10(math.factorial(x+1))) + 1 > N:
            return x
        x *= 2
        
# Tìm tất cả các số X thoả mãn X! có đúng N chữ số
def find_X(N):
    L = find_L(N)
    R = find_R(N)
    
    res = []
    for x in range(L, R+1):
        if math.floor(math.log10(math.factorial(x))) + 1 == N:
            res.append(x)
    
    return res

N = 45
print(find_X(N))

def check(a:int, b:int, c:int) -> str:
    if(a==b==c):
        return "Equilateral triangle"
    elif a!=b and a!=c and b!=c:
        return "Scalene triangle"
    else:
        return "Isosceles triangle"
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(check(a,b,c), end=" ")
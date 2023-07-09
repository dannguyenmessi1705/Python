def UCLN(a: int, b: int) -> int:
    if a == 0: return b
    if b == 0: return a
    return UCLN(b%a, a)
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(UCLN(a,b))
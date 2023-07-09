def sToI(lst: list) -> int:
    s = ""
    for i in lst:
        s+=i
    return int(s)
if __name__ == "__main__":
    n = int(input())
    lst:list = []
    for i in range(n):
        lst.append(input())
    print(sToI(lst))
def print1(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
print(print1(lst), end=" ")
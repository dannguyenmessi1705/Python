def EvenList(lst) -> list:
    res = []
    for i in lst:
        if i%2 == 0:
            res.append(i)
    return res
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
res = EvenList(lst)
print(res, end=" ")
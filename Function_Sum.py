def sum_list(lst):
    s = 0
    for i in lst:
        s+=i
    return s
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
print(sum_list(lst), end=" ")

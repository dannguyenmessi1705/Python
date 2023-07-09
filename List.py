n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
s=0
for i in lst:
    s+=i
print(s)
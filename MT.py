hang, cot = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
pos = 0
for i in range(hang):
    for j in range(cot):
        print(a[pos], end=' ')
        pos += 1
    print(end='\n')

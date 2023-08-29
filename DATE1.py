n, y = [int(x) for x in input().split()]
b = 28
if (y % 4 == 0 and y % 100 != 0) | (y % 400 == 0):
    b = 29
m = [31, b, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b = [31]
for i in range(0, len(m)-1):
    b.append(b[i] + m[i+1])
for i in range(0, len(b)):
    if(n <= b[i]  and i!=0 ): # Xét, nhưng với điều kiện i  là chỉ số 0, vì i-1 sẽ nhảy về cuối mảng 
        print(n - b[i-1], i+1) 
        break
    elif(n <= b[i] and i==0): # Xét nếu i không phải chỉ số 0, thì in bình thường
        print(n, i+1)
        break
    else:
        continue

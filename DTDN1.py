n = int(input())
a = [int(x) for x in input().split()]

b = [1] * n  # mảng b chứa độ dài dãy con tăng dài nhất kết thúc tại vị trí i
# ban đầu mỗi phần tử đều là 1 vì dãy con tăng dài nhất kết thúc tại vị trí i là chính nó => khai báo b = [1, 1, ..., 1]

for i in range(1, n):  # duyệt từ 1 đến n-1
    for j in range(i):   # duyệt từ 0 đến i-1
        # nếu a[i] > a[j] thì cập nhật b[i] = max(b[i], b[j] + 1)
        if a[i] > a[j]:
            # b[i] = max(b[i], b[j] + 1) có nghĩa là nếu tìm được dãy con tăng dài hơn thì cập nhật lại b[i]
            b[i] = max(b[i], b[j] + 1)
            # b[j] + 1 là dãy con tăng dài nhất kết thúc tại vị trí j + 1 phần tử a[i]
            # b[i] là dãy con tăng dài nhất kết thúc tại vị trí i + 1 phần tử a[i]
print(max(b))

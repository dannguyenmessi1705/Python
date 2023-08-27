def tongNghichDao(n, sum): # sum là mảng chứa tổng nghịch đảo của các số từ 1 đến n
    sum = [0, n**(1/2)]
    if n < len(sum): # Nếu n < len(sum) thì tổng nghịch đảo của n đã được tính trước đó (nằm trong mảng sum)
        return sum[n] # sum[n] là tổng nghịch đảo của n
    current_sum = sum[-1] # Lấy giá trị cuối cùng của mảng sum (tức là tổng nghịch đảo của n-1) để tính tiếp
    for i in range(len(sum), n + 1): # Tính tổng nghịch đảo của các số từ n-1 đến n
        current_sum += (n+1)-i
        current_sum = current_sum**(1/2)
        sum.append(current_sum) # Thêm tổng nghịch đảo của n vào mảng sum
    return current_sum # Trả về tổng nghịch đảo của n (giá trị mới nhất)

sum = []  # Khởi tạo mảng ban đầu chứa sẵn tổng nghịch đảo của n = 0 và n = 1
              # => n = 0 thì sum = 0, n = 1 thì sum = 1
test = int(input()) 
while test > 0:
    n = int(input())
    result = tongNghichDao(n, sum)
    print("{:.5f}".format(result))
    test -= 1

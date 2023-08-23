def count_digits(a, b):
    digit_counts = [0] * 10  # Khởi tạo danh sách đếm cho 10 chữ số từ 0 đến 9

    for digit in range(10):
        power = 1  # Lũy thừa của 10
        while power <= b:
            # Số lượng các số có chữ số 'digit' tại vị trí power
            count = (b // (10 * power)) * power

            # Xét trường hợp số cuối cùng trong dãy từ a đến b
            last_digits = b % (10 * power)
            if last_digits >= 2 * power - 1:
                count += min(last_digits - power + 1, power)

            # Xét trường hợp số đầu tiên trong dãy từ a đến b
            first_digits = a % (10 * power)
            if first_digits > 0 and first_digits <= 2 * power - 1:
                count -= min(first_digits, power)

            digit_counts[digit] += count

            power *= 10

    return digit_counts


# Thử nghiệm với a = 1024 và b = 1032
a = 1024
b = 1032
result = count_digits(a, b)

# In kết quả
for digit, count in enumerate(result):
    print(f"Số lần xuất hiện của chữ số {digit} là: {count}")

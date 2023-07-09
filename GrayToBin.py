def gray_to_binary(gray):
    binary = ""
    for i in range(len(gray)):
        if i == 0:
            binary += gray[i]
        else:
            if gray[i] == '0':
                binary += binary[i-1]
            else:
                binary += str(1 - int(binary[i-1]))
    return binary
test = int(input())
while(test>0):
    gray_str = input()
    binary_str = gray_to_binary(gray_str)
    print(f'{binary_str}')
    test = test-1

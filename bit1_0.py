def generateBinaryStrings(N, ones, zeros, s):
    if N == 0:
        print(s)
        return
    if ones != zeros:
        return
    generateBinaryStrings(N-1, ones+1, zeros, s+'1')
    generateBinaryStrings(N-1, ones, zeros+1, s+'0')
N = int(input())
if N % 2 != 0:
    print(-1)
else:
    generateBinaryStrings(N, 0, 0, '')
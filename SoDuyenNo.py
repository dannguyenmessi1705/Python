lst=[]
while True:
    try:
        n=input()
        lst.append(n)
    except EOFError:
        break
for v in lst:
    v = int(v)
    str_v = str(v)
    if str_v[0] == str_v[-1]:
        print("YES")
    else:
        print("NO")
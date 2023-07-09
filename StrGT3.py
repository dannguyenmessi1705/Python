def solve(s:str) -> list:
    ans = []
    lst = s.split(" ")
    for i in lst:
        if len(i) > 3:
            ans.append(i)
    return ans
if __name__ == "__main__":
    s = input()
    print(solve(s))
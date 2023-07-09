def add(s:str) -> str:
    l = len(s)
    if l < 3:
        return s
    elif s[l-3:l] == "ing":
        return s+"ly"
    else:
        return s+"ing"
if __name__ == "__main__":
    s = input()
    print(add(s))
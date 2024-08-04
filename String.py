def decoding(s):
    str  =[]
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            str.append(f"{s[i-1]}{count if count > 1 else '' }")
            count = 1
    str.append(f"{s[-1]}{count if count > 1 else '' }")
    return ''.join(str)
s = input()
print(decoding(s))

        # str.append()
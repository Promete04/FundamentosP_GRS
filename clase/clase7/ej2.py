def _split(s,seps):
    L=[]
    last_split = 0
    for i in range (len(s)):
        if s[i] in seps:
            L.append(s[last_split:i])
            last_split = i+1
    if s[last_split:]:
        L.append(s[last_split:])
    return L
_split("Hello word, I want to end you, mf",list(", ."))
print(_split)
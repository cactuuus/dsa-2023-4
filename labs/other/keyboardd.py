s = "so sticky "
t = "ssoo  ssttiicckkyy "

out = set()
i, j = 0, 0

while i < len(s):
    if s[i] == t[j]:
        i += 1
    else:
        out.add(t[j])
    j += 1

print("".join(out))
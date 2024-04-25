for _ in range(int(input())):
    n, x, y = map(int, input().split())
    remainder = 0
    y = y * 100
    for _ in range(n):
        add = y - int(float(input()[:-1])*100) % y
        if add < y:
            remainder += add
    if remainder/100 < x:
        print("NO")
    else:
        print("YES")




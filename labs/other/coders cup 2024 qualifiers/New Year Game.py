def newYearGame(n: int, a: list[int]):
    balsa = koca = 0
    for turn in range(n):
        removed = False
        if turn % 2 == 0:
            for num in a:
                if (abs((balsa + num) - koca)) % 3 != 0:
                    balsa += num
                    a.remove(num)
                    removed = True
                    break
            if not removed:
                balsa += a.pop()
        else:
            for num in a:
                if (abs(balsa - (koca + num))) % 3 == 0:
                    koca += num
                    a.remove(num)
                    removed = True
                    break
            if not removed:
                koca += a.pop()
    print("Koca" if abs(balsa - koca) % 3 == 0 else "Balsa")

newYearGame(3, [7,6,18])
newYearGame(1, [3])

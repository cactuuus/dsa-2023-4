def queensAttacktheKing(queens: list[list[int]], king: list[int]) -> list[list[int]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    can_attack = []
    for d in directions:
        k = king[:]
        print(k, d)
        while 8 > k[0] > -1 and 8 > k[1] > -1:
            k[0] += d[0]
            k[1] += d[1]
            print(k)
            if k in queens:
                can_attack.append(k)
                break
    return can_attack


print(queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))

def maximumBags(capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
    space_left = sorted([capacity[i] - rocks[i] for i in range(len(capacity))])

    for i in range(len(space_left)):
        if additionalRocks < space_left[i]:
            break
        additionalRocks -= space_left[i]
        space_left[i] = 0
        i += 1

    return space_left.count(0)

print(maximumBags([2,3,4,5], [1,2,4,4], 2))

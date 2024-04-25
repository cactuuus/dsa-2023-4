from collections import defaultdict


def journeyToMoon(n: int, astronaut: tuple[int, int]) -> int:
    countries = defaultdict(set)

    for x, y in astronaut:
        countries[x].add(y)
        countries[y].add(x)
    print(countries)

    for key in countries:
        values = list(countries[key])
        i = 0
        while i < len(values):
            target = values.pop()
            if target not in countries:
                continue
            if target == key:
                continue
            countries[key].update(countries[target])
            values += list(countries[target])
            countries[target].clear()
        print(countries)

    tot_pairs = n * (n - 1) // 2
    for country in countries.values():
        tot_pairs -= len(country) * (len(country) - 1) // 2
    return tot_pairs


print(journeyToMoon(5, [[0, 1], [2, 3], [0, 4], [3, 4]]))
print(journeyToMoon(5, [[0,3],[2,3],[0,4]]))


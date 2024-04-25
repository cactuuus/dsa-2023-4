from collections import defaultdict


def acmTeam(topic):
    counter = defaultdict(int)
    most_topics_known = 0

    for member1 in range(len(topic) - 1):
        for member2 in range(member1 + 1, len(topic)):
            topics_known = 0
            for i in range(len(topic[0])):
                if topic[member1][i] == "1" or topic[member2][i] == "1":
                    topics_known += 1
            counter[topics_known] += 1
            if topics_known > most_topics_known:
                most_topics_known = topics_known

    return [most_topics_known, counter[most_topics_known]]


print(acmTeam(["10101", "11100", "11010", "00101"]))

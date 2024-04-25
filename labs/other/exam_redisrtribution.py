n = input()
rooms = [int(x) for x in input().split(" ")]

if max(rooms) > sum(rooms)/2:
    print("impossible")

sorted_rooms = sorted(enumerate(rooms, 1), key=lambda x: x[1], reverse=True)

print(" ".join([str(x) for x, y in sorted_rooms]))

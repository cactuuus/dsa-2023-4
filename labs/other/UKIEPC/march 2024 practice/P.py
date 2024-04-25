import sys

lines = sys.stdin.readlines()
n, k = map(int, lines[0].split(" "))
arr = [int(x) for x in lines[1].split(" ")]

sorted_arr = sorted(arr)

# for _ in range(k):
#     for i in range(n-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]


print(sorted_arr)
print(*arr)



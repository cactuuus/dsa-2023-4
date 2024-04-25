n, tot_presses = map(int, input().split(" "))
modes = []

for _ in range(n):
    x, y = map(int, input().split(" "))
    modes.append((x, y))

presses = current = timer = 0
history = [0]
for p in range(tot_presses):
    timer += modes[current][1]
    while timer >= modes[current][0]:
        current += 1
        if current >= n:
            timer = 0
            break
    history.append(timer)
    presses += 1
    if timer == 0:
        break

if tot_presses == presses:
    print(timer)
else:
    print(history[tot_presses % presses])

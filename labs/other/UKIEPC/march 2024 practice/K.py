# input is a string of directions (ie "NESWE")

directions = "NESW"

moves = set()
output = ""
for d in directions:
    if d not in moves:
        moves.add(d)
        output += "R"
    else:
        moves.discard(d)
        output += "H"

if :
    print(output)
else:
    print("NO")

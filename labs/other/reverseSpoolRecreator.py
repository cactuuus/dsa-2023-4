with open("reverse600.gcode", "w") as output:
    output.write("M104 S220\n\nM109 S220\n\nM117 RECREATING FILAMENT\n")
    for i in range(439):
        output.write("G92 E100\nG0 E0 F600\n")
    output.write("M104 S0 ; turn off temperature\nM107 ; turn off fan\nM84 X Y E ; disable motors")




    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
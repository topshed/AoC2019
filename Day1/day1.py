modules = []
total_fuel = 0
with open("input.txt") as file:
    for line in file:
        m = line.rstrip()
        f = (int(float(m)/3)) -2
        total_fuel = total_fuel + f
        modules.append(m)

print(total_fuel)
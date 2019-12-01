
total_fuel = 0
with open("input.txt") as file:
    for line in file:
        m = line.rstrip()
        f = (int(float(m)/3)) -2
        print(f)
        total_fuel = total_fuel + f
        while f > 0:
            f = (int(float(f)/3)) -2
            print(f)
            if f > 0:
                total_fuel = total_fuel + f

print(total_fuel)
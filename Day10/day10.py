import math
#with open("test1.txt") as file:
asteroids = []
x = 0
y = 0
with open("input.txt") as file:
    for line in file:
        line = line.rstrip()
        x = 0
        for char in line:
            if char =="#":
                asteroids.append((x,y))
            x+=1
        y+=1

print(asteroids)

bob = []
in_way = []

angles = []
'''a = (5,8)
for b in asteroids:
    if a != b:
        angle = math.atan2(a[1]-b[1], a[0]-b[0])
        angles.append(angle)
print(len(set(angles)))'''

i = 0
for a in asteroids:
    angles = []
    for b in asteroids:
        if a != b:
            angle = round(math.atan2(a[1]-b[1], a[0]-b[0]),3)
            angles.append(angle)

    #print(len(set(angles)), len(angles))
    bob.append(len(set(angles)))
    if len(set(angles)) == 319:
        print(a)
    i+=1
print(i)

print("max", max(bob))
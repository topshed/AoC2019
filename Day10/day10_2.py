import math
from operator import itemgetter
asteroids = []
x = 0
y = 0
# (31,20)

def calculateDistance(p,q):  
     dist = math.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2) 
     return dist  


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

i = 0
a = (31,20)
#a =(8,3)
#a = (11,13)
angles = []
a_map = {}

for b in asteroids:
    if a != b:
        angle = round(math.atan2(a[1]-b[1], a[0]-b[0]),3)
        if angle< 0:
            angle = round(angle + 2*math.pi,3)
        #angle = math.degrees(angle)
        d = calculateDistance(a,b)
        a_map[b] = angle,d
        angles.append(angle)

#print(len(set(angles)), len(angles))
bob.append(len(set(angles)))

closest=[]
for i in a_map.items():
    #print(i[1][1])
    closest.append(i[1][1])

print(min(closest))

for i in a_map.items():
    #print(i[1][1])
    if i[1][1] == min(closest):
        print(i)
print("***********")
for i in a_map.items():
    print(i)

blasted = a_map.copy()
hits = 1
counter = 0
vaped = []
while len(blasted) > 1 and hits != 0:
    blasted = a_map.copy()
    r = 100000
    hits = 0
    for i in range(r):
        laser_angle = (math.pi/2) + ((math.pi*2)/r)*i
        if laser_angle > 2*math.pi:
            laser_angle = laser_angle - (2*math.pi)
        if round(laser_angle,3) == 0:
            print("zero************************************")
        on_path = []
        for target in a_map.items():
            if target[1][0] == round(laser_angle,3):
                
                #print("hit ", target[0])
                on_path.append(target[0])
                hits+=1

        if len(on_path) > 0:
            #print(on_path)
            dists = {}
            for h in on_path:
                dists[h] = a_map[h][1]
            closest = min(dists.items(),key=itemgetter(1))
            #print(dists)
            #print("closest ",closest)
                
            if len(blasted) > 1:
                 blasted.pop(closest[0],None)
                 counter+=1
                 if closest[0] not in vaped:
                     vaped.append(closest[0])
                 if counter == 200:
                     sol = closest
            
        
        #print(laser_angle,hits)
                                
    print(hits)
    print(blasted)
    a_map = blasted.copy()
#print("max", max(bob))

from shapely.geometry import LineString
from scipy.spatial import distance
from pprint import pprint

with open("input.txt") as file:
#with open("test3.txt") as file:
    line1 = file.readline()
    line2 = file.readline()

wire_1 = line1.rstrip().split(',')
wire_2 = line2.rstrip().split(',')


wire_1_coords = [[0,0]]
wire_2_coords = [[0,0]]

def mapper(wire, wire_coord):
    index = 0
    start_coord = wire_coord[0]
    for x in range(len(wire)):
        #print(wire[x])
        pos = wire[x]
        direction = pos[0]
        length = int(pos[1:])
        new_coord=(0,0)
        if direction == 'R':
            #new_coord[0] = start_coord[0] + length
            #new_coord[1] = start_coord[1]
            new_coord = (start_coord[0] + length, start_coord[1])
            wire_coord.append(new_coord)
        elif direction == 'L':
            #new_coord[0] = start_coord[0] - length
            #new_coord[1] = start_coord[1]
            new_coord = (start_coord[0] - length, start_coord[1])
            wire_coord.append(new_coord)
        elif direction == 'U':
            #new_coord[0] = start_coord[0] 
            #new_coord[1] = start_coord[1] + length
            new_coord = (start_coord[0], start_coord[1] + length)
            wire_coord.append(new_coord)
        elif direction == 'D':
            #new_coord[0] = start_coord[0] 
            #new_coord[1] = start_coord[1] - length
            new_coord = (start_coord[0], start_coord[1] - length)
            wire_coord.append(new_coord)
        else:
            print("Unknown direction")
        start_coord = new_coord
    return(wire_coord)
    
wire_1_mapped = mapper(wire_1,wire_1_coords)
wire_2_mapped = mapper(wire_2,wire_2_coords)
l1 = LineString(wire_1_mapped)
l2 = LineString(wire_2_mapped)
print(l1.length)
x = l1.intersection(l2)
print(x)
hits = []
for hit in x:
   
    cb = distance.cityblock([0, 0, 0], [hit.x, hit.y, 0])
    if cb > 0:
        hits.append(cb)
    #print(hit, cb)
print(min(hits))


    
    

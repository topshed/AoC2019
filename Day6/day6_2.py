orbits = {}
r_orbits = {}
planets = [] 

with open("input.txt") as file:
    for line in file:
        o = line.rstrip().split(")")
        orbits[o[1]] = o[0]
        if o[0] in r_orbits:
            r_orbits[o[0]].append(o[1])
        else:
            r_orbits[o[0]] = [o[1]]
        for p in o:
            planets.append(p)

planets = set(planets)

def plotter(planet, i=0):
    if planet == "COM":
        return i
    parent = orbits[planet]
    return plotter(parent, i + 1)

result = 0
for p in planets:
    result = result+plotter(p)

print(result)

visited = set()
nodes = [("YOU", 0)]
distances = set()
while len(visited) < len(planets) - 1:  # -1 to ignore the COM root node
    node = nodes.pop()
    if node[0] == "SAN":
        distances.add(node[1] - 2)
    else:
        visited.add(node[0])
        if node[0] in orbits:
            child_node = orbits[node[0]]
            if child_node not in visited:
                nodes.append((child_node, node[1] + 1))
        if node[0] in r_orbits:
            child_nodes = r_orbits[node[0]]
            for child_node in child_nodes:
                if child_node not in visited:
                    nodes.append((child_node, node[1] + 1))

print(f"PART 2: {min(list(distances))}")
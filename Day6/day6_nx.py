import networkx as nx

G = nx.Graph()

orbits = []


with open("input.txt") as file:
    for line in file:
        o = line.rstrip().split(")")
        orbits.append(o)

G.add_edges_from(orbits)

s =nx.single_source_shortest_path_length(G,"COM")

print(sum(s.values()))
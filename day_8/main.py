from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode
from scipy.spatial import KDTree
import numpy as np

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

# NumPy Vector Distance (why? see https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy)
#print(np.linalg.norm(v1-v2), type(np.linalg.norm(v2-v1)))

# 1st star
conn_limit = 1000 if "input" in filename else 10
numbers = [[int(nr) for nr in line.split(",")] for line in lines]
vprint(numbers)
vprint("Starting Tree Query...")

tree = KDTree(numbers)
distances, indices = tree.query(x=numbers, k=len(numbers), workers=8)
distances = np.array([distance[1:] for distance in distances])
indices = np.array([index[1:] for index in indices])
#print(distances, indices, sep="\n")
vprint(len(distances[0]))

vprint("Tree Query Done.")
vprint("Starting linked sorting (AI-generated code for this part, shame on me)...")


# !!! Following loc are GenAI created, because my own understanding was too limited and my own algorithm was too slow.

# --- Step 1: Create the Origin Index Array ---
# This array tells us the index of the QUERY vector (row 0 or row 1)
d_n, d_k = distances.shape # N=2 (rows/query vectors), k=3 (columns/neighbors)

# Create an array like [[0, 0, 0], [1, 1, 1]]
origin_indices = np.repeat(np.arange(d_n), d_k).reshape(d_n, d_k)

# --- Step 2: Flatten All Three Arrays ---
flat_distances = distances.ravel()    # [0.1, 0.3, 0.5, 0.2, 0.35, 0.6]
flat_indices = indices.ravel()        # [1, 3, 5, 2, 7, 6]
flat_origin_indices = origin_indices.ravel() # [0, 0, 0, 1, 1, 1]

# --- Step 3: Sort based on Distance ---
# np.argsort returns the indices that would sort the flat_distances
sort_order = np.argsort(flat_distances)

# --- Step 4: Apply the sort_order to all three arrays ---
globally_sorted_distances = flat_distances[sort_order]
globally_sorted_closest_indices = flat_indices[sort_order]
globally_sorted_origin_indices = flat_origin_indices[sort_order]

# !!! GenAI part over


distances, indices, orig_indices = globally_sorted_distances[::2], globally_sorted_closest_indices[::2], globally_sorted_origin_indices[::2]

vprint("Linked sorting done.")
vprint("Starting circuitry...")

# Former own slow algorithm
# for i in range(len(numbers)):
#     for j in range(len(distances[i])):
#         if [distances[i][j], int(indices[i][j]), i] not in possbile_connections:
#             possbile_connections.append( [distances[i][j], i, int(indices[i][j])] )
# print("len(possible_connections)", len(possbile_connections))
# possbile_connections = sorted(possbile_connections, key=lambda d:d[0])
# vprint([c[1:] for c in possbile_connections[1:11]])

circuits:list[set[int]] = [set([indices[0], orig_indices[0]])]
vprint(circuits)
for i in range(1, len(distances[:conn_limit])):
    # Hier alle Circuits einfügen (for loop hierunter mit range und index machen), in den die conn drin ist 
    # und weiter unten dann alle zusammenfügen, aka mergen und überschüssige löschen 
    # (oder bei 1 nur zahlen hinzufügen, oderoder bei 0 komplette conn hinzufügen)
    part_of_conn_in_any_circuit = []
    for c in range(len(circuits)):
        if orig_indices[i] in circuits[c] or indices[i] in circuits[c]:
            part_of_conn_in_any_circuit.append(c)
    #vprint(conn[1:], len(part_of_conn_in_any_circuit))
    if len(part_of_conn_in_any_circuit) == 0:
        circuits.append(set([indices[i], orig_indices[i]]))
    if len(part_of_conn_in_any_circuit) > 0:
        circuits[part_of_conn_in_any_circuit[0]].add(indices[i])
        circuits[part_of_conn_in_any_circuit[0]].add(orig_indices[i])
        if len(part_of_conn_in_any_circuit) == 2:
            for p in circuits[part_of_conn_in_any_circuit[1]]:
                circuits[part_of_conn_in_any_circuit[0]].add(p)
            circuits.remove(circuits[part_of_conn_in_any_circuit[1]])

#circuits.sort(key=lambda c:-len(c))
vprint("Cicuitry done.")
vprint([[int(i) for i in c] for c in circuits])

biggest_circuits = list(set(sorted([len(c) for c in circuits])))
product_biggest_circuits = biggest_circuits[-1] * biggest_circuits[-2] * biggest_circuits[-3]
vprint(biggest_circuits)

# 2nd star
vprint("####### 2nd star #######")
circuits = [set([indices[0], orig_indices[0]])]
vprint(circuits)
last_indices = []
for i in range(1, len(distances)):
    # Hier alle Circuits einfügen (for loop hierunter mit range und index machen), in den die conn drin ist 
    # und weiter unten dann alle zusammenfügen, aka mergen und überschüssige löschen 
    # (oder bei 1 nur zahlen hinzufügen, oderoder bei 0 komplette conn hinzufügen)
    part_of_conn_in_any_circuit = []
    for c in range(len(circuits)):
        if orig_indices[i] in circuits[c] or indices[i] in circuits[c]:
            part_of_conn_in_any_circuit.append(c)
    #vprint(conn[1:], len(part_of_conn_in_any_circuit))
    if len(part_of_conn_in_any_circuit) == 0:
        circuits.append(set([indices[i], orig_indices[i]]))
    if len(part_of_conn_in_any_circuit) > 0:
        circuits[part_of_conn_in_any_circuit[0]].add(indices[i])
        circuits[part_of_conn_in_any_circuit[0]].add(orig_indices[i])
        if len(part_of_conn_in_any_circuit) == 2:
            for p in circuits[part_of_conn_in_any_circuit[1]]:
                circuits[part_of_conn_in_any_circuit[0]].add(p)
            circuits.remove(circuits[part_of_conn_in_any_circuit[1]])

    if len(circuits) == 1 and len(circuits[0]) > len(numbers)-1:
        vprint(circuits)
        last_indices = [orig_indices[i], indices[i]]
        break

print(f"input {filename}:")
print(f"1. star: {np.prod(product_biggest_circuits)}")
print(f"2. star: {np.prod([numbers[last_indices[0]][0], numbers[last_indices[1]][0]])}")
from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

divider_index = lines.index("")

ranges, ids = [[int (y) for y in x.split("-")] for x in lines[:divider_index]], [int(x) for x in lines[divider_index+1:]]

#1st star
available_fresh_ingredients = 0

for id in ids:
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            available_fresh_ingredients += 1
            break

# 2nd star
ranges = sorted(ranges, key=lambda r: r[0])
del_ranges, new_ranges = set(), []
sum_fresh_ids = 0

# Combine ranges and note down which ranges are unnecessary after combining.
for i in range(len(ranges)):
    for j in range(i+1, len(ranges)):
        if ranges[j][0] <= ranges[i][1]:
            ranges[i][1] = max(ranges[i][1], ranges[j][1])
            del_ranges.add(j)
        else:
            i = j

for i in range(len(ranges)):
    if i not in del_ranges:
        new_ranges.append(ranges[i])

for nr in new_ranges:
    sum_fresh_ids += (nr[1]+1)-nr[0]

print(f"input {filename}: ")
print(f"1. star: {available_fresh_ingredients}")
print(f"2. star: {sum_fresh_ids}")
from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

points = [[int(x) for x in line.split(",")] for line in lines]

def give_rectangle_area_from_two_points(p1: list[int], p2: list[int]):
    # Bigger x - smaller x, same for y (both +1, see aoc). Then multiply them.
    x_side, y_side = max(p1[0],p2[0])-min(p1[0],p2[0])+1, max(p1[1],p2[1])-min(p1[1],p2[1])+1
    return x_side*y_side

#vprint(points[0], points[2], give_rectangle_area_from_two_points(points[0], points[2]))

# 1st star
biggest_area = 0

# Back at it again with the huge fits-all array
rectangles = []
for i in range(len(points)):
    for j in range(len(points)):
        rectangles.append([points[i], points[j], give_rectangle_area_from_two_points(points[i], points[j])])

#vprint(len(rectangles))

rectangles = sorted(rectangles, key=lambda r:r[2])

#vprint(rectangles, rectangles[-1][2])
biggest_area = rectangles[-1][2]

print(f"input {filename}:")
print(f"1. star: {biggest_area}")
print(f"2. star: {0}")
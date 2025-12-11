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

rectangles = sorted(rectangles, key=lambda r:r[2], reverse=True)

#vprint(rectangles, rectangles[-1][2])
biggest_area = rectangles[0][2]

# 2nd star
i = 0
for _ in range(len(rectangles)):
    # Original vertices of the rectangle
    bounds_x = sorted([rectangles[i][0][0], rectangles[i][1][0]])
    bounds_y = sorted([rectangles[i][0][1], rectangles[i][1][1]])
    #v1, v2 = [x-1 for x in rectangles[i][0]], [x-1 for x in rectangles[i][1]]
    # Diagonal vertices
    #v3, v4 = [rectangles[i][0][0]-1, rectangles[i][1][1]-1], [rectangles[i][1][0]-1, rectangles[i][0][1]-1]
    mark_for_removal = False
    for r in range(len(points)):
        if (points[r][0] > bounds_x[0] and points[r][0] <bounds_x[1]) and (points[r][1] > bounds_y[0] and points[r][1] <bounds_y[1]):
            mark_for_removal = True
            break
    if mark_for_removal:
        rectangles = rectangles[:i]+rectangles[i+1:]
        i -= 1
    i += 1
    
vprint(rectangles[0])
    

print(f"input {filename}:")
print(f"1. star: {biggest_area}")
print(f"2. star: {0}")
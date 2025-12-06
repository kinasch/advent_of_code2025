from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

def pretty_print_grid():
    for y in range(y_max+1):
        vprint(paper_grid[y])

def calc_pattern(y,x):
    sum = -1
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            sum += int(paper_grid[i][j])
    return sum

# --------x
# | .@.@@
# | @@@@.
# | ...@.
# y
# grid[y][x]

paper_grid = ["0"*(len(lines[0])+2)]
# Every "@" becomes a 1 and every "." a 0. Unnecessary, but my first thought.
paper_grid.extend(["0"+line.replace("@","1").replace(".","0")+"0" for line in lines])
paper_grid.append("0"*(len(lines[0])+2))
y_max, x_max = len(paper_grid)-1, len(paper_grid[0])-1

available_rolls_fewer_4 = 0
rerun_available_rolls = 0

# 1st star
for y in range(1, y_max):
    for x in range(1, x_max):
        if paper_grid[y][x] == "1":
            adjacent_sum = calc_pattern(y,x)
            available_rolls_fewer_4 += 1 if adjacent_sum<4 else 0

# 2nd star
prior_rerun_available_rolls = -1
iii = 0
while prior_rerun_available_rolls != rerun_available_rolls:
    iii += 1
    prior_rerun_available_rolls = rerun_available_rolls
    for y in range(1, y_max):
        for x in range(1, x_max):
            if paper_grid[y][x] == "1":
                adjacent_sum = calc_pattern(y,x)
                if adjacent_sum<4:
                    paper_grid[y] = paper_grid[y][:x]+"0"+paper_grid[y][x+1:]
                    rerun_available_rolls += 1

print(f"input {filename}: ")
print(f"1. star: {available_rolls_fewer_4}")
print(f"2. star: {rerun_available_rolls}, with {iii} reruns")
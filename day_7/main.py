from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

beams = set()
start_index = lines[0].index("S")
beams.add(start_index)
first_line = lines[0]
lines = lines[1:]

# 1st star
times_beam_split = 0

for line in lines:
    for i in range(len(line)):
        if i in beams:
            if line[i] == "^":
                times_beam_split += 1
                beams.remove(i)
                beams.add(i-1)
                beams.add(i+1)
                line = line[:i-1] + "|" + line[i:]
                line = line[:i+1] + "|" + line[i+2:]
            else:
                line = line[:i] + "|" + line[i+1:]
    #vprint(line)

# 2nd star
beams = {}
beams[str(start_index)] = 1
vprint(beams)

for line in lines:
    for i in range(len(line)):
        if str(i) in beams.keys():
            if line[i] == "^":
                prior_paths = beams.pop(str(i))
                if str(i-1) in beams.keys():
                    beams[str(i-1)] += prior_paths
                else:
                    beams[str(i-1)] = prior_paths
                if str(i+1) in beams.keys():
                    beams[str(i+1)] += prior_paths
                else:
                    beams[str(i+1)] = prior_paths
                line = line[:i-1] + "|" + line[i:]
                line = line[:i+1] + "|" + line[i+2:]
            else:
                line = line[:i] + "|" + line[i+1:]
    vprint(line)

vprint(beams)

beam_sum = 0
for beam in beams.items():
    beam_sum += beam[1]

print(f"input {filename}:")
print(f"1. star: {times_beam_split}")
print(f"2. star: {beam_sum}")
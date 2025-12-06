from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
print(f"Day 1 with input {filename}")
set_verbose_mode(not "input" in filename)

current_dial_pos, times_dial_at_zero, times_dial_over_zero, i = 50, 0, 0, 0

for line in lines:
    i += 1
    should_inc = 1 if i in [1,3,5,6,8,10] else 0

    prior_pos, prior_times = current_dial_pos, times_dial_over_zero
    current_dial_pos += (1 if line[0] == "R" else -1) * int(line[1:])

    # wenn prior_pos == 0 and current_dial_pos < 0 dann -1
    if prior_pos == 0 and current_dial_pos<0:
        times_dial_over_zero -= 1

    times_dial_over_zero += abs(current_dial_pos//100)

    if (current_dial_pos % 100 == 0 and current_dial_pos < 0) or current_dial_pos == 0:
        times_dial_over_zero += 1

    vprint(f"{i}:\t{prior_pos}\t{line}\t{current_dial_pos}\t({current_dial_pos%100})\t{times_dial_over_zero}\t({times_dial_over_zero-prior_times}/{should_inc})")


    current_dial_pos = current_dial_pos % 100

    if current_dial_pos == 0:
        times_dial_at_zero += 1

print(f"input {filename}: ")
print(f"1. star: {times_dial_at_zero}")
print(f"2. star: {times_dial_over_zero}")
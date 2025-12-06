from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, False)
set_verbose_mode(not "input" in filename)

lines = lines.split(",")

repeating_twice_invalid_ids_sum = 0
multiple_repeats_invalid_ids_sum = set()

for line in lines:
    range_limits = [int(x) for x in line.split("-")]
    for i in range(range_limits[0], range_limits[1]+1):
        s = str(i)
        s_len = len(s)
        s_len_floor_2 = s_len // 2

        # 2. star
        for j in range(2, s_len_floor_2):
            # j=2, 21212121, len=8 (4) -> 21*(8//2) = 21*4 
            if s[:j]*(s_len//j) == s:
                multiple_repeats_invalid_ids_sum.add(i)
        if s[0]*(s_len) == s and s_len > 1:
            multiple_repeats_invalid_ids_sum.add(i)

        # 1. star
        if s_len%2==1:
            continue
        if s[:s_len_floor_2] == s[s_len_floor_2:]:
            repeating_twice_invalid_ids_sum += i
            multiple_repeats_invalid_ids_sum.add(i)


print(f"input {filename}: ")
print(f"1. star: {repeating_twice_invalid_ids_sum}")
print(f"2. star: {sum(multiple_repeats_invalid_ids_sum)}")
vprint(multiple_repeats_invalid_ids_sum)
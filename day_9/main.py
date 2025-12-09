from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

print(f"input {filename}:")
print(f"1. star: {0}")
print(f"2. star: {0}")
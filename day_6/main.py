from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode
import re

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

operators = [x.replace(" ","") for x in lines[-1].split(" ") if x in ["*","+"]]
vprint(operators)

# 1st star
sum_of_exercise_answers = 0
numbers_by_line = [[y for y in x.split(" ") if re.match(r"\d+",y)] for x in lines[:-1]]
vprint(numbers_by_line[0])

for i in range(len(numbers_by_line[0])):
    eval_string = ""
    for j in range(len(numbers_by_line)):
        eval_string += numbers_by_line[j][i]+operators[i]
    sum_of_exercise_answers += eval(eval_string[:-1])

# 2nd star
cephalopod_exercise_sum = 0
operators_with_spaces = [x.replace(" ","") for x in lines[-1]]
# Extend to cope with for loop later
# For loop checks for operator to note down up to which point it should note down the numbers.
# This would usually not include the last numbers, but by extending it to the expected amount,
# (one space and another operator) this can be circumvented.
# We do not want the last shadow operator to be included, so we use a dot.
# Could this have been done better? Yes. Was it done this way anyway? Also yes.
operators_with_spaces.append("")
operators_with_spaces.append(".")
lines = [(line + " .") for line in lines]
numbers_by_cephalopod = []

prior_index = 0
for i in range(1,len(operators_with_spaces)):
    if operators_with_spaces[i] in ["*","+","."]:
        numbers_in_block = []
        for j in range(prior_index,i-1):
            number = []
            for k in range(len(lines)-1):
                number.append(lines[k][j])
            vprint(number, prior_index, j, i-1)
            numbers_in_block.append(int("".join(number)))
        numbers_by_cephalopod.append(numbers_in_block)
        prior_index = i

vprint(numbers_by_cephalopod)

for i in range(len(numbers_by_cephalopod)):
    eval_string = ""
    for j in range(len(numbers_by_cephalopod[i])):
        eval_string += str(numbers_by_cephalopod[i][j])+operators[i]
    cephalopod_exercise_sum += eval(eval_string[:-1])

print(f"input {filename}:")
print(f"1. star: {sum_of_exercise_answers}")
print(f"2. star: {cephalopod_exercise_sum}")
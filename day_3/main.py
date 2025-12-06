from util import read_from_file_and_split_lines_by_linebreak, get_current_filename, vprint, set_verbose_mode

filename = get_current_filename()
lines = read_from_file_and_split_lines_by_linebreak(filename, True)
set_verbose_mode(not "input" in filename)

two_bank_joltage = 0
twelve_bank_joltage = 0

for line in lines:
    vprint(line)

    # erst biggest finden, wenn pos = len-1
    # - davor nochmal biggest suchen
    # wenn nicht,
    # - danach nochmal biggest suchen

    line_as_int_arr = [int(x) for x in line]
    biggest, biggest_pos = 0, []
    for i in range(len(line_as_int_arr)):
        if line_as_int_arr[i]>biggest:
            biggest = line_as_int_arr[i]
            biggest_pos = [i]
        elif line_as_int_arr[i]==biggest:
            biggest_pos.append(i)

    sub_biggest = 0

    if len(biggest_pos) > 1:
        two_bank_joltage += int(str(biggest)+str(biggest))
    else:
        if min(biggest_pos) == len(line_as_int_arr)-1:
            # Edge Case, biggest ganz rechts
            for int_in_line in line_as_int_arr[:-1]:
                sub_biggest = int_in_line if int_in_line>sub_biggest else sub_biggest
            two_bank_joltage += int(str(sub_biggest)+str(biggest))

        else:
            # Normaler Case, hinter biggest schauen
            for int_in_line in line_as_int_arr[min(biggest_pos)+1:]:
                sub_biggest = int_in_line if int_in_line>sub_biggest else sub_biggest
            two_bank_joltage += int(str(biggest)+str(sub_biggest))


    # 2. star
    # erste biggest in line[:-12] finden (abbruch bei erster 9)
    # - wenn biggest_pos min == -12 (letzte zahl mit 11 nachfolgenden) --> auf die summe, zack
    # sub array dahinter danach betrachten
    # - also dann biggest in line[biggest_pos:-11], dann biggest in line[biggest2_pos:-10] ... etc.
    bank = ""
    left_bound = 0
    line_as_int_arr_length = len(line_as_int_arr)

    for right_bound in range(11,-1,-1):
        biggest, biggest_pos = 0, []

        for i in range(left_bound, line_as_int_arr_length-right_bound):
            if line_as_int_arr[i]>biggest:
                biggest = line_as_int_arr[i]
                biggest_pos = [i]
            elif line_as_int_arr[i]==biggest:
                biggest_pos.append(i)
        
        bank += str(biggest)
        left_bound = min(biggest_pos)+1
    
    vprint(bank)
    twelve_bank_joltage += int(bank)
    
        
print(f"input {filename}: ")
print(f"1. star: {two_bank_joltage}")
print(f"2. star: {twelve_bank_joltage}")
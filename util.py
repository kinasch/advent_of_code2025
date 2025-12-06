verbose_mode = False

def read_from_file_and_split_lines_by_linebreak(filename_relative_path, split=True):
    f = open(filename_relative_path, "r")
    content = f.read()
    if split:
        return content.split('\n')
    else:
        return content

def get_current_filename():
    import sys
    cli_args = sys.argv
    current_day_prefix = cli_args[0].split("\\")[-2]
    filename = f"./{current_day_prefix}/input"
    if len(cli_args) > 1:
        filename = f"./{current_day_prefix}/"+cli_args[1]
    return filename

def set_verbose_mode(flag):
    global verbose_mode
    verbose_mode = flag

def vprint(*args):
    """
    Verbose mode only print
    """
    global verbose_mode
    if verbose_mode:
        print(*args)

if __name__ == "__main__":
    print("Import this!")
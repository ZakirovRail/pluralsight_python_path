def read_txt(fn):
    with open(fn) as f:
        print(f.read())


def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()


def write_new_txt(fn, string):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(string)


def append_line_txt(fn, string):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(string)


# read_txt('../files_to_read/backup.py')
# read_txt_by_line('../files_to_read/backup.py')
# write_new_txt('../files_to_read/exampl.txt', 'This is a new line')
# read_txt('../files_to_read/exampl.txt')
# append_line_txt('../files_to_read/exampl.txt', 'This is an extra line')
#  read_txt('../files_to_read/exampl.txt')

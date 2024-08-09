import os, fnmatch


def match(fld, search):
    # print(os.scandir(fld))
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)


# dirs = os.listdir()
# print([i for i in dirs])

# match('./05_working_with_files/files', '*_file*.*')
# match('../files', '*_file_*.*')
match('../files', '*2_*_*.*')

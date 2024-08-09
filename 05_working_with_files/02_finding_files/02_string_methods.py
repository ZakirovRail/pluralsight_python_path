import os


def end_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)


def starts_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)


# end_with('./files', '.txt')
starts_with('./files', '01_test')

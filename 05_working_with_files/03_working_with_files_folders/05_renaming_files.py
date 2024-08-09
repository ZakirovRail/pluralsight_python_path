import os
from pathlib import Path


def rename_files_1(src, dst):
    os.rename(src, dst)


def rename_files_2(src, dst):
    f = Path(src)
    f.rename(dst)


# rename_files_1('../files/text.txt', '../files/test.txt')
rename_files_1('../files/test.txt', '../files/text.txt')

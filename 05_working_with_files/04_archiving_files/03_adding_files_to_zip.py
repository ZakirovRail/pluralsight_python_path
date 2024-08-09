import os
import zipfile


to_add = ['../files/subfolder/01_test_file.csv',
          '../files/subfolder/01_test_file.txt']


def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            if os.path.isfile(f):
                lst = archive.namelist()
                if f not in lst:
                    archive.write(f)
            else:
                print(f'File exists in zip: {f}')


add_to_zip('../files.zip', to_add, 'a')

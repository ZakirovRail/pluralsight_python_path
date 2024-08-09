import os.path
import zipfile


to_zip = ['../files/subfolder/01_file_test.csv',
          '../files/subfolder/01_file_test.txt']


def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            if os.path.isfile(f):
                try:
                    archive.write(f)
                except FileNotFoundError as e:
                    print(f'Error: {f} : {e.strerror}')
            else:
                print(f'Error: {f} is not a valid file')


create_zip('../files.zip', to_zip, 'w')

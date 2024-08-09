import zipfile


def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
             zinf = archive.getinfo(l)
             print(f'{l} => {zinf.file_size} bytes, {zinf.compress_size} compressed size')


read_zip('../files.zip')

import zipfile


def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)


# extract_file('../files_test.zip', 'files/subfolder/01_file_test.csv', '../extracted/files')
extract_all('../files_test.zip', '../extracted')

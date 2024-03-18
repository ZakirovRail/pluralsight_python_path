import os

# folder = '/Users/rzakirov/Downloads'
#
# entries = os.scandir(folder)
#
# for entry in entries:
#     if os.path.isfile(entry):
#         print('File:', entry.name)
#     if os.path.isdir(entry):
#         print('Directory:', entry.name)
#
# folder_original = '/Users/rzakirov/Downloads'
# folder_destination = '/Users/rzakirov/Downloads/CleanedUp'
#
# location_original = os.path.join(folder_original, 'new.txt')
# location_destination = os.path.join(folder_destination, 'new.txt')


# ==============================================================================================================
folder_original = '/Users/rzakirov/Downloads'
folder_destination = '/Users/rzakirov/Downloads/CleanedUp'

os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)






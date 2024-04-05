file_handle = open('mbox-short.txt') # in order to open the file, we must run the code at the folder where the file is placed
# print(file_handle)

for line in file_handle:
    line = line.rstrip()
    print(line.upper())
file_handler = open('./Exercise_06/mbox-short.txt')

for line in file_handler:
    
    line = line.rstrip()
    words = line.split()

    # Guardian pattern in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue

    print(words[2])
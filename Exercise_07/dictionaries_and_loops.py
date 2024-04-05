file_name = input("Enter file: ")

if len(file_name) < 1:
    file_name = "clown.txt"

file_handler = open(f"./Exercise_07/{file_name}")

# dict()
dictionary = {}

for line in file_handler:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # idiom: retrieve/create/update counter
        dictionary[word] = dictionary.get(word, 0) + 1

# finding the most common word
largest = -1
for key, value in dictionary.items():
    if value > largest:
        largest = value
        theword = key  # capture/remember the key that was largest

print(theword, largest)

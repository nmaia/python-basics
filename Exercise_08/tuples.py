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

# print(dictionary)

# list()
temp = []
for key, value in dictionary.items():
    new_tuple = (value, key)
    temp.append(new_tuple)  # flip the tuple items

temp = sorted(temp, reverse=True)
# print("Sorted:", temp[:5])

for value, key in temp[:5]:  # the 1st 5 items
    print(key, value)

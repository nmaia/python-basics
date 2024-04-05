import urllib.request, urllib.parse, urllib.error

# beyond other features, the lib above creates an abstraction to use sockets, making it simpler

file_handler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# get a list of the ocurrencies for each word in the http response content
counts = {}
for line in file_handler:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

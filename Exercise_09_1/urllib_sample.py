import urllib.request, urllib.parse, urllib.error

# beyond other features, the lib above creates an abstraction to use sockets, making it simpler

file_handler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# print each line of the http response. we could also use the urllib to return the header content as well
for line in file_handler:
    print(line.decode().strip())

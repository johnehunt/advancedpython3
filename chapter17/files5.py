# Alternative to reading lines from a file
# A file object is iterable

file = open('myfile.txt', 'r')

for line in file:
    print(line, end='')

file.close()

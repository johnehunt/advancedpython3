# File type implements the Context Manager Protocol
# can therefore use a file in a with as statement

with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')

print('Done')

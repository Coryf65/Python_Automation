# Automation with Python

# now learning how to write files

# open the file with read permissions
f = open('inputFile.txt', 'r')

# creates a new file
passFile = open('PassFile.txt', 'w')

# now we are tasked to only get the ones who passed
for line in f:
    # each data point is using space as a delimeter
    line_split = line.split()
    # print the line if = P
    if line_split[2] == 'P':
        # write to the file
        passFile.write(line)

f.close()
passFile.close()
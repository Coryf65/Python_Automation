# Automation with Python

# open the file with read permissions
f = open('inputFile.txt', 'r')

# creates a new file
passFile = open('PassFile.txt', 'w')
failFile = open('FailFile.txt', 'w')


# now we are tasked to only get the ones who passed
for line in f:
    # each data point is using space as a delimeter
    line_split = line.split()
    # print the line if = P
    if line_split[2] == 'P':
        # write to the file
        passFile.write(line)
    else:
        failFile.write(line)
    
f.close()
passFile.close()
failFile.close()
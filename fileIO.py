# Automation with Python

# open the file with read permissions
f = open('inputFile.txt', 'r')

count = 0
# now we are tasked to only get the ones who passed
for line in f:
    # each data point is using space as a delimeter
    line_split = line.split()
    # print the line if = P
    if line_split[2] == 'P':
        # print the line
        print(line)

f.close()
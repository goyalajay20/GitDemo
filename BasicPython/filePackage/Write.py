
# for this case no need to close the file
# read the file and store all the lines in list
# reverse the file
# write the list back to files

with open('test.txt','r') as reader:
    content = reader.readlines()
    contents = reversed(content)

    with open('test.txt', 'w') as writer:
        for wrLine in contents:
            writer.write(wrLine)






# first, open the file either to read and write

file = open('test.txt')
#file.read() # read all the content of the file
#print(file.read(10))  # read n number of character by passing parameter
#print("------------------")
#print(file.read())
#print("------------------")
#print(file.readline())
#print(file.readline())


# Print line by line using readLine method
line = file.readline()
while line!="":
    print(line)
    line =file.readline()
file.close()
print("----------------------")
file1 = open('test.txt')
for line in file1.readlines():
    print(line)

file1.close()


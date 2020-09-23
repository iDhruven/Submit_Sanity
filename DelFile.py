a_file = open("File.py", "r")

lines = a_file.readlines()

a_file.close()

del lines[0:2]
#del lines[1]

new_file = open("File.py", "w+")

for line in lines:
    new_file.write(line)

new_file.close()

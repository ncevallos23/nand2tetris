import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

file1_array = []
file2_array = []

f1 = open(file1, "r")
for line in f1:
    file1_array.append(line)
f2 = open(file2, "r")
for line in f2:
    file2_array.append(line)

for line_num in range(0, len(file1_array)):
    if file1_array[line_num] != file2_array[line_num]:
        print("Comparison failed at line " + str(line_num) + ":")
        print(file1_array[line_num])
        print(file2_array[line_num])
        print("")
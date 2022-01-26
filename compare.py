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

print(file1_array[0].strip())

compare = []
compare_num = []

first = True

for line_num in range(0, len(file1_array)):
    for char_num in range(0, len(file1_array[line_num])):
        if file1_array[line_num][char_num] == "*" or file2_array[line_num][char_num] == "*":
            continue
        if file1_array[line_num][char_num] != file2_array[line_num][char_num]:
            if first:
                compare.append(["line " + str(line_num) + ":", file1_array[line_num-1].strip(), file2_array[line_num-1].strip(), ""])
                first = False
            compare.append(["Comparison failed at line " + str(line_num+1) + ":", file1_array[line_num].strip(), file2_array[line_num].strip(), ""])
            compare_num.append(line_num)
            break

for state in compare:
    for a in state:
        print(a)
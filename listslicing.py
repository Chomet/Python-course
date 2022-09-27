listnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# position:    0  1  2  3  4  5  6  7  8   9

# [start_position:end_position:step]
# by default, start position is 0
# if start position is given, it is included in slice
# by default, end position is length of list
# if end position is given, it is not included in slice
# by default, step is 1

print(listnumbers[2:5])  # [3, 4, 5] -> start from 3 until 5 step 1
print(listnumbers[5:])  # [6, 7, 8, 9, 10] -> start from 6 until end step 1
print(listnumbers[:5])  # [1, 2, 3, 4, 5] -> start from start until 5 step 1
print(listnumbers[2:5:2])  # [3, 5] -> start from 3 until 5 step 2
print(listnumbers[3::3])  # [4, 7, 10] -> start from 4 until end step 3
print(listnumbers[5:2:1])  # [] -> nothing is printed (end is bigger than start)

# if negative step is given, then we go from start_position to the left in list
# because of this reason, end position should be always higher than start position if we want to slice stuff
# in this case, by default, start position is length of list
# if start position is given, it is included in slice
# in this case, by default, end position is 0
# # if end position is given, it is not included in slice
print(listnumbers[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] -> start from end until the start step 1
print(listnumbers[5::-2])  # [6, 4, 2] -> start from end until 6 step 2
print(listnumbers[:5:-2])  # [10, 8] -> start from end until 7 step 2
print(listnumbers[8:2:-1])  # [9, 8, 7, 6, 5, 4] -> start from 9 until 4 end step 1
print(listnumbers[3:5:-1])  # [] -> nothing is printed (start is bigger than end)

import time
from binary_search_tree import BinarySearchTree

start_time = time.time()


# Replace the nested for loops below with your improvements

""" Tries 1 and 2 with List storage """
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()


f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

""" Try 1: runs in 6+ seconds """
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print('\n----- Try 1 -----')
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

""" Try 2: runs in 1.4 seconds """
duplicates.clear()
start_time = time.time()

for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)

end_time = time.time()
print('\n----- Try 2 -----')
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


"""-----------------------------------------------"""
"""------- Uncomment below to run Try 3 ----------"""
"""-----------------------------------------------"""


""" Try 3 with double binary tree storage """

start_time = time.time()

""" Binary tree initialization """
b1 = BinarySearchTree('m')
b2 = BinarySearchTree('m')
f = open('names_2.txt', 'r')
[b1.insert(v.lower()) for v in f.read().split("\n")]  # List containing 10000 names
f.close()

f = open('names_1.txt', 'r')
[b2.insert(v.lower()) for v in f.read().split("\n")]  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

""" Try 3: runs in .11 seconds """
b2.for_each(b1.contains, duplicates.append)

end_time = time.time()
print('\n----- Try 3 -----')
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


"""-----------------------------------------------"""
"""------- Uncomment below to run Try 4 ----------"""
"""-----------------------------------------------"""


""" Try 4 with single binary tree storage """

start_time = time.time()

""" Binary tree initialization """
b1 = BinarySearchTree('m')
""" Try 4: runs in .07 seconds"""
f = open('names_2.txt', 'r')
[b1.insert(v.lower()) for v in f.read().split("\n")]  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

f = open('names_1.txt', 'r')
[duplicates.append(v) for v in f.read().split("\n") if b1.contains(v.lower())]  # List containing 10000 names
f.close()

end_time = time.time()
print('\n----- Try 4 -----')
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

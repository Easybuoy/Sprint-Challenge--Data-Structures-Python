import time
import os
from binary_search_tree import BinarySearchTree

start_time = time.time()

firstPath = os.getcwd() + '/names/names_1.txt'
f = open(firstPath, 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

secondPath = os.getcwd() + '/names/names_2.txt'
f = open(secondPath, 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
tree = BinarySearchTree(names_1[0])
for name_1 in names_1:
    tree.insert(name_1)
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_1)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

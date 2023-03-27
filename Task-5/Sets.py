# Creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform union of two sets
set3 = set1.union(set2)
print("Union: ", set3)

# Perform update of set1 with set2
set1.update(set2)
print("Update: ", set1)

# Perform intersection of two sets
set4 = set1.intersection(set2)
print("Intersection: ", set4)

# Perform update of intersection of set1 with set2
set1.intersection_update(set2)
print("Update intersection: ", set1)

# Perform difference between set1 and set2
set5 = set1.difference(set2)
print("Difference: ", set5)

# Perform symmetric difference between set1 and set2
set6 = set1.symmetric_difference(set2)
print("Symmetric difference: ", set6)

# Check if the sets are disjoint
disjoint = set1.isdisjoint(set2)
print("disjoint?: ", disjoint)

# Check if set1 is a superset of set2
superset = set1.issuperset(set2)
print("Is set1 a superset of set2?: ", superset)

# Check if set2 is a subset of set1
subset = set2.issubset(set1)
print("Is set2 a subset of set1?: ", subset)

# Add an element to set1
set1.add(9)
print("Add: ", set1)

# Remove an element from set2
set2.remove(7)
print("Remove 7 : ", set2)

# Discard an element from set1
set1.discard(1)
print("Discard 1: ", set1)

# Pop an element from set2
popped_element = set2.pop()
print("Pop an element from set2: ", popped_element)
print("Set2 after popping: ", set2)

# Delete the entire set1
del set1
print("Set1 has been deleted")

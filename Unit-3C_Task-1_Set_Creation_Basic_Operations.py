# Python program to demonstrate set creation and
# basic set operations: Union, Intersection, Difference

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)
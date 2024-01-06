mySet = {1, 2, 3, 4, 2, 9, 4, 'a', 'b', 'c'}

otherSet = {5, 6, 7, 8, 'c', 'd', 'd'}

mySet.remove(9)

print(mySet)

unionSet = mySet.union(otherSet)

print(unionSet)

intersectionSet = mySet.intersection(otherSet)

print(intersectionSet)
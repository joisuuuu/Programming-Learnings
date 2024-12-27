listDevelopers = ["Joyce", "Adam", "Rachel", "Karl"]

"""All about reading list (start)"""
# [(+index)] > returns item based on positive index
print(listDevelopers[1])

# [(-index)] > returns item based on the negative index
print(listDevelopers[-2])

# [(startIndex:numberOfItems)] > return items starting on the index until the literal number order of (numberOfItems)
print(listDevelopers[1:3])

# [(startIndex:)] > return items starting on the index up until the last item
print(listDevelopers[2:])

# [(:numberOfItems)] > return items starting on the first item until the literal number order of (numberOfItems)
print(listDevelopers[:2])
"""All about reading list (end)"""

# Replace specified index item's value
listDevelopers[3] = "Jen"
print(listDevelopers)

# len > counts all the items in the list
print("This returns the number of item in the list: " + str(len(listDevelopers)))

# count > counts all occurrences of a specific value
print("The occurrence of Joyce is: " + str(listDevelopers.count("Joyce")))

# Append > adds an item at the end of the list
listDevelopers.append("Migz")
print("Added 'Migz' at the end: " + str(listDevelopers))

# insert > adds an item at the specified index in the list
listDevelopers.insert(0, "Meljohn")
print("Added 'Meljohn' at the start: " + str(listDevelopers))

# pop(index) > removes the item based on index
print("Removed index 5: " + str(listDevelopers.pop(5)))

# remove(value) > removes the item based on value
listDevelopers.remove("Meljohn")

# pop() > removes the last item from the list
listDevelopers.pop()

# reverse() > reverses the list
listDevelopers.reverse()

# sort() > sorts the items in the list by asc
listDevelopers.sort()

# sort(reverse=True) > sorts the items in the list by desc
listDevelopers.sort(reverse=True)

# del list[index] > deletes an item based on the index
#del listDevelopers[0]

# del list > deletes the whole list, will return an error if you call/use the list
#del listDevelopers

# clear() > deletes all the items in the list
#listDevelopers.clear()
#print(listDevelopers) # list will print [] as an empty list

# copy > copies the whole list to another list
listDevelopersTemp = listDevelopers.copy()
print("This prints a copy of the list: " + str(listDevelopersTemp.copy()))

# list + list2 > combines two lists
listDepartment = ["SDD", "DTSD"]
print(listDevelopers + listDepartment)

# list.extend(list2) > combines two lists
listDepartment.extend(listDevelopers)
print(listDepartment)

# list.append(list2) > extends list with list2 items (will have list inside a list)
listDepartment.append(listDevelopers)
print(listDepartment)
print(listDepartment[5][0]) # prints the specific value in the 2nd list

"""TUPLES (start)"""
# tuples is the same as list but is read-only, un-assignable and can only delete all items not 1 by 1
# tuples value will be declared as () compared to list which is []
# tuples are usually used in constants. ex: pie, number of months in a year, etc.

# tuple(list) > converts list to tuple
# list(tuple) > converts tuple to list
"""TUPLES (end)"""
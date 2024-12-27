"""
Sets > A partially writable (can add, cannot edit) list
     > Unordered and un-indexed type of list
     > If you add a value twice, it will not add. Value is Unique
"""

setNumbers = { 1, 2, 3, 4 }
setNumbers2 = {}
setNumbers.add(5) # Adds single value
setNumbers.update({5, 6, 7, 8}) # Adds multiple values. Can use {} (set) / [] (list) / () (tuple)
setNumbers.remove(5) # Removes a single value in the set
setNumbers.pop() # Removes the first item in the set
setNumbers.discard(9) # Removes a single value even when the value is not in the set
setNumbers2 = setNumbers.copy() # Copies the set
setNumbers.clear() # Empty the set
print(setNumbers2)

"""union (start)"""
setNumbers = { 1, 2, 3, 4 }
setNumbers2 = { 5, 6, 7, 8 }
print(setNumbers.union(setNumbers2)) # If set is number or float, union will
print(setNumbers2.union(setNumbers)) # order it by ascending

strSetNumbers = { "1", "2", "3", "4" }
strSetNumbers2 = { "5", "6", "7", "8" }
print(strSetNumbers.union(strSetNumbers2)) # If set is string, union will randomly sort the set
"""union (end)"""

"""difference (start)"""
"""returns the set containing values on the left set and not on the right set"""
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.difference(set2))
"""difference (end)"""

"""intersection (start)"""
"""returns a set containing values that exists on both sets"""
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.intersection(set2))
"""intersection (end)"""

"""symmetric_difference (start)"""
"""returns a set containing the combined distinct items, but the item is not in both sets. """
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.symmetric_difference(set2))
"""symmetric_difference (end)"""

"""subset (start)"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {4, 5, 6, 7}
print(set2.issubset(set1)) # Asks if left set is a set in right set
print(set1.issuperset(set2)) # Asks if left set is the main/mother set of the right set
"""subset (end)"""
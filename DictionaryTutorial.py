"""
Dictionary
  > Collection of Key Pairs that is unique, unordered, changeable and indexed.
  > declared as 'dict'
"""
employee1 = {
    "Name":"Joyce",
    "Department":"SDD"
}
employee2 = {
    "Name":"Jester",
    "Department":"Marketing"
}
print(employee1["Name"]) # Returns the value based on the key name
print(employee2.get("Department")) # Returns the value based on the key name

employee1["Gender"] = "Female" # Adds a key pair value to the dictionary
print(employee1)

employee1.pop("Gender") # Removes a key pair value to the dictionary
print(employee1)

print(employee1.keys()) # Returns all keys from the dictionary
print(employee1.values()) # Returns all values from the dictionary

employees = []
employees.append(employee1)
print(employees)
employees.append(employee2)
print(employees)

print(employees[1]["Name"])

"""Nested Dictionary > Dictionary in a dictionary"""
employee1Info = {
    "Age":28,
    "Gender":"Female"
}
employee1["Other Info"] = employee1Info
print(employee1)
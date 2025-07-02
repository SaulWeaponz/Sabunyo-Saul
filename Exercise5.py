# 1.	With reference to the dictionary below, write a python program to print the value of the shoe size. 
# Add this dictionary to your .py file
Shoes ={
 	"brand" : "Nick",
	"color" : "black",
	"size" : 40
	}
print(Shoes["size"])
# 2.	Write a python program to change the value “Nick” to “Adidas”
# 3.	Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
# 4.	Write a python program to return a list of all the keys in the dictionary above.
# 5.	Write a python program to return a list of all the values in the dictionary above.
# 6.	Check if the key “size” exists in the dictionary above.
# 7.	Write a python program to loop through the dictionary above.
# 8.	Write a python program to remove “color” from the dictionary.
# 9.	Write a python program to empty the dictionary above.
# 10.	Write a dictionary of your choice and make a copy of it.
# 11.	Write a python program to show nested dictionaries

# Solutions
# Task 1: Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("1. Shoe size is:", Shoes["size"])

# Task 2: Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("2. Updated brand:", Shoes["brand"])

# Task 3: Add a key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("3. Dictionary after adding type:", Shoes)

# Task 4: Return a list of all the keys
keys = list(Shoes.keys())
print("4. Keys in the dictionary:", keys)

# Task 5: Return a list of all the values
values = list(Shoes.values())
print("5. Values in the dictionary:", values)

# Task 6: Check if the key "size" exists
if "size" in Shoes:
    print("6. The key 'size' exists in the dictionary.")
else:
    print("6. The key 'size' does NOT exist.")

# Task 7: Loop through the dictionary
print("7. Looping through dictionary:")
for key, value in Shoes.items():
    print(f"   {key}: {value}")

# Task 8: Remove "color" from the dictionary
Shoes.pop("color", None)
print("8. Dictionary after removing 'color':", Shoes)

# Task 9: Empty the dictionary
Shoes.clear()
print("9. Dictionary after clearing:", Shoes)

# Task 10: Copy a dictionary of your choice
Person = {
    "name": "Alice",
    "age": 30,
    "country": "Kenya"
}
PersonCopy = Person.copy()
print("10. Original dictionary:", Person)
print("    Copied dictionary:", PersonCopy)

# Task 11: Show nested dictionaries
Nested = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Jane", "age": 28},
    "person3": {"name": "Mike", "age": 22}
}
print("11. Nested dictionary:")
for person, details in Nested.items():
    print(f"   {person} -> {details}")

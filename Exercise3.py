#1.	Use the set() constructor to create a set of 3 of your favorite beverages.
FavouriteBeverages = set(("Twebelelemu","Nile","Guiness"))
print(FavouriteBeverages)
#2.	Use the correct method to add 2 more items to the beverages set.
New = {"Spear", "Express"}
FavouriteBeverages.update(New)
print(FavouriteBeverages)
#3.	Given the set below;
mySet = {"Oven", "kettle", "microwave", "refrigerator"}
#Check if microwave is present in the set.
print("microwave" in mySet)
#4.	Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet)
#5.	Write a python program to loop through the set above.
for x in mySet:
    print(x)
#6.	Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
theSet = {"Saul","Arthur","John","Frank"}
theList = ("Sabunyo","Kbanda")
theSet.update(theList)
print(theSet)
#7.	Write two sets, one containing your ages and the other your first names. Join the two sets.
setOne = {20,21,22}
firstNames = {"Saul","Arthur","John"}
setOne.update(firstNames)
print(setOne)

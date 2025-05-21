Mylist = ["Saul","Frank","Arthur","John","Joel"]
print(Mylist[1])

Mylist[0]="Sabunyo"
print(Mylist)

Mylist.append("Evelyn")
print(Mylist)

Mylist.insert(2, "Bathel")
print(Mylist)

Mylist.pop(3)
print(Mylist)

print(Mylist[-1])

Newlist = ["one","two","three","four","five","six","seven"]
print(Newlist[2:5])

CountryList = ["Uganda","Kenya","Tanzania","DR Congo","Rwanda","Burundi","South Sudan"]
CountryCopy =CountryList.copy()
print(CountryCopy)

print("----------------------------------------------------------------------------------------")
for x in CountryList:
    print(x)
print("----------------------------------------------------------------------------------------")

AnimalList =["Cow","Goat","Sheep","Rabbit","Dog"]
AnimalList.sort()
print(AnimalList)

AnimalList.sort(reverse=True)
print(AnimalList)

NewAnimallist = [x for x in AnimalList if "a" in x]
print(NewAnimallist)


FirstNames = ["Saul","Frank","Arthur","John","Joel"]
SecondNames = ["Sabunyo","Ogwenorwoth","Kaband","Garang","Ariko"]
JoinedList = FirstNames + SecondNames
print(JoinedList)
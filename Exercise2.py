x = ("samsung","iphone","tecno","redmi")
# 1.output favourite phone brand
print("My favourite phone brand is "+ x[0])
# 2. 2nd last item using negative indexing.
print(x[-2])
# 3. Update  iphone to itel
y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)
# 4. Add Huawei
y = list(x)
y.append("Huawei")
x = tuple(y)
print(x)
# 5. Looping through the tuple
for x in x:
    print(x)
# 6. reemoving/deleting the first item in the table
x = ("samsung","iphone","tecno","redmi")
y = list(x)
y.remove("samsung")
x = tuple(y)
print(x)    
# 7. Use a tuple constructor to create a tuple of cities in Uganda.
Cities = tuple(("Kampala","Jinja", "Mbale","Mbarara","Hoima"))
print(Cities)
# 8.unpack the cities.
(Capital, Nile, MasabaLand, BeautyLand, PeaceLand) = Cities
print(Capital)
print(Nile)
print(MasabaLand)
print(BeautyLand)
print(PeaceLand)
#9.  Use a range of indexes to print 2nd, 3rd and 4th cities
Cities = tuple(("Kampala","Jinja", "Mbale","Mbarara","Hoima"))
print(Cities[1:4])
#10.	Write two tuples, one containing your first names and the other your second names. Join the two tuples.
firstNames = ("Saul","Frank","John","Arthur","Joel")
secondNames = ("Sabunyo","Ogwenorwoth","Garang","Kabanda","Ariko")
joinedNames = firstNames + secondNames
print(joinedNames)
#11.	Create a tuple of colors and multiply it by 3.
MyColors = ("Black"," Yellow","Red")
MultipleColors = MyColors * 3
print(MultipleColors)
#12.	Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
y = thistuple.count(8)
print(y)
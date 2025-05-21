x = ("samsung","iphone","tecno","redmi")
print("My favourite phone brand is "+ x[0])
print(x[-2])
y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)
y = list(x)
y.append("Huawei")
x = tuple(y)
print(x)

for x in x:
    print(x)

x = ("samsung","iphone","tecno","redmi")
y = list(x)
y.remove("samsung")
x = tuple(y)
print(x)    

Cities = tuple(("Kampala","Jinja", "Mbale","Mbarara","Hoima"))
print(Cities)

(Capital, Nile, MasabaLand, BeautyLand, PeaceLand) = Cities
print(Capital)
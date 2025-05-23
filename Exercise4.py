#1.	Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
Name = "Saul"
Number = 8
Player = Name +" " + str(Number)
print(Player) 
#2.	Consider the example below;
txt = "      Hello,       Uganda!       "
#Output the string without spaces at the beginning, in the middle and at the end.
print(txt.strip())
#3.	Write a python program to convert the value of ‘txt’ to uppercase.
print(txt.upper())
#4.	Write a python program to replace character ‘U’ with ‘V’ in the string above.
print(txt.replace("U","V"))
#5.	Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
y = "I am proudly Ugandan"
print(y[2:5])
#6.	The piece of code below will give an error when output;
#x = "All "Data Scientists" are cool!" 
#Write a python program to correct it.
x = "All \"Data Scientists\" are cool!"
print(x)
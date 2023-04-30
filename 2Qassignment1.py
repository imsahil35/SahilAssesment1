str = input("Enter a string : ")
str = str.lower()
list = []
for i in str:
    if i not in list:
        list.append(i)
    else:
        pass
finalstr = (",").join(list)
print(finalstr)
    

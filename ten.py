a = [2,3.5,2+5j,True,5,"A"]
b = []                        # Question no:- 7
for i in a:
    if type(i) == int:
        b.append(i)       
print(b)
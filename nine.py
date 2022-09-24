n = int(input("Enter existing element of list ")) 
count = -1                # Question no :- 9
mylist = [1,0,5,1,9,1,2,5]
i = 0
while i < len(mylist):
    if mylist.count(n) == 0:
        print("element is not exist in the list")
        break
    elif mylist[i] == n:
        count += 1
        print("element is",n,"and indices is",count)
    elif mylist[i] != n:
        count += 1
    i += 1
print()
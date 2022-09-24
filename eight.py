l = [1,3,5,2,3,3,6,5]                 # Question no :- 8
a,b,c,d,e = 0,0,0,0,0
i = 0
while i<len(l):
    if l[i] == 1: 
        if a<1:
            print("element is",l[i],"and frequency is",l.count(l[i]))
            a += 1
    elif l[i] == 3: 
        if b<1: 
            print("element is",l[i],"and frequency is",l.count(l[i]))
            b += 1
    elif l[i] == 5: 
        if c<1: 
            print("element is",l[i],"and frequency is",l.count(l[i]))
            c += 1
    elif l[i] == 2: 
        if d<1: 
            print("element is",l[i],"and frequency is",l.count(l[i]))
            d += 1
    elif l[i] == 6: 
        if e<1: 
            print("element is",l[i],"and frequency is",l.count(l[i]))
            e += 1
    i += 1
print()

             
        
        
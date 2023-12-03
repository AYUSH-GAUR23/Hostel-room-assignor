floors = int(input("Enter no of floors in hostel: "))
rooms = int(input("Enter no of rooms in a floor: "))

n = floors*(rooms*4)
print("Student capacity:",n)

l1 = []

for i in range(n):
    name = input("Enter name: ")
    l1.append(name)


l2 = []

l3= ["Bed A","Bed B","Bed C","Bed D"]

for i in range(1,floors+1):
    
    for j in range(1,rooms+1):
        for k in range(len(l3)):
            a =  "Floor no "+str(i)
            b = "Room no "+str(j)
            c = l3[k]
            d = (a,b,c)
            l2.append(d)

dict1 = dict(zip(l1,l2))

for key,value in dict1.items():
    print( key,"---->",value)
        
    

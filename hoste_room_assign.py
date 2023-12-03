floors = int(input("Enter no of floors in hostel: "))  # Takes input from user about hostel details
rooms = int(input("Enter no of rooms in a floor: "))   

n = floors*(rooms*4)
print("Student capacity:",n)                    # calculates capacity of hostel

l1 = []

for i in range(n):
    name = input("Enter name: ")                # Takes input as student name and create a list of it
    l1.append(name)


l2 = []

l3= ["Bed A","Bed B","Bed C","Bed D"]          # bed names in a room 

for i in range(1,floors+1):                    # A list is created which contains tuples as element containing uniqe details
    for j in range(1,rooms+1):
        for k in range(len(l3)):
            a =  "Floor no "+str(i)
            b = "Room no "+str(j)
            c = l3[k]
            d = (a,b,c)
            l2.append(d)

dict1 = dict(zip(l1,l2))                       # A dicttionary is created out of two above lists

for key,value in dict1.items():
    print( key,"---->",value)
        
    

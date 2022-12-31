#we use enumerate function with for loop to track position of our item in iterable
names=["Ankit","sonu","chaubey"]
# pos=0
# for name in names:
#     print(f"{pos} --->{names}")
#     pos +=1

# for pos,name in enumerate(names):
#     print(f"{pos} --->{names}") 


def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1
print(find_pos(names,"abc"))

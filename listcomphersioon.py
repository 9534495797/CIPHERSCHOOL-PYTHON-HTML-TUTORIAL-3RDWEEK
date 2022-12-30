square=[]
for i in range(1,11):
    square.append(i**2)
print(square)


square1=[i**2 for i in range(1,11)]
print(square1)


negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)

negative1=[-i for i in range(1,11)]
print(negative)

names=['harshit','mohit','rohit']
new_list=[]
for i in names:
    new_list.append(i[0])
print(new_list)
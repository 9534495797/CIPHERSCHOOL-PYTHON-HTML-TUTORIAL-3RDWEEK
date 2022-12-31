def is_even(a):
    return a%2==0
numbers=[3,2,4,5,7,1,6,8,0,9]
evens=filter(lambda a:a%2==0,numbers)
for i in evens:
    print(i)

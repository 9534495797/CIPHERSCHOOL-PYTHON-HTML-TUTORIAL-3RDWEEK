numbers=[1,2,3,4]
def square(a):
     return a**2
# print(square(4))

squares=list(map(square,numbers))
print(squares)
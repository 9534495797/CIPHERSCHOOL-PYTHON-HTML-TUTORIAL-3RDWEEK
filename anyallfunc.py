# num1=[2,4,6,8,10]
# num2=[1,2,3,4,5,6]
# even1=[]
# for num in num1:
#     even1.append(num%2==0)
# print(even1)




# def my_sum(*args):
#     total=0
#     for num in args:
#         total +=num
#     return total


# print(my_sum(2,3,4,5))



def my_sum(*args):
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        print("invalid input")

print(my_sum(2,3,4,5,"Ankit"))
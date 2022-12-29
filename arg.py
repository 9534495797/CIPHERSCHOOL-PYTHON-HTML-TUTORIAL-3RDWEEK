def total(a,b):
    return a+b


def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total
print(all_total(1,2,3,4))




def multiply_nums(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply
nums=[2,3,4]
print(multiply_nums(*nums))  #unpack
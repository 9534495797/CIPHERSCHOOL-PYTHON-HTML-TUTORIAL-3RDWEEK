numbers=list(range(1,11))
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)

even_nums=[i for i in numbers if i%2==0]
print(even_nums)


def num_to_string(l):
    return[str(i) for i in l if (type(i)==int or type(i)==float)]
print(num_to_string([True,False,[1,2,3],1,1.0,3]))
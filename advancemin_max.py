# def func(item):
#     return len(item)
# names=["Ankit","Sonu","Vivek","Chaubey"]
# print(max(names,key=func))



students=[
    {'name':'ankit','score':90,'age':20},
    {'name':'amkit','score':80,'age':26}
]
      

print(max(students,key=lambda item:item.get('score'))['name'])



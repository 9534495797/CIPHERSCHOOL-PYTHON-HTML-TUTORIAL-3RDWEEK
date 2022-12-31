# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func(first_name="Ankit",last_name="chaubey")




# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# func(first_name="Ankit",last_name="chaubey")



# def func(name="unknown",age=20):
#     print(name)
#     print(age)
# func("Ankit",22)


# def func(name,*args,last_name="unknown",**kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)
# func("ankit",1,2,3,"chaubey",a=1,b=2)

def func(l,**kwargs):
    if kwargs.get("reverse-str")==True:
        return[name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names=["Ankit","Satya"]
print(func(names,reverse_str=True))

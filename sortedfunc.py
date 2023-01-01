# fruits=["apple","mango","guava"]
# fruits.sort()
# print(fruits)


# fruits=("apple","mango","guava")
# print(sorted(fruits))


guitars=[
    {'model': 'yamha f310', 'price':8500},
    {'model': 'faith naptune', 'price':50000}

]
sorted_guitars=sorted(guitars,key=lambda d:d['price'],reverse=True)
print(sorted_guitars)
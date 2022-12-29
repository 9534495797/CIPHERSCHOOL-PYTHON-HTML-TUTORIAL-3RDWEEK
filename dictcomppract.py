string="harshit"
#{'h':1,'a':1}
word_count={char:string.count(char) for char in string}
print(word_count)


odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)



s={k**2 for k in range(1,11)}
print(s)

names=['harshit','mohit','rohit']
first={name[0] for name in names}
print(first)
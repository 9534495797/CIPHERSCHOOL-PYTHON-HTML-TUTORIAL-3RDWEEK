#square={1:1,2:4,3:9}
square={num:num**2 for num in range(1,11)}
print(square)

square1={f"square of {num} is":num**2 for num in range(1,11)}
print(square1)



square2={f"square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k}:{v}")
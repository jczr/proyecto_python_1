"""
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("fizz")
    else:
        print (i)

"""

for i in range(1, 51):
    print("fizz"*(i%3==0) + "buzz"*(i%5==0) or i)
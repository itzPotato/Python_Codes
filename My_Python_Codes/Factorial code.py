print ("Enter your number for factorial output")
x =  int(input())
f = 1
for n in range(x):
    y = x - n
    f *= y
print ("The factorial of the input number is: " + str(f))

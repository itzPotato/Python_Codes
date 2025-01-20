print ("How many numbers from the fibonacci series would you like")
x = int(input())
a=0
b=1
print (int(a))
print (int(b))
for n in range (2, int(x)):
    c=a+b
    print (c)
    a=b
    b=c
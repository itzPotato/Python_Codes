print ("How many numbers of the fibonacci series do you want?")
x = input ()
a = 0 
b = 1
print (a)
print (b) 
for n in range (2, int(x)):
    c = a + b
    print (c)
    a= b
    b= c


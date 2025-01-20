print("Enter your first number!")
x = input ()
print("Enter your second number!")
y = input ()
print("Enter your third number!")
z = input ()
print("The given three numbers in ascending order are:")
if x<y:
    if x<z:
        if z<y:
            print(str(x)+","+ str(z)+","+ str(y))
        else:
            print(str(x)+","+ str(y)+","+ str(z))
    else:
        print(str(y)+","+ str(x)+","+ str(z))

else:
    print(str(y)+","+ str(z)+","+ str(x))


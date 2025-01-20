print("This program arranges your numbers in ascending order. What is the first number?")
x=float(input())
print("What is your second number?")
y=float(input())
if x>y:
    print(x,"is greater than", y)
elif x<y:
    print(y,"is greater than", x)
else:
    print("Hey! That's not fair! Both the numbers are equal!!!!")
#JaiSrirama
print ("This is a program to guess the number you're thinking of. Rules: Has to be inbetween 1 and 10, Answer the questions with Yes or No, No 0s or Decimals!")
answer1 = input("Enter a Yes when you're ready...")
if answer1 == "yes":
    print ("Is it more less than or equal to 5?")
    answer2 = input()
    if answer2 == "yes":
        print ("Is your number even?")
        answer3 = input()
        if answer3 == "yes":
            print("Is your number even and prime?")
            ans4 = input()
            if ans4 == "yes":
                print ("The number you are thinking of is 2")
            elif ans4 == "no":
                print ("The number you are thinking of is 4")
        elif answer3 == "no":
            print ("Can it be the hypotenuse of a triangle of rational sides")
            ans5 = input()
            if ans5 == "yes":
                print ("The number you are thinking of is 5")
            elif ans5 == "no":
                print("Is the cube of your number 9x3?")
                ans6 = input()
                if ans6 == "yes":
                    print ("The number you are thinking of is 3")
                elif ans6 == "no":
                    print ("The number you are thinking of is 1")
    elif answer2 == "no":
        print("Is the number you are thinking of prime?")
        ans7 = input()
        if ans7 == "yes":
            print("The number you are thinking of is 7")
        elif ans7 == "no":
            print("Is it a perfect square?")
            ans8 = input()
            if ans8 == "yes":
                print("The number you are thinking of is 9")
            elif ans8 == "no":
                print("Is the number you are thinking of a perfect cube")
                ans9 = input()
                if ans9 == "yes":
                    print("The number you are thinking of is 8")
                elif ans9 == "no":
                    print("Is your number divisble by 3?")
                    ans10 = input()
                    if ans10 == "yes":
                        print ("The number you are thinking of is 6")
                    elif ans10 == "no":
                        print("The number you are thinking of is 10")
elif answer1 == "no":
    print("Ok, let's stop here...")
else:
    print("Please enter yes after reloading the program when you're ready...")
    #06-06-23
    #3hrs 0mins
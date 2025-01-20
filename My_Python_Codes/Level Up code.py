print("What is your score?")
score = int(input())
print("How much brick did you collect?")
brick = int(input())
if (score > 100) and (brick > 500):
    print("Yay! You have enough materials to move on to level!")
else:
    print("Oh No! Sorry to break this sad news to you but you don't have a score high enough or enough brick to move on to the next level!")


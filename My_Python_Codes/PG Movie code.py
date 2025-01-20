print("Today we are going to watch one of the world's best movie...Ghosts vs Shadows! But....Hold your horses! It is PG so, I need to know your age... So enter it below...")
x = int(input())
if x>16:
    print("NICE! You're over the age of 16, so you can watch the movie!")
else:
    print("OOOOOOF! You're not over 16! Comeback in",16-int(x),"years!")

import random
hardask = raw_input("Do you want to play on hard difficulty? (y/n)")
rand_num = random.randint(1,100)
hardmaybe = True
if hardask.lower() == "y":
    hardmaybe = True
    print("You are now on hard mode. It is a dynamic mode in which the program adapts to what you choose. My number is from 1-100.")
if hardask.lower() == "n":
    hardmaybe = False
    print("My number is from 1-100. Have fun!")
def Guess():
    ask = int(raw_input("Guess my number!"))
    if ask < rand_num:
        print("My number is greater that that!")
    if ask > rand_num:
        print("My number is smaller than that!")
    if ask == rand_num:
        print("You guessed my number! You win! Maybe it's time to try hard mode?")
        raw_input("Press Enter to close.")
        quit()
def HardGuess():
    global rand_num
    ask = int(raw_input("Guess my number!"))
    assert isinstance(rand_num, object)
    if ask < rand_num:
        if rand_num < 95:
            print("My number is greater that that! I just increased my number by 5!")
            rand_num += 5
        else:
            print("That's not my number! (I won't increase it by 5 because then it will be over 100!)")
    if ask > rand_num:
        if rand_num > 5:
            print("My number is smaller than that! I just decreased my number by 5!")
            rand_num -= 5
        else:
            print("That's not my number! (I won't decrease it by 5 because then it will be negative!)")
    if ask == rand_num:
        print("You guessed my number, in HARD MODE! Awesome job!")
        raw_input("Press Enter to close!")
        quit()
while True:
    if hardmaybe == False:
        Guess()
    if hardmaybe == True:
        HardGuess()

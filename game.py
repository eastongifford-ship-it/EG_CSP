print("Welcome player, what is your name?")
player_name = input()
print("Hello", player_name)
print(player_name, "are you ready to have the battle of your life?")
ready = input().lower()
if ready == "yes":
    print("Good, then let's get started!")
    
elif ready == "no":
    print("You're not ready! Well then, get out of my training center. or pick a color")
    color = input("Choose your color (red, blue, green): ").lower()
    if color == "red":
        print("You have chosen red! A bold choice.")
    elif color == "blue":
        print("You have chosen blue! A calm choice.")
    elif color == "green": 
        print("You have chosen green! A natural choice.")
    else:
        print("That's not a valid color. You get no color.")

    
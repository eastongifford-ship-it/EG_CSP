# EG 7th variables
# egithub connection
print("welcome to the game")
player_name = input("what is your name?")
print("hello", player_name)
print("are you ready to play", player_name)
answer = input("yes or no?")
if answer == "yes":
    print("let's play")
print("game is starting")
print("loading...")
print("game loaded")
print("okay 3..2..1..go!")
print("you are in a dark room")
print("you have two options")
print("1. left")
print("2. right")
print("which option do you choose?")
answer = input("left or right?")
if answer == "left":
    print("you have entered a room full of fire")
    print("you are dead")
    if answer == "right":
        print("you have entered a room full of water")
        print("you are alive")
        print("then you see a monster coming towards you")
player_health = 100
monster_health = 100

while monster_health > 0 and player_health > 0:
    print(f"Your health: {player_health}")
    print(f"Monster health: {monster_health}")
    answer = input("Choose your attack (punch or kick): ")
    if answer == "punch":
        monster_health -= 20
        print("You punched the monster! Monster lost 20 health.")
    elif answer == "kick":
        monster_health -= 30
        print("You kicked the monster! Monster lost 30 health.")
        player_health -= 20
        print("The monster attacked you! You lost 20 health.")
    else:
        print("Invalid attack. Try again.")
    print()  # Blank line for readability

if monster_health <= 0:
    print("You have defeated the monster!")
    print("Congratulations", player_name)
elif player_health <= 0:
    print("You have been defeated by the monster.")
    print("okay, see you next time", player_name)





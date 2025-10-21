# LC RV EG CP AS 7th Group Game 
# Jobs:
# Lindon- Ask Questions
# Alexa- Directions/corrections
# Easton- Print
# Fernando/Ciara- Situations


import time #Lindon
 # Lindon and Easton
spear = False
medkit = False
def stop(num):
    print("...")
    time.sleep(num)

def game():

    name = input("Welcome to our game what is your name\n").strip().capitalize()
    print("hello " + name)
    while True:
        direction1 = input('You arive at a dark forest with three ways, (Right, Left, and Forward) which will you take: ').capitalize()# Easton
        if direction1 in ["Right", "Left", "Forward"]:
            break
        else:
            print("It must be Right, Left, or Forward")
    if direction1 == "Right":
        print('You come upon a math wizard in order to pass by you must awnser his equation.')
        number = int(input("What's 60 + 7: "))#Fernando and ciara
        if number == 67:
            print("You are correct! Here is a spear you may need this in the future.")
            spear = True
            while True:
                direction3 = input("You like to you start walking and you come across another turn.(Right, Left, and Forward): ").capitalize()# Alexa added the word "and" and space between : and ) # easton
                if direction3 in ["Right", "Left", "Forward"]:
                    break
                else:
                    print("It must be Right, Left, or Forward")
            if direction3 == "Right":
                print("you fell down a hole") # Easton Lindon and Alexa
                stop(1)
                stop(1.5)
                stop(2)
                print("Good job you finished at Wonderland, thought you where dead huh well nope!! You got the Wonderland ending!!")# Alexa added Wonderland to the print statement
                game()
            elif direction3 == "Left":
                while True:
                    cabin = input("You come a cross an abandoned cabin and look into through the window and you see no one inside would you like to enter?: ").capitalize()# easton and lindon
                    if cabin in ["Yes", "No"]:
                        break
                    else:
                        print("You must say Yes or No.")
                if cabin == "Yes":
                    print("Well you enter and see a bed and take a nap.")
                    ("ZZZ")
                    stop(2)
                    print(f"Welp you never woke up!")#lindon
                    game()
                elif cabin == "No":
                    print("You take to long and end up getting attacked by a bear unless you have a spear")# lindon
                    if spear == True:
                        stop(4)
                        print("Good job you defeated the bear and move on.") # Alexa fixed "Defeated"
                    while True:
                        move = input("Would you like to move on or live in the cabin ").capitalize()
                        if move in ["Live", "Move on"]:
                            break
                        else:
                            print("You must say, Live or Move on")
                    if move == "Live":
                        print("Congrates you beat the game!!")
                        game()
                    elif move == "Move on":
                        print("You traveled the forest and come across a man with a question!")
                        answer = input("How many states are in the USA ")#fernado and ciara
                        if answer == "50":
                            print("You got it correct! king 7w7!")
                            stop(2)
                            print("You got the question right but he got mad at you and stabbed you!")
                            game()
                        else:
                            print(f"you are not correct and he kills you.")
                            game() 
        else:
            print("You got it wrong and died")

    elif direction1 == "Forward":# Alexa
        print(f'You have stumbled on some rocks and fell off a cliff.')
        game()
    elif direction1 == "Left":# Easton and Alexa
        print('Good job you avoided the first obstical and gained a spear') # Alexa fixed the grammer to the word "avoided"
        spear = True
    while True:
        direction2 = input('after a while you find a fork in the road which direction will you choose. left or right: ').capitalize()# easton
        if direction2 in ["Left", "Right"]:
            break
        else:
            print("You must say, Left or Right.")
    if direction2 == "Left":
        print("You come across a drunk man!?")

        pais = input("De que pais eres? ")#fernando and Ciara
        if pais == "USA":
            print("Correcto, sigue tu camino.")
            stop(2)
            print("Well you beat the game congrates!")
        else:
            print(f"ight u not from there.(Then he stabs you.)")# fernando and ciara
            game()

    elif direction2 == "Right":
        while True:
            chest1 = input('You come across a strange chest, do you wish to open it? ').capitalize()# Lindon
            if chest1 in ["Yes", "No"]:
                break
            else:
                print("You must say, Yes or No")
        if chest1 == "Yes":
            while True:
                item1=input("as you come close to the chest, you hear a strange noise. You are fearfull so you act fast. You only take one item, which do you choose? The spear or the medkit: ").capitalize() # Alexa fixed the grammar # easton
                if item1 in ["Spear", "Medkit"]:
                    break
                else:
                    print("You have to choose Spear or Medkit")
            if item1 == "Spear":
                print('You take the spear as fast as you can and run')
                spear =True
                print('As you are walking you see a bridge')# Easton
                while True:
                    bridge=input('the bridge is making some weird nosies, are you sure you want to cross? ').capitalize()#easton
                    if bridge in ["Yes", "No"]:
                        break
                    else:
                        print("You must say, Yes or no.")
                if bridge=="Yes":
                    print('good thing you trusted your gut! You made it across the bridge safely and beat the game')#Easton
                elif bridge=='No':
                    print(f'man you stupid infact you so stupid that you get eaten by a shark')#Easton
                    game()
            elif item1=="Medkit":
                print('As you are walking you see a bridge')#Easton
                while True:
                    bridge2=input('the bridge looks scary are you sure you want to cross ').capitalize()#Easton
                    if bridge2 in ["Yes", "No"]:
                        break
                    else:
                        print("You must say, Yes or No.")
                if bridge2=="Yes":
                    print(f'you fall through the bridge and died')#Easton
                    game()
                elif bridge2=="No":
                    print('you swim safely across and beat the game')# Easton
        elif chest1 == "No":
            print("ok maybe you got lucky, or maybe not, I don't know")
            while True:
                moveing =  input("You come across a turn and and no other way would you like to move on? ").capitalize()
                if moving in ["Yes", "No"]:
                    break
                else:
                    print("You must say, Yes or no.")
            if moveing == "Yes":
                print("A nerd comes up to you and asked?")
                number = input("What's the tuffest number? ")#ciara and fernando
                if number == "67":
                    print("you are correct and tuff!")
                    stop(3)
                    Print("Well congrats you win")
                else:
                    print(f"boi you died for not being tuff.")
                    game()
            elif moveing == "No":
                print(f"You dumb dumb, you died")
                game()
game()
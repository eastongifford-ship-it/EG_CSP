#eg 7th functions

#def welcome():
   # name=input("what is your name")
    #print('hello')
#print("hello")
#welcome()

def add(number, number_two):
    number+= number_two
    print(number)
num_one=12
mum_two=3
import random



strength = roll(0)
dex= roll(1)
smarts= roll(1)
isma=roll(0)
def roll(mod):
    return random.randint(2,18)+mod
print(f"strength: {strength}\ndex: {dex}\nInt: {smarts}\nChar: {isma}")

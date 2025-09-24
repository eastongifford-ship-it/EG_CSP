# eg 7th team game text based adventure game

age = int(input("how old are you"))

if age >= 4 and age <= 14:
    print("you can go to school")
elif age == 15:
    print("you can have a permit")
elif age <= 17 and age >= 16:
    print('you can have a licence ')
elif age <=3:
    print('no your to young')
else:
    print("you can vote")
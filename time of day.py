# EG 7th time of day

time = int(input("what time is it"))
if time >=17 and time <= 24:
    print("good evening")
elif time <= 11 and time > 0:
    print("good morning")
elif time >= 12 and time <=16:
    print('good afternoon')
else:
    print('please enter a valid time')

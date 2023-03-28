import random
# while True:
print("welcome to the dice simulator!!!")
start=input('Type "start" to begin:')
if start.lower()=="start":
    while True:
        x=random.randint(1,7)
        y=random.randint(1,7)
        print(f'your roll is {x} and {y}')
        roll=input("type roll to roll again or anything else to exit:")
        if roll.lower() != 'roll':
            break
        else:
            continue
else:
    print("invalid input!!")



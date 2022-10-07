import random

def npc(mood):
    num = random.randrange(0,100)
    print("this is num",num)
    if num <=20:
        print("Bro shorts right?!")
        
    elif num <=30 and num > 20:
        print("im not slippy or falco")
        
    elif num <= 45 and num > 30:
        print("science? Never heard of her")
        
    elif num <= 80 and num > 45:
        print("I live in a manhole")
        
    else:
        print("I used to be an adveturer like you, but then I had to use the bathroom really bad")
        
    if num%2 == 0:
        mood = True
        return mood
    elif num%2 == 1:
        mood = False
        return mood



gold = 100

sus = True

for i in range(5):
    npc(sus)
    print(gold)
    if sus is True:
        print("shmoney$$$$$")
        gold += random.randrange(1,60)
    elif sus is False:
        print("bye bye money")
        gold -= random.randrange(1,60)
        
#I gave up C++ is better idk why it wont work--------------------------------
        
x = input("gimmie band 1")
y = input("gimmie band 2")
z = input("gimmie band 3")

bands = [x,y,z]
print(bands[1])

food = input("gimmie food")
food2 = input("gimmie food")
food3 = input("gimmie food")
food4 = input("gimmie food")
food5 = input("gimmie food")

meal = (food,food2,food3,food4,food5)
print(meal(4))

print("I cant rember dictionary")

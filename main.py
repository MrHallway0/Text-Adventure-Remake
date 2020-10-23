'''
____________________________________
Project   | Text adventure remake
Programer | Mr. Hallway
Version   | Alpha 0.1
____________________________________
'''

# Set settings to defualt
friends = 0

# add/remove to friends score
def addFriend(int(num)):
  try:
    friends = friends + num
    print("You now have " + str(friends) + "!")
  except:
    print("DEBUG: ERROR could not convert `num` to int check that it's given in all times it's told to run or that it's not messed with... Adding one to `friends`")
    friends = friends + 1
    print("You now have " + str(friends) + "!")

# Get things that are needed!
from time import sleep as wait

# Death actions
def deadForGood():
  print("You go home. Plop down and die at an old age...")

# Break in text
def break(time):
  try:
    time.sleep(time)
  except:
    time.sleep(0.5)
  print("")

# Y,N Question define
def yn(str(q)):
  answer = str(input(q + " (y,n)")).lower()

# Ask for username
name = input('''Welcome! Please enter your name...

''')

wait(0.5)

# Intro
print('''Welcome, ''' + name + '''!
I hope you enjoy this game a lot!
''')

wait(0.5)

print('''
You at your small humble home on a bright sunny day.
''')

wait(0.5)

print('''You walk outside into the hot heat to get your daily mail.
''')

wait(0.5)

print('''Inside is your overdue taxes and a letter...''')

wait(0.25)

print(''' A letter about your late grandfather's will's.''')

wait(0.5)

print('''Your grandfather owned a great farm and it's being passed down to you!
''')

wait(0.75)

# Ask if user wishes to go...
goQ = input('''You have the choice to go... (y,n)
''').lower()

if goQ == "y":
  print("You pack your bags get into your small beetle and drive on")
  break(0)
  for i in range(0,3):
    print("Driving...")
    break(0.25)
  
  print("It's late by the time you get to the barn. Although the people in the town heard a car, witch doesn't happen often.")
  break()
  print("You are greeted.")
  yn("Do you leave them and just go inside the home?")
  if answer("y"):
    addFriend(3)
    
    print("You are spending time with your new friends...")
    break(2)
  
  else:
    addFriends(0)
    
  print("You sleep through the night...")
  break(2)

else:
  deadForGood()

print("THANK YOU FOR USING THE BETA! I have more to the story it's just not added yet! :)")

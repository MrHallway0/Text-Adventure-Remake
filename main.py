'''
____________________________________
Project   | Text adventure remake
Programer | Mr. Hallway
Version   | Alpha 0.1
____________________________________
'''

# Get things that are needed!
from time import sleep as wait

# Death actions
def deadForGood():
  print("You go home. Plop down and die at an old age...")

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
  print("You go...")

else:
  deadForGood()

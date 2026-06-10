print("Alien 1:")
alien_colour = 'green'
if alien_colour == 'green':
    print("You just earned 5 points!")

alien_colour = 'red'
if alien_colour == 'green':
    print("You just earned 5 points!")

#Else if chain:
print("\nAlien 2:")
alien_colour = 'yellow'
if alien_colour == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
    
alien_colour = 'green'
if alien_colour == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
    
#Alien 3
print("\nAlien 3:")

alien_colour = 'green'

if alien_colour == 'green':
    print("You just earned 5 points for shooting the green alien!")
elif alien_colour == 'red':
    print("You just earned 15 points for shooting the red alien!")
else:
    print("You just earned 10 points for shooting the yellow alien!")

alien_colour = 'yellow'

if alien_colour == 'green':
    print("You just earned 5 points for shooting the green alien!")
elif alien_colour == 'red':
    print("You just earned 15 points for shooting the red alien!")
else:
    print("You just earned 10 points for shooting the yellow alien!")

alien_colour = 'red'

if alien_colour == 'green':
    print("You just earned 5 points for shooting the green alien!")
elif alien_colour == 'red':
    print("You just earned 15 points for shooting the red alien!")
else:
    print("You just earned 10 points for shooting the yellow alien!")
"""Copies a list of favourite foods into a new list, appends a
different item to each, then prints both lists."""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)

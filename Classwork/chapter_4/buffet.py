foods = ("pasta", "steak", "chicken", "fish", "seafood")
# foods[0] = "pizza" #intentional type error
print("Original menu:")
for food in foods:
    print(food.title())
foods = ("pizza", "steak", "chicken", "fish", "oysters")
print("\nUpdated menu:")
for food in foods:
    print(food.title())
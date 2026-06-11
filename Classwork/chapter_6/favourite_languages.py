favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }
# language = favourite_languages['sarah'].title()
# print(f"Sarah's favourite langauge is {language}")

for name, lang in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {lang.title()}.")

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi, {name.title()}!")

    if name in friends:
        lang = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {lang}!")

if 'erin' not in favourite_languages.keys():
            print("\nErin, please take our poll!")
print()
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

#Using set() to build a set from unique items in the collection.   
print("\nThe following languages have been mentioned:")
for lang in set(favourite_languages.values()):
    print(lang.title())
#building a set directly using braces and seperating the elements with commas:
#lang = {'python', 'rust', 'python', 'c'}
#print(lang) >>> {'rust', 'python', 'c'}
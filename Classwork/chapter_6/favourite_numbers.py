people_fav_num = {
    'jackson': [42, 21],
    'james': [12, 873],
    'michael': [813, 421],
    'jadon': [19, 27],
    'joel': [81, 9],
}

for person, nums in people_fav_num.items():
    print(f"{person.title()}'s favourite numbers are: "
          "{' and '.join(map(str, nums))}\n")

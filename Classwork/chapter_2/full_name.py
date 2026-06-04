#Summary: This code defines two variables, first_name and last_name, 
# storing the strings "ethan" and "smith" respectively. 
# It then combines them into a single full_name variable using an f-string, 
# and formats it with .title() to capitalize each word when building a greeting message. 
# Finally, it prints that message to the console, outputting Hello, Ethan Smith!

first_name = "ethan"
last_name = "smith"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
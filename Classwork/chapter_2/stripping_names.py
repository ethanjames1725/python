"""Summary: This code demonstrates how to use the .lstrip(), .rstrip(),
and .strip() string methods to remove whitespace from a string.
The variable name is assigned a string with leading and trailing
whitespace, including newline and tab characters.
The code then prints the original string, followed by the results of
applying each of the three methods
to show how they remove whitespace from different parts of the string.
.lstrip() removes leading whitespace,
.rstrip() removes trailing whitespace, and .strip() removes both leading
and trailing whitespace."""

name = " \n\tJohn Doe\n\t "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

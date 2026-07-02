"""Prompt the user for a favourite book title and print a sentence
announcing it, demonstrating a function that takes one argument."""


def favourite_book(title):
    """Display favourite book title"""
    print(f"One of my favourite books is {title.title()}")


favourite_book(input("What is one of your favourite books?"))

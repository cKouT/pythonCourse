# coding=utf-8

"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
name = "éric"
name = name.title()

print("Hello " + name + ", would you like to learn some Python today?")

print(name.upper())
print(name.lower())
print(name.title())

print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

famous_person = "albert einstein"
quote = "A person who never made a mistake never tried anything new."

message = famous_person.title() + 'once said "' + quote + '"'

famous_person = "\t salvador dali \n"

print(famous_person.lstrip() + famous_person.rstrip() + famous_person.strip())

message = message.upper()
print(message)

from bonus.converters14 import convert
from bonus.parsers14 import parse

feet_inches = input('Enter feet and inches: ')

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equals to {result}")

if result < 1:
     print('Kid is too small.')
else:
    print('kid can use the slide.')
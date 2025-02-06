with open('../files/doc.txt') as file:
    file.read()
    content = file.read() # won't be read again, so it'll be empty

print(content)
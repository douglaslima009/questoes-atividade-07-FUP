string = input("Digite uma string: ")
L1 = input("Digite a letra a ser substituída: ")
L2 = input("Digite a letra substituta: ")

newstring = ""
for char in string:
    if char == L1:
        newstring += L2
    else:
        newstring += char

print("String original:", string)
print("String modificada:", newstring)
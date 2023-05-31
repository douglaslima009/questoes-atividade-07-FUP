vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
string = input("Digite uma string: ")

newstring = ''
for letra in string:
    if letra not in vogais:
        newstring += letra
print("String sem vogais:", newstring)
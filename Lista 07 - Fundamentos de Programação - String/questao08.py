string = input("Digite a string original: ")
caractere_antigo = "0"
caractere_novo = "1"

newstring = ""
for char in string:
    if char == caractere_antigo:
        newstring += caractere_novo
    else:
        newstring += char

print("String modificada:", newstring)
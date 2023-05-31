cadeia = input("Digite uma cadeia de caracteres: ")
cadeia_maiuscula = ""

for caractere in cadeia:
    if 'a' <= caractere <= 'z':
        caractere = chr(ord(caractere) - 32)
    cadeia_maiuscula += caractere

print("Os caracteres da cadeia em maiúsculo:", cadeia_maiuscula)
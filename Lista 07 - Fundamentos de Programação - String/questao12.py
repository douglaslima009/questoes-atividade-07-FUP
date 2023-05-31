entrada = input("Digite uma cadeia de caracteres: ")
resultado = ""

for char in entrada:
    if 'a' <= char <= 'z':
        diff = ord('A') - ord('a')
        novo_valor_ascii = ord(char) + diff
        char = chr(novo_valor_ascii)
    resultado += char
print("Resultado: ", resultado)
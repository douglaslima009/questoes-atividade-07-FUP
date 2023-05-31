string = input("Digite a string: ")
count = 0

for char in string:
    if char == '1':
        count += 1

print("Quantidade de uns:", count)

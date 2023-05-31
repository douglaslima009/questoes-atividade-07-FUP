string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if len(string1) != len(string2):
    print("As strings são diferentes.")
else:
    iguais = True
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            iguais = False
            break

    if iguais:
        print("As strings são iguais.")
    else:
        print("As strings são diferentes.")

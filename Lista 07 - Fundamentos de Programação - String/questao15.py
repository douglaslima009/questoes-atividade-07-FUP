s1 = ""

while True:
    print("MENU")
    print("(a) Ler uma string S1")
    print("(b) Imprimir o tamanho da string S1")
    print("(c) Comparar a string S1 com uma nova string S2")
    print("(d) Concatenar a string S1 com uma nova string S2")
    print("(e) Imprimir a string S1 de forma reversa")
    print("(f) Contar quantas vezes um dado caractere aparece na string S1")
    print("(g) Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2")
    print("(h) Verificar se uma string S2 é uma substring de S1")
    print("(i) Retornar uma substring da string S1")
    print("(q) Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == 'a':
        s1 = input("Digite a string S1 (tamanho máximo de 20 caracteres): ")
    elif opcao == 'b':
        tamanho = len(s1)
        print("O tamanho da string S1 é:", tamanho)
    elif opcao == 'c':
        s2 = input("Digite a string S2: ")
        if s1 == s2:
            print("As strings S1 e S2 são iguais.")
        else:
            print("As strings S1 e S2 são diferentes.")
    elif opcao == 'd':
        s2 = input("Digite a string S2: ")
        s1_s2 = s1 + s2
        print("A concatenação de S1 e S2 é:", s1_s2)
    elif opcao == 'e':
        s1_reversa = s1[::-1]
        print("A string S1 de forma reversa é:", s1_reversa)
    elif opcao == 'f':
        caractere = input("Digite o caractere a ser contado: ")
        contador = s1.count(caractere)
        print("O caractere", caractere, "aparece", contador, "vezes na string S1.")
    elif opcao == 'g':
        c1 = input("Digite o caractere a ser substituído: ")
        c2 = input("Digite o caractere de substituição: ")
        s1_substituida = s1.replace(c1, c2, 1)
        print("A primeira ocorrência do caractere", c1, "foi substituída pelo caractere", c2 + ".")
        print("A string S1 modificada é:", s1_substituida)
    elif opcao == 'h':
        s2 = input("Digite a string S2: ")
        if s2 in s1:
            print("A string S2 é uma substring de S1.")
        else:
            print("A string S2 não é uma substring de S1.")
    elif opcao == 'i':
        posicao = int(input("Digite a posição inicial da substring: "))
        tamanho = int(input("Digite o tamanho da substring: "))
        substring = s1[posicao : posicao + tamanho]
        print("A substring de S1 é:", substring)
    elif opcao == 'q':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")

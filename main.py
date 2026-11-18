#criar uma lista contendo listas com as coordenadas de cada ponto.
lista_de_pontos = []
num_de_pontos = int(input("Quantos pontos voce deseja inserir?\n"))
for i in range(num_de_pontos):
    ponto = input().split()
    lista_de_pontos.append(ponto)
    lista_de_pontos[i][0] = int(lista_de_pontos[i][0])
    lista_de_pontos[i][1] = int(lista_de_pontos[i][1])

lista_de_conexoes = []

timemanager = 1
while timemanager == 1:
    print("Qual operação você deseja realizar?")
    print("[1]: Adicionar uma conexão entre pontos\n[2]: Calcular uma rota entre cidades\n[3]: Listar os pontos\n[4]: Sair do programa")
    escolha = input("Operação: ")

    if escolha == "1":
        print("\033c", end="")
        ponto_partida = input("Qual é o ponto de partida?\n")
        ponto_chegada = input("Qual é o ponto de chegada?\n")
        conxexao = [ponto_partida,ponto_chegada]
        if conxexao in lista_de_conexoes:
            print("Conexão já existe!")
        else:
            lista_de_conexoes.append(conxexao)
            print(lista_de_conexoes)
    elif escolha == "2":
        print("\033c", end="")
        print("escolheu 2")
    elif escolha == "3":
        print("\033c", end="")
        for i in range(num_de_pontos):
            print(f"{i} : {lista_de_pontos[i]}")
    elif escolha == "4":
        print("\033c", end="")
        print("Obrigado por usar o meu programa!")
        timemanager = 0
    else:
        print("\033c", end="")
        print("Opção Inválida.")



#Fazer outro dict de conexao? Listando as conexoes entre pontos


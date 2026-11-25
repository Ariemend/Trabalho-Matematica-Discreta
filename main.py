import graphfunc as gf


#criar uma lista contendo listas com as coordenadas de cada ponto.
with open("instancia-cidades.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    num_de_pontos = int(linhas[0])
    lista_de_vertices = {}
    lista_de_conexoes = [[] for i in range(num_de_pontos)]
    for i in range(1, num_de_pontos + 1):
        x, y = map(int, linhas[i].split())
        lista_de_vertices[i - 1] = [x, y]


runmanager = 1
while runmanager == 1:
    print("Qual operação você deseja realizar?")
    print("[1]: Adicionar uma conexão entre pontos\n[2]: Calcular a(s) rota(s) entre cidades\n"
    "[3]: Resolver o problema do Caixeiro Viajante\n[4]: Listar os pontos\n[5]: Listar as conexões de um ponto\n"
    "[6]: Verificar as relações\n[7]: Mostrar as distâncias entre os pontos\n"
    "[8]: Sair do programa")
    escolha = input("Operação: ") #Simples menu de terminal

    if escolha == "1":
        print("\033c", end="")
        p_primeiro = int(input("Qual é o número do primeiro ponto?\n")) #escolhendo os pontos em que sera criado uma conexao
        p_segundo = int(input("Qual é o número do segundo ponto?\n"))
        if not (0 <= p_primeiro < num_de_pontos and 0 <= p_segundo < num_de_pontos):
            print("Digite um índice válido.")
        elif p_primeiro == p_segundo:
            print("Não é possível conectar um ponto a ele mesmo.")                 #OBS: assumi que a relacao de conexao é reflexiva, ou seja, todo ponto
        else:                                             # A que conecte com B, B também conecta com A              
            lista_de_conexoes[p_primeiro].append(p_segundo)
            lista_de_conexoes[p_segundo].append(p_primeiro) #propriedade simetrica
            print(lista_de_conexoes)

    elif escolha == "2":
        print("\033c", end="")
        p1 = int(input("Qual é o ponto de origem?\n"))
        p2 = int(input("Qual é o ponto final?\n"))
        caminhos = gf.todos_os_caminhos(p1, p2, lista_de_conexoes)
        if not caminhos:
            print("Caminho inexistente!")
        else:
            print(f"Caminhos de {p1} até {p2}:")
            for c in caminhos:
                comp = gf.comprimento(c,lista_de_vertices)
                print(" -> ".join(map(str, c)),end=" ")
                print(f"| Comprimento : {comp}")
                
    elif escolha == "3":
        print("escolha 3")

    elif escolha == "4":
        print("\033c", end="")
        for i in lista_de_vertices:
            print(f"Ponto {i}: {lista_de_vertices[i]}")

    elif escolha == "5":
        print("\033c", end="")
        ponto = int(input("De qual ponto você deseja saber as conexões?\n"))
        print(f"As conexões são: {lista_de_conexoes[ponto]}")

    elif escolha == "6":
        print("escolha 6")

    elif escolha == "7":
        print("\033c", end="")
        gf.Matriz_Distancias(num_de_pontos,lista_de_vertices)

    elif escolha == "8":
        print("\033c", end="")
        print("Obrigado por usar o meu programa!")
        runmanager = 0
    else:
        print("\033c", end="")
        print("Opção Inválida.")

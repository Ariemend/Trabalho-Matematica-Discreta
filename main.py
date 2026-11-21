import graphfunc as gf


#criar uma lista contendo listas com as coordenadas de cada ponto.
lista_de_pontos = []
num_de_pontos = int(input("Quantos pontos voce deseja inserir?\n"))
lista_de_conexoes = [[] for i in range(num_de_pontos)] #Cria uma lista de listas, cada uma representando um ponto especificado pelo úsuario. Os índices são equivalentes
for i in range(num_de_pontos):
    ponto = input().split()
    lista_de_pontos.append(ponto)                            
    lista_de_pontos[i][0] = int(lista_de_pontos[i][0])  #Cria um dicionario em que a chave é igual ao índice na lista de
    lista_de_pontos[i][1] = int(lista_de_pontos[i][1])  #conexoes, já o conteudo é igual ao ponto no plano cartesiano, representado
lista_de_vertices = dict(enumerate(lista_de_pontos,0))  #por uma lista contendo 2 elementos.



runmanager = 1
while runmanager == 1:
    print("Qual operação você deseja realizar?")
    print("[1]: Adicionar uma conexão entre pontos\n[2]: Calcular uma rota entre cidades\n[3]: Listar os pontos\n[4]: Listar as conexões de um ponto\n[5]: Sair do programa")
    escolha = input("Operação: ") #Simples menu de terminal

    if escolha == "1":
        print("\033c", end="")
        p_primeiro = int(input("Qual é o número do primeiro ponto?\n")) #escolhendo os pontos em que sera criado uma conexao
        p_segundo = int(input("Qual é o número do segundo ponto?\n"))
        if p_primeiro in lista_de_conexoes[p_segundo]:
            print("Conexão já existe!")                   #OBS: assumi que a relacao de conexao é reflexiva, ou seja, todo ponto
        else:                                             # A que conecte com B, B também conecta com A              
            lista_de_conexoes[p_primeiro].append(p_segundo)
            lista_de_conexoes[p_segundo].append(p_primeiro) #propriedade reflexiva
            print(lista_de_conexoes)

    elif escolha == "2":
        print("\033c", end="")
        print("Qual método de busca você quer utilizar?\n")

    elif escolha == "3":
        print("\033c", end="")
        for i in lista_de_vertices:
            print(f"Ponto {i}: {lista_de_vertices[i]}")

    elif escolha == "4":
        print("\033c", end="")
        ponto = int(input("De qual ponto você deseja saber as conexões?\n"))
        print(lista_de_conexoes[ponto])

    elif escolha == "5":
        print("\033c", end="")
        print("Obrigado por usar o meu programa!")
        runmanager = 0
    else:
        print("\033c", end="")
        print("Opção Inválida.")



#https://medium.com/pythoneers/master-the-art-of-graphs-implementation-in-python-5f49ec9ba42b
#https://www.w3schools.com/python/python_dsa_graphs.asp
#https://www.youtube.com/watch?v=rHemTXFJIPM
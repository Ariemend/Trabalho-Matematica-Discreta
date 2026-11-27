import graphfunc as gf
import time

with open("instancia-cidades.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    num_de_pontos = int(linhas[0])
    lista_de_vertices = {} #dicionario, chave é o índice, conteúdo é o ponto
    lista_de_conexoes = [[] for i in range(num_de_pontos)] #lista de listas, cada indice é um ponto. Elementos das listas vão ser os pontos que estam conectados com o ponto daquele índice
    for i in range(1, num_de_pontos + 1):
        x, y = map(int, linhas[i].split())
        lista_de_vertices[i - 1] = [x, y]


runmanager = 1
while runmanager == 1:
    print("Qual operação você deseja realizar?")
    print("[1]: Gerenciar as conexões entre pontos\n[2]: Calcular a(s) rota(s) entre cidades\n"
    "[3]: Listar os pontos\n[4]: Listar as conexões de um ponto\n"
    "[5]: Mostrar as distâncias entre os pontos\n[6]: Sair do programa")
    escolha = input("Operação: ") #Simples menu de terminal

    if escolha == "1":
        print("\033c", end="")
        opcao1 = int(input("[1]: Todos os pontos conectados entre si\n[2]: Criar conexões manuais\n"
        "[3]: Apagar as conexões de um ponto\n[4]: Apagar todas as conexões\n"))
        if opcao1 == 1:
            todos_conectados = True
            for i in range(num_de_pontos):  #limpar todas as conexões para não ter repetição
                lista_de_conexoes[i].clear()      
            for i in range(num_de_pontos):
                for j in range(num_de_pontos):
                    if i == j:
                        pass            #inserindo as conexões nas listas
                    else:
                        lista_de_conexoes[i].append(j)
        elif opcao1 == 2:
            p_primeiro = int(input("Qual é o número do primeiro ponto?\n")) #escolhendo os pontos em que sera criado uma conexao
            p_segundo = int(input("Qual é o número do segundo ponto?\n"))
            if not (0 <= p_primeiro < num_de_pontos and 0 <= p_segundo < num_de_pontos):
                print("Digite um índice válido.")
            elif p_primeiro == p_segundo:
                print("Não é possível conectar um ponto a ele mesmo.")                 #OBS: assumi que a relacao de conexao é reflexiva, ou seja, todo ponto
            elif p_segundo in lista_de_conexoes[p_primeiro]:                                # A que conecte com B, B também conecta com A  
                print("Conexão já existe!")
            else:                                                                                   
                lista_de_conexoes[p_primeiro].append(p_segundo)
                lista_de_conexoes[p_segundo].append(p_primeiro) #propriedade simetrica
        elif opcao1 == 3:
                p_apagar = int(input("De qual ponto você deseja apagar as conexões?\n"))
                lista_de_conexoes[p_apagar].clear() # Apaga todas as conexões de um ponto
                todos_conectados = False 
        elif opcao1 == 4:
            for i in range(num_de_pontos):
                lista_de_conexoes[i].clear() #loop da lógica de apagar as conexões
                todos_conectados = False
        else:
            print("Opção inválida")
        

    elif escolha == "2":
        print("\033c", end="")
        p1 = int(input("Qual é o ponto de origem?\n"))
        p2 = int(input("Qual é o ponto final?\n"))       #Pega o ponto inicial e final
        qtd_pontos = int(input("O caminho deve conter no maximo quantos pontos? "))  #Define o tamanho maximo do caminho entre pontos
        caminhos = gf.caminhos_limitados(p1, p2, lista_de_conexoes, qtd_pontos)
        if not caminhos:
            print("Caminho inexistente!")
            pass
        gf.calculo_combinacao(qtd_pontos,p1,lista_de_conexoes)
        print(f"\nCaminhos de {p1} até {p2}:")
        for c in caminhos:
            comp = gf.comprimento(c,lista_de_vertices)
            print(" -> ".join(map(str, c)),end=" ") #Printar cada um dos caminhos
            print(f"| Comprimento : {comp}")
        time.sleep(3)
                
    elif escolha == "3":
        print("\033c", end="")
        for i in lista_de_vertices: #print da lista basico
            print(f"Ponto {i}: {lista_de_vertices[i]}")

    elif escolha == "4":
        print("\033c", end="")
        ponto = int(input("De qual ponto você deseja saber as conexões?\n"))
        print(f"As conexões são: {lista_de_conexoes[ponto]}") #outro print basico

    elif escolha == "5":
        print("\033c", end="")
        gf.Matriz_Distancias(num_de_pontos,lista_de_vertices)

    elif escolha == "6":
        print("\033c", end="")
        print("Obrigado por usar o meu programa!")
        runmanager = 0
    else:
        print("\033c", end="")
        print("Opção Inválida.")

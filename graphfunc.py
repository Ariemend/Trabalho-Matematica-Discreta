import math

def todos_os_caminhos(p_inicial, p_final, lista_conexoes):
    caminhos = []
    caminho = [p_inicial]
    visitados = {p_inicial}

    def dfs(ponto):
        if ponto == p_final:
            caminhos.append(caminho.copy())
            return
        for vizinho in lista_conexoes[ponto]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                caminho.append(vizinho)
                dfs(vizinho)
                caminho.pop()            # desfaz o passo
                visitados.remove(vizinho)  # libera o ponto para outros caminhos

    dfs(p_inicial)
    return caminhos

def Distancia_Euclidiana(lista_vertices,ponto1,ponto2):
    coord1 = lista_vertices[ponto1]
    coord2 = lista_vertices[ponto2]
    distancia = math.sqrt(((coord1[0] - coord2[0]) * (coord1[0] - coord2[0])) + ((coord1[1] - coord2[1]) * (coord1[1] - coord2[1])))
    distancia = round(distancia,2)
    return distancia

def Matriz_Distancias(num_de_pontos,lista_de_vertices):
    matriz = [[] for i in range(num_de_pontos)]

    for i in range(num_de_pontos):
        for j in range(num_de_pontos):
            matriz[i].append(Distancia_Euclidiana(lista_de_vertices,i,j))
        print(f"{i} : {matriz[i]}")

def comprimento(caminho, lista_vertices):
    return round(sum(Distancia_Euclidiana(lista_vertices, a, b)
                     for a, b in zip(caminho, caminho[1:])), 2)
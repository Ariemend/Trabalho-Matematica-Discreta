import math
import time

def caminhos_limitados(p_inicial, p_final, lista_conexoes, n_cidades):
    caminhos = []
    caminho = [p_inicial]
    visitados = {p_inicial}  

    def dfs(ponto):
        #se já passou do limite, não adianta continuar
        if len(caminho) > n_cidades:
            return
        if ponto == p_final:
            if len(caminho) == n_cidades:   # só aceita se tiver exatamente n cidades
                caminhos.append(caminho.copy())
            return
        for vizinho in lista_conexoes[ponto]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                caminho.append(vizinho)
                dfs(vizinho)
                caminho.pop()
                visitados.remove(vizinho)
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

def calculo_combinacao(qtd_pontos, p_inicial, lista_conexoes):
    lista = []
    j = 0
    for i in lista_conexoes[p_inicial]:
        j += 1
        lista.append(j)
    lista.reverse()
    lista = lista[:qtd_pontos+1]
    print("OBS: A operação possui complexidade:")
    for elemento in lista:
        print(f"{elemento}! ",end=" ")

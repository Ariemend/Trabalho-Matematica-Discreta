def Depth_first_search(p_inicial,p_final,lista_conexoes,vistados=None,caminho=None):
    if vistados is None:
        vistados = set()
    if caminho is None:
        caminho = []

    vistados.add(p_inicial)
    caminho.append(p_inicial)

    if p_inicial == p_final:
        return caminho.copy()
    for vizinho in lista_conexoes[p_inicial]:
        if vizinho not in vistados:
            resultado = Depth_first_search(vizinho,p_final,lista_conexoes,vistados,caminho)
            if resultado != None:
                return resultado
    caminho.pop()
    return None

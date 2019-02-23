# dirigido !
def lista_adjacencia_dirigido(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
    return grafo

# nao dirigido !
def lista_adjacencia_nao_dirigido(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
        grafo[aresta[1]].append(aresta[0])
    return grafo

# Recebe uma lista de adjacencia no formato dicionario
def matriz_adjacencia(lista):
    # Cria a matriz num X num
    matriz = gerar_matriz(len(lista) + 1, len(lista)+ 1)

    # Popula os cabeçalhos
    i = 0
    for key in lista.keys():
        matriz[0][i+1] =  key
        matriz[i + 1][0] =  key
        i += 1

    return matriz

def gerar_matriz (n_linhas, n_colunas):
    matriz = []

    for _ in range(n_linhas):
        matriz.append( [" "] * n_colunas )

    return matriz
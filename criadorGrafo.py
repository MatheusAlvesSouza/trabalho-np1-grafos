# dirigido !
def lista_adjacencia_dirigido_sem_peso(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
    return grafo

# nao dirigido !
def lista_adjacencia_nao_dirigido_sem_peso(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
        grafo[aresta[1]].append(aresta[0])
    return grafo

# dirigido !
def lista_adjacencia_dirigido_com_peso(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append((aresta[1], aresta[2]))
    return grafo

# nao dirigido !
def lista_adjacencia_nao_dirigido_com_peso(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append((aresta[1], aresta[2]))
        grafo[aresta[1]].append((aresta[0], aresta[2]))
    return grafo

# Recebe uma lista de adjacencia no formato dicionario
def matriz_adjacencia_sem_peso(lista):
    # Cria a matriz num X num
    matriz = gerar_matriz(len(lista) + 1, len(lista)+ 1)

    # Popula os cabeçalhos
    i = 0
    for key in lista.keys():
        matriz[0][i+1] =  key
        matriz[i + 1][0] =  key
        i += 1

    # Percorre linhas da matriz
    i = 0
    for linha in matriz:
        # Verifica se é o cabecalho
        if i == 0:
            i += 1
            continue
        # Vertice a ser analisado
        vertice = linha[0]
        # Adjacencias do vertice
        adjacencias = lista[vertice]
        for adjacencia in adjacencias:
            # Num é igual ao numero de ocorrencias de um vertice adjacente
            num = adjacencias.count(adjacencia)
            indice_adjacencia = descobrir_indice(adjacencia, matriz[0])
            # Atribui a matriz
            linha[indice_adjacencia] = str(num)

        i += 1
    return matriz

# Recebe uma lista de adjacencia no formato dicionario
def matriz_adjacencia_com_peso(lista):
    # Cria a matriz num X num
    matriz = gerar_matriz(len(lista) + 1, len(lista)+ 1)

    # Popula os cabeçalhos
    i = 0
    for key in lista.keys():
        matriz[0][i+1] =  key
        matriz[i + 1][0] =  key
        i += 1

    # Percorre linhas da matriz
    i = 0
    for linha in matriz:
        # Verifica se é o cabecalho
        if i == 0:
            i += 1
            continue
        # Vertice a ser analisado
        vertice = linha[0]
        # Adjacencias do vertice
        adjacencias = lista[vertice]
        for adjacencia in adjacencias:
            # Num é igual ao numero de ocorrencias de um vertice adjacente
            num = adjacencia[1]
            indice_adjacencia = descobrir_indice(adjacencia[0], matriz[0])
            # Atribui a matriz
            linha[indice_adjacencia] = str(num)

        i += 1
    return matriz

def gerar_matriz (n_linhas, n_colunas):
    matriz = []

    for _ in range(n_linhas):
        matriz.append( [" "] * n_colunas )

    return matriz

# Interno para descobrir indice
def descobrir_indice (valor, array):
    for indice, var in enumerate(array):
        if var == valor:
            return indice
    return
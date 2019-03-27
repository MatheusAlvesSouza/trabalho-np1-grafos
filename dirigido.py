# Functions dirigido
import criadorGrafo

def sem_peso():
    printarOpcoes(False)

def com_peso():
    printarOpcoes(True)

def printarOpcoes(peso):
    print('________________________')
    print('1 - Lista')
    print('2 - Matriz')
    print('________________________')
    print('Qual deseja inserir :', end=" ")
    op = int(input())

    if peso == False and op == 1:
        # Ex: a b c 
        print('\nInsira os vertices:', end=" ")
        #Array
        lista_vertices = map(str,input().split())
    
        #Ex: 2
        print('Insira o numero de arestas:', end=" ")
        n = int(input())
        print('Insira as adjacencias uma por vez \n(Ex: a b ) \n(Ex: a c )', end="\n")

        keys = [1]
        values = [1]

        for i in range(0,n):
            word = input().split()
            keys.append(word[0])
            values.append(word[1])

        arestas = list(zip(keys, values))
        del arestas[0]

        lista = criadorGrafo.lista_adjacencia_dirigido_sem_peso(lista_vertices, arestas)
        print("\n\n\nLista de adjacência: \n")
        for  row in lista.items():
            print(row, end="\n")
        
        matriz = criadorGrafo.matriz_adjacencia_sem_peso(lista)
        print("\nMatriz de adjacência: \n")
        for row in matriz:
            print(row, end="\n")

        return
    elif peso == False and op == 2:
         # Ex: a b c 
        print('\nInsira os vertices:', end=" ")
        #Array
        lista_vertices = list(map(str,input().split()))
        sub_lista = lista_vertices[:]

        print('Insira as adjacencias uma por vez \n(Ex: a b = 1 ) \n(Ex: a c = 0)', end="\n")
        
        keys = [1]
        values = [1]
        adjacentes = [1]

        i = 0
        for vertice in lista_vertices:
            for indice, sub_vertice in enumerate(sub_lista):
                print(str(vertice) + " " + str(sub_vertice) + " = ", end=" ")
                n = int(input())
                if n > 0:
                    for x in range(0, n):
                        adjacentes.append(str(vertice)+str(sub_vertice))
                        keys.append(vertice)
                        values.append(sub_vertice)
            i += 1

        arestas = list(zip(keys, values))
        del arestas[0]

        lista = criadorGrafo.lista_adjacencia_dirigido_sem_peso(lista_vertices, arestas)
        matriz = criadorGrafo.matriz_adjacencia_sem_peso(lista)
        
        print("\n\n\nMatriz de adjacência: \n")
        for row in matriz:
            print(row, end="\n")

        print("\nLista de adjacência: \n")
        for  row in lista.items():
            print(row, end="\n")

        return
    elif peso == True and op == 1:
        # Ex: a b c 
        print('\nInsira os vertices:', end=" ")
        #Array
        lista_vertices = map(str,input().split())
    
        #Ex: 2
        print('Insira o numero de arestas:', end=" ")
        n = int(input())
        print('Insira as adjacencias com peso uma por vez \n(Ex: a b 3) \n(Ex: a c 1)', end="\n")

        keys = [1]
        values = [1]
        weight = [1]

        for i in range(0,n):
            word = input().split()
            keys.append(word[0])
            values.append(word[1])
            weight.append(word[2])

        arestas = list(zip(keys, values, weight))
        del arestas[0]
        
        lista = criadorGrafo.lista_adjacencia_dirigido_com_peso(lista_vertices, arestas)
        print("\n\n\nLista de adjacência: \n")
        for  row in lista.items():
            print(row, end="\n")
        
        matriz = criadorGrafo.matriz_adjacencia_com_peso(lista)
        print("\nMatriz de adjacência: \n")
        for row in matriz:
            print(row, end="\n")

        return
    else:
        print("Opção indisponivel - Não é possivel converter uma matriz com peso para uma lista")
    return
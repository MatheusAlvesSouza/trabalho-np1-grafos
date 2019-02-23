# Functions grafo não dirigido
import criadorGrafo

def sem_peso():
    printarOpcoes(False)

def com_peso():
    print("Teste com peso")

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

        lista = criadorGrafo.lista_adjacencia_nao_dirigido(lista_vertices, arestas)
        print("\n\n\n\nLista de adjacência: \n")
        for  row in lista.items():
            print(row, end="\n")
        
        matriz = criadorGrafo.matriz_adjacencia(lista)
        print("\nMatriz de adjacência: \n")
        for row in matriz:
            print(row, end="\n")

        return
    return
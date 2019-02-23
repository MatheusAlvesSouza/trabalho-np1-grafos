import naoDirigido as grafosNaoDirigidos
import dirigido as grafosDirigidos

print('________________________')
print('0 - Grafo não dirigido')
print('1 - Grafo dirigido')
print('________________________')
print('Selecione uma opção :', end=" ")
dirigido = int(input())

print('________________________')
print('0 - O caminho não tem peso')
print('1 - O caminho tem peso')
print('________________________')
print('Selecione uma opção :', end=" ")
peso = int(input())

if dirigido == 0 and peso == 0:
    grafosNaoDirigidos.sem_peso()
elif dirigido == 0 and peso == 1:
    grafosNaoDirigidos.com_peso()
elif dirigido == 1 and peso == 0:
    grafosDirigidos.sem_peso()
elif dirigido == 1 and peso == 1:
    grafosDirigidos.com_peso()
else:
    print("Opção inválida!")
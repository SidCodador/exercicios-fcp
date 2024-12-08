import numpy as np

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        print(f'Iteração {i+1}: {lista}')
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

###############################################################

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        print(f'Iteração {i+1}: {lista}')
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

#############################################################

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        resultado = quick_sort(left) + middle + quick_sort(right)
        print(f"Sublista ordenada: {resultado}")
        return resultado
    
#################################################################
#################################################################

def executar_algoritmo():
    print("Selecione o algoritmo de ordenação:")
    print("1 - Bubble Sort")
    print("2 - Selection Sort")
    print("3 - Quick Sort")
    
    escolha_algoritmo = int(input("Digite o número da sua escolha: "))
    
    print("\nSelecione o tipo de lista:")
    print("1 - Lista fixa")
    print("2 - Lista aleatória")
    
    escolha_lista = int(input("Digite o número da sua escolha: "))

    if escolha_lista == 1:
        lista = [5, -3, 8, -6, 2, 7, 4, 1]
    elif escolha_lista == 2:
        N = int(input("\nDigite o tamanho da lista (N): "))
        lista = np.random.randint(-100, 101, N).tolist()
    print(f"\nLista inicial: {lista}")

    if escolha_algoritmo == 1:
        resultado = bubble_sort(lista)
    elif escolha_algoritmo == 2:
        resultado = selection_sort(lista)
    elif escolha_algoritmo == 3:
        resultado = quick_sort(lista)
        return
    
    print(f"\nLista ordenada: {resultado}")

executar_algoritmo()
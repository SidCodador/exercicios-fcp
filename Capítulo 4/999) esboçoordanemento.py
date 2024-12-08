import numpy as np

# Funções de ordenação
def bubble_sort(lista, exibir_passos=True):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        if exibir_passos:
            print(f'Iteração {i+1}: {lista}')
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista, exibir_passos=True):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_index = i
        if exibir_passos:
            print(f'Iteração {i+1}: {lista}')
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def quick_sort(lista, exibir_passos=True):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        resultado = quick_sort(left, exibir_passos) + middle + quick_sort(right, exibir_passos)
        if exibir_passos:
            print(f"Sublista ordenada: {resultado}")
        return resultado

# Funções principais
lista_fixa = [2, 6, 3, 5, 7, 10, 1, 8, 4, 9]
N = [100, 200, 400, 800, 1600]

def chamar_fixa():
    print('Para Bubble Sort, segue o passo a passo:\n')
    bubble_sort(lista_fixa, exibir_passos=True)
    print('\nPara Selection Sort, segue o passo a passo:\n')
    selection_sort(lista_fixa, exibir_passos=True)
    print('\nPara Quick Sort, segue o passo a passo:\n')
    quick_sort(lista_fixa, exibir_passos=True)

def chamar_aleatoria():
    print("\nOrdenação de listas aleatórias:\n")
    for n in N:
        lista_ale = np.random.randint(0, 1000, n).tolist()
        print(f"Lista inicial de tamanho {n}: {lista_ale[:10]}... (mostrando apenas os 10 primeiros elementos)\n")
        
        print("Bubble Sort:")
        resultado_bubble = bubble_sort(lista_ale, exibir_passos=False)
        print(f"Resultado final: {resultado_bubble[:10]}... (mostrando apenas os 10 primeiros elementos)\n")
        
        print("Selection Sort:")
        resultado_selection = selection_sort(lista_ale, exibir_passos=False)
        print(f"Resultado final: {resultado_selection[:10]}... (mostrando apenas os 10 primeiros elementos)\n")
        
        print("Quick Sort:")
        resultado_quick = quick_sort(lista_ale, exibir_passos=False)
        print(f"Resultado final: {resultado_quick[:10]}... (mostrando apenas os 10 primeiros elementos)\n")
        
        print('-' * 50)

# Execução
print("Ordenação de Lista Fixa:\n")
chamar_fixa()

print("\nOrdenação de Listas Aleatórias:\n")
chamar_aleatoria()



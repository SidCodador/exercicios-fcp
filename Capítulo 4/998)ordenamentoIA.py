import numpy as np
import time
import matplotlib.pyplot as plt

def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        print(f'Iteração {i+1}: {lista}')
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_index = i
        print(f'Iteração {i+1}: {lista}')
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

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
    
lista_fixa = [2, 6, 3, 5, 7, 10, 1, 8, 4, 9]
N = [100, 200, 400, 800, 1600]
tempos_bubble = []
tempos_selection = []
tempos_quick = []

def chamar_fixa():
    print('Para Bubble Sort, segue o ordenamento:\n')
    bubble_sort(lista_fixa)
    print('\n')
    print('Para Selection Sort, segue o ordenamento:\n')
    selection_sort(lista_fixa)
    print('\n')
    print('Para Quick Sort, segue o ordenamento:\n')
    quick_sort(lista_fixa)

def chamar_aleatoria():
    for n in N:
        lista_aleatoria = np.random.randint(0, 1000, n).tolist()

        inicio = time.time()
        bubble_sort(lista_aleatoria)
        fim = time.time()
        tempos_bubble.append(fim - inicio)

        inicio = time.time()
        selection_sort(lista_aleatoria)
        fim = time.time()
        tempos_selection.append(fim - inicio)

        inicio = time.time()
        quick_sort(lista_aleatoria)
        fim = time.time()
        tempos_quick.append(fim - inicio)

    plt.figure(figsize=(10, 6))
    plt.loglog(N, tempos_bubble, label="Bubble Sort", marker="o")
    plt.loglog(N, tempos_selection, label="Selection Sort", marker="s")
    plt.loglog(N, tempos_quick, label="Quick Sort", marker="^")
    plt.xlabel("Tamanho da lista (N)")
    plt.ylabel("Tempo (s)")
    plt.title("Tempo de execução dos algoritmos")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

chamar_fixa()
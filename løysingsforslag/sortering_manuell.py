'''
    Skriv en kode som bytter plass på verdiene i lista tall = [3, 4, 1, 2, 5] 
    slik at den blir sortert. Du skal altså sortere lista manuelt.
'''

import timeit

# Boblesortering
def bubble_sort(tall):
    n = len(tall)
    for i in range(n):
        for j in range(0, n-i-1):
            if tall[j] > tall[j+1]:
                tall[j], tall[j+1] = tall[j+1], tall[j]

# Utvalgssortering
def selection_sort(tall):
    n = len(tall)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if tall[j] < tall[min_idx]:
                min_idx = j
        tall[i], tall[min_idx] = tall[min_idx], tall[i]

# Liste som skal sorteres
tall = [3, 4, 1, 2, 5]

# Tid for boblesortering
tid_bubble = timeit.timeit(lambda: bubble_sort(tall.copy()), number=10000)
print(f"Boblesortering tid: {tid_bubble}")

# Tid for utvalgssortering
tid_selection = timeit.timeit(lambda: selection_sort(tall.copy()), number=10000)
print(f"Utvalgssortering tid: {tid_selection}")
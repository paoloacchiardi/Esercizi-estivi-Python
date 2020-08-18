def somma_nidificata(t):
    somma = 0
    for elemento in t:
        for valore in elemento:
            somma += valore
    return somma

def main():
    lista = [[1,2],[3,4,5],[2,0]]
    value = somma_nidificata(lista)
    print(f"{value}")

if __name__ == "__main__":
    main()
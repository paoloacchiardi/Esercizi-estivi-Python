def somma_cumulata(t):
    somma = 0
    index = -1
    t2 = []
    for elemento in t:
        index += 1
        somma += elemento
        t2.append(elemento)
    t2[index] = somma
    return t2
    
def main():
    lista = [1,2,3]
    lista2 = somma_cumulata(lista)
    print(f"origin: {lista}\nnew: {lista2}")

if __name__ == "__main__":
    main()
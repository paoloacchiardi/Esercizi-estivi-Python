from random import randint

def ha_duplicati(lista):
    lista2 = []
    for elemento in lista:
        lista2.append(elemento)
    lista2.sort()
    count = 0
    for elemento in lista2:
        if(count != 0):
            if(lista2[count] == lista2[count-1]):
                return True
        count += 1
    return False

def main():
    studenti = 23
    lista = []
    prob = 0
    for n in range(1,1000):
        trovato = False
        while(not trovato):
            count = 0
            while(count < studenti):
                lista.append(randint(1,365))
                count += 1
            if(ha_duplicati(lista)):
                trovato = True
            prob += 1
            del lista[:]
    statistica = (1000/prob)*100
    print(f"Questa probabilità si genera il {statistica:.2f}% circa delle volte.")

if __name__ == "__main__":
    main()
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
    lista = [1,2,3,4]
    lista2 = [1,2,2]
    if(ha_duplicati(lista)):
        print(f"La lista {lista} ha almeno un elemento duplicato.")
    else:
        print(f"La lista {lista} non ha elementi duplicati.")
    if(ha_duplicati(lista2)):
        print(f"La lista {lista2} ha almeno un elemento duplicato.")
    else:
        print(f"La lista {lista2} non ha elementi duplicati.")

if __name__ == "__main__":
    main()
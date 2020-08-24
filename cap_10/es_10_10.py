def bisezione(lista, parola):
    value = len(lista) 
    value_app = len(lista)
    tro = False
    lista2 = []
    lista2.append(parola)
    count = True
    while(not tro and value_app > 0):
        if((value_app % 2) != 0):
            value_app -= 1
        value_app /= 2
        if(count):
            value -= value_app
        else:
            value += value_app
        if(lista[int(value)] == parola):
            tro = True
        else:
            lista2.append(lista[int(value)])
            lista2.sort()
            if(lista2[0] == parola):
                count = True
            else:
                count = False
            lista2.remove(lista[int(value)])
    return tro

def main():
    file = open('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')
    lista = []
    for riga in file:
        parola = riga.strip()
        lista.append(parola)
    element = input("Inserisci la parola da ricercare:\t")
    if(bisezione(lista,element)):
        print(f"La parola {element} è presente nella lista.")
    else:
        print(f"La parola {element} non è presente nella lista.")

if __name__ == "__main__":
    main()
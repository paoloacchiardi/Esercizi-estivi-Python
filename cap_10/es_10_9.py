def file_to_list_1():
    file = open('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')
    lista = []
    for riga in file:
        parola = riga.strip()
        lista.append(parola)
    return lista

def file_to_list_2():
    file = open('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')
    lista = []
    for riga in file:
        parola = riga.strip()
        lista += [parola]
    return lista

def main():
    lista1  = file_to_list_1()
    for elemento in lista1:
        print(f"{elemento}")
    lista2 = file_to_list_2()
    for elemento in lista2:
        print(f"{elemento}")

if __name__ == "__main__":
    main()
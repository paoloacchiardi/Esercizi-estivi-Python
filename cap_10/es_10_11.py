def parole_bifronte(lista):
    print("Parole bifronte:")
    app = 0
    for element in range(0,len(lista)):
        app = lista[element]
        if(lista.count(app[::-1]) > 0):  #se count > 0 allora l'elemento è nella lista, [::-1] inverte la stringa
            print(f"{lista[element]}")

def file_to_list(indirizzo_file):
    file = open(indirizzo_file)
    lista = []
    for riga in file:
        parola = riga.strip()
        lista.append(parola)
    return lista

def main():
    lista = file_to_list('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')
    parole_bifronte(lista)

if __name__ == "__main__":
    main()
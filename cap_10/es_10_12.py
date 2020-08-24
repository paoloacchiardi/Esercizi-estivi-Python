def file_to_list(indirizzo_file):
    file = open(indirizzo_file)
    lista = []
    for riga in file:
        parola = riga.strip()
        lista.append(parola)
    return lista

def coppie_parole_incastrabili(lista):
    print("Possono incastrarsi:")
    value = 'vghc'
    for element in range(0,len(lista)):
        for count in range(0,len(lista)):
            if(element != count):
                value = lista[element] + lista[count]
            for word in range(0,len(lista)):
                if(sorted(value) == sorted(lista[word])):
                    print(f"{lista[element]} + {lista[count]} = {lista[word]}")
                    break

def main():
    lista = file_to_list('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')
    coppie_parole_incastrabili(lista)

if __name__ == "__main__":
    main()
def dizionario_ruotato(dizionario):
    new_dict = {}
    value = 0
    lista = []
    lista2 = []
    for key in dizionario:
        lista.clear()
        lista = dizionario[key]
        for key2 in dizionario:
            if(dizionario[key] is not dizionario[key2] and len(dizionario[key]) == len(dizionario[key2])):
                count = 0
                inverso = True
                lista2.clear()
                lista2 = dizionario[key2]
                value = ord(lista[count]) - ord(lista2[count])
                count += 1
                while(count < len(lista)):
                    if((ord(lista[count]) - ord(lista2[count])) != value):
                        inverso = False
                        break
                    else:
                        count += 1
                if(inverso):
                    new_dict[key] = []
                    new_dict[key].append(key2)
    return new_dict

def list_to_dict(lista):
    dizionario = {}
    for element in lista:
        dizionario[element] = []
        for lettera in element:
            dizionario[element].append(lettera)
    return dizionario

def main():
    lista = []
    fin = open('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')
    for riga in fin:
        parola = riga.strip()
        lista.append(parola)
    dizionario = list_to_dict(lista)
    dizionario_ruotabile = dizionario_ruotato(dizionario)
    print(f"Parole ruotate:\n{dizionario_ruotabile}")

if __name__ == "__main__":
    main()
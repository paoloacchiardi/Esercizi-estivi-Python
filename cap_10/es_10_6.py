def anagramma(stringa1,stringa2):
    lista1 = list(stringa1)
    lista2 = list(stringa2)
    lista1.sort()
    lista2.sort()
    count = -1
    for elemento in lista1:
        count += 1
        if(lista1[count] != lista2[count]):
            return False
    return True

def main():
    if(anagramma("mari","armi")):
        print("'mari' e 'armi' sono anagrammi.")
    else:
        print("'mari' e 'armi' non sono anagrammi.")
    if(anagramma("ciao","pallone")):
        print("'ciao' e 'pallone' sono anagrammi.")
    else:
        print("'ciao' e 'pallone' non sono anagrammi.")

if __name__ == "__main__":
    main()
def alfabetica(parola):
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    valore = 0
    count = 0
    for lettere in parola:
        count = 0
        for lettera in alfa:
            count += 1
            if(lettera == lettere):
                if(valore > count):
                    return False
                valore = count
                break
    return True

def main():
    fin = open('words.txt')
    counter = 0
    for riga in fin:
        parola = riga.strip()
        if(alfabetica(parola)):
            counter += 1
    print(f"Ci sono {counter} parole 'alfabetiche'.")

if __name__ == "__main__":
    main()
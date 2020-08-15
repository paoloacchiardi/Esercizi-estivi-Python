def evita(parola, vietate):
    for lettere in vietate:
        for lettera in parola:
            if(lettera == lettere):
                return False
    return True

def main():
    lettere = input("Inserisci una stringa contenente le lettere vietate:\t")
    fin = open('words.txt')
    counter = 0
    for riga in fin:
        parola = riga.strip()
        if(evita(parola,lettere)):
            counter += 1
    print(f"Ci sono {counter} parole senza lettere vietate.")

if __name__ == "__main__":
    main()
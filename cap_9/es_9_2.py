def niente_e(parola):
    for lettera in parola:
        if(lettera == 'e'):
            return False
    return True

def main():
    fin = open('words.txt')
    counter = 0
    counter_no_e = 0
    for riga in fin:
        counter += 1
        parola = riga.strip()
        if(niente_e(parola)):
            print(parola)
            counter_no_e += 1
    print(f"Percentuale: {(counter_no_e/counter) * 100}%") 

if __name__ == "__main__":
    main()
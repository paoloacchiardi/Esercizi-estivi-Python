def usa_tutte(parola,dausare):
    tro = True
    for lettera in dausare:
        if(not tro):
            return False
        for lettere in parola:
            tro = False
            if(lettere == lettera):
                tro = True
                break
    return tro

def main():
    fin = open('words.txt')
    count_one = 0
    count_two = 0
    for riga in fin:
        parola = riga.strip()
        if(usa_tutte(parola,"aeiou")):
            count_one += 1
            if(usa_tutte(parola,"aeiouy")):
                count_two += 1
    print(f"Ci sono {count_one} parole che contengono le lettere 'aeiou'.\nCi sono {count_two} parole che contengono le lettere 'aeiouy'.")

if __name__ == "__main__":
    main()

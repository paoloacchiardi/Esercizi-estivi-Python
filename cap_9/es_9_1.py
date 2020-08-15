def main():
    fin = open('words.txt')
    for riga in fin:
        parola = riga.strip()
        if(len(parola) > 20):
            print(parola)

if __name__ == "__main__":
    main()
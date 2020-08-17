def triple_double(parola):
    count = 1
    global_count = 0
    while(count < len(parola)):
        if(parola[count-1] == parola[count]):
            global_count += 1
            count += 2
            if(global_count == 3):
                return True
        else:
            global_count = 0
            count += 1
    return False

def main():
    fin = open('words.txt')
    print("Lista parole con tre doppie lettere uguali consecutive:")
    count = 0
    for riga in fin:
        parola = riga.strip()
        if(triple_double(parola)):
            count += 1
            print(f"{parola}")
    print(f"Esistono {count} parole con tre doppie lettere uguali consecutive.")


if __name__ == "__main__":
    main()
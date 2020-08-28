def ha_duplicati(dizionario):
    dizionario2 = {}
    for key in dizionario:
        if dizionario[key] in dizionario2.values():
            return True
        else:
            dizionario2[key] = dizionario[key]
    return False

def main():
    dizionario = {"A":1 , "B": 2, "C": 1, "D": 3}
    dizionario2 = {"A":1 , "B": 2, "C": 4, "D": 3}
    if(ha_duplicati(dizionario)):
        print(f"{dizionario} ha dei valori duplicati.")
    else:
        print(f"{dizionario} non ha dei valori duplicati.")
    if(ha_duplicati(dizionario2)):
        print(f"{dizionario2} ha dei valori duplicati.")
    else:
        print(f"{dizionario2} non ha dei valori duplicati.")

if __name__ == "__main__":
    main()
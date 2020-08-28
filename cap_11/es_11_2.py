def inverti_diz(d):
    inverso = dict()
    for chiave in d:
        if(d[chiave] not in inverso):
            lista = list()
            lista.append(chiave)
            x = inverso.setdefault(d[chiave],lista)
        else:
            inverso[d[chiave]].append(chiave)
    return inverso

def main():
    dizionario = {"A":1 , "B": 2, "C": 1, "D": 3}
    inverso = inverti_diz(dizionario)
    print(dizionario)
    print(inverso)

if __name__ == "__main__":
    main()
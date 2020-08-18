def mediani(t):
    t2 = t[1:len(t)-1]
    return t2

def main():
    lista = [1,2,3,4]
    lista2 = mediani(lista)
    print(f"origin: {lista}\nnew: {lista2}")

if __name__ == "__main__":
    main()
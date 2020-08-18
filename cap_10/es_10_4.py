def tronca(t):
    del t[len(t)-1]
    del t[0]

def main():
    lista = [1,2,3,4]
    tronca(lista)
    print(f"{lista}")

if __name__ == "__main__":
    main()
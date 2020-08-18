def ordinata(t):
    t2 = []
    count = 0
    for elemento in t:
        t2.append(elemento)
    t2.sort()
    while(count < len(t)-1):
        count += 1
        if(t[count] != t2[count]):
            return False
    return True

def main():
    lista_ord = [1,2,3,4]
    lista_non_ord = [1,6,3,2,5]
    if(ordinata(lista_ord)):
        print(f"Lista ordinata: {lista_ord}") 
    else:
        print(f"Lista non ordinata: {lista_ord}") 
    if(ordinata(lista_non_ord)):
        print(f"Lista ordinata: {lista_non_ord}")
    else:
        print(f"Lista non ordinata: {lista_non_ord}") 

if __name__ == "__main__":
    main()
def file_to_dict(indirizzo_file):
    file = open(indirizzo_file)
    dizionario = dict()
    count = 0
    for riga in file:
        dizionario[riga.strip()] = count
        count += 1
    return dizionario

def main():  
    dizionario = file_to_dict('D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt')  
    key = input("Insert a string:\t")
    if(key in dizionario):
        print(f"{key} : {dizionario[key]}")
        print("The string is in the dictionary.")
    else:
        print("The string isn't in the dictionary.")

if __name__ == "__main__":
    main()  
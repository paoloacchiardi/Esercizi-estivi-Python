from __future__ import print_function, division
def read_dictionary(filename='D:\Desktop\COMPITI_VACANZE\compiti_svolti\es_python_sistemi\cap_9\words.txt'):
    d = dict()
    fin = open(filename)
    for line in fin:
        if line[0] == '#': continue
        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron
    return d

def main():
    pronuncia = read_dictionary()
    word = []
    app1 = []
    app2 = []
    stringa_app1 = ""
    stringa_app2 = ""
    homophone_words = []
    for key in pronuncia:
        if(len(key)>1):
            word.clear()
            app1.clear()
            app2.clear()
            stringa_app1 = ""
            stringa_app2 = ""
            count = 0
            for lettera in key:
                word.append(lettera)
                if(count != 0):
                    app1.append(lettera)
                if(count != 1):
                    app2.append(lettera)
                count += 1
            stringa_app1 = "".join(app1)
            stringa_app1 = "".join(app2)
            if((stringa_app1 in pronuncia) and (stringa_app2 in pronuncia)):
                if(pronuncia[key] == pronuncia[stringa_app1] == pronuncia[stringa_app2]):
                    homophone_words.append(key)
    print(f"Homophone words: {homophone_words}")

if __name__ == "__main__":
    main()
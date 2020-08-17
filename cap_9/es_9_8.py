def controllo(uno,due,tre,quattro,cinque,sei):
    if((tre == sei) and (quattro == cinque)):
        sei += 1
        if(sei == 10):
            sei = 0
            cinque += 1
            if(cinque == 10):
                cinque = 0
                quattro += 1
                if(quattro == 10):
                    quattro = 0
                    tre += 1
                    if(tre == 10):
                        tre = 0
                        due += 1
                        if(due == 10):
                            due = 0
                            uno += 1
                            if(uno == 10):
                                return False
        if((due == sei) and (tre == cinque)):
            sei += 1
            if(sei == 10):
                sei = 0
                cinque += 1
                if(cinque == 10):
                    cinque = 0
                    quattro += 1
                    if(quattro == 10):
                        quattro = 0
                        tre += 1
                        if(tre == 10):
                            tre = 0
                            due += 1
                            if(due == 10):
                                due = 0
                                uno += 1
                                if(uno == 10):
                                    return False
            if((due == cinque) and (tre == quattro)):
                sei += 1
                if(sei == 10):
                    sei = 0
                    cinque += 1
                    if(cinque == 10):
                        cinque = 0
                        quattro += 1
                        if(quattro == 10):
                            quattro = 0
                            tre += 1
                            if(tre == 10):
                                tre = 0
                                due += 1
                                if(due == 10):
                                    due = 0
                                    uno += 1
                                    if(uno == 10):
                                        return False
                if((uno == sei) and (due == cinque) and (tre == quattro)):
                    return True
    return False

def main():
    print(f"Numeri che soddisfano le condizioni indicate:")
    massimo = 10
    cifra_uno = 0
    cifra_due = 0
    cifra_tre = 0
    cifra_quattro = 0
    cifra_cinque = 0
    cifra_sei = 0
    while(cifra_uno < massimo):
        if(controllo(cifra_uno, cifra_due, cifra_tre, cifra_quattro, cifra_cinque, cifra_sei)):
            print(f"{cifra_uno}{cifra_due}{cifra_tre}{cifra_quattro}{cifra_cinque}{cifra_sei}")
        cifra_sei += 1
        if(cifra_sei == 10):
            cifra_sei = 0
            cifra_cinque += 1
            if(cifra_cinque == 10):
                cifra_cinque = 0
                cifra_quattro += 1
                if(cifra_quattro == 10):
                    cifra_quattro = 0
                    cifra_tre += 1
                    if(cifra_tre == 10):
                        cifra_tre = 0
                        cifra_due += 1
                        if(cifra_due == 10):
                            cifra_due = 0
                            cifra_uno += 1


if __name__ == "__main__":
    main()
def usa_solo(parola, giuste):
    result = True
    for lettera in parola:
        if(not result): #se una lettera non è valida
            return False
        for lettere in giuste:
            if(lettera == lettere): #se la lettera della parola è valida
                result = True
                break #si passa alla lettera successiva
            result = False #se la lettera della parola non è valida
    return result
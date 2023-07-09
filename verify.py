import pickle



### A função "def checker_cpf_" foi baseada nos slides e aulas do professor Flavius Gorgonio(Semana 16 - Subprogramas, Passagem de Parâmetros, Variáveis Locais e Globais (19/06/2023 - 22/06/2023))### 
def checker_cpf_br(cpf):
    list_cpf = list(cpf) 
    if len(list_cpf) != 11:
            return False
    else:
        digt10 = int(list_cpf[10])
        digt09 = int(list_cpf[9])
        digt08 = 2*int(list_cpf[8])
        digt07 = 3*int(list_cpf[7])
        digt06 = 4*int(list_cpf[6])
        digt05 = 5*int(list_cpf[5])
        digt04 = 6*int(list_cpf[4])
        digt03 = 7*int(list_cpf[3])
        digt02 = 8*int(list_cpf[2])
        digt01 = 9*int(list_cpf[1])
        digt00 = 10*int(list_cpf[0])
        validation = cpf.isdigit()
        if validation == True:
            total = digt08 + digt07 + digt06 + digt05 + digt04 + digt03 + digt02 + digt01 + digt00
            rest = total % 11
            if rest == 0 or rest == 1 :
                comp = 0
            else:
                comp = 11 - rest
            if digt09 != comp:
                return False
            else:
                digt10 = int(list_cpf[10])
                digt09 = 2*int(list_cpf[9])
                digt08 = 3*int(list_cpf[8])
                digt07 = 4*int(list_cpf[7])
                digt06 = 5*int(list_cpf[6])
                digt05 = 6*int(list_cpf[5])
                digt04 = 7*int(list_cpf[4])
                digt03 = 8*int(list_cpf[3])
                digt02 = 9*int(list_cpf[2])
                digt01 = 10*int(list_cpf[1])
                digt00 = 11*int(list_cpf[0])
                total = digt09 + digt08 + digt07 + digt06 + digt05 + digt04 + digt03 + digt02 + digt01 + digt00
                rest = total % 11
                if rest == 0 or rest == 1:
                    comp = 0
                else:
                    comp = 11 - rest
                if digt10 != comp:
                    return False
                else:
                    return True
        else:
            return False   



def checker_cel_br(cel):
    list_ddd = [61, 62, 64, 65, 66, 67, 82, 71, 73, 74, 75, 77,
                85, 88, 98, 99, 83, 81, 87, 86, 89, 84, 79, 68,
                96, 92, 97, 91, 93, 94, 69, 95, 63, 27, 28, 31,
                32, 33, 34, 35, 37, 38, 21, 22, 24, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 41, 42, 43, 44, 45, 46,
                51, 53, 54, 55, 47, 48, 49]
    validation = cel.isdigit()
    if validation == True:
        list_cel = list(cel)
        if len(list_cel) == 11:
            ddd = int(list_cel[0] + list_cel[1])
            if ddd in list_ddd:
                    if list_cel[2] == "9":
                        return True
            else:
                return False
        else:
            return False
    else:
        return False



def checker_name(name):
    name = name.replace(" ","")
    validation = name.isalpha()
    if validation == True:
        return True
    else:
        return False

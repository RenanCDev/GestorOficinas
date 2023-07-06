def checker_cpf_br(cpf):
    list_cpf = list(cpf) 
    if len(list_cpf) != 11:
            return False
    else:
        d10 = int(list_cpf[10])
        d09 = int(list_cpf[9])
        d08 = 2*int(list_cpf[8])
        d07 = 3*int(list_cpf[7])
        d06 = 4*int(list_cpf[6])
        d05 = 5*int(list_cpf[5])
        d04 = 6*int(list_cpf[4])
        d03 = 7*int(list_cpf[3])
        d02 = 8*int(list_cpf[2])
        d01 = 9*int(list_cpf[1])
        d00 = 10*int(list_cpf[0])
        validation = cpf.isdigit()
        if validation == True:
            total = d08 + d07 + d06 + d05 + d04 + d03 + d02 + d01 + d00
            rest = total % 11
            if rest == 0 or rest == 1 :
                comp = 0
            else:
                comp = 11 - rest
            if d09 != comp:
                return False
            else:
                d10 = int(list_cpf[10])
                d09 = 2*int(list_cpf[9])
                d08 = 3*int(list_cpf[8])
                d07 = 4*int(list_cpf[7])
                d06 = 5*int(list_cpf[6])
                d05 = 6*int(list_cpf[5])
                d04 = 7*int(list_cpf[4])
                d03 = 8*int(list_cpf[3])
                d02 = 9*int(list_cpf[2])
                d01 = 10*int(list_cpf[1])
                d00 = 11*int(list_cpf[0])
                total = d09 + d08 + d07 + d06 + d05 + d04 + d03 + d02 + d01 + d00
                rest = total % 11
                if rest == 0 or rest == 1:
                    comp = 0
                else:
                    comp = 11 - rest
                if d10 != comp:
                    return False
                else:
                    return True
        else:
            return False   
cpf = input()
validation = checker_cpf_br(cpf)
print(validation)

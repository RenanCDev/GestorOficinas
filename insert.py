import os
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
    


def data(va):
    va = va.replace(" ","")
    va = va.replace(".","")
    va = va.replace(",","")
    va = va.replace("-","")
    va = va.replace("(","")
    va = va.replace(")","")
    va = va.replace("/","")
    va = va.replace("+","")
    va = va.upper()
    return va



def data_invalid():
    os.system("clear")
    print("ENTRADA INVÁLIDA!!!")
    print()
    input("Pressione ENTER para inserir novamente")



def print_orcament():
    cpf = orcamentos[id][0], print("CPF: ",cpf)
    print()
    model = orcamentos[id][1], print("Modelo: ",model)
    print()
    id = orcamentos[id][2], print("Identificador: ",id)
    print()
    problem = orcamentos[id][3], print("Problema: ", problem)
    print()
    servic = orcamentos[id][4], print("Serviço: ",servic)
    print()
    val_servic = orcamentos[id][5], print("Valor do serviço: ", val_servic)
    print()
    val_m_obra = orcamentos[id][6], print("Valor da mão de obra: ", val_m_obra)
    print()
    mec = orcamentos[id][7], print("Refrigerista: ", mec)
    print()



def transf_ord_serv_abert(id):
    os_aberta[id] = orcamentos[id]
    del(orcamentos[id])
    os.system("clear")
    print("CPF: ",os_aberta[id][0])
    print()
    print("Modelo: ",os_aberta[id][1])
    print()
    print("Identificador: ",os_aberta[id][2])
    print()
    print("Problema: ",os_aberta[id][3])
    print()
    print("Serviço: ",os_aberta[id][4])
    print()
    print("Valor do serviço: ",os_aberta[id][5])
    print()
    print("Valor da mão de obra: ",os_aberta[id][6])
    print()
    print("Refrigerista: ",os_aberta[id][7])
    print()



def print_orcament_0(id):
    os.system("clear")
    print("CPF: ",orcamentos[id][0])
    print()
    print("Modelo: ",orcamentos[id][1])
    print()
    print("Identificador: ",orcamentos[id][2])
    print()
    print("Problema: ", orcamentos[id][3])
    print()
    print("Serviço: ",orcamentos[id][4])
    print()
    print("Valor do serviço: ", orcamentos[id][5])
    print()
    print("Valor da mão de obra: ", orcamentos[id][6])
    print()
    print("Refrigerista: ", orcamentos[id][7])
    print()



def print_ord_serv_abert0():
    os.system("clear")
    print("CPF: ",os_aberta[id][0])
    print()
    print("Modelo: ",os_aberta[id][1])
    print()
    print("Identificador: ",os_aberta[id][2])
    print()
    print("Problema: ",os_aberta[id][3])
    print()
    print("Serviço: ",os_aberta[id][4])
    print()
    print("Valor do serviço: ",os_aberta[id][5])
    print()
    print("Valor da mão de obra: ",os_aberta[id][6])
    print()
    print("Refrigerista: ",os_aberta[id][7])
    print()



def print_ord_serv_abert():
    cpf = os_aberta[id][0], print("CPF: ",cpf)
    print()
    model = os_aberta[id][1], print("Modelo: ",model)
    print()
    id = os_aberta[id][2], print("Identificador: ",id)
    print()
    problem = os_aberta[id][3], print("Problema: ", problem)
    print()
    servic = os_aberta[id][4], print("Serviço: ",servic)
    print()
    val_servic = os_aberta[id][5], print("Valor do serviço: ", val_servic)
    print()
    val_m_obra = os_aberta[id][6], print("Valor da mão de obra: ", val_m_obra)
    print()
    mec = os_aberta[id][7], print("Refrigerista: ", mec)
    print()



def transf_ord_serv_fechad():
    os_fechada[id] = os_aberta[id]
    del(os_aberta[id])
    os.system("clear")
    print("CPF: ",os_fechada[id][0])
    print()
    print("Modelo: ",os_fechada[id][1])
    print()
    print("Identificador: ",os_fechada[id][2])
    print()
    print("Problema: ",os_fechada[id][3])
    print()
    print("Serviço: ",os_fechada[id][4])
    print()
    print("Valor do serviço: ",os_fechada[id][5])
    print()
    print("Valor da mão de obra: ",os_fechada[id][6])
    print()
    print("Refrigerista: ",os_fechada[id][7])
    print()



def print_ord_serv_fechad():
    os.system("clear")
    print("CPF: ",os_fechada[id][0])
    print()
    print("Modelo: ",os_fechada[id][1])
    print()
    print("Identificador: ",os_fechada[id][2])
    print()
    print("Problema: ",os_fechada[id][3])
    print()
    print("Serviço: ",os_fechada[id][4])
    print()
    print("Valor do serviço: ",os_fechada[id][5])
    print()
    print("Valor da mão de obra: ",os_fechada[id][6])
    print()
    print("Refrigerista: ",os_fechada[id][7])
    print()



def print_colab(cpf):
    os.system("clear")
    cpf = cpf
    cel = colaboradores[cpf][0]
    nasc = colaboradores[cpf][1]
    name = colaboradores[cpf][2]
    print("CPF: ", cpf)
    print("Cel: ", cel)
    print("Data de nascimento: ", nasc)
    print("Nome: ", name)
    print()



def print_client(cpf):
    os.system("clear")
    cpf = cpf
    cel = clientes[cpf][0]
    nasc = clientes[cpf][1]
    name = clientes[cpf][2]
    print("CPF: ", cpf)
    print("Cel: ", cel)
    print("Data de nascimento: ", nasc)
    print("Nome: ", name)
    print()



def insert_cpf():
    os.system("clear")
    print("Por favor, insira o CPF")
    print("Apenas números.")
    print()
    cpf = input("CPF: ")
    cpf = data(cpf)
    return cpf



def insert_cel():
    os.system("clear")
    print("Por favor, digite o celular.")
    print("Exemplo: DD N NNNN NNNN.")
    print()
    print("D = DDD do estado.")
    print("N = Número do celular.") 
    print()
    cel = input("Celular: ")
    cel = data(cel)
    return cel



def insert_name():
    os.system("clear")
    print("Por favor, insira o nome completo")
    print("Apenas letras.")
    print()
    name = input("Nome: ")
    name = name.upper()
    return name



def insert_nasciment():
    os.system("clear") 
    print("Por favor, digite a data de nascimento")    
    print()
    print("Exemplo: DDMMAAAA")
    print("D = dia. ")
    print("M = mês. ")
    print("A = ano. ")
    print()
    nasciment = input("Data de nascimneto: ")
    nasciment = data(nasciment)
    return nasciment



def option_pesq_cad():
    print("\t1 - Editar cadastro")
    print("\t2 - Excluir cadastro")
    print("\t0 - Voltar")
    print()
    option = input("Qual opção deseja fazer? ")
    return option



def exc_client(cpf):  
        os.system("clear")
        del(clientes[cpf])
        print("Perfil excluido com sucesso!")
        input("Tecle ENTER para continuar")



def edit_cel():
    cel = insert_cel()
    verif = checker_cel_br(cel)
    while verif != True:
        os.system("clear")
        data_invalid
        cel = insert_cel()
        verif = checker_cel_br(cel)
    return cel



def edit_name():
    name = insert_name()
    verif = checker_name(name)
    while verif != True:
        os.system("clear")
        data_invalid
        name = insert_name() 
        verif = checker_name(name)
    return name



if option == "1":
                print_client(cpf)
                edit = input("Deseja alterar o celular? (s/n) ")
                if edit == "s":
                    cel = edit_cel()
                elif edit != "n" and edit != "s" :
                    data_invalid()
                    cel = clientes[cpf][0]    
                else:
                    cel = clientes[cpf][0]    
                print_client(cpf)
                edit = input("Deseja alterar o nome? (s/n) ")
                if edit == "s":
                    name = edit_name()
                elif edit != "n" and edit != "s":
                    data_invalid()
                    name = clientes[cpf][1]
                else:
                    name = clientes[cpf][1]
                print_client(cpf)
                edit = input("Deseja alterar a data de nascimento? (s/n) ")
                if edit == "s":
                    print_client(cpf)
                    nasciment = insert_nasciment()
                elif edit != "n" and edit != "s":
                    data_invalid()
                    nasciment = clientes[cpf][2]
                else:
                    nasciment = clientes[cpf][2]
                os.system("clear")
                print("Cadastro alterado com sucesso!")
                clientes[cpf] = [cel, nasciment, name]
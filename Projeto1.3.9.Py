#########################
### PROJECT - SisGORA ###
#########################
import os
from unicodedata import name



clientes = {"11729951414":["83999008017", "22071999", "RENAN MISSIAS RODRIGUES ALVES DA COSTA"]}
colaboradores = {"11729951414":["83999008017", "22071999", "RENAN MISSIAS RODRIGUES ALVES DA COSTA"]}
orcamentos = {"ABC1D23":["11729951414", "GM - CORSA", "ABC1D23", "PROBLEMA", "SERVIÇO", 500, 280, "ARON SILVA"]}
os_aberta = {}
os_fechada = {}



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
    input("Pressione ENTER continuar")



def print_orcament(id):
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



def print_ord_serv_abert0(id):
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



def print_ord_serv_abert(id):
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



def transf_ord_serv_fechad(id):
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



def print_ord_serv_fechad(id):
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
        print()
        input("Tecle ENTER para continuar")



def exc_colab(cpf):
    os.system("clear")
    del(colaboradores[cpf])
    print("Perfil excluido com sucesso!")
    print()
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



def insert_model():
    os.system("clear")
    print("Por favor, insira a marca e o modelo do carro.")
    print("Exemplo: VW - Gol")
    print()
    model = input("Qual a marca e modelo ?")
    return model



def insert_id():
    os.system("clear")
    print("Por favor, insira o identificador do carro.")
    print("Exemplo: ABC1D23")
    print()
    id = input("Qual o identificador ?")
    id = data(id)
    return id



def insert_problem():
    os.system("clear")
    print("Por favor, descreva o problema.")
    print()
    problem = input("Problema: ")
    return problem 



def insert_servic():
    os.system("clear")
    print("Por favor, descreva o serviço.")
    print()
    servic = input("Serviço: ")
    return servic



def insert_val_servic():
    os.system("clear")
    print("Por favor, insira o valor do serviço.")
    print("Apenas números inteiros.")
    print()
    val_servic = int(input("Valor: "))
    return val_servic



def insert_val_m_obra():
    os.system("clear")
    print("Por favor, insira o valor da mão de obra.")
    print("Apenas números inteiros.")
    print()
    val_m_obra = int(input("Valor: "))
    return val_m_obra



def edit_cad_client(cpf):
    print_client(cpf)
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = edit_cel()
    else:
        cel = clientes[cpf][0]
        if edit != "n" and edit != "s" :
            data_invalid()
    print_client(cpf)
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        name = edit_name()
    else:
        name = clientes[cpf][1]
        if edit != "n" and edit != "s":
            data_invalid()
    print_client(cpf)
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        print_client(cpf)
        nasciment = insert_nasciment()
    else:
        nasciment = clientes[cpf][2]
        if edit != "n" and edit != "s":
            data_invalid()
    os.system("clear")
    print("Cadastro alterado com sucesso!")
    clientes[cpf] = [cel, nasciment, name]
    return clientes[cpf]



def edit_cad_colab(cpf):
    print_colab(cpf)
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = edit_cel()
    else:
        cel = colaboradores[cpf][0]
        if edit != "n" and edit != "s" :
            data_invalid()
    print_colab(cpf)
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        name = edit_name()
    else:
        name =  colaboradores[cpf][1]
        if edit != "n" and edit != "s":
            data_invalid()
    print_colab(cpf)
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        print_client(cpf)
        nasciment = insert_nasciment()
    else:
        nasciment = colaboradores[cpf][2]
        if edit != "n" and edit != "s":
            data_invalid()
    os.system("clear")
    print("Cadastro alterado com sucesso!")
    clientes[cpf] = [cel, nasciment, name]
    return clientes[cpf]



def edit_orcament(id):
    os.system("clear")
    print_orcament(id)
    edit = input("Deseja alterar o CPF? (s/n) ")   
    if edit == "s":
        cpf = insert_cpf()
    else:
        cpf = orcamentos[id][0]
        if edit != "n" and edit != "s":
            data_invalid()
    print_orcament(id)
    edit = ("Deseja alterar o modelo? (s/n) ")
    if edit == "s":    
        model = insert_model()
    else:
        model = orcamentos[id][1]
        if edit != "n" and edit != "n":
            data_invalid()
    print_orcament(id)
    edit = input("Deseja alterar o identificador: ")
    if edit == "s":
        id = insert_id()
    else:
        id = orcamentos[id][2]
        if edit != "n" and edit != "n":
            data_invalid()
    print_orcament(id)
    edit = input("Deseja alterar o problema? (s/n) ")
    if edit == "s":
        problem = insert_problem()
    else:
        problem = orcamentos[id][3]
        if edit != "n" and edit != "n":
            data_invalid()
    print_orcament(id)
    edit = input("Deseja alterar o serviço? (s/n) ")
    if edit == "s":
        servic = insert_servic()
    else:
        servic = orcamentos[id][4]
        if edit != "n" and edit != "n":
            data_invalid()
    print_orcament(id)
    edit = input("Deseja alterar o valor do serviço? (s/n) ")
    if edit == "s":
        val_servic = insert_val_servic()
    else:
        val_servic = orcamentos[id][5]
        if edit != "n" and edit != "n":
            data_invalid()
    print_orcament(id)
    edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
    if edit == "s":
        val_m_obra = insert_val_m_obra()
    else:
        val_m_obra = orcamentos[id][6]
        if edit != "n" and edit != "n":
            data_invalid()
    print_orcament(id)
    edit = input("Deseja alterar o refrigerista? (s/n) ")
    if edit == "s":
        os.system("clear")
        mec = input("Novo refrigerista: ") 
    else:
        mec = orcamentos[id][7]
        if edit != "n" and edit != "n":
            data_invalid()
    orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    return orcamentos[id]



def edit_ord_serv_abert(id):
    os.system("clear")
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o CPF? (s/n) ")   
    if edit == "s":
        cpf = insert_cpf()
    else:
        cpf = os_aberta[id][0]
        if edit != "n" and edit != "s":
            data_invalid()
    print_ord_serv_abert(id)
    edit = ("Deseja alterar o modelo? (s/n) ")
    if edit == "s":    
        model = insert_model()
    else:
        model = os_aberta[id][1]
        if edit != "n" and edit != "n":
            data_invalid()
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o identificador: ")
    if edit == "s":
        id = insert_id()
    else:
        id = os_aberta[id][2]
        if edit != "n" and edit != "n":
            data_invalid()
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o problema? (s/n) ")
    if edit == "s":
        problem = insert_problem()
    else:
        problem = os_aberta[id][3]
        if edit != "n" and edit != "n":
            data_invalid()
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o serviço? (s/n) ")
    if edit == "s":
        servic = insert_servic()
    else:
        servic = os_aberta[id][4]
        if edit != "n" and edit != "n":
            data_invalid()
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o valor do serviço? (s/n) ")
    if edit == "s":
        val_servic = insert_val_servic()
    else:
        val_servic = os_aberta[id][5]
        if edit != "n" and edit != "n":
            data_invalid()
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
    if edit == "s":
        val_m_obra = insert_val_m_obra()
    else:
        val_m_obra = os_aberta[id][6]
        if edit != "n" and edit != "n":
            data_invalid()
    print_ord_serv_abert(id)
    edit = input("Deseja alterar o refrigerista? (s/n) ")
    if edit == "s":
        os.system("clear")
        mec = input("Novo refrigerista: ") 
    else:
        mec = os_aberta[id][7]
        if edit != "n" and edit != "n":
            data_invalid()
    os_aberta[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    return os_aberta[id]




def option_orcamentos():
    print()
    print("\t1 - Tornar o orçamento em O.S. aberta.")
    print("\t2 - Editar orçamento.")
    print("\t3 - Excluir orçamento.")
    print("\t0 - Voltar ao menu anterior")
    print()
    option = input("Escolha uma opção: ")
    return option



def main_menu():
    os.system("clear")
    print("#####            #####  #####  #####  #####")
    print("#                #      #   #  #  #   #   #")
    print("#      ###  ###  #      #   #  # #    #   #")
    print("#####   #   #    #      #   #  ##     #   #")
    print("    #   #   ###  #  ##  #   #  # #    #####")
    print("    #   #     #  #   #  #   #  #  #   #   #")
    print("    #   #     #  #   #  #   #  #   #  #   #")
    print("#####  ###  ###  #####  #####  #   #  #   #")
    print()
    print("\t+------------------+")
    print("\t| MENU - PRINCIPAL |")
    print("\t+------------------+")
    print()
    print("\t1 - Clientes")
    print("\t2 - Colaboradores")
    print("\t3 - Orçamentos e Ordens de serviços(O.S.)")
    print("\t4 - Loja")
    print("\t5 - Administrativo")
    print("\t0 - Sair")
    print()
    option = input("Escolha uma opção por favor: ")
    return option



def menu_clientes():
    os.system("clear")
    print("\t+-----------------+")
    print("\t| MENU - CLIENTES |")
    print("\t+-----------------+")
    print()
    print("\t1 - Novo cadastro")
    print("\t2 - Pesquisar cadastro")
    print("\t0 - Voltar ao menu anterior")
    print ()
    option = input("Escolha uma opção por favor: ")
    return option



def cad_clientes():
    cpf = insert_cpf()
    verif = checker_cpf_br(cpf)
    while verif != True:
        data_invalid()
        cpf = insert_cpf()
        verif = checker_cpf_br(cpf)
    if cpf not in clientes:
        cel = insert_cel()
        verif = checker_cel_br(cel)
        while verif != True:
            data_invalid()
            cel = insert_cel()
            verif = checker_cel_br(cel)
        os.system("clear")
        name = insert_name()
        verif = checker_name(name)
        while verif != True:
            data_invalid()
            name = insert_name()
            verif = checker_name(name)
        nasciment = insert_nasciment()
        os.system("clear")
        clientes[cpf] = [cel, nasciment, name]  
        print("Cadastro realizado com sucesso!")
        print()
        input("Tecle ENTER para continuar")
    else:
        os.system("clear")
        print("CPF já cadastrado")
        print()
        input("Tecle ENTER para continuar")



def pesq_clientes():
    cpf = insert_cpf()
    verif = checker_cpf_br(cpf)
    while verif != True:
        data_invalid()
        cpf = insert_cpf()
        verif = checker_cpf_br(cpf)
    if cpf in clientes:
        print_client(cpf)
        option = option_pesq_cad()
        if option != "0":
            if option == "1":
                cpf
                clientes[cpf] = edit_cad_client(cpf)
                print("Cadastro alterado com sucesso!")
                print()
                input("Tecle ENTER para continuar")
            elif option == "2":
                print_client(cpf)
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    exc_client(cpf)
                elif exc != "n" and exc != "s":
                    data_invalid()
            else:
                os.system("clear")
                input("Tecle ENTER para continuar")
        else:
            data_invalid()
    else:
        os.system("clear")
        print("CPF NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def menu_colab():
    os.system("clear")
    print("\t+----------------------+")
    print("\t| MENU - COLABORADORES |")
    print("\t+----------------------+")
    print()
    print("\t1 - Novo cadastro")
    print("\t2 - Pesquisar colaborador")
    print("\t0 - Voltar ao menu anterior")
    print()
    option = input("Escolha uma opção por favor: ")
    return option



def cad_colab():
    cpf = insert_cpf()
    verif = checker_cpf_br(cpf)
    while verif != True:
        data_invalid()
        cpf = insert_cpf()
        verif = checker_cpf_br()
    if cpf not in colaboradores:
        cel = insert_cel()
        verif = checker_cel_br(cel)
        while verif != True:
            data_invalid()
            cel = insert_cel()
            verif = checker_cel_br()
        name = insert_name()
        verif = checker_name(name)
        while verif != True:
            name = insert_name()
            verif = checker_name()
        nasciment = insert_nasciment()
        os.system("clear")
        colaboradores[cpf] = [cel, nasciment, name]  
        print("Cadastro realizado com sucesso!")
        print()
        input("Tecle ENTER para continuar")
    else:
        os.system("clear")
        print("CPF CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def pesq_colab():
    cpf = insert_cpf()
    verif = checker_cpf_br(cpf)
    while verif != True:
        data_invalid()
        cpf = insert_cpf()
        verif = checker_cpf_br(cpf)     
    if cpf in colaboradores:
        print_colab(cpf)
        option = option_pesq_cad()
        if option != "0":
            if option == "1":
                cpf
                colaboradores[cpf] = edit_cad_colab(cpf)
                print("Cadastro alterado com sucesso!")
                print()
                input("Tecle ENTER para continuar")
            elif option == "2":
                print_colab(cpf)
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    exc_colab(cpf)
                elif exc != "n" and exc != "s":
                    data_invalid()
            else:
                data_invalid()
        else:
            data_invalid()
    else:
        os.system("clear")
        print("CPF NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def menu_ord_serv():
    os.system("clear")
    print("\t+---------------------------+")
    print("\t| MENU - ORDENS DE SERVIÇOS |")
    print("\t+---------------------------+")
    print()
    print("\t1 - Novo orçamento")
    print("\t2 - Pesquisar orçamentos")
    print("\t3 - O.S. Abertas")
    print("\t4 - O.S. Fechadas")
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op



def cad_orcament():
    os.system("clear")
    print("\t+---------------------------+")
    print("\t| CADASTRO - NOVO ORÇAMENTO |")
    print("\t+---------------------------+")
    cpf = insert_cpf()
    verif = checker_cpf_br(cpf)
    while verif != True:
        data_invalid()
        cpf = insert_cpf
        verif = checker_cpf_br
    if cpf in clientes:
        model = insert_model()
        id = insert_id()
        problem = insert_problem()
        servic = insert_servic()
        val_servic = insert_val_servic()
        val_m_obra = insert_val_m_obra()
        os.system("clear")
        mec = input("Refrigerista: ")
        orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    else:
        print("CPF NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def pesq_orcament():
    os.system("clear")
    print("\t+-----------------------+")
    print("\t| PESQUISA - ORÇAMENTOS |")
    print("\t+-----------------------+")
    print()
    print("\t1 - Pesquisar por CPF e identificador")
    print("\t0 - Coltar ao menu anterior")
    print()
    option = input("O que deseja fazer ? ")
    if option != "0":
        if option == "1":
            os.system("clear")
            cpf = insert_cpf()
            verif = checker_cpf_br(cpf)
            while verif != True:
                data_invalid()
                cpf = insert_cpf()
                verif = checker_cpf_br(cpf)
            if cpf in clientes:
                id = insert_id()
                if id in orcamentos:
                    print_orcament_0(id)
                    option = option_orcamentos()
                    if option != "0":
                        if option == "1":
                            transf_ord_serv_abert(id)
                        elif option == "2":
                            id
                            orcamentos[id] = edit_orcament(id)
                        elif option == "3":
                            del(orcamentos[id])
                            print("Orçamento excluido com sucesso!")
                            print()
                            input("Tecle enter para continuar")
                        else:
                            data_invalid()
                else:
                    print("IDENTIFICADOR NÃO CADASTRADO!!!")
                    print()
                    input("Tecle ENTER para continuar")
            else:
                print("CPF NÃO CADASTRADO!!!")
                print()
                input("Tecle ENTER para continuar")
        else:
            data_invalid()



def pesq_ord_serv_abert():
    os.system("clear")
    print("\t+------------------------+")
    print("\t| PESQUISA - OSs ABERTAS |")
    print("\t+------------------------+")
    input("Tecle ENTER para continuar")
    id = insert_id()
    if id in os_aberta:
        option = option_pesq_cad()
        if option != "0":
            if option == "1":
                id
                transf_ord_serv_fechad(id)
            elif option == "2":
                os.system("clear")
                print_ord_serv_abert(id)
                if option != "0":
                    if option == "1":
                        transf_ord_serv_fechad(id)
                    elif option == "2":
                        id
                        os_aberta[id] = edit_ord_serv_abert(id)
                    elif option == "3":
                        del(os_aberta[id])
                        print("Ordem de serviço excluida com sucesso!")
                        print()
                        input("Tecle ENTER para continuar")
                    else:
                        data_invalid()
            else:
                data_invalid()
    else:
        print("IDENTIFICADOR NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def pesq_ord_serv_fechad():
    os.system("clear")
    print("\t+-------------------------+")
    print("\t| PESQUISA - OSs FECHADAS |")
    print("\t+-------------------------+")
    option = input("Deseja pesquisar alguma ordem de serviço fechada ? (s/n) ")
    if option == "s":
        if id in os_fechada:
            os.system("clear")
            print_ord_serv_fechad(id)
            print()
            input("Tecle ENTER para continuar")
        else:
            print("IDENTIFICADOR NÃO CADASTRADO!!!")
            print()
            input("Tecle ENTER para continuar")
    elif option != "n" and option != "s":
        data_invalid()



def menu_loja():
    os.system("clear")
    print("\t+-------------+")
    print("\t| MENU - LOJA |")
    print("\t+-------------+")
    print()
    print("\t1 - Nova venda")
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op



def cad_venda():
    os.system("clear")
    print("\t+------------------+")
    print("\t| CADASTRO - VENDA |")
    print("\t+------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def menu_adm():
    os.system("clear")
    print("\t+-----------------------+")
    print("\t| MENU - ADMINISTRATIVO |")
    print("\t+-----------------------+")
    print()
    print("\t1 - Pedidos")
    print("\t2 - Vendas")
    print("\t3 - Comissões")
    print("\t4 - Finanças")
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op



def ped():
    os.system("clear")
    print("\t+---------+")
    print("\t| PEDIDOS |")
    print("\t+---------+")
    print()
    print("\t1 - Cadastrar pedido")
    print("\t2 - Pesquisar pedido")
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op



def cad_ped():
    os.system("clear")
    print("\t+-------------------+")
    print("\t| CADASTRO - PEDIDO |")
    print("\t+-------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def p_ped():
    os.system("clear")
    print("\t+--------------------+")
    print("\t| PESQUISA - PEDIDOS |")
    print("\t+--------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def venda():
    os.system("clear")
    print("\t+--------+")
    print("\t| VENDAS |")
    print("\t+--------+")
    print()
    print("\t1 - Pesquisar venda") 
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op


    
def p_venda():
    os.system("clear")
    print("\t+-------------------+")
    print("\t| PESQUISA - VENDAS |")
    print("\t+-------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")


def comis():
    os.system("clear")
    print("\t+-----------+")
    print("\t| COMISSÕES |")
    print("\t+-----------+")
    print()
    print("\t1 - Lançar comissão")
    print("\t2 - Pesquisar comissão")
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op



def bx_comis():
    os.system("clear")
    print("\t+-------------------+")
    print("\t| LANÇAR - COMISSÃO |")
    print("\t+-------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def p_comis():
    os.system("clear")
    print("\t+----------------------+")
    print("\t| PESQUISA - COMISSÕES |")
    print("\t+----------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")


def deb():
    os.system("clear")
    print("\t+---------+")
    print("\t| DÉBITOS |")
    print("\t+---------+")
    print()
    print("\t1 - Cadastrar débito")
    print("\t2 - Pesquisar débito")
    print("\t0 - Voltar ao menu anterior")
    print()
    op = input("Escolha uma opção por favor: ")
    return op



def cad_deb():
    os.system("clear")
    print("\t+------------------------+")
    print("\t| CADASTRO - NOVO DÉBITO |")
    print("\t+------------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def p_deb():
    os.system("clear")
    print("\t+---------------------------------+")
    print("\t| PESQUISA - CADASTROS DE DEBITOS |")
    print("\t+---------------------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



####################
## MAIN - PROGRAM ##
####################
op1 = main_menu()
while op1 != "0":
    if op1 == "1":
        op2 = menu_clientes()
        while op2 != "0":
            if op2 == "1":
                op3 = cad_clientes()
                op2 = menu_clientes()
            elif op2 == "2":
                op3 = pesq_clientes()
                op2 = menu_clientes()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                op2 = menu_clientes()
                input("Tecle ENTER para continuar")
        op1 = main_menu()
    elif op1 == "2":
        op2 = menu_colab()
        while op2 != "0":    
            if op2 == "1":
                op3 = cad_colab()
                op2 = menu_colab()
            elif op2 == "2":
                op3 = pesq_colab()
                op2 = menu_colab()
            else:
                print("OPÇÃO INVÁLIDA")
                op2 = menu_colab()
                input("Tecle ENTER para continuar")
        op1 = main_menu()
    elif op1 == "3":
        op2 = menu_ord_serv()
        while op2 != "0":
            if op2 == "1":
                op3 = cad_orcament()
                op2 = menu_ord_serv()
            elif op2 == "2":
                op3 = pesq_orcament()
                op2 = menu_ord_serv()
            elif op2 == "3":
                op3 = pesq_ord_serv_abert()
                op2 = menu_ord_serv()
            elif op2 == "4":
                op3 = pesq_ord_serv_fechad()
                op2 = menu_ord_serv()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                op2 = menu_ord_serv()
        op1 = main_menu()
    elif op1 == "4":
        op2 = menu_loja()
        while op2 != "0":
            if op2 == "1":
                op3 = cad_venda()
                op2 = menu_loja()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                op2 = menu_loja()
        op1 = main_menu()
    elif op1 == "5":
        op2 = menu_adm()
        while op2 != "0":
            if op2 == "1":
                op3 = ped()
                while op3 != "0":
                    if op3 == "1":
                        op4 = cad_ped()
                        op3 = ped()
                    elif op3 == "2":
                        op4 = p_ped()
                        op3 = ped()
                    else:
                        print("OPÇÃO INVÁLIDA!!!")
                        input("Tecle ENTER para continuar")
                        op3 = ped()
                op2 = menu_adm()
            elif op2 == "2":
                op3 = venda()
                while op3 != "0":
                    if op3 == "1":
                        op4 = p_venda()
                        op3 = venda()
                    else:
                        print("OPÇÃO INVÁLIDA!!!")
                        input("Tecle ENTER para continuar")
                        op3 = venda()
                op2 = menu_adm()
            elif op2 == "3":
                op3 = comis()
                while op3 != "0":
                    if op3 == "1":
                        op4 = bx_comis()
                        op3 = comis()
                    elif op3 == "2":
                        op4 = p_comis()
                        op3 = comis()
                    else:
                        print("OPÇÃO INVÁLIDA!!!")
                        input("Tecle ENTER para continuar")
                        op3 = comis()
                op2 = menu_adm()
            elif op2 == "4":
                op3 = deb()
                while op3 != "0":
                    if op3 == "1":
                        op4 = cad_deb()
                        op3 = deb()
                    elif op3 == "2":
                        op4 = p_deb()
                        op3 = deb()
                    else:
                        print("OPÇÃO INVÁLIDA!!!")
                        input("Tecle ENTER para continuar")
                        op3 = deb()
                op2 = menu_adm()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                op2 = menu_adm()
        op1 = main_menu()
    else:
        print("=            OPÇÃO INVÁLIDA !!!!!           =")
        input("Tecle ENTER para continuar")
        op1 = main_menu()
print("=             PROGRAMA ENCERRADO            =")
print("=                ATÉ BREVE !                =")
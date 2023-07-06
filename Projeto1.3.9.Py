#########################
### PROJECT - SisGORA ###
#########################
import os
from unicodedata import name



clientes = {}
colaboradores = {}
orcamentos = {}
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
            comp = 11 - rest
            if rest != 0 and rest != 1 :
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
                    comp = 11 - rest
                    if rest != 0 and rest!= 1:
                        if d10 != comp:
                            return False
                        else:
                            return True
                    else:
                        return False
            else:
                return False   
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



def prt_orc():
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


def tr_os():
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



def prt_orc_0():
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



def prt_os_a0():
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



def prt_os_a():
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



def tr_os_f():
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



def prt_os_f():
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



def prt_colab():
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



def prt_cliente():
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
    op = input("Escolha uma opção por favor: ")
    return op



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
    op = input("Escolha uma opção por favor: ")
    return op



def cad_clientes():
    os.system("clear")
    print("\t+---------------------+")
    print("\t| CADASTRO -  CLIENTE |")
    print("\t+---------------------+")
    print()
    print("Por favor, digite o CPF.")
    print("Insira apenas números.")
    print()
    cpf = input("CPF: ")
    cpf = data(cpf)
    #verif = checker_cpf_br(cpf)#
    #while verif != True:
    #    os.system("clear")
    #    print("CPF inválido! Digite novamente.")
    #    print()
    #    cpf = input("CPF: ")
    #    verif = checker_cpf_br(cpf)
    os.system("clear")
    print("Por favor, digite o celular.")
    print("Exemplo: DD N NNNN NNNN.")
    print()
    print("D = DDD do estado.")
    print("N = Número do celular.") 
    print()
    cel = input("Celular: ")
    cel = data(cel)
    #verif = checker_cel_br(cel)#
    #while verif != True:
    #    os.system("clear")
    #    print("Exemplo: DD N NNNN NNNN.")
    #    print()
    #    print("D = DDD do estado.")
    #    print("N = Número do celular.")        
    #    print()
    #    print("Celular inválido! Digite novamente.")
    #    print()
    #    cel = input("Cel.: ")
    #    verif = checker_cel_br(cel)
    os.system("clear")
    print("Por favor, insira o nome completo")
    print("Apenas letras.")
    print()
    name = input("Nome: ")
    #verif = checker_name(name)
    #while verif != True:
    #    os.system("clear")
    #    print("Nome inválido! Digite novamente.")
    #    print()
    #    name = input("Nome: ")
    #    verif = checker_name(name)
    name = name.upper()
    os.system("clear")
    print("Por favor, digite a data de nascimento")    
    print()
    print("Exemplo: DDMMAAAA")
    print("D = dia. ")
    print("M = mês. ")
    print("A = ano. ")
    print()
    nasc = input("Data de nascimento: ")
    nasc = data(nasc)
    os.system("clear")
    clientes[cpf] = [cel, nasc, name]  
    print("Cadastro realizado com sucesso!")
    input("Tecle ENTER para continuar")



def p_clientes():
    os.system("clear")
    print("\t+---------------------+")
    print("\t| PESQUISA - CLIENTES |")
    print("\t+---------------------+")
    print()
    print("Por favor, digite o CPF que deseja localizar: ")
    print()
    cpf = input("CPF: ")
    cpf = data(cpf)
    if cpf in clientes:
        prt_cliente()
        print("\t1 - Editar cadastro")
        print("\t2 - Excluir cadastro")
        print("\t0 - Voltar")
        print()
        op = input("Qual operação deseja fazer?")
        while op != "0":
            if op == "1":
                prt_cliente()
                edit = input("Deseja alterar o celular? (s/n) ")
                if edit == "s":
                    os.system("clear")
                    print("Novo celular: ")
                    print()
                    print("Exemplo: DD N NNNN NNNN.")
                    print("D = DDD do estado.")
                    print("N = Número do celular.") 
                    print()
                    cel = input("Celular: ")
                    cel = data(cel)
                    #verif = checker_cel_br(cel)
                    #while verif != True:
                    #    os.system("clear")
                    #    print("Exemplo: DD N NNNN NNNN.")
                    #    print("D = DDD do estado.")
                    #    print("N = Número do celular.")      
                    #    print()              
                    #    print("Celular inválido! Digite novamente.")
                    #    cel = input("Cel.: ")
                    #    verif = checker_cel_br(cel)
                elif edit != "n" and edit != "s" :
                    os.system("clear")
                    print("OPERAÇÃO INVÁLIDA!!!")
                    input("Tecle ENTER para continuar")
                prt_cliente()
                edit = input("Deseja alterar o nome? (s/n) ")
                if edit == "s":
                    prt_cliente()
                    print("Por favor, insira o novo nome completo.")
                    print("Apenas letras.")
                    print()
                    name = input("Nome: ")
                    #verif = checker_name(name)
                    #while verif != True:
                    #    os.system("clear")
                    #    print("Apenas letras.")
                    #    print()
                    #    print("Nome inválido! Digite novamente.")
                    #    name = input("Nome: ")
                    #    verif = checker_name(name
                    name = name.upper()
                elif edit != "n" and edit != "s":
                    os.system("clear")
                    print("OPERAÇÃO INVÁLIDA!!!")
                    input("Tecle ENTER para continuar")
                prt_cliente()
                edit = input("Deseja alterar a data de nascimento? (s/n) ")
                if edit == "s":
                    prt_cliente()
                    nasc = input("Nova data de nascimento: ")
                    nasc = data(nasc)
                elif edit != "n" and edit != "s":
                    os.system("clear")
                    print("OPERAÇÃO INVÁLIDA!!!")
                    input("Tecle ENTER para continuar")
                os.system("clear")
                print("Cadastro alterado com sucesso!")
                clientes[cpf] = [cel, nasc, name]
            elif op == "2":
                prt_cliente()
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    os.system("clear")
                    del(clientes[cpf])
                    print("Perfil excluido com sucesso!")
                    input("Tecle ENTER para continuar")
                elif exc != "n" and exc != "s":
                    os.system("clear")
                    print("OPERAÇÃO INVÁLIDDA!!!")
                    input("Tecle ENTER para continuar")
            else:
                os.system("clear")
                input("Tecle ENTER para continuar")
    else:
        os.system("clear")
        print("Cadastro inexistente!")
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
    op = input("Escolha uma opção por favor: ")
    return op



def cad_colab():
    os.system("clear")
    print("\t+------------------------+")
    print("\t| CADASTRO - COLABORADOR |")
    print("\t+------------------------+")
    print()
    print("Por favor, digite o CPF.")
    print("Insira apenas números.")
    print()
    cpf = input("CPF: ")
    cpf = data(cpf)
    #verif = checker_cpf_br(cpf)
    #while verif != True:
    #    os.system("clear")
    #    print("CPF inválido! Digite novamente.")
    #    print()
    #    cpf = input("CPF: ")
    #    verif = checker_cpf_br(cpf)
    os.system("clear")
    print("Por favor, digite o celular.")
    print("Exemplo: DD N NNNN NNNN.")
    print()
    print("D = DDD do estado.")
    print("N = Número do celular.") 
    print()
    cel = input("Celular: ")
    cel = data(cel)
    #verif = checker_cel_br(cel)
    #while verif != True:
    #    os.system("clear")
    #    print("Exemplo: DD N NNNN NNNN.")
    #    print()
    #    print("D = DDD do estado.")
    #    print("N = Número do celular.")        
    #    print()
    #    print("Celular inválido! Digite novamente.")
    #    print()
    #    cel = input("Cel.: ")
    #    verif = checker_cel_br(cel)
    os.system("clear")
    print("Por favor, insira o nome completo")
    print("Apenas letras.")
    print()
    name = input("Nome: ")
    #verif = checker_name(name)
    #while verif != True:
    #    os.system("clear")
    #    print("Nome inválido! Digite novamente.")
    #    print()
    #    name = input("Nome: ")
    #    verif = checker_name(name)
    name = name.upper()
    os.system("clear")
    print("Por favor, digite a data de nascimento")    
    print()
    print("Exemplo: DDMMAAAA")
    print("D = dia. ")
    print("M = mês. ")
    print("A = ano. ")
    print()
    nasc = input("Data de nascimento: ")
    nasc = data(nasc)
    os.system("clear")
    colaboradores[cpf] = [cel, nasc, name]  
    print("Cadastro realizado com sucesso!")



def p_colab():
    os.system("clear")
    print("\t+--------------------------+")
    print("\t| PESQUISA - COLABORADORES |")
    print("\t+--------------------------+")
    print()
    print("Por favor, digite o CPF que deseja localizar: ")
    print()
    cpf = input("CPF: ")
    cpf = data(cpf)
    if cpf in colaboradores:
        prt_colab()
        print("\t1 - Editar cadastro")
        print("\t2 - Excluir cadastro")
        print("\t0 - Voltar")
        print()
        op = input("Qual operação deseja fazer? ")
        while op != "0":
            prt_colab()
            print("\t1 - Editar cadastro")
            print("\t2 - Excluir cadastro")
            print("\t0 - Voltar")
            print()
            op = input("Qual operação deseja fazer? ")
        if op == "1":
            prt_colab()
            edit = input("Deseja alterar o celular? (s/n) ")
            if edit == "s":
                prt_colab()
                print("Novo celular: ")
                print()
                print("Exemplo: DD N NNNN NNNN.")
                print("D = DDD do estado.")
                print("N = Número do celular.") 
                print()
                cel = input("Celular: ")
                cel = data(cel)
                #verif = checker_cel_br(cel)
                #while verif != True:
                #    os.system("clear")
                #    print("Exemplo: DD N NNNN NNNN.")
                #    print("D = DDD do estado.")
                #    print("N = Número do celular.")      
                #    print()              
                #    print("Celular inválido! Digite novamente.")
                #    cel = input("Cel.: ")
                #    verif = checker_cel_br(cel)
            elif edit != "n" and edit != "s":
                os.system("clear")
                print("OPERAÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
            os.system("clear")
            prt_colab()         
            edit = input("Deseja alterar o nome? (s/n) ")
            if edit == "s":
                prt_colab()
                print("Por favor, insira o nome completo")
                print("Apenas letras.")
                print()
                name = input("Nome: ")
                #verif = checker_name(name)
                #while verif != True:
                #    os.system("clear")
                #    print("Apenas letras.")
                #    print()
                #    print("Nome inválido! Digite novamente")
                #    name = input("Nome: ")
                #    verif = checker_name(name)
                name = name.upper()
            elif edit != "n" and edit != "s":
                os.system("clear")
                print("OPERAÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
            prt_colab()
            edit = input("Deseja alterar a data de nascimento? (s/n) ")
            if edit == "s":
                prt_colab()
                print("Por favor, digite a data de nascimento")    
                print()
                print("Exemplo: DDMMAAAA")
                print("D = dia. ")
                print("M = mês. ")
                print("A = ano. ")
                print()
                nasc = input("Nova data de nascimento: ")
                nasc = data(nasc)
            elif edit != "n" and edit != "s":
                os.system("clear")
                print("OPERAÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
            os.system("clear")
            print("Cadastro alterado com sucesso!")
            colaboradores[cpf] = [cel, nasc, name]
        elif op == "2":
            prt_colab()
            exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
            if exc == "s":
                os.system("clear")
                del(colaboradores[cpf])
                print("Perfil excluido com sucesso!")
                input("Tecle ENTER para continuar")
            elif exc != "n" and exc != "s":
                os.system("clear")
                print("OPERAÇÃO INVÁLIDDA!!!")
                input("Tecle ENTER para continuar")
        else:
            os.system("clear")
            print("OPERAÇÃO INVÁLIDA!!!")
            input("Tecle ENTER para continuar")
    else:
        os.system("clear")
        print("Cadastro inexistente!")
        input("Tecle ENTER para continuar")



def menu_os():
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



def cad_orc():
    os.system("clear")
    print("\t+---------------------------+")
    print("\t| CADASTRO - NOVO ORÇAMENTO |")
    print("\t+---------------------------+")
    print()
    print("Por favor, digite o CPF cadastrado.")
    print("Insira apenas números.")
    print()
    cpf = input("CPF: ")
    cpf = data(cpf)
    #verif = checker_cpf_br(cpf)#
    #while verif != True:
    #    os.system("clear")
    #    print("CPF inválido! Digite novamente.")
    #    print("Caso deseje voltar ao menu anterior.")
    #    print()
    #    cpf = input("CPF: ")
    #    verif = checker_cpf_br(cpf)
    if cpf in clientes:
        os.system("clear")
        print("Por favor, insira a marca e o modelo do carro.")
        print("Exemplo: VW - Gol")
        print()
        model = input("Qual a marca e modelo ?")
        os.system("clear")
        print("Por favor, insira o identificador do carro.")
        print("Exemplo: ABC1D23")
        print()
        id = input("Qual o identificador ?")
        id = data(id)
        os.system("clear")
        print("Por favor, descreva o problema.")
        print()
        problem = input("Problema: ")
        os.system("clear")
        print("Por favor, descreva o serviço")
        print()
        servic = input("Serviço: ")
        os.system("clear")
        print("Por favor, insira o valor do serviço.")
        print("Apenas números inteiros.")
        print()
        val_servic = int(input("Valor: "))
        os.system("clear")
        print("Por favor, insira o valor da mão de obra.")
        print("Apenas números inteiros.")
        print()
        val_m_obra = int(input("Valor: "))
        os.system("clear")
        print("Por favor, insira o nome do colaborador.")
        print()
        mec = input("Refrigerista: ")
        orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    else:
        print("CPF NÃO CADASTRADO!!!")
        input("Tecle ENTER para continuar")



def p_orc():
    os.system("clear")
    print("\t+-----------------------+")
    print("\t| PESQUISA - ORÇAMENTOS |")
    print("\t+-----------------------+")
    print()
    print("\t1 - Pesquisar por CPF e identificador")
    print("\t0 - voltar ao menu anterior")
    print()
    op = input("O que deseja fazer ? ")
    while op != "0":
        if op == "1":
            os.system("clear")
            print("Por favor, insira o CPF")
            print("Apenas números.")
            print()
            cpf = input("CPF: ")
            cpf = data(cpf)
            #verif = checker_cpf_br(cpf)#
            #while verif != True:
            #    os.system("clear")
            #    print("CPF INVÁLIDO!!!")
            #    print("insira um CPF válido.")
            #    print()
            #    cpf = input("CPF: ")
            #    verif = checker_cpf_br(cpf)
            if cpf in clientes:
                os.system("clear")
                print("Por favor, insira o identificador do veiculo")
                print("Exemplo: ABC1D23")
                print()
                id = input("Identificador: ")
                id = data(id)
                if id in orcamentos:
                    prt_orc_0()
                    print("\t1 - Tornar o orçamento em O.S. aberta.")
                    print("\t2 - Editar orçamento.")
                    print("\t0 - Excluir orçamento.")
                    print()
                    op = input("Escolha uma opção por favor.")
                    while op != "0":
                        if op == "1":
                            tr_os()
                        elif op == "2":
                            os.system("clear")
                            prt_orc()
                            edit = input("Deseja alterar o CPF? (s/n) ")
                            while edit == "n" or edit == "s":    
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    cpf = input("Novo CPF: ")
                                    cpf = data(cpf)
                            edit = ("Deseja alterar o modelo? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":    
                                    os.system("clear")
                                    prt_orc()
                                    model = input("Novo modelo: ")
                            edit = input("Deseja alterar o identificador: ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    id = input("Novo identificador: ")
                                    id = data(id)
                            edit = input("Deseja alterar o problema? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    problem = input("Novo problema: ")
                            edit = input("Deseja alterar o serviço? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    servic = input("Novo serviço: ")
                            edit = input("Deseja alterar o valor do serviço? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    val_servic = input("Novo valor do serviço: ")
                            edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    val_m_obra = input("Novo valor da mão de obra: ")
                            edit = input("Deseja alterar o refrigerista? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_orc()
                                    mec = input("Novo refrigerista: ") 
                        else:
                            os.system("clear")
                            print("OPERAÇÃO INVÁLIDA!!!")
                            input("Tecle ENTER para continuar")
                else:
                    print("IDENTIFICADOR NÃO CADASTRADO!!!")
                    input("Tecle ENTER para continuar")
            else:
                print("CPF NÃO CADASTRADO!!!")
                input("Tecle ENTER para continuar")
        else:
            os.system("clear")
            print("OPERAÇÃO INVÁLIDA!!!")
            input("Tecle ENTER para continuar")



def p_os_aberta():
    os.system("clear")
    print("\t+------------------------+")
    print("\t| PESQUISA - OSs ABERTAS |")
    print("\t+------------------------+")
    print()
    print("\t1 - Pesquisar por CPF e identificador")
    print("\t0 - voltar ao menu anterior")
    print()
    op = input("O que deseja fazer ? ")
    while op != "0":
        if op == "1":
            os.system("clear")
            print("Por favor, insira o CPF")
            print("Apenas números.")
            print()
            cpf = input("CPF: ")
            cpf = data(cpf)
            #verif = checker_cpf_br(cpf)#
            #while verif != True:
            #    os.system("clear")
            #    print("CPF INVÁLIDO!!!")
            #    print("insira um CPF válido.")
            #    print()
            #    cpf = input("CPF: ")
            #    verif = checker_cpf_br(cpf)
            if cpf in clientes:
                os.system("clear")
                print("Por favor, insira o identificador do veiculo")
                print("Exemplo: ABC1D23")
                print()
                id = input("Identificador: ")
                id = data(id)
                if id in os_aberta:
                    prt_os_a0()
                    print("\t1 - Transformar em ordem de serviço fechada")
                    print("\t1 - Editar ordem de serviço")
                    print("\t0 - Excluir ordem de serviço")
                    print()
                    op = input("Escolha uma opção por favor.")
                    while op != "0":
                        if op == "1":
                            tr_os_f()
                        elif op == "2":
                            os.system("clear")
                            prt_os_a()
                            edit = input("Deseja alterar o CPF? (s/n) ")
                            while edit == "n" or edit == "s":    
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    cpf = input("Novo CPF: ")
                                    cpf = data(cpf)
                            edit = ("Deseja alterar o modelo? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":    
                                    os.system("clear")
                                    prt_os_a()
                                    model = input("Novo modelo: ")
                            edit = input("Deseja alterar o identificador: ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    id = input("Novo identificador: ")
                                    id = data(id)
                            edit = input("Deseja alterar o problema? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    problem = input("Novo problema: ")
                            edit = input("Deseja alterar o serviço? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    servic = input("Novo serviço: ")
                            edit = input("Deseja alterar o valor do serviço? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    val_servic = input("Novo valor do serviço: ")
                            edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    val_m_obra = input("Novo valor da mão de obra: ")
                            edit = input("Deseja alterar o refrigerista? (s/n) ")
                            while edit == "n" or edit == "s":
                                if edit == "s":
                                    os.system("clear")
                                    prt_os_a()
                                    mec = input("Novo refrigerista: ") 
                        else:
                            os.system("clear")
                            print("OPERAÇÃO INVÁLIDA!!!")
                            input("Tecle ENTER para continuar")
                else:
                    print("IDENTIFICADOR NÃO CADASTRADO!!!")
                    input("Tecle ENTER para continuar")
            else:
                print("CPF NÃO CADASTRADO!!!")
                input("Tecle ENTER para continuar")
        else:
            os.system("clear")
            print("OPERAÇÃO INVÁLIDA!!!")
            input("Tecle ENTER para continuar")



def p_os_fechada():
    os.system("clear")
    print("\t+-------------------------+")
    print("\t| PESQUISA - OSs FECHADAS |")
    print("\t+-------------------------+")
    print()
    print("\t1 - Pesquisar por CPF e identificador")
    print("\t0 - voltar ao menu anterior")
    print()
    op = input("O que deseja fazer ? ")
    while op != "0":
        if op == "1":
            os.system("clear")
            print("Por favor, insira o CPF")
            print("Apenas números.")
            print()
            cpf = input("CPF: ")
            cpf = data(cpf)
            #verif = checker_cpf_br(cpf)#
            #while verif != True:
            #    os.system("clear")
            #    print("CPF INVÁLIDO!!!")
            #    print("insira um CPF válido.")
            #    print()
            #    cpf = input("CPF: ")
            #    verif = checker_cpf_br(cpf)
            if cpf in clientes:
                os.system("clear")
                print("Por favor, insira o identificador do veiculo")
                print("Exemplo: ABC1D23")
                print()
                id = input("Identificador: ")
                id = data(id)
                if id in os_aberta:
                    prt_os_f()
                    input("Tecle ENTER para continuar")
                else:
                    print("IDENTIFICADOR NÃO CADASTRADO!!!")
                    input("Tecle ENTER para continuar")
            else:
                print("CPF NÃO CADASTRADO!!!")
                input("Tecle ENTER para continuar")
        else:
            os.system("clear")
            print("OPERAÇÃO INVÁLIDA!!!")
            input("Tecle ENTER para continuar")




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
                op3 = p_clientes()
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
                op3 = p_colab()
                op2 = menu_colab()
            else:
                print("OPÇÃO INVÁLIDA")
                op2 = menu_colab()
                input("Tecle ENTER para continuar")
        op1 = main_menu()
    elif op1 == "3":
        op2 = menu_os()
        while op2 != "0":
            if op2 == "1":
                op3 = cad_orc()
                op2 = menu_os()
            elif op2 == "2":
                op3 = p_orc()
                op2 = menu_os()
            elif op2 == "3":
                op3 = p_os_aberta()
                op2 = menu_os()
            elif op2 == "4":
                op3 = p_os_fechada()
                op2 = menu_os()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                op2 = menu_os()
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
#test.comit#
#####################
# PROJECT - SisGORA #
#####################
import os
def checker_cpf():
    cpf = input("Digite seu CPF por favor: ")
    cpf1 = cpf.replace(" ","")
    cpf = cpf1.replace(".","")
    cpf1 = cpf.replace(",","")
    cpf = cpf1.replace("-","")
    validation = cpf.isdigit()
    if validation == True:
        list_cpf = list(cpf)
        if len(list_cpf) != 11:
            cpf = input("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
            return cpf
        else:
            d10 = list_cpf[10]
            d09 = list_cpf[9]
            d08 = 2*list_cpf[8]
            d07 = 3*list_cpf[7]
            d06 = 4*list_cpf[6]
            d05 = 5*list_cpf[5]
            d04 = 6*list_cpf[4]
            d03 = 7*list_cpf[3]
            d02 = 8*list_cpf[2]
            d01 = 9*list_cpf[1]
            d00 = 10*list_cpf[0]
            total = d08 + d07 + d06 + d05 + d04 + d03 + d02 + d01 + d00
            rest = total % 11
            if d09 != 11 - rest:
                cpf = input("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
                return cpf
            else:
                d10 = list_cpf[10]
                d09 = 2*list_cpf[9]
                d08 = 3*list_cpf[8]
                d07 = 4*list_cpf[7]
                d06 = 5*list_cpf[6]
                d05 = 6*list_cpf[5]
                d04 = 7*list_cpf[4]
                d03 = 8*list_cpf[3]
                d02 = 9*list_cpf[2]
                d01 = 10*list_cpf[1]
                d00 = 11*list_cpf[0]
                total = d09 + d08 + d07 + d06 + d05 + d04 + d03 + d02 + d01 + d00
                rest = total % 11
                if d10 != 11 - rest:
                    cpf = input("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
                    return cpf
        cpf = (cpf,"CPF válido!")
        return cpf
    else:
        cpf = input("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
        return cpf
def checker_celular():
    celular = input("Digite seu celular por favor: ")
    celular1 = celular.replace(" ","")
    celular = celular1.replace(".","")
    celular1 = celular.replace(",","")
    celular = celular1.replace("-","")
    celular1 = celular.replace("(","")
    celular = celular1.replace(")","")
    celular1 = celular.replace("+","")
    validation = celular1.isdigit()
    if validation == True:

def main_menu():
    os.system("clear")
    print("#####            #####  #####  #####  #####")
    print("#                #      #   #  #  #   #   #")
    print("#      ###  ###  #      #   #  # #    #   #")
    print("#####   #   #    #  ##  #   #  # #    #####")
    print("    #   #   ###  #   #  #   #  #  #   #   #")
    print("    #   #     #  #   #  #   #  #   #  #   #")
    print("#####  ###  ###  #####  #####  #   #  #   #")
    print("=============================================================================================")
    print("=MENU PRINCIPAL - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("=============================================================================================")
    print("\t01 - Clientes")
    print("\t02 - Colaboradores")
    print("\t03 - Ordens de serviços(O.S.)")
    print("\t04 - Orçamentos e agendamentos")
    print("\t05 - Loja")
    print("\t06 - Administrativo")
    print("\t00 - Sair")
    option = input("Escolha uma opção por favor: ")
    return option
def clientes_menu():
    os.system("clear")
    print("============================================================================================")
    print("=MENU CLIENTES - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("============================================================================================")
    print("\t01 - Novo cadastro")
    print("\t02 - Pesquisar cadastro")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def cadastro_cliente():
    cpf = checker_cpf()

def colaboradores_menu():
    os.system("clear")
    print("=================================================================================================")
    print("=MENU COLABORADORES - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("=================================================================================================")
    print("\t01 - Novo cadastro")
    print("\t02 - Pesquisar colaborador")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def os_menu():
    os.system("clear")
    print("======================================================================================================")
    print("=MENU ORDENS DE SERVIÇOS - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("======================================================================================================")
    print("\t01 - Nova O.S.")
    print("\t02 - O.S. Abertas")
    print("\t03 - O.S. Fechadas")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def orcamentos_menu():
    os.system("clear")
    print("=============================================================================================================")
    print("=MENU ORÇAMENTOS E AGENDAMENTOS - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("=============================================================================================================")
    print("\t01 - Novo orçamento")
    print("\t02 - Pesquisar orçamento")
    print("\t03 - Novo agendamento")
    print("\t04 - Pesquisar agendamento")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def loja_menu():
    os.system("clear")
    print("========================================================================================")
    print("=MENU LOJA - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("========================================================================================")
    print("\t01 - Nova venda")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def administrativo_menu():
    os.system("clear")
    print("==================================================================================================")
    print("=MENU ADMINISTRATIVO - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("==================================================================================================")
    print("\t01 - Pedidos")
    print("\t02 - Vendas")
    print("\t03 - Comissões")
    print("\t04 - Finanças")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
##################
# MAIN - PROGRAM #
##################
operation01 = main_menu()
while operation01 != "0" or operation01 != "00":
    if operation01 == "1" or operation01 == "01":
        print("=        MENU - Clientes selecionado        =")
        operation02 = clientes_menu()
        while operation02 != "0" or operation02 != "00":
            if operation02 == "1" or operation02 == "01":
    elif operation01 == "2" or operation01 == "02":
        print("=     MENU - Colaboradores selecionado      =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "3" or operation01 == "03":
        print("=MENU - Ordens de Serviços(O.S.) selecionado=")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "4" or operation01 == "04":
        print("=MENU - Oçamentos e agendamentos selecionado=")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "5" or operation01 == "05":
        print("=          MENU - Loja selecionado          =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "6" or operation01 == "06":
        print("=     MENU - Administrativo selecionado     =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "0" or operation01 == "00":
        print("=             PROGRAMA ENCERRADO            =")
        print("=                ATÉ BREVE !                =")
    else:
        print("=            OPÇÃO INVÁLIDA !!!!!           =")
    input("Tecla ENTER para continuar")
    operation01 = main_menu()
print("FIM")

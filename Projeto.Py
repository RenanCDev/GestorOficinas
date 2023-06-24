#test.comit#
#####################
# PROJECT - SisGORA #
#####################
import os
def checker_cpf():
    print("Digite seu CPF por favor: ")
    cpf = input("")
    cpf1 = cpf.replace(" ","")
    cpf2 = cpf1.replace(".","")
    cpf3 = cpf2.replace(",","")
    cpf = cpf3.replace("-","")
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
    print("============================================================================================")
    print("=MENU CLIENTES - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("============================================================================================")
    print("\t01 - Novo cadastro")
    print("\t02 - Pesquisar cadastro")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def colaboradores_menu():
    print("=================================================================================================")
    print("=MENU COLABORADORES - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("=================================================================================================")
    print("\t01 - Novo cadastro")
    print("\t02 - Pesquisar colaborador")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def os_menu():
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
    print("========================================================================================")
    print("=MENU LOJA - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("========================================================================================")
    print("\t01 - Nova venda")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def administrativo_menu():
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
operation = main_menu()
while operation != 0:
    if operation == "1" or operation == "01":
        print("=        MENU - Clientes selecionado        =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation == "2" or operation == "02":
        print("=     MENU - Colaboradores selecionado      =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation == "3" or operation == "03":
        print("=MENU - Ordens de Serviços(O.S.) selecionado=")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation == "4" or operation == "04":
        print("=MENU - Oçamentos e agendamentos selecionado=")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation == "5" or operation == "05":
        print("=          MENU - Loja selecionado          =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation == "6" or operation == "06":
        print("=     MENU - Administrativo selecionado     =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation == "0" or operation == "00":
        print("=             PROGRAMA ENCERRADO            =")
        print("=                ATÉ BREVE !                =")
    else:
        print("=            OPÇÃO INVÁLIDA !!!!!           =")
    input("Tecla ENTER para continuar")
    operation = main_menu()
print("FIM")

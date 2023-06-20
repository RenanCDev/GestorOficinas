#####################
# PROJECT - SisGORA #
#####################
import os
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
    print("\t04 - Administrativo")
    print("\t00 - Sair")
    option = input("Escolha uma opção por favor: ")
    return option
##################
# MAIN - PROGRAM #
##################
operation01 = main_menu()
while operation01 != 0:
    if operation01 == "1" or operation01 == "01":
        print("=        MENU - Clientes selecionado        =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "2" or operation01 == "02":
        print("=     MENU - Colaboradores selecionado      =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "3" or operation01 == "03":
        print("=MENU - Ordens de Serviços(O.S.) selecionado=")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    elif operation01 == "4" or operation01 == "04":
        print("=     MENU - Administrativo selecionado     =")
        print("=   EM DESENVOLVIMENTO, VOLTE EM BREVE !    =")
    else:
        print("=            OPÇÃO INVÁLIDA !!!!!           =")
    input("Tecla ENTER para continuar")
    operation01 = main_menu()
print("FIM")

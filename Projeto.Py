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
            print("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
            cpf = checker_cpf
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
                print("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
                cpf = checker_cpf
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
                    print("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
                    cpf = checker_cpf
                    return cpf
        cpf = cpf
        print("CPF válido!")
        return cpf
    else:
        print("CPF INVÁLIDO!!! Insira um CPF válido, por favor:")
        cpf = checker_cpf()
        return cpf
def checker_celular():
    print("O celular deve estar com o DDD Ex.: (XX)XXXXX-XXXX ")
    celular = input("Digite seu celular por favor: ")
    celular1 = celular.replace(" ","")
    celular = celular1.replace(".","")
    celular1 = celular.replace(",","")
    celular = celular1.replace("-","")
    celular1 = celular.replace("(","")
    celular = celular1.replace(")","")
    celular1 = celular.replace("+","")
    celular = celular1
    validation = celular.isdigit()
    list_celular = list(celular)
    if validation == True and len(list_celular) == 11:
        print("Celular válidado com sucesso")
        return celular
    else:
        print("CELULAR INVÁLIDO!!!")
        celular = checker_celular
        return celular
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
    os.system("clear")
    cpf = checker_cpf()
    celular = checker_celular()
    print("EM DESENVOLVIMENTO!")
def p_cadastro_cliente():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
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
def cadastro_colaborador():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_cadastro_colaborador():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
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
def cadastro_os():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_os_aberta():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_os_fechada():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
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
def cadastro_orcamento():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_orcamento():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def cadastro_agendamento():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_agendamento():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def loja_menu():
    os.system("clear")
    print("========================================================================================")
    print("=MENU LOJA - Sistema de Gerenciamento Para Oficinas de Refrigeração Automotiva(SisGORA)=")
    print("========================================================================================")
    print("\t01 - Nova venda")
    print("\t00 - Voltar ao menu anterior")
    option = input("Escolha uma opção por favor: ")
    return option
def cadastro_venda():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
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
def cadastro_pedido():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_pedido():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_venda():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def baixar_comissao():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_comissao():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def cadastrar_debito():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
def p_debito():
    os.system("clear")
    print("EM DESENVOLVIMENTO!")
##################
# MAIN - PROGRAM #
##################
operation01 = main_menu()
while operation01 != "0" or operation01 != "00":
    if operation01 == "1" or operation01 == "01":
        print("== MENU - Clientes selecionado ==")
        operation02 = clientes_menu()
        while operation02 != "0" or operation02 != "00":
            if operation02 == "1" or operation02 == "01":
                print("== CADASTRO - NOVO CLIENTE ==")
                cadastro = cadastro_cliente()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation01 == "2" or operation02 == "02":
                print("== PESQUISAR - CADASTROS DE CLIENTES ==")
                pesquisa = p_cadastro_cliente()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
        input("Tecle ENTER para continuar")
        operation01 = main_menu()
    elif operation01 == "2" or operation01 == "02":
        print("== MENU - Colaboradores selecionado ==")
        operation02 = colaboradores_menu()
        while operation02 != "0" or operation02 != "00":    
            if operation02 == "1" or operation02 == "01":
                print("== CADASTRO - NOVO COLABORADOR ==")
                cadastro = cadastro_colaborador()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "2" or operation02 == "02":
                print("== PESQUISAR - CADASTROS DE COLABORADORES ==")
                pesquisa = p_cadastro_colaborador()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
        input("Tecle ENTER para continuar")
        operation01 = main_menu()
    elif operation01 == "3" or operation01 == "03":
        print("== MENU - Ordens de Serviços(O.S.) selecionado ==")
        operation02 = os_menu()
        while operation02 != "0" or operation02 != "00":
            if operation02 == "1" or operation02 == "01":
                print("== CADASTRO - NOVA ORDEM DE SERVICO ==")
                cadastro = cadastro_os()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "2" or operation01 == "02":
                print("== PESQUISAR - OSs ABERTAS ==")
                pesquisa = p_os_aberta()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "3" or operation02 == "03":
                print("== PESQUISAR - OSs FECHADAS ==")
                pesquisa = p_os_fechada()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
        input("Tecle ENTER para continuar")
        operation01 = main_menu()
    elif operation01 == "4" or operation01 == "04":
        print("== MENU - Oçamentos e agendamentos selecionado ==")
        operation02 = orcamentos_menu()
        while operation02 != "0" or operation02 != "00":
            if operation02 == "1" or operation02 == "01":
                print("== CADASTRO - NOVO ORÇAMENTO ==")
                cadastro = cadastro_orcamento()
                input("Tecle ENTER para continuar")
                operation01 = main_menu
            elif operation02 == "2" or operation02 == "02":
                print("== PESQUISAR - CADASTROS DE ORÇAMENTOS ==")
                pesquisa = p_orcamento()
                input("Tecle ENTER para continuar")
                operation01 = main_menu
            elif operation02 == "3" or operation02 == "03":
                print("== CADASTRO - AGENDAMENTO ==")
                cadastro = cadastro_agendamento()
                input("Tecle ENTER para continuar")
                operation01 = main_menu
            elif operation02 == "4" or operation01 == "04":
                print("== PESQUISAR - CADASTROS DE AGENDAMENTOS ==")
                pesquisa = p_agendamento
                input("Tecle ENTER para continuar")
                operation01 = main_menu
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
        input("Tecle ENTER para continuar")
        operation01 = main_menu()
    elif operation01 == "5" or operation01 == "05":
        print("== MENU - Loja selecionado ==")
        operation02 = loja_menu()
        while operation02 != "0" or operation02 != "00":
            if operation02 == "1" or operation02 == "01":
                print("== CADASTRO - NOVA VENDA ==")
                cadastro = cadastro_venda
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
        input("Tecle ENTER para continuar")
        operation01 = main_menu()
    elif operation01 == "6" or operation01 == "06":
        print("== MENU - Administrativo selecionado ==")
        operation02 = administrativo_menu()
        while operation02 != "0" or operation02 != "00":
            if operation02 == "1" or operation02 == "01":
                print("== CADASTRO - NOVO PEDIDO ==")
                cadastro = cadastro_pedido()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "2" or operation02 == "02":
                print("== PESQUISAR - PEDIDOS ==")
                pesquisa = p_pedido()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "3" or operation02 == "03":
                print("== PESQUISAR - VENDAS ==")
                pesquisa = p_venda()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "4" or operation02 == "04":
                print("== BAIXAR - COMISSÃO ==")
                comissao = baixar_comissao()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "5" or operation02 == "05":
                print("== PESQUISA - CADASTROS DE COMISSÃO ==")
                pesquisa = p_comissao()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "6" or operation02 == "06":
                print("== CADASTRO - NOVO DÉBITO ==")
                cadastro = cadastrar_debito()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            elif operation02 == "7" or operation02 == "07":
                print("== PESQUUISAR - CADASTROS DE DEBITOS ==")
                pesquisa = p_debito()
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
            else:
                print("OPÇÃO INVÁLIDA!!!")
                input("Tecle ENTER para continuar")
                operation01 = main_menu()
        input("Tecle ENTER para continuar")
        operation01 = main_menu()
    else:
        print("=            OPÇÃO INVÁLIDA !!!!!           =")
    input("Tecle ENTER para continuar")
    operation01 = main_menu()
print("=             PROGRAMA ENCERRADO            =")
print("=                ATÉ BREVE !                =")
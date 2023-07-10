#########################
### PROJECT - SisGORA ###
#########################



#PROGRAMA IDEALIZADO E DEZENVOLVIDO POR: RENAN MISSIAS RODRIGUES ALVES DA COSTA##
#NÚMERO DE MATRICULA: 20230078244#
#COLABORADORES E CONSULTORES:#
##PROFESSOR - FLAVIUS GORGONIO##
##ALUNO - GUILHERME DE MEDEIROS SANTOS - 20230032755##
##ALUNO - DENNER BISMARCK DE LUCENA FRANÇA - 20230031014##
##ALUNO - ARON DA SILVA BEZERRA - 20230059632##
##ALUNO - JEFERSON HENRIQUE SOBRINHO - 20230064991##
##ALUNO - MARLISON SOARES DA SILVA - 20230035407##



import os
import insert
import prt
import edit
import opt
import arquivs
import reload



clientes = {}
colaboradores = {}
orcamentos = {}
ord_serv_abert = {}
ord_serv_fechad = {}



clientes = arquivs.read_all("clientes.dat")
colaboradores = arquivs.read_all("colaboradores.dat")
orcamentos = arquivs.read_all("orcamentos.dat")
ord_serv_abert = arquivs.read_all("ord_serv_abert.dat")
ord_serv_fechad = arquivs.read_all("ord_serv_fechad.dat")



def main_menu():
    os.system("clear || cls")
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
    os.system("clear || cls")
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
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    cpf = insert.insert_cpf()
    if cpf not in clientes:
        cel = insert.insert_cel()
        os.system("clear || cls")
        name = insert.insert_name()
        nasciment = insert.insert_nasciment()
        os.system("clear || cls")
        clientes[cpf] = [cel, nasciment, name]  
        arquivs.insert("clientes.dat", clientes)
        print("Cadastro realizado com sucesso!")
        print()
        input("Tecle ENTER para continuar")
    else:
        os.system("clear || cls")
        print("CPF já cadastrado")
        print()
        input("Tecle ENTER para continuar")



def pesq_clientes():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    cpf = insert.insert_cpf()
    if cpf in clientes:
        prt.print_client(cpf)
        option = opt.option_pesq_cad()
        if option != "0":
            if option == "1":
                cpf
                clientes[cpf] = edit.edit_cad_client(cpf)
                print()
                input("Tecle ENTER para continuar")
            elif option == "2":
                prt.print_client(cpf)
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    edit.exc_client(cpf)
                elif exc != "n" and exc != "s":
                    prt.data_invalid()
            else:
                prt.data_invalid()
                input("Tecle ENTER para continuar")
    else:
        os.system("clear || cls")
        print("CPF NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def menu_colab():
    os.system("clear || cls")
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
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    cpf = insert.insert_cpf()
    if cpf not in colaboradores:
        cel = insert.insert_cel()
        name = insert.insert_name()
        nasciment = insert.insert_nasciment()
        os.system("clear || cls")
        colaboradores[cpf] = [cel, nasciment, name]  
        arquivs.insert("colaboradores.dat", colaboradores)
        print("Cadastro realizado com sucesso!")
        print()
        input("Tecle ENTER para continuar")
    else:
        os.system("clear || cls")
        print("CPF CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def pesq_colab():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    cpf = insert.insert_cpf()
    if cpf in colaboradores:
        prt.print_colab(cpf)
        option = opt.option_pesq_cad()
        if option != "0":
            if option == "1":
                colaboradores[cpf] = edit.edit_cad_colab(cpf)
                print("Cadastro alterado com sucesso!")
                print()
                input("Tecle ENTER para continuar")
            elif option == "2":
                prt.print_colab(cpf)
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    edit.exc_colab(cpf)
                elif exc != "n" and exc != "s":
                    prt.data_invalid()
            else:
                prt.data_invalid()
        else:
            prt.data_invalid()
    else:
        os.system("clear || cls")
        print("CPF NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def menu_ord_serv():
    os.system("clear || cls")
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
    option = input("Escolha uma opção por favor: ")
    return option



def cad_orcament():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    print("\t+---------------------------+")
    print("\t| CADASTRO - NOVO ORÇAMENTO |")
    print("\t+---------------------------+")
    cpf = insert.insert_cpf()
    if cpf in clientes:
        model = insert.insert_model()
        id = insert.insert_id()
        problem = insert.insert_problem()
        servic = insert.insert_servic()
        val_servic = insert.insert_val_servic()
        val_m_obra = insert.insert_val_m_obra()
        os.system("clear || cls")
        mec = input("Refrigerista: ")
        orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
        arquivs.insert("orcamentos.dat", orcamentos)
    else:
        print("CPF NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def pesq_orcament():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    print("\t+-----------------------+")
    print("\t| PESQUISA - ORÇAMENTOS |")
    print("\t+-----------------------+")
    print()
    option = opt.option_pesq_orcament()
    while option != "0" and option != "1":
        prt.data_invalid()
        option = opt.option_pesq_orcament() 
    if option == "1":
            clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
            id = insert.insert_id()
            if id in orcamentos:
                prt.print_orcament(id)
                option = opt.option_orcament()
                while option != "0" and option != "1" and option != "2" and option != "3":
                    prt.data_invalid()
                    prt.print_orcament(id)
                    option = opt.option_orcament()
                if option == "1":
                    os.system("clear || cls")
                    print("Orçamento transformado em ordem de serviço aberta com sucesso!")
                    print()
                    input("Tecle ENTER para continuar")
                    edit.transf_ord_serv_abert(id)
                elif option == "2":
                    orcamentos[id] = edit.edit_orcament(id)
                    arquivs.insert("orcamentos.dat", orcamentos)
                elif option == "3":
                    del(orcamentos[id])
                    arquivs.insert("orcamentos.dat", orcamentos)
                    os.system("clear || cls")
                    print("Orçamento excluido com sucesso!")
                    print()
                    input("Tecle ENTER para continuar")
                else:
                    prt.data_invalid()
            else:
                os.system("clear || cls")
                print("IDENTIFICADOR NÃO CADASTRADO!!!")
                print()
                input("Tecle ENTER para continuar")



def pesq_ord_serv_abert():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    print("\t+------------------------+")
    print("\t| PESQUISA - OSs ABERTAS |")
    print("\t+------------------------+")
    print()
    input("Tecle ENTER para continuar")
    id = insert.insert_id()
    if id in ord_serv_abert:
        prt.print_ord_serv_abert(id)
        option = opt.option_ord_serv_abert()
        while option != "0" and option != "1" and option != "2" and option != "3":
            prt.data_invalid()
            prt.print_orcament(id)
            option = opt.option_ord_serv_abert()
        if option == "1":
            os.system("clear || cls")
            print("Ordem de serviço transformada em ordem de serviço fechada com sucesso!")
            print()
            input("Tecle ENTER para continuar")
            edit.transf_ord_serv_fechad(id)
        elif option == "2":
            ord_serv_abert[id] = edit.edit_ord_serv_abert(id)
            arquivs.insert("ord_serv_abert.dat", ord_serv_abert)
        elif option == "3":
            del(ord_serv_abert[id])
            arquivs.insert("ord_serv_abert.dat", ord_serv_abert)
            os.system("clear || cls")
            print("Ordem de serviço excluida com sucesso!")
            print()
            input("Tecle ENTER para continuar")
        else:
            prt.data_invalid()
    else:
        os.system("clear || cls")
        print("IDENTIFICADOR NÃO CADASTRADO!!!")
        print()
        input("Tecle ENTER para continuar")



def pesq_ord_serv_fechad():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    print("\t+-------------------------+")
    print("\t| PESQUISA - OSs FECHADAS |")
    print("\t+-------------------------+")
    option = input("Deseja pesquisar alguma ordem de serviço fechada ? (s/n) ")
    if option == "s":
        id = insert.insert_id()
        if id in ord_serv_fechad:
            os.system("clear || cls")
            prt.print_ord_serv_fechad(id)
            print()
            input("Tecle ENTER para continuar")
        else:
            print("IDENTIFICADOR NÃO CADASTRADO!!!")
            print()
            input("Tecle ENTER para continuar")
    elif option != "n" and option != "s":
        prt.data_invalid()



def menu_loja():
    os.system("clear || cls")
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
    os.system("clear || cls")
    print("\t+------------------+")
    print("\t| CADASTRO - VENDA |")
    print("\t+------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def menu_adm():
    os.system("clear || cls")
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
    os.system("clear || cls")
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
    os.system("clear || cls")
    print("\t+-------------------+")
    print("\t| CADASTRO - PEDIDO |")
    print("\t+-------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def p_ped():
    os.system("clear || cls")
    print("\t+--------------------+")
    print("\t| PESQUISA - PEDIDOS |")
    print("\t+--------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def venda():
    os.system("clear || cls")
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
    os.system("clear || cls")
    print("\t+-------------------+")
    print("\t| PESQUISA - VENDAS |")
    print("\t+-------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")


def comis():
    os.system("clear || cls")
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
    os.system("clear || cls")
    print("\t+-------------------+")
    print("\t| LANÇAR - COMISSÃO |")
    print("\t+-------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def p_comis():
    os.system("clear || cls")
    print("\t+----------------------+")
    print("\t| PESQUISA - COMISSÕES |")
    print("\t+----------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")


def deb():
    os.system("clear || cls")
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
    os.system("clear || cls")
    print("\t+------------------------+")
    print("\t| CADASTRO - NOVO DÉBITO |")
    print("\t+------------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



def p_deb():
    os.system("clear || cls")
    print("\t+---------------------------------+")
    print("\t| PESQUISA - CADASTROS DE DEBITOS |")
    print("\t+---------------------------------+")
    print()
    print("EM DESENVOLVIMENTO!")
    input("Tecle ENTER para continuar")



######################
### MAIN - PROGRAM ###
######################



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
                prt.data_invalid()
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
                prt.data_invalid()
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
                prt.data_invalid()
                op2 = menu_ord_serv()
        op1 = main_menu()
    elif op1 == "4":
        op2 = menu_loja()
        while op2 != "0":
            if op2 == "1":
                op3 = cad_venda()
                op2 = menu_loja()
            else:
                prt("OPÇÃO INVÁLIDA!!!")
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
                        prt("OPÇÃO INVÁLIDA!!!")
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
                        prt("OPÇÃO INVÁLIDA!!!")
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
                        prt.data_invalid()
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
                        prt.data_invalid()
                        op3 = deb()
                op2 = menu_adm()
            else:
                prt.data_invalid()
                op2 = menu_adm()
        op1 = main_menu()
    else:
        prt.data_invalid()
        op1 = main_menu()
print("=             PROGRAMA ENCERRADO            =")
print("=                ATÉ BREVE !                =")
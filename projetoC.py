#########################
### PROJECT - SisGORA ###
#########################
import os
import func_insert
import func_print
import func_edit
import func_option



clientes = {"11729951414":["83999008017", "22071999", "RENAN MISSIAS RODRIGUES ALVES DA COSTA"]}
colaboradores = {"11729951414":["83999008017", "22071999", "RENAN MISSIAS RODRIGUES ALVES DA COSTA"]}
orcamentos = {"ABC1D23":["11729951414", "GM - CORSA", "ABC1D23", "PROBLEMA", "SERVIÇO", 500, 280, "ARON SILVA"]}
os_aberta = {"ABC1D23":["11729951414", "GM - CORSA", "ABC1D23", "PROBLEMA", "SERVIÇO", 500, 280, "ARON SILVA"]}
os_fechada = {"ABC1D23":["11729951414", "GM - CORSA", "ABC1D23", "PROBLEMA", "SERVIÇO", 500, 280, "ARON SILVA"]}



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
    cpf = func_insert.insert_cpf()
    if cpf not in clientes:
        cel = func_insert.insert_cel()
        os.system("clear")
        name = func_insert.insert_name()
        nasciment = func_insert.insert_nasciment()
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
    cpf = func_insert.insert_cpf()
    if cpf in clientes:
        func_print.print_client(cpf)
        option = func_option.option_pesq_cad()
        if option != "0":
            if option == "1":
                cpf
                clientes[cpf] = func_edit.edit_cad_client(cpf)
                print("Cadastro alterado com sucesso!")
                print()
                input("Tecle ENTER para continuar")
            elif option == "2":
                func_print.print_client(cpf)
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    func_edit.exc_client(cpf)
                elif exc != "n" and exc != "s":
                    func_print.data_invalid()
            else:
                os.system("clear")
                input("Tecle ENTER para continuar")
        else:
            func_print.data_invalid()
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
    cpf = func_insert.insert_cpf()
    if cpf not in colaboradores:
        cel = func_insert.insert_cel()
        name = func_insert.insert_name()
        nasciment = func_insert.insert_nasciment()
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
    cpf = func_insert.insert_cpf()
    if cpf in colaboradores:
        func_print.print_colab(cpf)
        option = func_option.option_pesq_cad()
        if option != "0":
            if option == "1":
                cpf
                colaboradores[cpf] = func_edit.edit_cad_colab(cpf)
                print("Cadastro alterado com sucesso!")
                print()
                input("Tecle ENTER para continuar")
            elif option == "2":
                func_print.print_colab(cpf)
                exc = input("Deseja mesmo excluir esse perfil? (s/n) ")
                if exc == "s":
                    func_edit.exc_colab(cpf)
                elif exc != "n" and exc != "s":
                    func_print.data_invalid()
            else:
                func_print.data_invalid()
        else:
            func_print.data_invalid()
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
    option = input("Escolha uma opção por favor: ")
    return option



def cad_orcament():
    os.system("clear")
    print("\t+---------------------------+")
    print("\t| CADASTRO - NOVO ORÇAMENTO |")
    print("\t+---------------------------+")
    cpf = func_insert.insert_cpf()
    if cpf in clientes:
        model = func_insert.insert_model()
        id = func_insert.insert_id()
        problem = func_insert.insert_problem()
        servic = func_insert.insert_servic()
        val_servic = func_insert.insert_val_servic()
        val_m_obra = func_insert.insert_val_m_obra()
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
    option = func_option.option_pesq_orcament()
    while option != "0" and option != "1":
        func_print.data_invalid()
        option = func_option.option_pesq_orcament() 
    if option == "1":
            id = func_insert.insert_id()
            if id in orcamentos:
                func_print.print_orcament_0(id)
                option = func_option.option_orcament()
                while option != "0" and option != "1" and option != "2" and option != "3":
                    func_print.data_invalid()
                    func_print.print_orcament(id)
                    option = func_option.option_orcament()
                if option == "1":
                    os.system("clear")
                    print("Orçamento transformado em ordem de serviço aberta com sucesso!")
                    print()
                    input("Tecle ENTER para continuar")
                    func_edit.transf_ord_serv_abert(id)
                elif option == "2":
                    orcamentos[id] = func_edit.edit_orcament(id)
                elif option == "3":
                    del(orcamentos[id])
                    os.system("clear")
                    print("Orçamento excluido com sucesso!")
                    print()
                    input("Tecle ENTER para continuar")
                else:
                    func_print.data_invalid()
            else:
                os.system("clear")
                print("IDENTIFICADOR NÃO CADASTRADO!!!")
                print()
                input("Tecle ENTER para continuar")



def pesq_ord_serv_abert():
    os.system("clear")
    print("\t+------------------------+")
    print("\t| PESQUISA - OSs ABERTAS |")
    print("\t+------------------------+")
    print()
    input("Tecle ENTER para continuar")
    id = func_insert.insert_id()
    if id in os_aberta:
        func_print.print_ord_serv_abert(id)
        option = func_option.option_ord_serv_abert()
        while option != "0" and option != "1" and option != "2" and option != "3":
            func_print.data_invalid()
            func_print.print_orcament_0(id)
            option = func_option.option_ord_serv_abert()
        if option == "1":
            os.system("clear")
            print("Ordem de serviço transformada em ordem de serviço fechada com sucesso!")
            print()
            input("Tecle ENTER para continuar")
            func_edit.transf_ord_serv_fechad(id)
        elif option == "2":
            os_aberta[id] = func_edit.edit_ord_serv_abert(id)
        elif option == "3":
            del(os_aberta[id])
            os.system("clear")
            print("Ordem de serviço excluida com sucesso!")
            print()
            input("Tecle ENTER para continuar")
        else:
            func_print.data_invalid()
    else:
        os.system("clear")
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
        id = func_insert.insert_id()
        if id in os_fechada:
            os.system("clear")
            func_print.print_ord_serv_fechad(id)
            print()
            input("Tecle ENTER para continuar")
        else:
            print("IDENTIFICADOR NÃO CADASTRADO!!!")
            print()
            input("Tecle ENTER para continuar")
    elif option != "n" and option != "s":
        func_print.data_invalid()



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
                func_print.data_invalid()
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
                func_print.data_invalid()
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
                func_print.data_invalid()
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
                        func_print.data_invalid()
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
                        func_print.data_invalid()
                        op3 = deb()
                op2 = menu_adm()
            else:
                func_print.data_invalid()
                op2 = menu_adm()
        op1 = main_menu()
    else:
        func_print.data_invalid()
        op1 = main_menu()
print("=             PROGRAMA ENCERRADO            =")
print("=                ATÉ BREVE !                =")

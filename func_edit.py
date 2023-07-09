import os
import func_insert
import func_print
import database
import pickle



def edit_cad_client(cpf):
    func_print.print_client(cpf)
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = func_insert.insert_cel()
    else:
        cel = database.clientes[cpf][0]
        if edit != "n" and edit != "s" :
            func_print.data_invalid()
    func_insert.print_client(cpf)
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        name = func_insert.insert_name()
    else:
        name = database.clientes[cpf][1]
        if edit != "n" and edit != "s":
            func_print.data_invalid()
    func_print.print_client(cpf)
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        func_print.print_client(cpf)
        nasciment = func_insert.insert_nasciment()
    else:
        nasciment = database.clientes[cpf][2]
        if edit != "n" and edit != "s":
            func_print.data_invalid()
    os.system("clear")
    print("Cadastro alterado com sucesso!")
    database.clientes[cpf] = [cel, nasciment, name]
    return database.clientes[cpf]



def edit_cad_colab(cpf):
    func_print.print_colab(cpf)
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = func_insert.insert_cel()
    else:
        cel = database.colaboradores[cpf][0]
        if edit != "n" and edit != "s" :
            func_print.data_invalid()
    func_print.print_colab(cpf)
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        name = func_insert.insert_name()
    else:
        name =  database.colaboradores[cpf][1]
        if edit != "n" and edit != "s":
            func_print.data_invalid()
    func_print.print_colab(cpf)
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        func_print.print_client(cpf)
        nasciment = func_insert.insert_nasciment()
    else:
        nasciment = database.colaboradores[cpf][2]
        if edit != "n" and edit != "s":
            func_print.data_invalid()
    os.system("clear")
    print("Cadastro alterado com sucesso!")
    database.clientes[cpf] = [cel, nasciment, name]
    return database.clientes[cpf]



def edit_orcament(id):
    os.system("clear")
    database.orcamentos[id]
    func_print.print_orcament(id)
    edit = input("Deseja alterar o CPF? (s/n) ")   
    if edit == "s":
        cpf = func_insert.insert_cpf()
    else:
        cpf = database.orcamentos[id][0]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o problema? (s/n) ")
    if edit == "s":
        problem = func_insert.insert_problem()
    else:
        problem = database.orcamentos[id][3]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o serviço? (s/n) ")
    if edit == "s":
        servic = func_insert.insert_servic()
    else:
        servic = database.orcamentos[id][4]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o valor do serviço? (s/n) ")
    if edit == "s":
        val_servic = func_insert.insert_val_servic()
    else:
        val_servic = database.orcamentos[id][5]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
    if edit == "s":
        val_m_obra = func_insert.insert_val_m_obra()
    else:
        val_m_obra = database.orcamentos[id][6]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o refrigerista? (s/n) ")
    if edit == "s":
        os.system("clear")
        mec = input("Novo refrigerista: ") 
    else:
        mec = database.orcamentos[id][7]
        if edit != "n":
            func_print.data_invalid()
    model = database.orcamentos[id][1]
    database.orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    return database.orcamentos[id]



def edit_ord_serv_abert(id):
    os.system("clear")
    database.os_aberta[id]
    func_print.print_orcament(id)
    edit = input("Deseja alterar o CPF? (s/n) ")   
    if edit == "s":
        cpf = func_insert.insert_cpf()
    else:
        cpf = database.os_aberta[id][0]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o problema? (s/n) ")
    if edit == "s":
        problem = func_insert.insert_problem()
    else:
        problem = database.os_aberta[id][3]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o serviço? (s/n) ")
    if edit == "s":
        servic = func_insert.insert_servic()
    else:
        servic = database.os_aberta[id][4]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o valor do serviço? (s/n) ")
    if edit == "s":
        val_servic = func_insert.insert_val_servic()
    else:
        val_servic = database.os_aberta[id][5]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
    if edit == "s":
        val_m_obra = func_insert.insert_val_m_obra()
    else:
        val_m_obra = database.os_aberta[id][6]
        if edit != "n":
            func_print.data_invalid()
    func_print.print_orcament(id)
    edit = input("Deseja alterar o refrigerista? (s/n) ")
    if edit == "s":
        os.system("clear")
        mec = input("Novo refrigerista: ") 
    else:
        mec = database.os_aberta[id][7]
        if edit != "n":
            func_print.data_invalid()
    model = database.os_aberta[id][1]
    database.os_aberta[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    return database.os_aberta[id]



def transf_ord_serv_abert(id):
    database.os_aberta[id] = database.orcamentos[id]
    del(database.orcamentos[id])
    os.system("clear")
    print("CPF: ",database.os_aberta[id][0])
    print()
    print("Modelo: ",database.os_aberta[id][1])
    print()
    print("Identificador: ",database.os_aberta[id][2])
    print()
    print("Problema: ",database.os_aberta[id][3])
    print()
    print("Serviço: ",database.os_aberta[id][4])
    print()
    print("Valor do serviço: ",database.os_aberta[id][5])
    print()
    print("Valor da mão de obra: ",database.os_aberta[id][6])
    print()
    print("Refrigerista: ",database.os_aberta[id][7])
    print()



def transf_ord_serv_fechad(id):
    database.os_fechada[id] = database.os_aberta[id]
    del(database.os_aberta[id])
    os.system("clear")
    print("CPF: ",database.os_fechada[id][0])
    print()
    print("Modelo: ",database.os_fechada[id][1])
    print()
    print("Identificador: ",database.os_fechada[id][2])
    print()
    print("Problema: ",database.os_fechada[id][3])
    print()
    print("Serviço: ",database.os_fechada[id][4])
    print()
    print("Valor do serviço: ",database.os_fechada[id][5])
    print()
    print("Valor da mão de obra: ",database.os_fechada[id][6])
    print()
    print("Refrigerista: ",database.os_fechada[id][7])
    print()



def exc_client(cpf):  
    os.system("clear")
    del(database.clientes[cpf])
    print("Perfil excluido com sucesso!")
    print()
    input("Tecle ENTER para continuar")



def exc_colab(cpf):
    os.system("clear")
    del(database.colaboradores[cpf])
    print("Perfil excluido com sucesso!")
    print()
    input("Tecle ENTER para continuar")




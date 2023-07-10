import os
import insert
import prt
import arquivs
import reload


# essas variáveis só existem nesse arquivo, importar outros arquivos apenas trará as variáveis deles se fizer:
# from reload import variavel
# mas isso nem sempre significa que você pegará a última versão de algo que a variável contém
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



def edit_cad_client(cpf):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    print(clientes)
    input()
    prt.print_client(cpf)
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = insert.insert_cel()
    else:
        cel = clientes[cpf][0]
        if edit != "n" and edit != "s" :
            prt.data_invalid()
    prt.print_client(cpf)
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        name = insert.insert_name()
    else:
        name = clientes[cpf][1]
        if edit != "n" and edit != "s":
            prt.data_invalid()

    prt.print_client(cpf)
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        prt.print_client(cpf)
        nasciment = insert.insert_nasciment()
    else:
        nasciment = clientes[cpf][2]
        if edit != "n" and edit != "s":
            prt.data_invalid()
    os.system("clear || cls")
    print("Cadastro alterado com sucesso!")
    clientes[cpf] = [cel, nasciment, name]
    print(clientes)
    arquivs.insert("clientes.dat", clientes) # dados atualizados no arquivo, prints depois daqui conterão os novos dados
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    print(clientes)



def edit_cad_colab(cpf):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    prt.print_colab(cpf)
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = insert.insert_cel()
    else:
        cel = colaboradores[cpf][0]
        if edit != "n" and edit != "s" :
            prt.data_invalid()
    prt.print_colab(cpf)
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        name = insert.insert_name()
    else:
        name =  colaboradores[cpf][1]
        if edit != "n" and edit != "s":
            prt.data_invalid()
    prt.print_colab(cpf)
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        prt.print_client(cpf)
        nasciment = insert.insert_nasciment()
    else:
        nasciment = colaboradores[cpf][2]
        if edit != "n" and edit != "s":
            prt.data_invalid()
    os.system("clear || cls")
    prt("Cadastro alterado com sucesso!")
    clientes[cpf] = [cel, nasciment, name]
    arquivs.insert("colaboradores.dat", colaboradores)
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def edit_orcament(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    orcamentos[id]
    prt.print_orcament(id)
    edit = input("Deseja alterar o CPF? (s/n) ")   
    if edit == "s":
        cpf = insert.insert_cpf()
    else:
        cpf = orcamentos[id][0]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o problema? (s/n) ")
    if edit == "s":
        problem = insert.insert_problem()
    else:
        problem = orcamentos[id][3]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o serviço? (s/n) ")
    if edit == "s":
        servic = insert.insert_servic()
    else:
        servic = orcamentos[id][4]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o valor do serviço? (s/n) ")
    if edit == "s":
        val_servic = insert.insert_val_servic()
    else:
        val_servic = orcamentos[id][5]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
    if edit == "s":
        val_m_obra = insert.insert_val_m_obra()
    else:
        val_m_obra = orcamentos[id][6]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o refrigerista? (s/n) ")
    if edit == "s":
        os.system("clear || cls")
        mec = input("Novo refrigerista: ") 
    else:
        mec = orcamentos[id][7]
        if edit != "n":
            prt.data_invalid()
    model = orcamentos[id][1]
    orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    arquivs.insert("orcamentos.dat", orcamentos)
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def edit_ord_serv_abert(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    ord_serv_abert[id]
    prt.print_orcament(id)
    edit = input("Deseja alterar o CPF? (s/n) ")   
    if edit == "s":
        cpf = insert.insert_cpf()
    else:
        cpf = ord_serv_abert[id][0]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o problema? (s/n) ")
    if edit == "s":
        problem = insert.insert_problem()
    else:
        problem = ord_serv_abert[id][3]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o serviço? (s/n) ")
    if edit == "s":
        servic = insert.insert_servic()
    else:
        servic = ord_serv_abert[id][4]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o valor do serviço? (s/n) ")
    if edit == "s":
        val_servic = insert.insert_val_servic()
    else:
        val_servic = ord_serv_abert[id][5]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o valor da mão de obra? (s/n) ")
    if edit == "s":
        val_m_obra = insert.insert_val_m_obra()
    else:
        val_m_obra = ord_serv_abert[id][6]
        if edit != "n":
            prt.data_invalid()
    prt.print_orcament(id)
    edit = input("Deseja alterar o refrigerista? (s/n) ")
    if edit == "s":
        os.system("clear || cls")
        mec = input("Novo refrigerista: ") 
    else:
        mec = ord_serv_abert[id][7]
        if edit != "n":
            prt.data_invalid()
    model = ord_serv_abert[id][1]
    ord_serv_abert[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    arquivs.insert("ord_serv_abert.dat", ord_serv_abert)
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def transf_ord_serv_abert(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    ord_serv_abert[id] = orcamentos[id]
    del(orcamentos[id])
    arquivs.insert("orcamentos.dat", orcamentos)
    arquivs.insert("ord_serv_abert.dat", ord_serv_abert)
    os.system("clear || cls")
    print("CPF: ",ord_serv_abert[id][0])
    print()
    print("Modelo: ",ord_serv_abert[id][1])
    print()
    print("Identificador: ",ord_serv_abert[id][2])
    print()
    print("Problema: ",ord_serv_abert[id][3])
    print()
    print("Serviço: ",ord_serv_abert[id][4])
    print()
    print("Valor do serviço: ",ord_serv_abert[id][5])
    print()
    print("Valor da mão de obra: ",ord_serv_abert[id][6])
    print()
    print("Refrigerista: ",ord_serv_abert[id][7])
    print()
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def transf_ord_serv_fechad(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    ord_serv_fechad[id] = ord_serv_abert[id]
    del(ord_serv_abert[id])
    arquivs.insert("ord_serv_abert.dat", ord_serv_abert)
    arquivs.insert("ord_serv_fechad.dat", ord_serv_fechad)
    ord_serv_abert = arquivs.read_all("ord_serv_abert.dat") 
    ord_serv_fechad = arquivs.read_all("ord_serv_fechad.dat")
    os.system("clear || cls")
    print("CPF: ",ord_serv_fechad[id][0])
    print()
    print("Modelo: ",ord_serv_fechad[id][1])
    print()
    print("Identificador: ",ord_serv_fechad[id][2])
    print()
    print("Problema: ",ord_serv_fechad[id][3])
    print()
    print("Serviço: ",ord_serv_fechad[id][4])
    print()
    print("Valor do serviço: ",ord_serv_fechad[id][5])
    print()
    print("Valor da mão de obra: ",ord_serv_fechad[id][6])
    print()
    print("Refrigerista: ",ord_serv_fechad[id][7])
    print()
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def exc_client(cpf):  
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    del clientes[cpf]
    print("Perfil excluido com sucesso!")
    print()
    input("Tecle ENTER para continuar")
    arquivs.insert("clientes.dat", clientes)
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def exc_colab(cpf):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    del colaboradores[cpf]
    print("Perfil excluido com sucesso!")
    print()
    input("Tecle ENTER para continuar")
    arquivs.insert("colaboradores.dat", colaboradores)
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
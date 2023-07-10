import os
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



def data_invalid():
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    print("ENTRADA INVÁLIDA!!!")
    print()
    input("Pressione ENTER continuar")
    os.system("clear || cls")
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def print_client(cpf):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    # o cliente printado aqui é o que ta salvo no arquivo, então você apenas verá novos dados depois que atualizar o arquivo
    # além disso, não é necessário salvar os arquivos novamente ao terminar de printar os dados, apenas de atualizar
    os.system("clear || cls")
    cel = clientes[cpf][0]
    nasc = clientes[cpf][1]
    name = clientes[cpf][2]
    print("CPF: ", cpf)
    print("Cel: ", cel)
    print("Data de nascimento: ", nasc)
    print("Nome: ", name)
    print()
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def print_colab(cpf):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    cel = colaboradores[cpf][0]
    nasc = colaboradores[cpf][1]
    name = colaboradores[cpf][2]
    print("CPF: ", cpf)
    print("Cel: ", cel)
    print("Data de nascimento: ", nasc)
    print("Nome: ", name)
    print()
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def print_orcament(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    os.system("clear || cls")
    orcamentos[id]
    cpf = orcamentos[id][0]
    print("CPF: ",cpf)
    print()
    model = orcamentos[id][1]
    print("Modelo: ",model)
    print()
    id = orcamentos[id][2]
    print("Identificador: ",id)
    print()
    problem = orcamentos[id][3]
    print("Problema: ", problem)
    print()
    servic = orcamentos[id][4]
    print("Serviço: ",servic)
    print()
    val_servic = orcamentos[id][5]
    print("Valor do serviço: ", val_servic)
    print()
    val_m_obra = orcamentos[id][6]
    print("Valor da mão de obra: ", val_m_obra)
    print()
    mec = orcamentos[id][7]
    print("Refrigerista: ", mec)
    print()
    orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def print_ord_serv_abert(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
    cpf = ord_serv_abert[id][0]
    print("CPF: ",cpf)
    print()
    model = ord_serv_abert[id][1]
    print("Modelo: ",model)
    print()
    id = ord_serv_abert[id][2]
    print("Identificador: ",id)
    print()
    problem = ord_serv_abert[id][3]
    print("Problema: ", problem)
    print()
    servic = ord_serv_abert[id][4]
    print("Serviço: ",servic)
    print()
    val_servic = ord_serv_abert[id][5]
    print("Valor do serviço: ", val_servic)
    print()
    val_m_obra = ord_serv_abert[id][6]
    print("Valor da mão de obra: ", val_m_obra)
    print()
    mec = ord_serv_abert[id][7]
    print("Refrigerista: ", mec)
    print()
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()



def print_ord_serv_fechad(id):
    clientes, colaboradores, orcamentos, ord_serv_abert, ord_serv_fechad = reload.get_dados()
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

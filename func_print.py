import os
import database
import pickle



def data_invalid():
    os.system("clear")
    print("ENTRADA INVÁLIDA!!!")
    print()
    input("Pressione ENTER continuar")
    os.system("clear")



def print_client(cpf):
    os.system("clear")
    cpf = cpf
    cel = database.clientes[cpf][0]
    nasc = database.clientes[cpf][1]
    name = database.clientes[cpf][2]
    print("CPF: ", cpf)
    print("Cel: ", cel)
    print("Data de nascimento: ", nasc)
    print("Nome: ", name)
    print()



def print_colab(cpf):
    os.system("clear")
    cpf = cpf
    cel = database.colaboradores[cpf][0]
    nasc = database.colaboradores[cpf][1]
    name = database.colaboradores[cpf][2]
    print("CPF: ", cpf)
    print("Cel: ", cel)
    print("Data de nascimento: ", nasc)
    print("Nome: ", name)
    print()



def print_orcament(id):
    os.system("clear")
    database.orcamentos[id]
    cpf = database.orcamentos[id][0]
    print("CPF: ",cpf)
    print()
    model = database.orcamentos[id][1]
    print("Modelo: ",model)
    print()
    id = database.orcamentos[id][2]
    print("Identificador: ",id)
    print()
    problem = database.orcamentos[id][3]
    print("Problema: ", problem)
    print()
    servic = database.orcamentos[id][4]
    print("Serviço: ",servic)
    print()
    val_servic = database.orcamentos[id][5]
    print("Valor do serviço: ", val_servic)
    print()
    val_m_obra = database.orcamentos[id][6]
    print("Valor da mão de obra: ", val_m_obra)
    print()
    mec = database.orcamentos[id][7]
    print("Refrigerista: ", mec)
    print()
    database.orcamentos[id] = [cpf, model, id, problem, servic, val_servic, val_m_obra, mec]



def print_ord_serv_abert(id):
    cpf = database.os_aberta[id][0]
    print("CPF: ",cpf)
    print()
    model = database.os_aberta[id][1]
    print("Modelo: ",model)
    print()
    id = database.os_aberta[id][2]
    print("Identificador: ",id)
    print()
    problem = database.os_aberta[id][3]
    print("Problema: ", problem)
    print()
    servic = database.os_aberta[id][4]
    print("Serviço: ",servic)
    print()
    val_servic = database.os_aberta[id][5]
    print("Valor do serviço: ", val_servic)
    print()
    val_m_obra = database.os_aberta[id][6]
    print("Valor da mão de obra: ", val_m_obra)
    print()
    mec = database.os_aberta[id][7]
    print("Refrigerista: ", mec)
    print()



def print_ord_serv_fechad(id):
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




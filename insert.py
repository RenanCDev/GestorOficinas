import os
def insert_model():
    os.system("clear")
    print("Por favor, insira a marca e o modelo do carro.")
    print("Exemplo: VW - Gol")
    print()
    model = input("Qual a marca e modelo ?")
    return model



def insert_id():
    os.system("clear")
    print("Por favor, insira o identificador do carro.")
    print("Exemplo: ABC1D23")
    print()
    id = input("Qual o identificador ?")
    id = data(id)
    return id



def insert_problem():
    os.system("clear")
    print("Por favor, descreva o problema.")
    print()
    problem = input("Problema: ")
    return problem 



def insert_servic():
    os.system("clear")
    print("Por favor, descreva o serviço")
    print()
    servic = input("Serviço: ")
    return servic



def val_servic():
    os.system("clear")
    print("Por favor, insira o valor do serviço.")
    print("Apenas números inteiros.")
    print()
    val_servic = int(input("Valor: "))
    return val_servic



def insert_val_m_obra():
    os.system("clear")
    print("Por favor, insira o valor da mão de obra.")
    print("Apenas números inteiros.")
    print()
    val_m_obra = int(input("Valor: "))
    return val_m_obra
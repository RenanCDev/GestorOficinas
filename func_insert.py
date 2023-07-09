import os
import verify 
import func_print



def data(va):
    va = va.replace(" ","")
    va = va.replace(".","")
    va = va.replace(",","")
    va = va.replace("-","")
    va = va.replace("(","")
    va = va.replace(")","")
    va = va.replace("/","")
    va = va.replace("+","")
    va = va.upper()
    return va



def insert_cpf():
    os.system("clear")
    print("Por favor, insira o CPF")
    print("Apenas números.")
    print()
    cpf = input("CPF: ")
    verif = verify.checker_cpf_br(cpf)
    while verif != True:
        func_print.data_invalid()
        os.system("clear")
        print("Por favor, insira o CPF")
        print("Apenas números.")
        print()
        cpf = input("CPF: ")
        verif = verify.checker_cpf_br(cpf)
    cpf = data(cpf)
    return cpf



def insert_cel():
    os.system("clear")
    print("Por favor, digite o celular.")
    print("Exemplo: DD N NNNN NNNN.")
    print()
    print("D = DDD do estado.")
    print("N = Número do celular.") 
    print()
    cel = input("Celular: ")
    verif = verify.checker_cel_br(cel)
    while verif != True:
        func_print.data_invalid()
        os.system("clear")
        print("Por favor, digite o celular.")
        print("Exemplo: DD N NNNN NNNN.")
        print()
        print("D = DDD do estado.")
        print("N = Número do celular.") 
        print()
        cel = input("Celular: ")
        verif = verify.checker_cel_br(cel)
    cel = data(cel)
    return cel



def insert_name():
    os.system("clear")
    print("Por favor, insira o nome completo")
    print("Apenas letras.")
    print()
    name = input("Nome: ")
    verif = verify.checker_name(name)
    while verif != True:
        func_print.data_invalid()
        os.system("clear")
        print("Por favor, insira o nome completo")
        print("Apenas letras.")
        print()
        name = input("Nome: ")
        verif = verify.checker_name(name)
    name = name.upper()
    return name



def insert_nasciment():
    os.system("clear") 
    print("Por favor, digite a data de nascimento")    
    print()
    print("Exemplo: DDMMAAAA")
    print("D = dia. ")
    print("M = mês. ")
    print("A = ano. ")
    print()
    nasciment = input("Data de nascimneto: ")
    nasciment = data(nasciment)
    return nasciment



def insert_model():
    os.system("clear")
    print("Por favor, insira a marca e o modelo do carro.")
    print("Exemplo: VW-GOL")
    print()
    model = input("Qual a marca e modelo ?")
    model = model.upper()
    return model



def insert_id():
    os.system("clear")
    print("Por favor, insira o identificador do carro.")
    print("Exemplo: ABC1D23")
    print()
    id = input("Qual o identificador ? ")
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
    print("Por favor, descreva o serviço.")
    print()
    servic = input("Serviço: ")
    return servic



def insert_val_servic():
    os.system("clear")
    print("Por favor, insira o valor do serviço.")
    print("Apenas números inteiros.")
    print()
    val_servic = input("Valor: ")
    verif = val_servic.isdigit()
    while verif != True:
        func_print.data_invalid()
        val_servic = input("Valor do serviço: ")
        verif = val_servic.isdigit()
    return val_servic



def insert_val_m_obra():
    os.system("clear")
    print("Por favor, insira o valor da mão de obra.")
    print("Apenas números inteiros.")
    print()
    val_m_obra = input("Valor: ")
    verif = val_m_obra.isdigit()
    while verif != True:
        func_print.data_invalid()
        val_m_obra = input("Valor da mão de obra: ")
        verif = val_m_obra.isdigit()
    return int(val_m_obra)

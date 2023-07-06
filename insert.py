import os
def insert_cpf():
    os.system("clear")
    print("Por favor, insira o CPF")
    print("Apenas números.")
    print()
    cpf = input("CPF: ")
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
    cel = data(cel)



def insert_name():
    os.system("clear")
    print("Por favor, insira o nome completo")
    print("Apenas letras.")
    print()
    name = input("Nome: ")
    name = name.upper()



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



def pesq_por_cpf(cpf):
    os.system("clear")
    cpf = insert_cpf()
    verif = checker_cpf_br(cpf)
    re_insert_cpf(verif)




def data_invalid():
    print("ENTRADA INVÁLIDA!!!")
    input("Pressione ENTER para inserir novamente")



def print_option_cad():
    print("\t1 - Editar cadastro")
    print("\t2 - Excluir cadastro")
    print("\t0 - Voltar")
    print()
    option = input("Qual opção deseja fazer? ")
    return option



def edit_cad_client():
    print_client()
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = insert_cel()
        verif = checker_cel_br(cel)
        while verif != True:
            data_invalid
            cel = insert_cel()
            verif = checker_cel_br(cel)
    elif edit != "n" and edit != "s" :
        data_invalid()
    print_client()
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        print_client()
        name = insert_name()
        verif = checker_name(name)
        while verif != True:
            data_invalid
            name = insert_name()
            verif = checker_name(name)
    elif edit != "n" and edit != "s":
        data_invalid()
    print_client()
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        print_client()
        nasciment = insert_nasciment()
    elif edit != "n" and edit != "s":
        data_invalid()
    os.system("clear")
    print("Cadastro alterado com sucesso!")
    clientes[cpf] = [cel, nasciment, name]
    return clientes[cpf]



def edit_cad_colab():
    print_colab()
    edit = input("Deseja alterar o celular? (s/n) ")
    if edit == "s":
        cel = insert_cel()
        verif = checker_cel_br(cel)
        while verif != True:
            data_invalid
            cel = insert_cel()
            verif = checker_cel_br(cel)
    elif edit != "n" and edit != "s" :
        data_invalid()
    print_colab()
    edit = input("Deseja alterar o nome? (s/n) ")
    if edit == "s":
        print_colab()
        name = insert_name()
        verif = checker_name(name)
        while verif != True:
            data_invalid
            name = insert_name()
            verif = checker_name(name)
    elif edit != "n" and edit != "s":
        data_invalid()
    print_colab()
    edit = input("Deseja alterar a data de nascimento? (s/n) ")
    if edit == "s":
        print_colab()
        nasciment = insert_nasciment()
    elif edit != "n" and edit != "s":
        data_invalid()
    os.system("clear")
    print("Cadastro alterado com sucesso!")
    colaboradores[cpf] = [cel, nasciment, name]
    return colaboradores[cpf]



def exc_client(exc):  
    if exc == "s":
        os.system("clear")
        del(clientes[cpf])
        print("Perfil excluido com sucesso!")
        input("Tecle ENTER para continuar")
    elif exc != "n" and exc != "s":
        data_invalid()


    
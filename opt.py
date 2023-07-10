import os



def option_pesq_cad():
    os.system("clear || cls")
    print()
    print("\t1 - Editar cadastro")
    print("\t2 - Excluir cadastro")
    print("\t0 - Voltar")
    print()
    option = input("Qual opção deseja fazer? ")
    return option



def option_orcament():
    print()
    print("\t1 - Tornar o orçamento em O.S. aberta.")
    print("\t2 - Editar orçamento.")
    print("\t3 - Excluir orçamento.")
    print("\t0 - Voltar ao menu anterior")
    print()
    option = input("Escolha uma opção: ")
    return option



def option_pesq_orcament():
    os.system("clear || cls")
    print()
    print("\t1 - Pesquisar por identificador")
    print("\t0 - Voltar ao menu anterior")
    print()
    option = input("O que deseja fazer ? ")
    return option



def option_ord_serv_abert():
    print()
    print("\t1 - Tornar o O.S. em O.S. fechada.")
    print("\t2 - Editar O.S.")
    print("\t3 - Excluir O.S.")
    print("\t0 - Voltar ao menu anterior")
    print()
    option = input("Escolha uma opção: ")
    return option
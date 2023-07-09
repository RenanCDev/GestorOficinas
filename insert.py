            id = insert_id()
            if id in orcamentos:
                print_orcament_0(id)
                option = option_orcament()
                while option != "0" and option != "1" and option != "2" and option != "3":
                    data_invalid()
                    print_orcament_0(id)
                    option = option_orcament()
                if option == "1":
                    os.system("clear")
                    print("Orçamento transformado em ordem de serviço aberta com sucesso!")
                    print()
                    input("Tecle ENTER para continuar")
                    transf_ord_serv_abert(id)
                elif option == "2":
                    orcamentos[id] = edit_orcament(id)
                elif option == "3":
                    del(orcamentos[id])
                    os.system("clear")
                    print("Orçamento excluido com sucesso!")
                    print()
                    input("Tecle ENTER para continuar")
                else:
                    data_invalid()
            else:
                os.system("clear")
                print("IDENTIFICADOR NÃO CADASTRADO!!!")
                print()
                input("Tecle ENTER para continuar")
import arquivs

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
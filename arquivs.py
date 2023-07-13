import pickle



#FUNÇÃO CRIADA PELO PROFESSOR FLAVIUS GORGONIO# #ADAPTADA PELO ALUNO - JEFERSON HENRIQUE SOBRINHO - 20230064991#
#RE-ADAPTADA PELO ALUNO - RENAN MISSIAS RODRIGUES ALVES DA COSTA - 20230078244#



def insert(doc, data):
  doc = open(doc, 'wb')
  pickle.dump(data, doc)
  doc.close()

def read_all(doc):
  list = {}
  try:
    arquiv = open(doc, 'rb')
    list = pickle.load(arquiv)
    arquiv.close()
  except:
    doc = open(doc, 'wb')
    doc.close()
  return list

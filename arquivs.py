import pickle

def insert(doc, data):
  doc = open(doc, 'wb')
  pickle.dump(data, doc)
  doc.close()

def read_all(doc):
  list_arquiv = {}
  try:
    arquiv = open(doc, 'rb')
    list_arquiv = pickle.load(arquiv)
    arquiv.close()
  except:
    doc = open(doc, 'wb')
    doc.close()
  return list_arquiv

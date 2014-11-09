import datetime
import lista

class Evento:
  def __init__(self, nome, data):
    self.nome = nome
    self.data = data
    self.listas = {}

  def adicionar_lista(self, lista):
    self.listas[lista.nome] = lista


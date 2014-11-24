import datetime
import models.lista

class Evento(object):
  def __init__(self, nome, data, preco_padrao):
    self.nome = nome
    self.data = data
    self.listas = {}
    self.preco_padrao = preco_padrao
    self.aberto = False

  def adicionar_lista(self, lista):
    self.listas[lista.nome] = lista


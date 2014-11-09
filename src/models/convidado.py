import datetime

class Convidado:
  def __init__(self, nome, sexo):
    self.nome = nome
    self.sexo = sexo
    self.entrada = None

  def registrar_entrada(self):
    self.entrada = datetime.datetime.now()

from errors.comissario_sem_vagas import ComissarioSemVagasError

class Lista:
  def __init__(self, nome, precos):
    self.nome = nome
    self.precos = precos
    self.comissarios = {}
    self.convidados = []

  def adicionar_comissario(self, comissario, numero_convidados):
    self.comissarios[comissario] = numero_convidados

  def adicionar_convidado(self, convidado, comissario):
    if self.comissarios[comissario] > 0:
      self.convidados.append(convidado)
      self.comissarios[comissario] -= 1
    else:
      raise ComissarioSemVagasError

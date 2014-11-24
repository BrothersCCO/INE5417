from errors.comissario_sem_vagas import ComissarioSemVagasError

class Lista:
  def __init__(self, nome, precos):
    self.nome = nome
    self.precos = precos
    self.comissarios = {}
    self.convidados = []

  def adicionar_comissario(self, comissario, convidados):
    self.comissarios[comissario] = convidados

  def adicionar_convidado(self, comissario, convidado):
    if self.comissario[comissario] > 0:
      self.convidados.append(convidado)
      self.comissarios[comissario] -= 1
    else:
      raise ComissarioSemVagasError

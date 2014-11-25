from errors.comissario_sem_vagas import ComissarioSemVagasError

class Lista:
  def __init__(self, nome, precos):
    self.nome = nome
    self.precos = precos
    self.comissarios = {}
    self.convidados = []

  def adicionar_comissario(self, comissario, numero_convidados):
    self.comissarios[comissario.nome] = {
      'comissario': comissario,
      'numero_convidados': numero_convidados
    }

  def adicionar_convidado(self, convidado, nome_comissario):
    if self.comissarios[nome_comissario]['numero_convidados'] > 0:
      self.convidados.append(convidado)
      self.comissarios[nome_comissario]['comissario'].entradas += 1
      self.comissarios[nome_comissario]['numero_convidados'] -= 1
    else:
      raise ComissarioSemVagasError

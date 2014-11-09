class Lista:
  def __init__(self, nome):
    self.nome = nome
    self.precos = {}
    self.comissarios = {}
    self.convidados = []

  def adicionar_comissario(self, comissario, convidados):
    self.comissarios[comissario] = convidados

  def adicionar_convidado(self, convidado):
    self.convidados.append(convidado)

  def adicionar_preco(self, limite, masculino, feminino):
    self.precos['m'] = masculino
    self.precos['f'] = feminino

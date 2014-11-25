import datetime
import errors
import factories.comissario
import factories.convidado
import factories.evento
import factories.lista
import pickle

class Gerenciador:
  _instance = None

  def __init__(self):
    self.eventos = {}

  @staticmethod
  def get_instance():
    if Gerenciador._instance is None:
      Gerenciador._instance = Gerenciador()
    return Gerenciador._instance

  def cadastrar_evento(self, nome, data, preco_padrao):
    e = factories.evento.EventoFactory.criar_evento(nome, data, preco_padrao)
    self.eventos[nome] = e

  def exportar_evento(self, evento, arquivo):
    with open(arquivo, 'wb') as f:
      pickle.dump(self.eventos[evento], f)

  def importar_evento(self, arquivo):
    with open(arquivo, 'rb') as f:
      e = pickle.load(f)
      self.eventos[e.nome] = e

  def iniciar_evento(self, evento):
    self.eventos[evento].aberto = True

  def finalizar_evento(self, evento):
    self.eventos[evento].aberto = False

  def criar_lista(self, nome, preco, evento):
    l = factories.lista.ListaFactory.criar_lista(nome, preco)
    self.eventos[evento].listas[nome] = l

  def adicionar_comissario(self, nome, lista, evento, numero_convidados):
    c = factories.comissario.ComissarioFactory.criar_comissario(nome)
    self.eventos[evento].listas[lista].adicionar_comissario(c, numero_convidados)

  def adicionar_convidado(self, nome, sexo, lista, evento, comissario):
    c = factories.convidado.ConvidadoFactory.criar_convidado(nome, sexo)
    self.eventos[evento].listas[lista].adicionar_convidado(c, comissario)

  def registrar_entrada(self, nome, sexo, evento):
    if not self.evento[evento].aberto:
      raise EventoNaoIniciadoError

    for l in self.eventos[evento].listas.values():
      for c in l:
        if c.nome == nome:
          c.entrada = datetime.now()
          return l.preco[sexo]
    else:
      return self.eventos[evento].preco_padrao[sexo]

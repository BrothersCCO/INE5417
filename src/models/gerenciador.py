import datetime
import factories

class Gerenciador:
  _instance = None

  def Gerenciador(self):
    self.eventos = {}

  @staticmethod
  def get_instance():
    if Gerenciador._instance is None:
      Gerenciador._instance = Gerenciador()
    return Gerenciador._instance

  def cadastrar_evento(self, nome, data):
    e = factories.evento.EventoFactory.criar_evento(nome, data)
    self.eventos[nome] = e

  def criar_lista(self, nome, precos, evento):
    l = factories.lista.ListaFactory.criar_lista(nome, precos)
    self.eventos[evento].listas[nome] = l

  def adicionar_comissario(self, nome, lista, evento, convidados):
    c = factories.comissario.ComissarioFactory.criar_comissario(nome)
    self.eventos[evento].listas[lista].adicionar_comissario(c)

  def adicionar_convidado(self, nome, sexo, lista, evento):
    c = factories.convidado.ConvidadoFactory.criar_convidado(nome, sexo)
    self.eventos[evento].listas[lista].adicionar_convidado(c)

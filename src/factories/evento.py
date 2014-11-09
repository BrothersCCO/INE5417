import datetime
from models.evento import Evento

class EventoFactory:
  @staticmethod
  def criar_evento(nome, data):
    if not isinstance(nome, str):
      raise TypeError('O nome deve ser uma string')

    if not isinstance(data. datetime.datetime):
      raise TypeError('A data deve ser um datetime.datetime')

    return Evento(nome, data)

from errors.sexo_invalido import SexoInvalidoError
from models.convidado import Convidado

class ConvidadoFactory:
  @staticmethod
  def criar_convidado(nome, sexo):
    if not sexo in ('m', 'f'):
      raise SexoInvalidoError

    return Convidado(nome, sexo)

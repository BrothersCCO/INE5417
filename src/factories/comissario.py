from models.comissario import Comissario

class ComissarioFactory:
  @staticmethod
  def criar_comissario(nome):
    if not isinstance(nome, str):
      raise TypeError('O nome deve ser uma string')
    
    return Comissario(nome)

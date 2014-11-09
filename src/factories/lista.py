from models.listas import Lista

class ListaFactory:
  @staticmethod
  def criar_lista(nome, precos):
    if not isinstance(nome, str):
      raise TypeError('O nome deve ser uma string')

    if not isinstance(precos, dict):
      raise TypeError('Os preços devem ser um hashmap limite -> valores')

    return Lista(nome, precos)

class SexoInvalidoError(Exception):
  def __init__(self):
    super(SexoInvalidoError, self).__init__('O sexo informado é inválido')

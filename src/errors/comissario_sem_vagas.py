class ComissarioSemVagasError(Exception):
  def __init__(self):
    super(ComissarioSemVagasError, self).__init__('O comissário informado não tem vagas disponíveis')

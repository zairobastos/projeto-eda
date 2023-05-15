class Cartao:
    def __init__(self, numeroCartao, nomeTitular, dataValidade, bandeira, codSeguranca):
        self.numeroCartao = numeroCartao
        self.nomeTitular = nomeTitular
        self.dataValidade = dataValidade
        self.bandeira = bandeira
        self.codSeguranca = codSeguranca

    def __str__(self) -> str:
        return f'Cartao(Número do Cartão = {self.numeroCartao}, Nome do Titular = {self.nomeTitular},  Data de Validade = {self.dataValidade}, Bandeira = {self.bandeira}, Código de Segurança = {self.codSeguranca})'

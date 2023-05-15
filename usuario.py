class Usuario:
    def __init__(self, nome, cpf, endereco, numCartao) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.numCartao = numCartao

    def __str__(self) -> str:
        return f'Usuário(Nome = {self.nome}, CPF = {self.cpf}, Endereço = {self.endereco}, Número do Cartão = {self.numCartao})'

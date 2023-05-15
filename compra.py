class Compra:
    def __init__(self, itens, valor, cpf) -> None:
        self.itens = itens
        self.valorCompra = valor
        self.cpf = cpf

    def __str__(self) -> str:
        return f'Compras(CPF = {self.cpf},Itens = {self.itens}, Valor da Compra = R$ {self.valorCompra})'

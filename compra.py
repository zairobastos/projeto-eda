from datetime import datetime


class Compra:
    def __init__(self, itens, valor, cpf, idcompra) -> None:
        self.itens = itens
        self.valorCompra = valor
        self.cpf = cpf
        self.idcompra = idcompra
        self.dataCompra = datetime.now().strftime('%d/%m/%Y %H:%M')

    def __str__(self) -> str:
        return f'Compras(ID= {self.idcompra},CPF = {self.cpf},Itens = {self.itens}, Valor da Compra = R$ {self.valorCompra}, data = {self.dataCompra})'

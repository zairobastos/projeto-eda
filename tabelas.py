class Tabela:
    def __init__(self, tamUsuario, tamCartao) -> None:
        self.tabelaUsuario = [None]*tamUsuario
        self.tamMaxUser = tamUsuario
        self.tabelaCartao = [None]*tamCartao
        self.tamMaxCart = tamCartao

    # Funções do Usuário
    def taxaOcupacaoUsuario(self):
        num_elementos = len(
            list(filter(lambda x: x is not None, self.tabelaUsuario)))
        taxa = round((num_elementos/self.tamMaxUser)*100, 2)
        return taxa, num_elementos

    # Funções do Cartão
    def taxaOcupacaoCartao(self, tipo):
        num_elementos = len(
            list(filter(lambda x: x is not None, self.tabelaCartao)))
        taxa = round((num_elementos/self.tamMaxCart)*100, 2)
        return taxa, num_elementos

    def exibirCartoes(self):
        for i in range(0, self.tamMaxCart):
            print("Cartao[", i, "]: ", self.tabelaCartao[i])

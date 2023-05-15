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
    def taxaOcupacaoCartao(self):
        num_elementos = len(
            list(filter(lambda x: x is not None, self.tabelaCartao)))
        taxa = round((num_elementos/self.tamMaxCart)*100, 2)
        return taxa, num_elementos

    def exibirCartoes(self):
        for i in range(0, self.tamMaxCart):
            print("Cartao[", i, "]: ", self.tabelaCartao[i])

    def hashCartao(self, numCartao):
        return numCartao % self.tamMaxCart

    def hash2Cartao(self, nomeTitular, codigoSeguranca):
        valor = sum(ord(char) for char in nomeTitular)
        hash2 = 1 + (valor % (self.tamMaxCart-1))
        return (hash2+codigoSeguranca) % self.tamMaxCart

    def hashCompletoCartao(self, cartao):
        pos = self.hashCartao(cartao.numeroCartao)
        if (self.tabelaCartao[pos] is None):
            self.tabelaCartao[pos] = cartao
        else:
            pos2 = self.hash2Cartao(
                cartao.nomeTitular, cartao.codSeguranca) + pos
            if pos2 >= self.tamMaxCart:
                pos2 -= self.tamMaxCart
            while (self.tabelaCartao[pos2] is not None):
                pos2 = (pos2+1) % (self.tamMaxCart)
            self.tabelaCartao[pos2] = cartao

    def ajustarTabela(self, taxa):
        if (taxa >= 70):
            self.tamMaxCart *= 2
            aux = self.tabelaCartao
            self.tabelaCartao = [None] * self.tamMaxCart
            for key in aux:
                if key is not None:
                    hash_value = self.hashCompletoCartao(
                        key)
                    if hash_value is not None:  # Verificação adicional para evitar índices nulos
                        while self.tabelaCartao[hash_value] is not None:
                            hash_value = (
                                hash_value + 1) % self.tamMaxCart
                        self.tabelaCartao[hash_value] = key
                    else:
                        print("Error de cálculo do valor de hash")

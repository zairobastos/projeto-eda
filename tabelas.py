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

    def exibirUsuario(self):
        for i in range(0, self.tamMaxUser):
            print("Usuario[", i, "]: ", self.tabelaUsuario[i])

    def hashUsuario(self, cpf):
        return cpf % self.tamMaxUser

    def hash2Usuario(self, cpf):
        return (1 + (cpf % (self.tamMaxUser-1))) % self.tamMaxUser

    def hashCompletoUsuario(self, usuario):
        i = self.hashUsuario(usuario.cpf)
        if (self.tabelaUsuario[i] is None):
            self.tabelaUsuario[i] = usuario
            return True
        else:
            if self.tabelaUsuario[i].cpf == usuario.cpf:
                return False
            w = self.hash2Usuario(usuario.cpf)
            rh = (i+w) % self.tamMaxCart
            while (self.tabelaUsuario[rh] is not None):
                rh = (rh+w) % (self.tamMaxCart)
                if self.tabelaUsuario[rh].cpf == usuario.cpf:
                    return False
            self.tabelaUsuario[rh] = usuario
            return True

    def ajustarTabelaUsuario(self, taxa):
        if (taxa >= 60):
            self.tamMaxUser *= 2
            aux = self.tabelaUsuario
            self.tabelaUsuario = [None] * self.tamMaxUser
            for key in aux:
                if key is not None:
                    self.hashCompletoCartao(key)

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

    def hash2Cartao(self, numCartao):
        return (1 + (numCartao % (self.tamMaxCart-1))) % self.tamMaxCart

    def hashCompletoCartao(self, cartao):
        i = self.hashCartao(cartao.numeroCartao)
        if (self.tabelaCartao[i] is None):
            self.tabelaCartao[i] = cartao
            return True
        else:
            if self.tabelaCartao[i].numeroCartao == cartao.numeroCartao:
                return False
            w = self.hash2Cartao(cartao.numeroCartao)
            rh = (i+w) % self.tamMaxCart
            while (self.tabelaCartao[rh] is not None):
                rh = (rh+w) % (self.tamMaxCart)
                if self.tabelaCartao[rh].numeroCartao == cartao.numeroCartao:
                    return False
            self.tabelaCartao[rh] = cartao
            return True

    def ajustarTabela(self, taxa):
        if (taxa >= 60):
            self.tamMaxCart *= 2
            aux = self.tabelaCartao
            self.tabelaCartao = [None] * self.tamMaxCart
            for key in aux:
                if key is not None:
                    self.hashCompletoCartao(key)

    def buscarCartao(self, numCartao):
        i = self.hashCartao(numCartao)
        taxa, numEl = self.taxaOcupacaoCartao()
        if (self.tabelaCartao[i] is None):
            return False
        else:
            if (self.tabelaCartao[i].numeroCartao == numCartao):
                return True
            else:
                w = self.hash2Cartao(numCartao)
                rh = (i+w) % self.tamMaxCart
                numEl -= 1
                while numEl > 0:
                    if (self.tabelaCartao[i] is None):
                        return False
                    elif (self.tabelaCartao[rh].numeroCartao == numCartao):
                        return True
                    rh = (rh+w) % self.tamMaxCart
                    numEl -= 1
                return False

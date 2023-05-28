from menus import Menu
from arvoreAVL import ArvoreAVL


class Tabela:
    menu = Menu()
    avl = ArvoreAVL()

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
                if self.tabelaUsuario[rh].cpf == usuario.cpf:
                    return False
                rh = (rh+w) % (self.tamMaxCart)
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

    def buscaCPF(self, cpf):
        i = self.hashUsuario(cpf)
        taxa, numEl = self.taxaOcupacaoUsuario()
        if (self.tabelaUsuario[i] is None):
            return False
        else:
            if (self.tabelaUsuario[i].cpf == cpf):
                return i
            else:
                w = self.hash2Cartao(cpf)
                rh = (i+w) % self.tamMaxCart
                numEl -= 1
                while numEl > 0:
                    if (self.tabelaUsuario[i] is None):
                        return False
                    elif (self.tabelaUsuario[rh].cpf == cpf):
                        return rh
                    rh = (rh+w) % self.tamMaxCart
                    numEl -= 1
                return False

    def dadosUsuario(self):
        taxa, num_el = self.taxaOcupacaoUsuario()
        if num_el > 0:
            cpf = self.menu.formListaUsuario()
            existe_cpf = self.buscaCPF(cpf)
            if existe_cpf != False:
                print(
                    "Nome: ", self.tabelaUsuario[existe_cpf].nome)
                print(
                    "CPF: ", self.tabelaUsuario[existe_cpf].cpf)
                print(
                    "Endereço: ", self.tabelaUsuario[existe_cpf].endereco)
            else:
                print("CPF não encontrado na base de dados!")
        else:
            print("Nenhum usuário cadastrado")

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
            return i
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
            return rh

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
                return i
            else:
                w = self.hash2Cartao(numCartao)
                rh = (i+w) % self.tamMaxCart
                numEl -= 1
                while numEl > 0:
                    if (self.tabelaCartao[i] is None):
                        return False
                    elif (self.tabelaCartao[rh].numeroCartao == numCartao):
                        return rh
                    rh = (rh+w) % self.tamMaxCart
                    numEl -= 1
                return False

    def dadosCartao(self):
        taxa, num_el = self.taxaOcupacaoCartao()
        if num_el > 0:
            numCartao = self.menu.formListaCartao()
            existe_cartao = self.buscarCartao(numCartao)
            if existe_cartao != False:
                print(
                    "Nome: ", self.tabelaCartao[existe_cartao].nomeTitular)
                print(
                    "Número do cartão: ", self.tabelaCartao[existe_cartao].numeroCartao)
                print(
                    "Data de validade: ", self.tabelaCartao[existe_cartao].dataValidade)
                print(
                    "Bandeira: ", self.tabelaCartao[existe_cartao].bandeira)
                print(
                    "Código de Segurança: ", self.tabelaCartao[existe_cartao].codSeguranca)
            else:
                print("Número do cartão não encontrado na base de dados!")
        else:
            print("Nenhum cartão cadastrado")

    def comprasCartao(self):
        taxa, num_el = self.taxaOcupacaoCartao()
        if num_el > 0:
            numeroCartao = int(input("Digite o número do cartão: "))
            cartao = self.buscarCartao(numeroCartao)
            if cartao != False:
                self.avl.exibirArvoreCompras(
                    self.tabelaCartao[cartao])
            else:
                print("Cartão não encontrado")
        else:
            print("Nenhum cartão cadastrado")

from noAVL import NoAVL


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def cadastrarCompra(self, cartao, compra):
        if cartao.comprasAVL is None:
            cartao.comprasAVL = NoAVL(compra)
        else:
            cartao.comprasAVL = self.inserirCompra(cartao.comprasAVL, compra)

    def inserirCompra(self, no, compra):
        if no is None:
            return NoAVL(compra)
        if compra.idcompra < no.compra.idcompra:
            no.esquerda = self.inserirCompra(no.esquerda, compra)
        else:
            no.direita = self.inserirCompra(no.direita, compra)
        no.altura = 1 + max(self.getAltura(no.esquerda),
                            self.getAltura(no.direita))
        balanceamento = self.getBalanceamento(no)
        if balanceamento > 1:
            if compra.idcompra < no.esquerda.compra.idcompra:
                return self.rotacaoDireita(no)
            else:
                no.esquerda = self.rotacaoEsquerda(no.esquerda)
                return self.rotacaoDireita(no)
        if balanceamento < -1:
            if compra.idcompra > no.direita.compra.idcompra:
                return self.rotacaoEsquerda(no)
            else:
                no.direita = self.rotacaoDireita(no.direita)
                return self.rotacaoEsquerda(no)
        return no

    def getAltura(self, no):
        if no is None:
            return 0
        return no.altura

    def getBalanceamento(self, no):
        if no is None:
            return 0
        return self.getAltura(no.esquerda) - self.getAltura(no.direita)

    def rotacaoEsquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

    def rotacaoDireita(self, y):
        x = y.esquerda
        T2 = x.direita
        x.direita = y
        y.esquerda = T2
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        x.altura = 1 + max(self.getAltura(x.esquerda),
                           self.getAltura(x.direita))
        return x

    def exibirArvoreCompras(self, cartao):
        if cartao.comprasAVL is None:
            print("Nenhuma compra registrada para este cartão.")
        else:
            print("Compras registradas para o cartão:", cartao.numeroCartao)
            self.buscaRecursiva(cartao.comprasAVL)

    def buscaRecursiva(self, no):
        if no is not None:
            self.buscaRecursiva(no.esquerda)
            compra = no.compra
            print("ID da compra:", compra.idcompra)
            print("Itens:", compra.itens)
            print("Valor: R$", compra.valorCompra)
            print("Data da compra:", compra.dataCompra)
            print("--------------------")
            self.buscaRecursiva(no.direita)

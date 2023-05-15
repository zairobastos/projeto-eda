from cartao import Cartao
from compra import Compra
from usuario import Usuario
from menus import Menu
from tabelas import Tabela
import os


class Main():

    menu = Menu()
    tabelas = Tabela(tamCartao=3, tamUsuario=31)

    def opcao(self):
        repete = True
        while repete:
            opc = self.menu.menu()
            if (opc > 0 & opc < 7):
                if (opc == 1):
                    os.system("clear") or None
                    print("Opção selecionada: 1. Cadastrar Cartão\n")
                    nomeTitular, numeroCartao, dataValidade, bandeiraCartao, codigoSeguranca = self.menu.formCartao()
                    cartao = Cartao(numeroCartao, nomeTitular,
                                    dataValidade, bandeiraCartao, codigoSeguranca)
                    self.tabelas.hashCompletoCartao(cartao)
                    taxa, num_el = self.tabelas.taxaOcupacaoCartao()
                    if (taxa >= 70):
                        self.tabelas.tamMaxCart *= 2
                        aux = self.tabelas.tabelaCartao
                        self.tabelas.tabelaCartao = [
                            None] * self.tabelas.tamMaxCart
                        c = 0
                        for key in aux:
                            if key is not None:
                                hash_value = self.tabelas.hashCompletoCartao(
                                    key)
                                if hash_value is not None:  # Verificação adicional para evitar índices nulos
                                    while self.tabelas.tabelaCartao[hash_value] is not None:
                                        hash_value = (
                                            hash_value + 1) % self.tabelas.tamMaxCart
                                    self.tabelas.tabelaCartao[hash_value] = key
                            if (c >= (int(self.tabelas.tamMaxCart/2))):
                                break
                            c += 1

                elif (opc == 2):
                    os.system("clear") or None
                    print("Opção selecionada: 2. Cadastrar Usuário\n")
                    nome, cpf, endereco, cartaoUser = self.menu.formUsuario()
                elif (opc == 3):
                    os.system("clear") or None
                    print("Opção selecionada: 3. Cadastrar Compra\n")
                    itens, valor, cpf = self.menu.formCompra()
                elif (opc == 4):
                    os.system("clear") or None
                    print("Opção selecionada: 4. Listar Cartões\n")
                    self.tabelas.exibirCartoes()
            if (opc > 7 or opc < 0):
                print('aqui')
                os.system("clear") or None
                print("ERROR: OPÇÃO DIGITADA INVÁLIDA!\n")
                repete = True
            if (opc == 0):
                print("Fim da execução.")
                repete = False


main = Main()
main.opcao()

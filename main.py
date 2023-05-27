from cartao import Cartao
from compra import Compra
from usuario import Usuario
from menus import Menu
from tabelas import Tabela
import os


class Main():

    menu = Menu()
    tabelas = Tabela(tamCartao=31, tamUsuario=31)

    def cadCartao(self):
        print("Opção selecionada: 1. Cadastrar Cartão\n")
        nomeTitular, numeroCartao, dataValidade, bandeiraCartao, codigoSeguranca = self.menu.formCartao()
        cartao = Cartao(numeroCartao, nomeTitular,
                        dataValidade, bandeiraCartao, codigoSeguranca)
        cadastro = self.tabelas.hashCompletoCartao(cartao)
        if cadastro:
            print("Cartão cadastro com sucesso!")
            taxa, num_el = self.tabelas.taxaOcupacaoCartao()
            self.tabelas.ajustarTabela(taxa)
            return numeroCartao
        print("Cartão de crédito já cadastrado")
        return False

    def validaCadUser(self, nome, cpf, endereco, cartaoUser):
        usuario = Usuario(nome, cpf, endereco, cartaoUser)
        cadastro = self.tabelas.hashCompletoUsuario(usuario)
        if cadastro:
            print("Cadastro realizado com sucesso!")
            taxa, num_el = self.tabelas.taxaOcupacaoUsuario()
            self.tabelas.ajustarTabelaUsuario(taxa)
        else:
            print("Usuário já cadastrado!")

    def opcao(self):
        repete = True
        while repete:
            opc = self.menu.menu()
            if (opc > 0 & opc < 7):
                taxaCart, num_el_cart = self.tabelas.taxaOcupacaoCartao()
                if (opc == 1):
                    os.system("clear") or None
                    self.cadCartao()
                elif (opc == 2):
                    os.system("clear") or None
                    print("Opção selecionada: 2. Cadastrar Usuário\n")
                    lista_cartoes = []
                    taxa, num_el = self.tabelas.taxaOcupacaoCartao()
                    if num_el > 0:
                        nome, cpf, endereco, cartaoUser = self.menu.formUsuario()
                    else:
                        nome, cpf, endereco = self.menu.formUsuario2()
                        cartaoUser = self.cadCartao()
                    existe_cartao = self.tabelas.buscarCartao(cartaoUser)
                    if existe_cartao:
                        lista_cartoes.append(cartaoUser)
                        opicao = self.menu.novoCartao()
                        while opicao == 1:
                            cartaoUser = int(input("Número do cartão: "))
                            existe_cartao = self.tabelas.buscarCartao(
                                cartaoUser)
                            if existe_cartao:
                                if cartaoUser in lista_cartoes:
                                    print(
                                        "O cartão informado, já se encontra na sua lista de cartões")
                                else:
                                    lista_cartoes.append(cartaoUser)
                            else:
                                cartaoUser = self.cadCartao()
                                if cartaoUser != False:
                                    lista_cartoes.append(cartaoUser)
                            opicao = self.menu.novoCartao()
                        self.validaCadUser(nome, cpf, endereco, lista_cartoes)
                    else:
                        opicao = 1
                        while opicao == 1:
                            cartaoUser = self.cadCartao()
                            if cartaoUser != False:
                                lista_cartoes.append(cartaoUser)
                            opicao = self.menu.novoCartao()
                        self.validaCadUser(nome, cpf, endereco, lista_cartoes)

                elif (opc == 3):
                    os.system("clear") or None
                    print("Opção selecionada: 3. Cadastrar Compra\n")
                    itens, valor, cpf = self.menu.formCompra()
                elif (opc == 4):
                    os.system("clear") or None
                    print("Opção selecionada: 4. Listar Cartões\n")
                    self.tabelas.exibirCartoes()
                elif (opc == 5):
                    os.system("clear") or None
                    print("Opção selecionada: 5. Listar Usuário\n")
                    self.tabelas.exibirUsuario()
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

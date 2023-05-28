from cartao import Cartao
from compra import Compra
from usuario import Usuario
from menus import Menu
from tabelas import Tabela
from arvoreAVL import ArvoreAVL
import os


class Main():

    menu = Menu()
    tabelas = Tabela(tamCartao=31, tamUsuario=31)
    ArvoreAVL = ArvoreAVL()

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
            return cartao, cadastro
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

    def existeCartao(self, existe, nome, cpf, endereco, cartaoUser):
        lista_cartoes = []
        if existe != False:
            lista_cartoes.append(cartaoUser)
            opicao = self.menu.novoCartao()
            while opicao == 1:
                cartaoUser = int(input("Número do cartão: "))
                existe_cartao = self.tabelas.buscarCartao(
                    cartaoUser)
                if existe_cartao != False:
                    if cartaoUser in lista_cartoes:
                        print(
                            "O cartão informado, já se encontra na sua lista de cartões")
                    else:
                        lista_cartoes.append(
                            self.tabelas.tabelaCartao[cartaoUser])
                else:
                    cartaoUser, posCard = self.cadCartao()
                    if cartaoUser != False:
                        lista_cartoes.append(cartaoUser)
                opicao = self.menu.novoCartao()
            self.validaCadUser(nome, cpf, endereco, lista_cartoes)
        else:
            opicao = 1
            while opicao == 1:
                cartaoUser, posCard = self.cadCartao()
                if cartaoUser != False:
                    lista_cartoes.append(cartaoUser)
                opicao = self.menu.novoCartao()
            self.validaCadUser(nome, cpf, endereco, lista_cartoes)
        return cpf

    def cadUser(self):
        print("Opção selecionada: 2. Cadastrar Usuário\n")
        taxa, num_el = self.tabelas.taxaOcupacaoCartao()
        if num_el > 0:
            nome, cpf, endereco, cartaoUser = self.menu.formUsuario()
            existe_cartao = self.tabelas.buscarCartao(cartaoUser)
        else:
            nome, cpf, endereco = self.menu.formUsuario2()
            cartaoUser, posCard = self.cadCartao()
            existe_cartao = self.tabelas.buscarCartao(cartaoUser.numeroCartao)
        cpf2 = self.existeCartao(
            existe_cartao, nome, cpf, endereco, cartaoUser)
        return cpf2

    def escolhaCartao(self, existe_cpf):
        continua = True
        while continua:
            for i, item in enumerate(self.tabelas.tabelaUsuario[existe_cpf].numCartao):
                print(i, "- Cartão: ", item)
            opcao = int(input("Opção: "))
            if (opcao < 0 or opcao > len(self.tabelas.tabelaUsuario[existe_cpf].numCartao)):
                continua = True
            else:
                continua = False
        return opcao

    def existeUser(self, cpf):
        existe_cpf = self.tabelas.buscaCPF(cpf)
        if existe_cpf != False:
            print("Gostaria de pagar por qual cartão?")
            opcao = self.escolhaCartao(existe_cpf)
            print("Compra efetuada com sucesso!")
            return opcao, existe_cpf
        else:
            print("CPF não consta na base de dados!")
            return False

    def opcao(self):
        repete = True
        id_compra = 0
        while repete:
            opc = self.menu.menu()
            if (opc > 0 & opc < 9):
                taxaCart, num_el_cart = self.tabelas.taxaOcupacaoCartao()
                if (opc == 1):
                    os.system("clear") or None
                    self.cadCartao()
                elif (opc == 2):
                    os.system("clear") or None
                    self.cadUser()
                elif (opc == 3):
                    os.system("clear") or None
                    print("Opção selecionada: 3. Cadastrar Compra\n")
                    taxa, num_el = self.tabelas.taxaOcupacaoUsuario()
                    if num_el > 0:
                        itens, valor, cpf = self.menu.formCompra()
                        cartao_pos, cpf_pos = self.existeUser(cpf)
                        if cartao_pos == False:
                            print("Cadastre um usuário, antes de efetuar a compra")
                    else:
                        itens, valor = self.menu.formCompra2()
                        cpf = self.cadUser()
                        cartao_pos, cpf_pos = self.existeUser(cpf)
                    compra = Compra(itens, valor, cpf, id_compra)
                    id_compra += 1
                    if cartao_pos is not False:
                        cartao = self.tabelas.tabelaUsuario[cpf_pos].numCartao[cartao_pos]
                        self.ArvoreAVL.cadastrarCompra(cartao, compra)
                elif (opc == 4):
                    os.system("clear") or None
                    print("Opção selecionada: 4. Listar Cartões\n")
                    self.tabelas.exibirCartoes()
                elif (opc == 5):
                    os.system("clear") or None
                    print("Opção selecionada: 5. Listar Usuário\n")
                    self.tabelas.exibirUsuario()
                elif (opc == 6):
                    os.system("clear") or None
                    print("Opção selecionada: 6. Exibir dados do Usuário\n")
                    self.tabelas.dadosUsuario()
                elif (opc == 7):
                    print('Opção selecionada: 7. Exibir dados do Cartão')
                    self.tabelas.dadosCartao()
                elif (opc == 8):
                    print("Opção selecionada: 8. Exibir compras de um cartão")
                    self.tabelas.comprasCartao()

            if (opc > 9 or opc < 0):
                os.system("clear") or None
                print("ERROR: OPÇÃO DIGITADA INVÁLIDA!\n")
                repete = True
            if (opc == 0):
                print("Fim da execução.")
                repete = False


main = Main()
main.opcao()

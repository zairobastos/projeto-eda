class Menu():
    def formCartao(self):
        print("============================")
        print("     Cadastro de cartão     ")
        print("============================\n")
        nomeTit = input("Nome do titular: ")
        numeCar = int(input("Número do cartão: "))
        dataVal = input("Data de validade: ")
        bandCar = input("Bandeira do cartão: ")
        codiSeg = int(input("Código de segurança: "))
        return nomeTit, numeCar, dataVal, bandCar, codiSeg

    def formUsuario(self):
        print("=============================")
        print("     Cadastro de usuário     ")
        print("=============================\n")
        nomeUsu = input("Nome do Usuário: ")
        cpfUsua = int(input("CPF: "))
        endeUsu = input("Endereço do Usuário: ")
        cartUsu = int(input("Número do Cartão: "))
        return nomeUsu, cpfUsua, endeUsu, cartUsu

    def formUsuario2(self):
        print("=============================")
        print("     Cadastro de usuário     ")
        print("=============================\n")
        nomeUsu = input("Nome do Usuário: ")
        cpfUsua = int(input("CPF: "))
        endeUsu = input("Endereço do Usuário: ")
        return nomeUsu, cpfUsua, endeUsu

    def formListaUsuario(self):
        print("====================================")
        print("     Listar dados de um usuário     ")
        print("====================================\n")
        cpf = int(input("CPF: "))
        return cpf

    def formListaCartao(self):
        print("===================================")
        print("     Listar dados de um cartão     ")
        print("===================================\n")
        num = int(input("Número do Cartão: "))
        return num

    def formCompra(self):
        print("============================")
        print("     Cadastro de compra     ")
        print("============================\n")
        itemComp = input("Itens comprados: ")
        valoComp = float(input("Valor da compra: "))
        usuaComp = int(input("CPF: "))
        return itemComp, valoComp, usuaComp

    def formCompra2(self):
        print("============================")
        print("     Cadastro de compra     ")
        print("============================\n")
        itemComp = input("Itens comprados: ")
        valoComp = float(input("Valor da compra: "))
        return itemComp, valoComp

    def menu(self):
        print("======================================")
        print("MENU - Selecione uma das opções abaixo")
        print("======================================\n")
        print("0. SAIR")
        print("1. Cadastrar Cartão")
        print("2. Cadastrar Usuário")
        print("3. Cadastrar Compra")
        print("4. Listar Cartões")
        print("5. Listar Usuários")
        print("6. Exibir dados de um usuário")
        print("7. Exibir dados do Cartão")
        print("8. Exibir compras de um cartão")
        opc = int(input("Digite a opção: "))
        return opc

    def novoCartao(self):
        print("Deseja adicionar outro cartão?")
        print("1. sim")
        print("2. Não")
        ad_cart = int(input("Opção: "))
        return ad_cart

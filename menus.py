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

    def formCompra(self):
        print("============================")
        print("     Cadastro de compra     ")
        print("============================\n")
        itemComp = input("Itens comprados: ")
        valoComp = float(input("Valor da compra: "))
        usuaComp = int(input("CPF: "))
        return itemComp, valoComp, usuaComp

    def menu(self):
        print("======================================")
        print("MENU - Selecione uma das opções abaixo")
        print("======================================\n")
        print("0. SAIR")
        print("1. Cadastrar Cartão")
        print("2. Cadastrar Usuário")
        print("3. Cadastrar Compra")
        print("4. Listar Cartões")
        opc = int(input("Digite a opção: "))
        return opc

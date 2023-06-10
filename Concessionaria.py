import csv
from datetime import date

class Motocicleta:
    def __init__(self, id, marca, modelo, preco):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

class Cliente:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Venda:
    def __init__(self, id, id_motocicleta, id_cliente, data):
        self.id = id
        self.id_motocicleta = id_motocicleta
        self.id_cliente = id_cliente
        self.data = data

class Concessionaria:
    def __init__(self):
        self.motocicletas = []
        self.clientes = []
        self.vendas = []
        self.next_id_motocicleta = 1
        self.next_id_cliente = 1
        self.next_id_venda = 1

    def adicionar_motocicleta(self, marca, modelo, preco):
        motocicleta = Motocicleta(self.next_id_motocicleta, marca, modelo, preco)
        self.motocicletas.append(motocicleta)
        self.next_id_motocicleta += 1
        print("Motocicleta adicionada com sucesso.")

    def listar_motocicletas(self):
        if self.motocicletas:
            for motocicleta in self.motocicletas:
                print(f"ID: {motocicleta.id} | Marca: {motocicleta.marca} | Modelo: {motocicleta.modelo} | Preço: R${motocicleta.preco:.2f}")
        else:
            print("Nenhuma motocicleta cadastrada.")

    def obter_motocicleta_por_id(self, id):
        for motocicleta in self.motocicletas:
            if motocicleta.id == id:
                return motocicleta
        return None

    def excluir_motocicleta(self, id):
        motocicleta = self.obter_motocicleta_por_id(id)
        if motocicleta:
            self.motocicletas.remove(motocicleta)
            print("Motocicleta excluída com sucesso.")
        else:
            print("Motocicleta não encontrada.")

    def atualizar_motocicleta(self, id, marca, modelo, preco):
        motocicleta = self.obter_motocicleta_por_id(id)
        if motocicleta:
            motocicleta.marca = marca
            motocicleta.modelo = modelo
            motocicleta.preco = preco
            print("Motocicleta atualizada com sucesso.")
        else:
            print("Motocicleta não encontrada.")

    def adicionar_cliente(self, nome, email, telefone):
        cliente = Cliente(self.next_id_cliente, nome, email, telefone)
        self.clientes.append(cliente)
        self.next_id_cliente += 1
        print("Cliente adicionado com sucesso.")

    def listar_clientes(self):
        if self.clientes:
            for cliente in self.clientes:
                print(f"ID: {cliente.id} | Nome: {cliente.nome} | Email: {cliente.email} | Telefone: {cliente.telefone}")
        else:
            print("Nenhum cliente cadastrado.")

    def obter_cliente_por_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def excluir_cliente(self, id):
        cliente = self.obter_cliente_por_id(id)
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente excluído com sucesso.")
        else:
            print("Cliente não encontrado.")

    def atualizar_cliente(self, id, nome, email, telefone):
        cliente = self.obter_cliente_por_id(id)
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.telefone = telefone
            print("Cliente atualizado com sucesso.")
        else:
            print("Cliente não encontrado.")

    def adicionar_venda(self, id_motocicleta, id_cliente):
        motocicleta = self.obter_motocicleta_por_id(id_motocicleta)
        cliente = self.obter_cliente_por_id(id_cliente)
        if motocicleta and cliente:
            for venda in self.vendas:
                if venda.id_motocicleta == id_motocicleta:
                    print("Essa motocicleta já foi vendida.")
                    return
            data_atual = date.today()
            venda = Venda(self.next_id_venda, id_motocicleta, id_cliente, data_atual)
            self.vendas.append(venda)
            self.next_id_venda += 1
            print("Venda registrada com sucesso.")
        else:
            print("Motocicleta ou cliente não encontrados.")

    def listar_vendas(self):
        if self.vendas:
            for venda in self.vendas:
                motocicleta = self.obter_motocicleta_por_id(venda.id_motocicleta)
                cliente = self.obter_cliente_por_id(venda.id_cliente)
                print(f"ID: {venda.id} | Motocicleta: {motocicleta.marca} {motocicleta.modelo} | Cliente: {cliente.nome} | Data: {venda.data}")
        else:
            print("Nenhuma venda registrada.")

    def consultar_venda_por_id(self, id):
        for venda in self.vendas:
            if venda.id == id:
                motocicleta = self.obter_motocicleta_por_id(venda.id_motocicleta)
                cliente = self.obter_cliente_por_id(venda.id_cliente)
                print(f"ID: {venda.id} | Motocicleta: {motocicleta.marca} {motocicleta.modelo} | Cliente: {cliente.nome} | Data: {venda.data}")
                return
        print("Venda não encontrada.")

    def exportar_dados(self, opcao):
        if opcao.lower() == "motocicletas":
            filename = f"Motocicletas_{date.today()}.csv"
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Marca", "Modelo", "Preço"])
                for motocicleta in self.motocicletas:
                    writer.writerow([motocicleta.id, motocicleta.marca, motocicleta.modelo, motocicleta.preco])
            print(f"Dados de motocicletas exportados para o arquivo {filename}.")
        elif opcao.lower() == "clientes":
            filename = f"Clientes_{date.today()}.csv"
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nome", "Email", "Telefone"])
                for cliente in self.clientes:
                    writer.writerow([cliente.id, cliente.nome, cliente.email, cliente.telefone])
            print(f"Dados de clientes exportados para o arquivo {filename}.")
        elif opcao.lower() == "vendas":
            filename = f"Vendas_{date.today()}.csv"
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "ID Motocicleta", "ID Cliente", "Data"])
                for venda in self.vendas:
                    writer.writerow([venda.id, venda.id_motocicleta, venda.id_cliente, venda.data])
            print(f"Dados de vendas exportados para o arquivo {filename}.")
        else:
            print("Opção inválida.")

def main():
    concessionaria = Concessionaria()

    while True:
        print("\n=== MENU ===")
        print("1. Motocicletas")
        print("2. Clientes")
        print("3. Vendas")
        print("4. Exportação")
        print("0. Sair")

        opcao_menu = input("Selecione uma opção: ")

        if opcao_menu == "1":
            print("\n=== MENU MOTOCICLETAS ===")
            print("1. Adicionar motocicleta")
            print("2. Listar motocicletas")
            print("3. Excluir motocicleta")
            print("4. Atualizar motocicleta")
            print("0. Voltar")

            opcao_motocicletas = input("Selecione uma opção: ")

            if opcao_motocicletas == "1":
                marca = input("Digite a marca: ")
                modelo = input("Digite o modelo: ")
                preco = float(input("Digite o preço: "))
                concessionaria.adicionar_motocicleta(marca, modelo, preco)
            elif opcao_motocicletas == "2":
                concessionaria.listar_motocicletas()
            elif opcao_motocicletas == "3":
                id = int(input("Digite o ID da motocicleta: "))
                concessionaria.excluir_motocicleta(id)
            elif opcao_motocicletas == "4":
                id = int(input("Digite o ID da motocicleta: "))
                marca = input("Digite a marca: ")
                modelo = input("Digite o modelo: ")
                preco = float(input("Digite o preço: "))
                concessionaria.atualizar_motocicleta(id, marca, modelo, preco)
            elif opcao_motocicletas == "0":
                continue
            else:
                print("Opção inválida.")

        elif opcao_menu == "2":
            print("\n=== MENU CLIENTES ===")
            print("1. Adicionar cliente")
            print("2. Listar clientes")
            print("3. Excluir cliente")
            print("4. Atualizar cliente")
            print("0. Voltar")

            opcao_clientes = input("Selecione uma opção: ")

            if opcao_clientes == "1":
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                telefone = input("Digite o telefone: ")
                concessionaria.adicionar_cliente(nome, email, telefone)
            elif opcao_clientes == "2":
                concessionaria.listar_clientes()
            elif opcao_clientes == "3":
                id = int(input("Digite o ID do cliente: "))
                concessionaria.excluir_cliente(id)
            elif opcao_clientes == "4":
                id = int(input("Digite o ID do cliente: "))
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                telefone = input("Digite o telefone: ")
                concessionaria.atualizar_cliente(id, nome, email, telefone)
            elif opcao_clientes == "0":
                continue
            else:
                print("Opção inválida.")

        elif opcao_menu == "3":
            print("\n=== MENU VENDAS ===")
            print("1. Adicionar venda")
            print("2. Listar vendas")
            print("3. Consultar venda por ID")
            print("0. Voltar")

            opcao_vendas = input("Selecione uma opção: ")

            if opcao_vendas == "1":
                id_motocicleta = int(input("Digite o ID da motocicleta: "))
                id_cliente = int(input("Digite o ID do cliente: "))
                concessionaria.adicionar_venda(id_motocicleta, id_cliente)
            elif opcao_vendas == "2":
                concessionaria.listar_vendas()
            elif opcao_vendas == "3":
                id = int(input("Digite o ID da venda: "))
                concessionaria.consultar_venda_por_id(id)
            elif opcao_vendas == "0":
                continue
            else:
                print("Opção inválida.")

        elif opcao_menu == "4":
            print("\n=== MENU EXPORTAÇÃO ===")
            print("1. Exportar motocicletas")
            print("2. Exportar clientes")
            print("3. Exportar vendas")
            print("0. Voltar")

            opcao_exportacao = input("Selecione uma opção: ")

            if opcao_exportacao == "1":
                concessionaria.exportar_dados("motocicletas")
            elif opcao_exportacao == "2":
                concessionaria.exportar_dados("clientes")
            elif opcao_exportacao == "3":
                concessionaria.exportar_dados("vendas")
            elif opcao_exportacao == "0":
                continue
            else:
                print("Opção inválida.")

        elif opcao_menu == "0":
            break

        else:
            print("Opção inválida.")


main()

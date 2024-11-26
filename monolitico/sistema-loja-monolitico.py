#Guilherme Schulz RA10401501
import os
from datetime import datetime
from typing import List, Dict

class SistemaLoja:
    def __init__(self):
        self.produtos: Dict[int, dict] = {}
        self.vendas: List[dict] = []
        self.id_atual = 1
        
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def adicionar_produto(self, nome: str, preco: float, quantidade: int) -> None:
        """Adiciona um novo produto ao estoque"""
        self.produtos[self.id_atual] = {
            'id': self.id_atual,
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        self.id_atual += 1
        print(f"\nProduto {nome} adicionado com sucesso!")
        
    def atualizar_estoque(self, id_produto: int, quantidade: int) -> None:
        """Atualiza a quantidade em estoque de um produto"""
        if id_produto in self.produtos:
            self.produtos[id_produto]['quantidade'] += quantidade
            print(f"\nEstoque atualizado! Nova quantidade: {self.produtos[id_produto]['quantidade']}")
        else:
            print("\nProduto não encontrado!")
            
    def realizar_venda(self, id_produto: int, quantidade: int) -> None:
        """Registra uma venda e atualiza o estoque"""
        if id_produto not in self.produtos:
            print("\nProduto não encontrado!")
            return
            
        if self.produtos[id_produto]['quantidade'] < quantidade:
            print("\nQuantidade insuficiente em estoque!")
            return
            
        valor_total = self.produtos[id_produto]['preco'] * quantidade
        
        venda = {
            'data': datetime.now(),
            'produto_id': id_produto,
            'produto_nome': self.produtos[id_produto]['nome'],
            'quantidade': quantidade,
            'valor_total': valor_total
        }
        
        self.vendas.append(venda)
        self.produtos[id_produto]['quantidade'] -= quantidade
        
        print(f"\nVenda realizada com sucesso! Valor total: R$ {valor_total:.2f}")
        
    def listar_produtos(self) -> None:
        """Lista todos os produtos em estoque"""
        print("\n=== PRODUTOS EM ESTOQUE ===")
        for produto in self.produtos.values():
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print("-------------------------")
            
    def relatorio_vendas(self) -> None:
        """Gera um relatório de vendas"""
        if not self.vendas:
            print("\nNenhuma venda registrada!")
            return
            
        total_vendas = 0
        print("\n=== RELATÓRIO DE VENDAS ===")
        for venda in self.vendas:
            print(f"Data: {venda['data'].strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Produto: {venda['produto_nome']}")
            print(f"Quantidade: {venda['quantidade']}")
            print(f"Valor: R$ {venda['valor_total']:.2f}")
            print("-------------------------")
            total_vendas += venda['valor_total']
            
        print(f"\nTotal de vendas: R$ {total_vendas:.2f}")
        
    def menu_principal(self) -> None:
        """Exibe o menu principal do sistema"""
        while True:
            self.limpar_tela()
            print("\n=== SISTEMA DE LOJA ===")
            print("1. Adicionar Produto")
            print("2. Atualizar Estoque")
            print("3. Realizar Venda")
            print("4. Listar Produtos")
            print("5. Relatório de Vendas")
            print("6. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                nome = input("\nNome do produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade inicial: "))
                self.adicionar_produto(nome, preco, quantidade)
                
            elif opcao == "2":
                id_produto = int(input("\nID do produto: "))
                quantidade = int(input("Quantidade a adicionar: "))
                self.atualizar_estoque(id_produto, quantidade)
                
            elif opcao == "3":
                id_produto = int(input("\nID do produto: "))
                quantidade = int(input("Quantidade: "))
                self.realizar_venda(id_produto, quantidade)
                
            elif opcao == "4":
                self.listar_produtos()
                
            elif opcao == "5":
                self.relatorio_vendas()
                
            elif opcao == "6":
                print("\nSaindo do sistema...")
                break
                
            else:
                print("\nOpção inválida!")
                
            input("\nPressione Enter para continuar...")

# Iniciar o sistema
if __name__ == "__main__":
    sistema = SistemaLoja()
    sistema.menu_principal()

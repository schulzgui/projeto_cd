#Guilherme Schulz RA10401501
import os
from servidor_central import ServidorCentral

class InterfaceUsuario:
    def __init__(self):
        self.servidor = ServidorCentral()
        
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def menu_principal(self):
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
                resposta = self.servidor.adicionar_produto(nome, preco, quantidade)
                print(f"\n{resposta.dados['mensagem']}")
                
            elif opcao == "2":
                id_produto = int(input("\nID do produto: "))
                quantidade = int(input("Quantidade a adicionar: "))
                resposta = self.servidor.atualizar_estoque(id_produto, quantidade)
                print(f"\n{resposta.dados['mensagem']}")
                
            elif opcao == "3":
                id_produto = int(input("\nID do produto: "))
                quantidade = int(input("Quantidade: "))
                resposta = self.servidor.realizar_venda(id_produto, quantidade)
                print(f"\n{resposta.dados['mensagem']}")
                
            elif opcao == "4":
                resposta = self.servidor.listar_produtos()
                produtos = resposta.dados['produtos']
                print("\n=== PRODUTOS EM ESTOQUE ===")
                for produto in produtos.values():
                    print(f"ID: {produto['id']}")
                    print(f"Nome: {produto['nome']}")
                    print(f"Preço: R$ {produto['preco']:.2f}")
                    print(f"Quantidade: {produto['quantidade']}")
                    print("-------------------------")
                
            elif opcao == "5":
                resposta = self.servidor.relatorio_vendas()
                vendas = resposta.dados['vendas']
                total = resposta.dados['total']
                
                if not vendas:
                    print("\nNenhuma venda registrada!")
                else:
                    print("\n=== RELATÓRIO DE VENDAS ===")
                    for venda in vendas:
                        print(f"Data: {venda['data']}")
                        print(f"Produto: {venda['produto_nome']}")
                        print(f"Quantidade: {venda['quantidade']}")
                        print(f"Valor: R$ {venda['valor_total']:.2f}")
                        print("-------------------------")
                    print(f"\nTotal de vendas: R$ {total:.2f}")
                
            elif opcao == "6":
                print("\nSaindo do sistema...")
                break
                
            else:
                print("\nOpção inválida!")
                
            input("\nPressione Enter para continuar...")
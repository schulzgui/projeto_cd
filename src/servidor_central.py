#Guilherme Schulz RA10401501
import socket
from mensagens import Mensagem
from config import Config

class ServidorCentral:
    def __init__(self):
        self.config = Config()

    def enviar_mensagem(self, host: str, port: int, mensagem: Mensagem) -> Mensagem:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(mensagem.to_json().encode())
            resposta = s.recv(4096).decode()
            return Mensagem.from_json(resposta)

    def adicionar_produto(self, nome: str, preco: float, quantidade: int) -> Mensagem:
        mensagem = Mensagem('produtos', 'adicionar', {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        })
        return self.enviar_mensagem(self.config.PRODUTOS_HOST, self.config.PRODUTOS_PORT, mensagem)

    def atualizar_estoque(self, id_produto: int, quantidade: int) -> Mensagem:
        mensagem = Mensagem('produtos', 'atualizar', {
            'id': id_produto,
            'quantidade': quantidade
        })
        return self.enviar_mensagem(self.config.PRODUTOS_HOST, self.config.PRODUTOS_PORT, mensagem)

    def realizar_venda(self, id_produto: int, quantidade: int) -> Mensagem:
        # Primeiro, verifica o produto
        mensagem = Mensagem('produtos', 'get', {'id': id_produto})
        resposta = self.enviar_mensagem(
            self.config.PRODUTOS_HOST,
            self.config.PRODUTOS_PORT,
            mensagem
        )
        
        if resposta.acao == 'erro':
            return resposta
            
        produto = resposta.dados['produto']
        if produto['quantidade'] < quantidade:
            return Mensagem('vendas', 'erro', {'mensagem': 'Quantidade insuficiente'})
            
        # Atualiza o estoque
        self.atualizar_estoque(id_produto, -quantidade)
        
        # Registra a venda
        valor_total = produto['preco'] * quantidade
        mensagem = Mensagem('vendas', 'registrar', {
            'produto_id': id_produto,
            'produto_nome': produto['nome'],
            'quantidade': quantidade,
            'valor_total': valor_total
        })
        
        return self.enviar_mensagem(self.config.VENDAS_HOST, self.config.VENDAS_PORT, mensagem)

    def listar_produtos(self) -> Mensagem:
        mensagem = Mensagem('produtos', 'listar', {})
        return self.enviar_mensagem(self.config.PRODUTOS_HOST, self.config.PRODUTOS_PORT, mensagem)

    def relatorio_vendas(self) -> Mensagem:
        mensagem = Mensagem('vendas', 'relatorio', {})
        return self.enviar_mensagem(self.config.VENDAS_HOST, self.config.VENDAS_PORT, mensagem)

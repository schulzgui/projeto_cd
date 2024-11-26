#Guilherme Schulz RA10401501
import socket
import threading
from typing import Dict
from mensagens import Mensagem
from config import Config

class ProdutosService:
    def __init__(self):
        self.config = Config()
        self.produtos: Dict[int, dict] = {}
        self.id_atual = 1
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.config.PRODUTOS_HOST, self.config.PRODUTOS_PORT))

    def iniciar(self):
        self.socket.listen()
        print(f"Serviço de Produtos rodando em {self.config.PRODUTOS_HOST}:{self.config.PRODUTOS_PORT}")
        
        while True:
            conn, addr = self.socket.accept()
            thread = threading.Thread(target=self.handle_connection, args=(conn,))
            thread.start()

    def handle_connection(self, conn: socket.socket):
        try:
            data = conn.recv(4096).decode()
            mensagem = Mensagem.from_json(data)
            
            resposta = self.processar_mensagem(mensagem)
            conn.send(resposta.to_json().encode())
        finally:
            conn.close()

    def processar_mensagem(self, mensagem: Mensagem) -> Mensagem:
        if mensagem.acao == 'adicionar':
            return self.adicionar_produto(mensagem.dados)
        elif mensagem.acao == 'atualizar':
            return self.atualizar_estoque(mensagem.dados)
        elif mensagem.acao == 'listar':
            return self.listar_produtos()
        elif mensagem.acao == 'get':
            return self.get_produto(mensagem.dados)
        
        return Mensagem('produtos', 'erro', {'mensagem': 'Ação inválida'})

    def adicionar_produto(self, dados: dict) -> Mensagem:
        self.produtos[self.id_atual] = {
            'id': self.id_atual,
            'nome': dados['nome'],
            'preco': dados['preco'],
            'quantidade': dados['quantidade']
        }
        self.id_atual += 1
        return Mensagem('produtos', 'sucesso', {'mensagem': 'Produto adicionado'})

    def atualizar_estoque(self, dados: dict) -> Mensagem:
        id_produto = dados['id']
        quantidade = dados['quantidade']
        
        if id_produto not in self.produtos:
            return Mensagem('produtos', 'erro', {'mensagem': 'Produto não encontrado'})
            
        self.produtos[id_produto]['quantidade'] += quantidade
        return Mensagem('produtos', 'sucesso', {
            'mensagem': 'Estoque atualizado',
            'quantidade': self.produtos[id_produto]['quantidade']
        })

    def listar_produtos(self) -> Mensagem:
        return Mensagem('produtos', 'lista', {'produtos': self.produtos})

    def get_produto(self, dados: dict) -> Mensagem:
        id_produto = dados['id']
        if id_produto not in self.produtos:
            return Mensagem('produtos', 'erro', {'mensagem': 'Produto não encontrado'})
        return Mensagem('produtos', 'produto', {'produto': self.produtos[id_produto]})

if __name__ == "__main__":
    servico = ProdutosService()
    servico.iniciar()
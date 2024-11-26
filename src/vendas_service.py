#Guilherme Schulz RA10401501
import socket
import threading
from datetime import datetime
from typing import List
from mensagens import Mensagem
from config import Config

class VendasService:
    def __init__(self):
        self.config = Config()
        self.vendas: List[dict] = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.config.VENDAS_HOST, self.config.VENDAS_PORT))

    def iniciar(self):
        self.socket.listen()
        print(f"Serviço de Vendas rodando em {self.config.VENDAS_HOST}:{self.config.VENDAS_PORT}")
        
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
        if mensagem.acao == 'registrar':
            return self.registrar_venda(mensagem.dados)
        elif mensagem.acao == 'relatorio':
            return self.gerar_relatorio()
            
        return Mensagem('vendas', 'erro', {'mensagem': 'Ação inválida'})

    def registrar_venda(self, dados: dict) -> Mensagem:
        venda = {
            'data': datetime.now().isoformat(),
            'produto_id': dados['produto_id'],
            'produto_nome': dados['produto_nome'],
            'quantidade': dados['quantidade'],
            'valor_total': dados['valor_total']
        }
        self.vendas.append(venda)
        return Mensagem('vendas', 'sucesso', {'mensagem': 'Venda registrada'})

    def gerar_relatorio(self) -> Mensagem:
        total_vendas = sum(venda['valor_total'] for venda in self.vendas)
        return Mensagem('vendas', 'relatorio', {
            'vendas': self.vendas,
            'total': total_vendas
        })

if __name__ == "__main__":
    servico = VendasService()
    servico.iniciar()
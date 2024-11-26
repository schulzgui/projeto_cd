#Guilherme Schulz RA10401501
import threading
from produtos_service import ProdutosService
from vendas_service import VendasService
from interface_usuario import InterfaceUsuario

def iniciar_servico_produtos():
    servico = ProdutosService()
    servico.iniciar()

def iniciar_servico_vendas():
    servico = VendasService()
    servico.iniciar()

if __name__ == "__main__":
    # Inicia os serviços em threads separadas
    thread_produtos = threading.Thread(target=iniciar_servico_produtos)
    thread_vendas = threading.Thread(target=iniciar_servico_vendas)
    
    thread_produtos.start()
    thread_vendas.start()
    
    # Inicia a interface do usuário
    interface = InterfaceUsuario()
    interface.menu_principal()
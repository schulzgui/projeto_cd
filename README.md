# Sistema de Loja - Microsserviços

Este é um sistema de loja implementado com arquitetura de microsserviços usando sockets para comunicação.

## Requisitos

- Python 3.7+
- Dependências listadas em requirements.txt

## Instalação

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

1. Execute o arquivo principal a partir da pasta src:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

- `src/`: Código fonte do projeto
  - `config.py`: Configurações do sistema
  - `mensagens.py`: Definição do protocolo de mensagens
  - `produtos_service.py`: Serviço de produtos
  - `vendas_service.py`: Serviço de vendas
  - `servidor_central.py`: Servidor central
  - `interface_usuario.py`: Interface com o usuário
- `main.py`: Arquivo principal de execução

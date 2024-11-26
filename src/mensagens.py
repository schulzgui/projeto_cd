#Guilherme Schulz RA10401501
import json
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Mensagem:
    servico: str
    acao: str
    dados: Dict[str, Any]

    def to_json(self) -> str:
        return json.dumps({
            'servico': self.servico,
            'acao': self.acao,
            'dados': self.dados
        })

    @staticmethod
    def from_json(json_str: str) -> 'Mensagem':
        data = json.loads(json_str)
        return Mensagem(
            servico=data['servico'],
            acao=data['acao'],
            dados=data['dados']
        )
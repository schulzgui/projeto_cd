#Guilherme Schulz RA10401501
from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class Config:
    PRODUTOS_HOST: str = 'localhost'
    PRODUTOS_PORT: int = 5001
    VENDAS_HOST: str = 'localhost'
    VENDAS_PORT: int = 5002
    SERVIDOR_HOST: str = 'localhost'
    SERVIDOR_PORT: int = 5000

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
from dataclasses import dataclass

from model.connessione import Connessione


@dataclass
class Rifugio:
    id: int
    nome: str
    localita: str
    altitude: int
    aperto: bool
    def __str__(self):
        return f'{self.id}  {self.nome}'
    def __hash__(self):
        return hash(self.id)


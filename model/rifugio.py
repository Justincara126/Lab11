from dataclasses import dataclass

from model.connessione import Connessione


@dataclass
class Rifugio:
    id: int
    nome: str
    localita: str
    def __str__(self):
        return f'{self.nome} ,{self.localita}  --->         {self.id}'
    def __hash__(self):
        return hash(self.id)



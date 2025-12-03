from dataclasses import dataclass

from model.connessione import Connessione


@dataclass
class Rifugio:
    id: int
    nome: str
    localita: str
    altitude: int
    capienza:int
    aperto: bool

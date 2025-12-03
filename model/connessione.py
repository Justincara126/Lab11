from dataclasses import dataclass
@dataclass
class Connessione:
    id: int
    id_rifugio1: int
    id_rifugio2: int
    anno:int
    def __str__(self):
        f'{self.id_rifugio1}-{self.id_rifugio2}: {self.distanza} {self.difficolta}{self.anno}'
    def __hash__(self):
        return hash(self.id)
    def __lt__(self, other):
        return self.distanza < other.distanza